from cProfile import label
from random import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from threading import Thread
import time
import sys
import matplotlib.cm as cm
import random


done = False
doneSearching = False
error = False
threads = []
df = ""
planets = []

def norm2(vec):
    res = 0
    for el in vec:
        res += pow(el,2)
    res = res ** (1./2)
    return res


def animate():
    for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
        if doneSearching:
            break
        sys.stdout.write('\rLoading ' + c + ' Iteration : ' + str(iteration) + " 😳")
        sys.stdout.flush()
        time.sleep(0.1)

    print("Here are the results 😎😎😎:")
    for key,value in clusters.items():
        for p in value:
            print(key,
                  "|Name: " + str(p.name),
                  "|Density: " + str(p.planetDensity),
                  "|RatioToStellar: " + str(p.ratioToStellar),
                   "|Planet Mass: " + str(p.planetMass))



class Planet:
    def __init__(self, name, moonNum, orbitalPeriod, planetRadius, planetMass, planetDensity, radialVelocity, ratioToStellar):
        self.name = name
        self.moonNum = moonNum
        self.orbitalPeriod = orbitalPeriod
        self.planetRadius = planetRadius
        self.planetMass = planetMass
        self.planetDensity = planetDensity
        self.radialVelocity = radialVelocity
        self.ratioToStellar = ratioToStellar
        self.position = np.array([moonNum,orbitalPeriod,planetRadius,planetMass,planetDensity,radialVelocity,ratioToStellar])
        self.cluster = 0
        self.color = "#FFFFFF"

    def setCluster(self,clusterIndex):
        self.cluster = clusterIndex
    def setColor(self,col):
        self.color = col



def fetchData():
    global df
    df = pd.read_csv('ComputationalProblems/T2/DATA/Exoplanets2.csv', sep=',')
    df.dropna(inplace=True)


# pl_name
# sy_mnum
# disc_year
# pl_orbper
# pl_rade
# pl_bmasse
# pl_dens
# pl_rvamp
# name,moonNum,orbitalPeriod,planetRadius,planetMass,planetDensity,radialVelocity


def iterateThruData():
    for index in df.index:
        # if index > 300:
        #     break
        planet = Planet(
            df["pl_name"][index],
            df["sy_mnum"][index],
            df["pl_orbper"][index],
            df["pl_rade"][index],
            df["pl_bmasse"][index],
            df["pl_dens"][index],
            df["pl_rvamp"][index],
            df["pl_ratror"][index])
        global planets
        planets.append(planet)
    global done
    done = True


d = Thread(target=fetchData)
i = Thread(target=iterateThruData)

d.start()
d.join()
i.start()

K = int(input("CHOOSE NUMBER OF K: "))
Ks = []
for i in range(K):
    randy = random.randint(0,600)
    Ks.append(planets[randy].position + (random.random() * .5 - 1) * 200)
    

# COMPUTE DISTANCES WITH NORM 2 - EUCLIDEAN FORMULA
clusters = {}
def reGroup():
    for i in range(K):
        clusters.update({i:[]})
    for pIndex,planet in enumerate(planets):
        minDist = 999999999
        clusterNum = 0
        for kIndex, kPoint in enumerate(Ks):
            dist = norm2(planet.position - kPoint)
            if(dist < minDist):
                minDist = dist
                clusterNum = kIndex
        planet.setCluster(clusterNum)
        dic = clusters[clusterNum]
        dic.append(planet)
        clusters.update({clusterNum:dic})



def updateKs():
    count = 0
    tempKs = Ks
    for index,kPoint in enumerate(tempKs):
        newVec = [0] * 7
        count = len(clusters[index])
        for planet in clusters[index]:
           for ind,v in enumerate(planet.position):
                if count > 0:
                    newVec[ind] += v / count
        Ks[index] = newVec
    return Ks

iteration = 0
prevks = []
reGroup()
currKs = updateKs()
t = Thread(target=animate)
t.start()
while not doneSearching:
    currKs = updateKs()
    doneSearching = currKs == prevks
    reGroup()
    iteration += 1
    prevks = currKs.copy()

for key,value in clusters.items():
    hexV = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    col = ""
    for i in range(6):
        col += str(hexV[random.randint(0,len(hexV) - 1)])
    for p in value:
        p.setColor("#" + col)
    



random.seed(10)
x_data = list(map(lambda planet: planet.planetDensity + random.random() * 100, planets))
y_data = list(map(lambda planet:  planet.ratioToStellar + random.random() * 100, planets))
z_data = list(map(lambda planet: planet.planetMass + random.random() * 5000, planets))
colors = list(map(lambda planet: planet.color,planets))
ax = plt.axes(projection="3d")
planetRadiuses = []
for p in planets:
    planetRadiuses.append(p.planetRadius * 2)

ax.scatter(x_data, y_data, z_data, marker="o", s=planetRadiuses, color=colors, alpha=0.5)
ax.set_label("Pseudo visualisation of planets")

plt.show()

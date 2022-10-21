## 1.5.  Detect liquid level in a glass vessel (3 points)
* (a)  Simplified case:  digital camera and glass vessel are at constantlocations,  e.g.  in some laboratory.  Vessel is filled in at variouslevels  and  with  various  liquids  of  predefined  list.   Detect  fromvideo digital images:i.  if vessel is empty, full, or filled inxpercent, 0< x <100;ii.  which liquid it is
* (b)  Use matrix norms for detecting liquid in a glass vessel from thepredefined  list  of  liquids.   Consider  three  different  liquids,  forexample, water, green tea, and coffee.  How do you solve problemof possible color variations in each liquid?  Which norms do youapply?  Why?
* (c)  Describe your approach and algorithm in written.  Give reasonsfor justifying your choice.
* (d)  Generate synthetic data, run code, visualize output
* (e)  Are you happy with obtained solution?  Explain why.(f)  Test:  your code should work properly on data provided by TA

### Conclusion:
* a) Works on test cases provided and on the videos i included in the video folder
* b) I divide pixels in 3 different groups with K means clustering, also used frobenius and euclidean norms
* c) In the frame matrix, for every row i get Left and Right points(column indices) then i'm able to sum up all row lengths inside an object and get the area like that. I use same approach for calculating the Fill level but at the same time i'm assigning every row line to relevant liquid groups according to the k means algorithm.
Lastly percent = fill/area * 100
* d) Already done, even made my own test case videos, so you can get the idea what i had in mind while writing this program
* e) I am somewhat satisfied but would be happier if we had more clear problem descriptions,more testcases and real footage.
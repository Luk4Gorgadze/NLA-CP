## 1.4.  Partition of 225 freshmen students in 15 groups of 15 students in each(2 points)
* (a)  For  each  student  3-vector  is  available.   These  vectors  containNAEC  examination  scores  in  Georgian  language,  English  language and mathematics.
* (b)  Requirement is that each group should have approximately similar strength from the viewpoint of NAEC examination scores.
* (c)  Compare groups using matrix norm.  Which norm is better forthe task?  Explain.
* (d)  Describe your approach and algorithm.  Give reasons for justify-ing your choice.
* (e)  Generate synthetic data, run code, visualize output;
* (f)  Investigate (experimentally) how solution depends on vector andmatrix norms used in solution algorithm
* (g)  Are you happy with obtained solution?  Explain why.(h)  Test:  your code should work properly on data provided by TA

### Conclusion:

* a) Done
* b) Done
* c) Frobenius norm is the best for this task
* d) I am using my own version of Backtracing algorithm, I am calculating every possible permutation (Calculating frobenius norm (or just sum for simplicity) for every group and comparing them to average group score). I skip some permutations if my program "guesses" bad combinations of students. Maximum difference between groups is 1%
* e) Done
* f) Solution depends on matrix norms heavily, even on scales of scores
* g) I am very happy, YES 😎 🤣 
# algorithm-analyzer

An attempt to progrematically estimate an algorithm's Big O notation

Due to the Halting problem (https://en.wikipedia.org/wiki/Halting_problem), it is thought to be impossible to create a program that analyzes an algorithm's Big O notation, therefore I am attempting to estimate it by running random tests with incrementing sample-sizes and count the amount of operations, as accurately as I am able to do. Current tests show this to be a promising way to estimate Big O notation by using regression and MAE to find the best fit.

TODO:
- Add regression for all except logarithmic
- Implement Big O storage estimation
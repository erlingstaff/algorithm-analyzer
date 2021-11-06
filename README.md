# algorithm-analyzer

An attempt to progrematically estimate an algorithm's Big O notation

Due to the Halting problem (https://en.wikipedia.org/wiki/Halting_problem), it is thought to be impossible to create a program that analyzes an algorithm's Big O notation, therefore I am attempting to estimate it by running random tests with incrementing sample-sizes while counting the amount of operations. Current tests show this to be a promising way to estimate Big O notation by using linear as well as non-linear regression and MAE to find the best fit.

# Functions currently in the project scope

![image](https://user-images.githubusercontent.com/38101463/140611693-b3b90795-e911-4929-9be0-da0e9e9dff0a.png)

# Logarithmic regression estimation

![image](https://user-images.githubusercontent.com/38101463/140611593-c730355a-765e-41b6-b921-ccfec3460a0f.png)


TODO:
- Add regression for all except logarithmic
- Implement Big O storage estimation
- Add Big O notations from graph theory
- https://codemirror.net/ For website code interface
- https://skulpt.org/ Potential python sandbox/interpreter to sanitize user input
- Sanitize untrusted python code

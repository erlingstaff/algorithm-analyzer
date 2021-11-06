# algorithm-analyzer

An attempt to progrematically estimate an algorithm's Big O notation

Due to the Halting problem (https://en.wikipedia.org/wiki/Halting_problem), it is thought to be impossible to create a program that analyzes an algorithm's Big O notation, therefore I am attempting to estimate it by running random tests with incrementing sample-sizes and count the amount of operations, as accurately as I am able to do. Current tests show this to be a promising way to estimate Big O notation by using regression and MAE to find the best fit.

# Display of the different Big O notations this projects scope, as well as a user defined algorithm ("Algorithm"). Future versions will additionally include Big O notations from graph theory.

![image](https://user-images.githubusercontent.com/38101463/140611575-ba297e9f-68a6-417b-9149-54565f83dfbe.png)

# Logarithmic regression estimation

![image](https://user-images.githubusercontent.com/38101463/140611593-c730355a-765e-41b6-b921-ccfec3460a0f.png)


TODO:
- Add regression for all except logarithmic
- Implement Big O storage estimation

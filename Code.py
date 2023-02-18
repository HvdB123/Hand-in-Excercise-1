import numpy as np
import matplotlib.pyplot as plt

# logistic map is f(x) = R*x*(1-x)  with R in (0,4)
def logistic(x,R):
	y = R*x*(1.0-x)
	return y 

# fill an array with iteration n1 to n2 of the logistic map starting with x0 and with parameter R
# the function is modified to return time (t) aswell
def fillit(n1,n2,x0,R):
    x = x0
    z = np.zeros(n2 - n1)
    t = np.arange(0, n2 - n1)
    for i in range(0, n2 - n1):
        x = logistic(x, R)
        z[i] = np.clip(x, 0, 1)  # clip the output values between 0 and 1
    return t, z



#this function plots xn vs t, with changing initial conditions (x0)
def xn_vs_t_1(R, x0_values): 
    n1 = 100
    n2 = 200
    for x0 in x0_values:
        t, z = fillit(n1, n2, x0, R)
        plt.figure()
        plt.xlabel(r"$t$", fontsize=20)
        plt.ylabel(r"$x_n$", fontsize=20)
        plt.plot(t, z, "k-", linewidth=1)
        plt.title(f"R = {R}, x_0 = {x0}")
        plt.show()


#this function plots xn vs t, with values of R in an interval
def xn_vs_t_2(R_values, n1=100, n2=200, x0=0.5):
    for R in R_values:
        t, z = fillit(n1, n2, x0, R)
        plt.figure()
        plt.xlabel(r"$t$", fontsize=20)
        plt.ylabel(r"$x_n$", fontsize=20)
        plt.plot(t, z, "k-", linewidth=1)
        plt.title(f"R = {round(R,4)}, x_0 = {x0}")
        plt.show()

#question 4
R_values = np.arange(3.54,3.56,0.001)
print(xn_vs_t_2(R_values))

"""
below are all the commands to run the code for the particular questions.


#question 2
x0_values = [0.01, 0.1, 0.5]
print(xn_vs_t_1(2.9, x0_values))

#question 3
x0_values = [0.01, 0.1, 0.5]
print(xn_vs_t_1(3.1, x0_values))

x0_values = [0.01, 0.1, 0.5]
print(xn_vs_t_1(3.49, x0_values))

#question 4
R_values = np.arange(3.54,3.56,0.001)
print(xn_vs_t_2(R_values))

#question 5
x0_values = [0.5, 0.6]
print(xn_vs_t_1(4.0, x0_values))

"""

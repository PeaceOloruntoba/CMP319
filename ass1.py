# Name: Peace Oloruntoba
#Matric No.: AUL/SCI/21/00726
#Dept.: Mathematical Science

# a). Write a Code for the derived Euler's method to solve the classical initial value problem: y'=3x^2y as given in the class using varied step sizes of h=0.001, 0 0001 and 0.0000001 within the interval [0,1].
# b) Compare your result at every node with the exact solution given by y(x)= exp(x^3). Tabulate the results of your absolute errors.

import numpy as np

# Define the differential equation
def f(x, y):
    return 3 * x**2 * y

# Exact solution
def exact_solution(x):
    return np.exp(x**3)

# Euler's method for solving the differential equation
def euler_method(h, x0, y0, x_final):
    num_steps = int((x_final - x0) / h) + 1
    x_values = np.linspace(x0, x_final, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0

    for i in range(1, num_steps):
        y_values[i] = y_values[i-1] + h * f(x_values[i-1], y_values[i-1])

    return x_values, y_values

# Main function to perform the calculations
def main():
    x0 = 0
    y0 = 1  # Initial condition y(0) = 1
    x_final = 1

    # List of step sizes to be tested
    step_sizes = [0.001, 0.0001, 0.0000001]

    print("Step Size   | Max Absolute Error")
    print("==================================")
    
    for h in step_sizes:
        x_values, y_values = euler_method(h, x0, y0, x_final)
        exact_values = exact_solution(x_values)
        absolute_errors = np.abs(exact_values - y_values)
        max_absolute_error = np.max(absolute_errors)
        print(f"{h:.7f}     | {max_absolute_error:.7f}")

if __name__ == "__main":
    main()


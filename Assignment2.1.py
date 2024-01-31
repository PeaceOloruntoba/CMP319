import math

def function_f(x, y):
    """Define the function f(x, y) for the differential equation."""
    return 3 * x**2 * y

def exact_solution(x):
    """Define the exact solution for comparison."""
    return math.exp(x**3)

def adams_bashforth_2steps(x, y, h):
    """Implement the 2-steps Adams-Bashforth method."""
    f1 = function_f(x[-2], y[-2])
    f2 = function_f(x[-1], y[-1])
    y_pred = y[-1] + h * (3/2 * f2 - 1/2 * f1)
    return y_pred + h * (1/2 * function_f(x[-1], y_pred) + 1/2 * f2)

def adams_bashforth_3steps(x, y, h):
    """Implement the 3-steps Adams-Bashforth method."""
    f1 = function_f(x[-3], y[-3])
    f2 = function_f(x[-2], y[-2])
    f3 = function_f(x[-1], y[-1])
    y_pred = y[-1] + h * (23/12 * f3 - 4/3 * f2 + 5/12 * f1)
    return y_pred + h * (5/12 * function_f(x[-1], y_pred) + 2/3 * f3 - 1/12 * f2)

def solve_and_compare(h_values):
    """Solve the differential equation using Adams-Bashforth methods and compare with the exact solution."""
    for h in h_values:
        # Generate x values
        x_values = [i * h for i in range(int(1/h) + 1)]
        # Calculate the exact solution for comparison
        y_exact = [exact_solution(x) for x in x_values]

        # Adams-Bashforth 2-steps
        y_ab2 = [y_exact[0], y_exact[1]]
        for i in range(2, len(x_values)):
            y_ab2.append(adams_bashforth_2steps(x_values[:i+1], y_ab2, h))
        error_ab2 = [abs(y_exact[i] - y_ab2[i]) for i in range(len(x_values))]

        # Adams-Bashforth 3-steps
        y_ab3 = [y_exact[0], y_exact[1], y_exact[2]]
        for i in range(3, len(x_values)):
            y_ab3.append(adams_bashforth_3steps(x_values[:i+1], y_ab3, h))
        error_ab3 = [abs(y_exact[i] - y_ab3[i]) for i in range(len(x_values))]

        print(f"\nResults for h = {h}\n")
        print(" x      |   Exact   |   AB2     |   Error AB2")
        for i in range(len(x_values)):
            print(f"{x_values[i]:.4f} | {y_exact[i]:.6f} | {y_ab2[i]:.6f} | {error_ab2[i]:.6f}")

        print("\nAdams-Bashforth 3-steps:")
        print(" x      |   Exact   |   AB3     |   Error AB3")
        for i in range(len(x_values)):
            print(f"{x_values[i]:.4f} | {y_exact[i]:.6f} | {y_ab3[i]:.6f} | {error_ab3[i]:.6f}")

# Set the step sizes
h_values = [0.1, 0.0001, 0.000001]

# Call the function to solve and compare
solve_and_compare(h_values)

import math

def f(x, y):
    return 3 * x**2 * y

def exact_solution(x):
    return math.exp(x**3)

def adams_predictor_corrector_2steps(x, y, h):
    f1 = f(x[-2], y[-2])
    f2 = f(x[-1], y[-1])
    predictor = y[-1] + h * (3/2 * f2 - 1/2 * f1)
    corrector = y[-1] + h * (1/2 * (f(x[-1], predictor) + f2))
    return corrector

def adams_predictor_corrector_3steps(x, y, h):
    f1 = f(x[-3], y[-3])
    f2 = f(x[-2], y[-2])
    f3 = f(x[-1], y[-1])
    predictor = y[-1] + h * (23/12 * f3 - 4/3 * f2 + 5/12 * f1)
    corrector = y[-1] + h * (1/2 * (f(x[-1], predictor) + f3))
    return corrector

def solve_and_compare_predictor_corrector(h_values):
    for h in h_values:
        x_values = [i * h for i in range(int(1/h) + 1)]
        y_exact = [exact_solution(x) for x in x_values]

        # Adams Predictor-Corrector 2-steps
        y_pc2 = [y_exact[0], y_exact[1]]
        for i in range(2, len(x_values)):
            y_pc2.append(adams_predictor_corrector_2steps(x_values[:i+1], y_pc2, h))
        error_pc2 = [abs(y_exact[i] - y_pc2[i]) for i in range(len(x_values))]

        # Adams Predictor-Corrector 3-steps
        y_pc3 = [y_exact[0], y_exact[1], y_exact[2]]
        for i in range(3, len(x_values)):
            y_pc3.append(adams_predictor_corrector_3steps(x_values[:i+1], y_pc3, h))
        error_pc3 = [abs(y_exact[i] - y_pc3[i]) for i in range(len(x_values))]

        print(f"\nResults for h = {h}\n")
        print(" x     |   Exact   |   PC2     |   Error PC2")
        for i in range(len(x_values)):
            print(f"{x_values[i]:.4f} | {y_exact[i]:.6f} | {y_pc2[i]:.6f} | {error_pc2[i]:.6f}")

        print("\nAdams Predictor-Corrector 3-steps:")
        print(" x     |  Exact   |   PC3    |  Error PC3")
        for i in range(len(x_values)):
            print(f"{x_values[i]:.4f} | {y_exact[i]:.6f} | {y_pc3[i]:.6f} | {error_pc3[i]:.6f}")

# Set the step sizes
h_values = [0.1, 0.01, 0.001]

# Call the function to solve and compare with Predictor-Corrector
solve_and_compare_predictor_corrector(h_values)

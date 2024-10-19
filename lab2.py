import math
import matplotlib.pyplot as plt
import numpy as np

def lagrange_interpolation(x, x_points, y_points):
    def L(k, x):
        result = 1
        for i in range(len(x_points)):
            if i != k:
                result *= (x - x_points[i]) / (x_points[k] - x_points[i])
        return result

    result = 0
    for k in range(len(x_points)):
        result += y_points[k] * L(k, x)
    return result

def fx(x):
    return math.cos(x)

x_points = [0, 0.6]
y_points = [fx(0), fx(0.6)]
x = 0.45

interpolated_value = lagrange_interpolation(x, x_points, y_points)
true_value = math.cos(x)
print(f"Interpolated value at x = {x}: {interpolated_value}")
print("Absolute error:", abs(true_value - interpolated_value))

# Question 2b
x_points.append(0.9)
y_points.append(fx(0.9))

interpolated_value2 = lagrange_interpolation(x, x_points, y_points)
print(f"Interpolated value at x = {x}: {interpolated_value2}")
print("Absolute error:", abs(true_value - interpolated_value2))

# Question 3:
x = 1.35
x_points = [1.1, 1.2, 1.3, 1.4]
y_points = [9, 11, 13, 16]

interpolated_value3 = lagrange_interpolation(x, x_points, y_points)
print(f"Interpolated value at x = {x}: {interpolated_value3}")

def fx_3(x):
    return math.exp(2*x)

# Generate points for plotting
x_plot = np.linspace(min(x_points), max(x_points), 100)
y_plot_lagrange = [lagrange_interpolation(xi, x_points, y_points) for xi in x_plot]
y_plot_actual = [fx_3(xi) for xi in x_plot]

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot_lagrange, 'b-', label='Lagrange Interpolation')
plt.plot(x_plot, y_plot_actual, 'r-', label='Actual function')
plt.plot(x_points, y_points, 'go', label='Data points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Lagrange Interpolation and Actual Function')
plt.legend()
plt.grid(True)
plt.show()

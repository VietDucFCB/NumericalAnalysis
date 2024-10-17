import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 6
y_0 = 1
n = 100  # number of steps between each integer 

def f(x, y):
    return x * (1 + x**2) / y**2

deltaX = 1 / n  # step size for each unit interval

y_values = np.zeros(7)  # Array to store y0 to y6
y_values[0] = y_0

for i in range(1, 7):
    y = y_values[i-1]
    x_start = i - 1
    for j in range(n):
        x = x_start + j * deltaX
        y += deltaX * f(x, y)
    y_values[i] = y

print("Approximated y values:")
for i, y in enumerate(y_values):
    print(f"y{i} = {y:.6f}")

# Calculate actual values
y_actual = [(3/2*i**2 + 3/4*i**4 + 1)**(1/3) for i in range(7)]

print("\nActual y values:")
for i, y in enumerate(y_actual):
    print(f"y{i} = {y:.6f}")

# Calculate and print relative errors
print("\nRelative errors:")
for i in range(7):
    error = abs(y_values[i] - y_actual[i]) / y_actual[i] * 100
    print(f"Error for y{i}: {error:.4f}%")

# If you still want to calculate the integral
integral = 0
y = y_0
for i in range(6):
    for j in range(n):
        x = i + j * deltaX
        integral += deltaX * f(x, y)
        y += deltaX * f(x, y)

print(f"\nApproximate Integral: {integral:.6f}")

x = np.arange(7)
plt.figure(figsize=(10, 6))
plt.plot(x, y_values, 'ro-', label='Approximated y')
plt.plot(x, y_actual, 'bo-', label='Actual y')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Approximated and Actual y Values')
plt.legend()
plt.grid(True)
plt.xticks(x)
plt.show()

# Câu c
n = [25, 50, 100, 200]
E6_values = []

for i in range(0,4):
  for j in range(1, 7):
    y = y_values[j-1]
    x_start = j - 1
    for o in range(n[i]):
        x = x_start + o * deltaX
        y += deltaX * f(x, y)
    y_values[j] = y
  E6 = np.sqrt(np.sum((np.array(y_actual) - y_values)**2))
  print(f"For n = {n[i]}, E6 = {E6:.6f}")
  E6_values.append(E6)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(n, E6_values, 'bo-')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of Steps (n)')
plt.ylabel('E6 Error')
plt.title('E6 Error vs Number of Steps')
plt.grid(True)

# Add value labels
for i, txt in enumerate(E6_values):
    plt.annotate(f'{txt:.6f}', (n[i], E6_values[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()

# Print the values
for n, E6 in zip(n, E6_values):
    print(f"For n = {n}, E6 = {E6:.6f}")

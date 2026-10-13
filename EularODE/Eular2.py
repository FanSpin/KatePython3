import numpy as np
import matplotlib.pyplot as plt

# ODE: dy/dx = x*y,  y(0) = 1
# Analytical: y = exp(x²/2)

def dy(x, y):
    return x * y

f = lambda x: np.exp(x**2 / 2)

x0, xn, y0, h = 0, 1, 1, 0.1

N = round((xn - x0) / h)
x_vals = np.linspace(x0, xn, N + 1)
y_vals = np.zeros(N + 1)
y_vals[0] = y0

for i in range(N):
    y_vals[i + 1] = y_vals[i] + dy(x_vals[i], y_vals[i]) * h

# Table
print(f"{'x':>5}  {'y (Euler)':>10}  {'y (analytical)':>14}")
for i in range(N + 1):
    print(f"{x_vals[i]:5.1f}  {y_vals[i]:10.4f}  {f(x_vals[i]):14.4f}")

# Plot
plt.figure(figsize=(7, 5))
plt.plot(x_vals, y_vals, 'b+', markersize=8, label='Euler')
plt.plot(x_vals, f(x_vals), 'r-', label='Analytical')
plt.title('Euler Method: dy/dx = xy')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0, 2])
plt.ylim([0, 2])
plt.legend()
plt.grid(True)
plt.show()

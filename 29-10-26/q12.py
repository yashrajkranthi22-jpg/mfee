import numpy as np
import matplotlib.pyplot as plt

# Create the figure
fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface: z^2 = 2x^2 - y^2
# Therefore, z = +/- sqrt(2x^2 - y^2)

x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)

Z_squared = 2 * X**2 - Y**2

# Keep only points where Z_squared >= 0
Z_squared[Z_squared < 0] = np.nan
Z = np.sqrt(Z_squared)

# Plot both halves of the surface
ax.plot_surface(X, Y, Z, alpha=0.55, cmap='viridis')
ax.plot_surface(X, Y, -Z, alpha=0.55, cmap='viridis')

# Given point P = (1, 0, sqrt(2))
P = np.array([1, 0, np.sqrt(2)])

# Gradient of f = 2x^2 - y^2 - z^2
# grad(f) = (4x, -2y, -2z)
gradient = np.array([4, 0, -2 * np.sqrt(2)])

# Normalize the gradient to get the unit normal
unit_normal = gradient / np.linalg.norm(gradient)

# Mark the point P
ax.scatter(*P, color='red', s=80, label='P = (1, 0, sqrt(2))')

# Draw the gradient (normal) vector
ax.quiver(
    *P,
    *unit_normal,
    length=1.0,
    color='red',
    linewidth=3,
    arrow_length_ratio=0.2,
    label='Unit normal (gradient direction)'
)

# Draw the opposite unit normal
ax.quiver(
    *P,
    *(-unit_normal),
    length=1.0,
    color='blue',
    linewidth=3,
    arrow_length_ratio=0.2,
    label='Opposite unit normal'
)

# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(r'Surface $z^2=2x^2-y^2$ and its Normal at $P$')

ax.legend()
ax.set_box_aspect([1, 1, 1])
plt.tight_layout()
plt.savefig('q12.png')
plt.show()

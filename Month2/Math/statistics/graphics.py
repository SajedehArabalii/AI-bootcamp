import matplotlib.pyplot as plt
import numpy as np

# 1. Set up the random number generator
fig, ax = plt.subplots(figsize = (8, 8))


# 2. Create figure and axis using plt.subplots() (note the 's')
rng = np.random.default_rng(seed=42)

# 3. Generate data and plot
x = rng.standard_normal(100)
y = rng.standard_normal(100)

# ax.scatter(x, y, marker='o')
ax.plot(x, y, 'o')
ax.set_xlabel("This is X axis")
ax.set_ylabel("This is Y axis")
ax.set_title("This is the title")
plt.show()

# ----------------------
fig , axes = plt.subplots(
    nrows = 2,
    ncols = 3,
    figsize = (15, 5)
)

axes[0, 1].plot(x, y, 'o')
axes[1, 2].scatter(x, y, marker='+')
plt.show()

fig.savefig("figure.png", dpi = 400)
fig.savefig("figure.pdf", dpi = 200)

"""
# Save as a resolution-independent vector PDF
fig.savefig("figure.pdf")

# If you want to ensure transparent background is preserved or margins are clean:
fig.savefig("figure.pdf", bbox_inches="tight")

Pro-Tip: Always add bbox_inches='tight' when saving figures. It prevents Matplotlib from cropping out outer labels or titles that sit near the edges of the canvas!
"""
fig, ax = plt.subplots(figsize = (8, 8))

#Generates an array of 50 evenly spaced numbers ranging from $-\pi$ to $+\pi$.
x = np.linspace(-np.pi, np.pi, 50)
y = x

#Performs an outer product multiplication between two 1D vectors to build a 2D matrix ($50 \times 50$) of all possible pairwise products.
f = np.multiply.outer(np.cos(y), 1 / (1 + x**2))
#Draws 2D contour lines on the plot grid representing curves of equal height/value across matrix f.
ax.contour(x, y, f)
plt.show()

fig, ax = plt.subplots(figsize = (8, 8))
#Makes a heat map
ax.imshow(f)
plt.show()


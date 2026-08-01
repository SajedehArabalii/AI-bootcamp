import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


"""
.pdf(x) → Probability density at exactly x (height of the curve).
.cdf(x) → Probability of being up to x (area under the PDF curve from −∞ to x)
"""
np.random.seed(42)
# A dictionary that stores Matplotlib's runtime configuration parameters ("rc" stands for runtime configuration)
#'figure.figsize' => This key controls the width and height of every new figure.
"""
(6,4)      # small
(8,5)      # standard
(10,5)     # wide (good for line plots)
(12,6)     # presentation
(15,8)     # very large
"""
plt.rcParams['figure.figsize'] = (10,5)
# print(plt.rcParams)

# Priors (from the population)
P_GIRL ,P_BOY = 0.7, 0.3

# Class-conditional distributions
#These lines create normal (Gaussian) probability distributions as Python objects.
# stats.norm(...) → creates a Normal distribution.
# loc → the mean (μ).
# scale → the standard deviation (σ)
"""
- Girls: x|girl ≈ (mu=4, sigma=1.2)
- Boys:  x|boy ≈ (mu=7, sigma=1.5)
"""
girl_dist = stats.norm(loc=4.0, scale=1.2)
boy_dist  = stats.norm(loc=7.0, scale=1.5)

x = np.linspace(0, 12, 1000)


"""
This plots the probability density curve of the girls' hormone distribution.

x → x-axis values (hormone levels).
girl_dist.pdf(x) → y-axis values (density at each hormone level).
color='tab:red' → draw the line in red.
label='p(x|girl)' → name used in the legend.

In other words, it draws the graph of:

p(x∣girl)

which shows how likely different hormone levels are for girls.
"""
plt.plot(x, girl_dist.pdf(x), color='tab:red', label='p(x|girl)')
plt.plot(x, boy_dist.pdf(x), color='tab:blue', label='p(x|boy)')

plt.xlabel("tav-hormone level")
plt.ylabel("probability density")
plt.title("Class-conditional densities of the tav-hormone")

#displays a legend (key) on the plot, showing which line corresponds to which label.
plt.legend()
plt.show()

#TODO check this

plt.plot(x, girl_dist.pdf(x) * P_GIRL, color="tab:red", label="P(girl)·p(x|girl)") #label="p( girl| x)")
plt.plot(x, boy_dist.pdf(x) * P_BOY,  color="tab:blue", label="P(boy)·p(x|boy)")#label="p( boy | x)")
plt.xlabel("tav-hormone level")
plt.ylabel("probability density")
plt.title("Class-conditional densities of the tav-hormone")
plt.legend()
plt.show()

"""
girl_dist.pdf(x) => p(x∣girl) => Likelihood: "If the person is a girl, how likely is this hormone level x?"
girl_dist.pdf(x) * P_GIRL => p(x∣girl)P(girl) => Joint density (or the unnormalized posterior / Bayes numerator).
"""

"""
.cdf stands for Cumulative Distribution Function (CDF).

It gives the probability that a random variable is less than or equal to a value x:
"""
# Probability that a Girl has hormone level between 3 and 5
prob = girl_dist.cdf(5) - girl_dist.cdf(3)
print(f"P(3 <= x <= 5 | girl) = {prob:.3f}")



"""
This numerically integrates the PDF over its entire range.

    quad(...) → Performs numerical integration.
    girl_dist.pdf → The function to integrate.
    -np.inf to np.inf → Integrate from negative infinity to positive infinity.
    area → Stores the result.
    _ → Ignores the estimated integration error returned by quad.
"""
# The total area under each density curve is always 1:
from scipy.integrate import quad
area, _ = quad(girl_dist.pdf, -np.inf, np.inf)
print(f"Total area under p(x|girl) = {area:.3f}")


# Unnormalized posteriors
# g = P(girl)·P(x|girl)
# b = P(boy)·P(x|boy)
g_posterior = girl_dist.pdf(x) * P_GIRL
b_posterior = boy_dist.pdf(x) * P_BOY

"""
Meaning:

    boy_dist.pdf(x) → How likely the observed value x is if the person is a boy.
    P_BOY → The prior probability of being a boy.
    Their product → The unnormalized posterior (also called the Bayes numerator) for the boy class.
"""
idx = np.where(g_posterior < b_posterior)[0][0]
"""
First [0] → extract the array of matching indices.
Second [0] → extract the first matching index.
"""
x_star = x[idx]

newborns = 10000
n_girls =int(newborns * P_GIRL)
n_boys = newborns - n_girls

#Generate n_girls random hormone levels that follow the girls' distribution and store them in girl_samples
girl_samples = girl_dist.rvs(n_girls)
boy_samples = boy_dist.rvs(n_boys)
"""
girl_dist → The probability distribution for girls.
.rvs() → Random Variates Sampling: generates random values from the distribution.
n_girls → The number of samples to generate.
girl_samples → A NumPy array containing the generated hormone levels.
"""


"""
boy_samples → The data to plot.
bins=50 → Divide the data into 50 intervals (bars).
alpha=0.6 → Make the bars 60% opaque (slightly transparent).
color='tab:pink' → Color the bars pink.
label='girl' → Legend label (this is likely a mistake—it should probably be 'boy' since you're plotting boy_samples)
"""
plt.hist(girl_samples, bins = 50, alpha = 0.6, color='tab:pink', label='girl')
plt.hist(boy_samples, bins = 50, alpha = 0.6, color='tab:blue', label='boy')
plt.xlabel('tav-hormone level')
plt.ylabel('count')
plt.title(f"Histogram of {newborns:,} sampled newborns (70% girls / 30% boys)")
plt.legend()
plt.show()


"""
Meaning: It gives the unnormalized posterior (the numerator of Bayes' theorem) for the boy class. It is used to compare against the girl's value to decide which class is more likely.
"""
g = girl_dist.pdf(x) * P_GIRL
b = boy_dist.pdf(x) * P_BOY
"""
lw=2 → Line width of 2
ls='--' → Dashed line style
"""
plt.plot(x, g, color="deeppink", lw = 2, label="P(girl)·p(x|girl)")
plt.plot(x, b, color='navy', lw = 2, label="P(boy)·p(x|boy)")
plt.axvline(x_star, color='k', ls='--', label=f"decision boundary x*={x_star:.2f}")

plt.fill_between(x, np.minimum(g, b), color="red", alpha=0.25, label="unavoidable error")# Bayes error, the minimum possible rate for any classifier

plt.xlabel("tav-hormone level")
plt.ylabel("weighted density")
plt.title("The intersection point is the optimal decision boundary")
plt.legend()
plt.show()

"""
The boundary is shifted toward the boy's side, since girls are more common we need stronger evidence before predicting boy
"""

# Verify empirically: classify our samples with the threshold
pred_boy_g = girl_samples > x_star # Girls misclassified as boys
pred_girl_b = boy_samples <= x_star # Boys misclassified as girls

error_rate = (pred_boy_g.sum() + pred_girl_b.sum()) / newborns
print(f"Empirical error rate with x* = {error_rate:.4f}")

naive = ((girl_samples > 5.5).sum() + (boy_samples <= 5.5).sum()) / newborns
print(f"Empirical error rate with naive threshold 5.5 = {naive:.4f}")

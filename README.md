# The-Haynes-Shockley-Experiment

This is a group project that, as of 6/4/23, I am working on with my group. The aim of this project is to understand the motion of minority charge carriers (MCCs) in locally p-type silicon semiconductors. I am the computational physicist in this project; I produce simulations on what our results should look like.

## Background

For context, when electrons or the absence of charge (referred to as "holes" in this case) are injected into a semiconductor, the injected charge carriers will begin to diffuse away from the point of injection. The reason why their motion can be modelled as diffusion is because:

* They are very large in quantity and can therefore be labelled as a continuous system
* Their motion is random
* Only two outcomes exist in regards to their motion; a charge carrier will move either in the positive or negative x-direction (assuming that the semiconductor is one-dimensional)

With the reasoning above, it is possible to predict the diffusion of these MCCs within the semiconductor across time via a Gaussian distribution,

$P(x,t) = A(t)e^{-\frac{x^{2}}{4Dt}},$

where $A(t)$ is the normalisation function,

$A(t) = \frac{1}{\sqrt{4\pi Dt}},$

and D is the diffusion constant, given by

$D = \frac{\mu k_{b} T}{q}.$

Note that $\mu$ is the mobility of the semiconductor's MCCs, $k_{b}$ is Boltzmann's constant, $T$ is the temperature of the semiconductor, and $q$ is the charge of a single electron. For additional information, $\mu$ is defined as

$\mu = \frac{q \tau_{F}}{m}$,

where $\tau_{F}$ and $m$ are the carrier lifetime (more on this later) and mass of the minoirty charge carrires, respecitvely.

Now that our choice of modelling is justified, let us see what the motion of these minoirty charge carriers should look like:

[diffusion](https://user-images.githubusercontent.com/102374376/226909400-230ca4e8-aa51-4044-b80e-1f2a0e5b17b2.mp4)

Note: this animation can be found in videos/diffusion.mp4.

The animation above shows an initial peak at $x, t, = 0$, corresponding to the point of charge injection into the semiconductor. The charge carriers then spread out acorss both x-directions, lowering the peak and widening the curve. Note that in this case, since the Gaussian represents a probability distribution across the length of the semiconductor, and the number of MCCs within the semiconductor remains constant, the area under this distribution also remains constant. This is why the lowering and broadening of the distribution's peak is observed.

## Simulation Technique: The Random-Walk Algorithm

We have seen, now, an expectation of the MCCs' motion by means of visualising the diffusion equation, but the challenge of actually simulating such an event remains. For this, let us consider the random-walk algorithm.

Consider a particle at an origin, as in, $x = 0$, on a one-dimensional number line. Upon the tossing of a coin, the particle is to move by 1 in the postive x-direction if the coin lands on heads, and vice versa for tails. This process is repeated hundreds of times: say, 1000. After 1000 coin tosses, the particle will reach a final displacement from the origin. This process will be repeated for thousands of particles. Then, two types of data will be collected:

* The final displacement of each particle.
* The frequency of each final displacement.

By plotting the freuquency of each displacement against the displacement itself, we'll obtain a frequency distribution. Below is the reasoning on why this distrubution is very useful:

* A very large number of particles was involved, meaning we can model this distribution as a continuous one.
* Each particle's moiton was random.
* Each event (the coin toss, in this instance) had only two outcomes; the particle either moved in the positive or negative x-direction.

You may realise that the properties of this random-walk distribution mirror that of a Gaussian. What this means is that the random-walk algorithm can effectively simulate one-dimensional diffusion. To further prove my point, I will plot an exponential best-fit curve to the random-walk distribution:

![random](https://user-images.githubusercontent.com/102374376/230256953-c3636941-6a23-4906-9922-737db680612b.png)

## Overcoming the Limitations of the Random-Walk Algorithm

We have seen that the random-walk algorithm is useful in simulating one-dimensional diffusion, however the diffusion of MCCs in a semiconductor have two important properties that the simulation in question does not currently account for.

### Drift

Semiconductors are connected to circuits. As such, a voltage, $V$,  and therefore an electric field, $E$, is applied across them. The applied electric field exerts a force, $F = Eq$, on the MCCs, inducing a drift velocity within them, in the form of $v = \frac{\mu V}{d}$, with $d$ being the length of the semiconductor.

We will assume that:

* The induced $v$ causes motion in the positive x-direction.
* $E$, and therefore $v$, are constant.

Theoretically, the diffusion equation now becomes,

$P(x, t) = A(t)e^{-\frac{(x-vt)^{2}}{4Dt}}$.

Visualising this equation across time, we get:




but there is one more property that the simulation does not yet account for.

### Decay

Over time, the MCCs in the semiconductor will recombine with the opposite charges in the semiconductor as they drift across it. This leads to an exponential decrease in the number of MCCs across time. The rate of this exponential decay is dependent on the MCCs' average lifetime: their carrier lifetime, $\tau_{F}$. The decay is modelled as $e^{-\frac{t}{\tau_{F}}}$, so modifying the diffusion equation gives the final probability density distribution as

$P(x, t) = A(t) e^{-\frac{(x-vt)^{2}}{4Dt}} e^{-\frac{t}{\tau_{F}}}$.




## The Complete Simulation

Now that we have a complete understadning of the MCCs' motion, we can refine the simulation produced by the random-walk algorithm.

Up until now, the probability of a particle travelling in either x-direction has been equal upon each coin toss. If that probability were skewed, then the final position of each particle would be alligned towards a certain direction. Since $v$ is in the positive x-direction, we can increase the probability of the particle moving towards the right in the simulation.

Further, we can introduce a probability of decay, where each particle has a non-zero chance of being remvoed from the system. Note that by "system", I mean a distribution produced by a random-walk simulation.


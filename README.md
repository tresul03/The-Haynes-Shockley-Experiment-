# The-Haynes-Shockley-Experiment

The aim of this project is to understand the motion of minority charge carriers (MCCs) in locally p-type silicon semiconductors. I am the computational physicist in this project; I produce simulations on what our results should look like.

This REAMDE.md should provide a basic understanding of the motions of MCCs in one-dimensional semiconductors. I will not go into full derivations of the equations used. Rather, I will explain my approach used in deciding how to simulate the expeirment, and the limitations of the simulations themselves.

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

[diffusion](https://user-images.githubusercontent.com/102374376/232182922-491f5f13-fcab-4bcd-88d5-f390c2038849.mp4)

Note: this animation can be found in videos/diffusion.mp4.

The animation above shows an initial peak at $x, t, = 0$, corresponding to the point of charge injection into the semiconductor. The charge carriers then spread out acorss both x-directions, lowering the peak and widening the curve. Note that in this case, since the Gaussian represents a probability distribution across the length of the semiconductor, and the number of MCCs within the semiconductor remains constant, the area under this distribution also remains constant. This is why the lowering and broadening of the distribution's peak is observed.

![diffusion_colourmap](https://user-images.githubusercontent.com/102374376/232182939-b28827b2-7a3f-49a8-a00a-3522804b352c.png)

Above is another visualisation of the equation using a colourmap. A two dimensional grid, coordinates $x, t$, is formed, and each coordinate is coloured depending on the output of the diffusion equation at those coordinates.

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

![random](https://user-images.githubusercontent.com/102374376/232182955-292b77e7-36a4-48e0-b3ac-7aed6c7ff61d.png)

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

[drift](https://user-images.githubusercontent.com/102374376/232183043-e2b5a531-cbe3-43ed-be20-9068bc57bbe0.mp4)

but there is one more property that the simulation does not yet account for.

### Decay

Over time, the MCCs in the semiconductor will recombine with the opposite charges in the semiconductor as they drift across it. This leads to an exponential decrease in the number of MCCs across time. The rate of this exponential decay is dependent on the MCCs' average lifetime: their carrier lifetime, $\tau_{F}$. The decay is modelled as $e^{-\frac{t}{\tau_{F}}}$, so modifying the diffusion equation gives the final probability density distribution as

$P(x, t) = A(t) e^{-\frac{(x-vt)^{2}}{4Dt}} e^{-\frac{t}{\tau_{F}}}$,

which looks like this:

[decay](https://user-images.githubusercontent.com/102374376/232183092-61fb0b33-a54e-4470-a16a-86308d10ee58.mp4)

## The Complete Simulation

Now that we have a complete understadning of the MCCs' motion, we can refine the simulation produced by the random-walk algorithm.

Up until now, the probability of a particle travelling in either x-direction has been equal upon each coin toss. If that probability were skewed, then the final position of each particle would be alligned towards a certain direction. Since $v$ is in the positive x-direction, we can increase the probability of the particle moving towards the right in the simulation.

Further, we can introduce a probability of decay, where each particle has a non-zero chance of being removed from the system. Note that by "system", I mean a distribution produced by a random-walk simulation.

I'll explain these concepts further, but perhaps I should demonstrate what I mean by means of displaying the improved simulation first:

![random-multiple](https://user-images.githubusercontent.com/102374376/232182996-fbd077c1-afb5-4174-85e1-5a1e3da1dea5.png)

Here, we observe five systems, each having a constant probability of drift. The number of steps increases of each system is different. The higher the number of steps, the higher the probability of decay. The reason why the probability of decay increases with the number of steps is because the decay term of the diffusion equation becomes more dominant as time progresses. In the simulation, the probability of decay serves to represent the decay term. Since a larger number of steps indicates a longer-duration of simulation, it is implied that a larger number of steps represents a longer progression of time. Therefore, in order for the probability of decay to have an increased effect on the simulation as the number of steps increase - much like the decay term in the diffusion equation - the probability of decay must increase with the number of steps, as is done above. Perhaps a physical interpretation of this simulation will help. The number of steps in the simulation represents the progression of time. As time progresses, the width of a diffusion curve widens, and its peak is lowered.

Note that despite the resemblance of a Gaussian distribution that each system holds, I have not fitted to them a Gaussian best-fit curve. The reason for this is that Gaussian distrubutions are normalised, but accounting for decay in the simulation reduces the area under a system's curve, especially as the probability of decay increases. This denormalises the system, rendering it devoid of its Gaussian attribute.

Note further that this simulation is not free of limitations. I'll list three of them below:

* The simulation is one-dimensional. In reality, semiconductors are three-dimensional. What I've done is applied a plane parallel to the length of the semiconductor and simulated the motion of MCCs from a perpendicular perspective to that plane.
* I've assumed that no two particles' motions affect each other. In reality, there may exist a force of repulsion between any number of MCCs. The motion of the particles, therefore, is not completely random, contrary to what the simulation assumes.
* Through the random-walk, I've assumed that the motion of the MCCs themselves are random. This is an inaccuracy for a similar reason as discussed above; forces of attraction, the applied voltage across the semiconductor, and even external magnetic fields across the semiconductor have not been accounted for, none of which have a random nature.

For your interest, below are the effects of drift and decay, but viewed analytically:

![decay-static](https://user-images.githubusercontent.com/102374376/232183143-5b7b433a-ef87-47cb-a0ef-729ed58c8c6c.png)

As shown above, a very slight drift can be observed theoretically. The drift being very gradual is due to the carrier lifetime of the MCCs. A near complete decay of the system is expected to occur within $100\mu s$, so not much drift can occur, except under extremely high voltages.

# The-Haynes-Shockley-Experiment

This is a group project that, as of 6/3/23, I am working on with my group. The aim of this project is to understand the motion of minority charge carriers in locally p-type silicon semiconductors. I am the computational physicist in this project; I produce simulations on what our results should look like.

For context, when electrons or the absence of charge (referred to as "holes" in this case) are injected into a semiconductor, the injected charge carriers will begin to diffuse away from the point of injection. The reason why their motion can be modelled as diffusion is because:

* They are very large in quantity and can therefore be labelled as a continuous system
* Their motion is random
* Only two outcomes exist in regards to their motion; a charge carrier will move either in the positive or negative x-direction (assuming that the semiconductor is one-dimensional)

With the reasoning above, it is possible to predict the diffusion of these minority charge carriers within the semiconductor across time via a Gaussian distribution,

$P(x,t) = A(t)e^{-\frac{x^{2}}{4Dt}},$

where $A(t)$ is the normalisation function,

$A(t) = \frac{1}{\sqrt{4\pi Dt}},$

and D is the diffusion constant, given by

$D = \frac{\mu k_{b} T}{q}.$

https://user-images.githubusercontent.com/102374376/226909400-230ca4e8-aa51-4044-b80e-1f2a0e5b17b2.mp4

---
layout: post
title: "Buoyancy beyond 3D"
date: 2025-01-09
---

## Derivation of the 3D Buoyancy Formula

The buoyancy force acting on a submerged object can be derived from fundamental principles of fluid mechanics. Let's start with the pressure distribution in a static fluid.

### Pressure in a Static Fluid

In a static fluid, the pressure at a depth $h$ below the surface is given by:

$$P(h) = P_0 + \rho g h$$

where:
- $P_0$ is the atmospheric pressure at the surface
- $\rho$ is the fluid density
- $g$ is the acceleration due to gravity
- $h$ is the depth below the surface

![Pressure vs Depth]({{ "/assets/images/buoyancy-beyond-3d/pressure_vs_depth.png" | relative_url }})

### Force on a Submerged Object

Consider an object of arbitrary shape submerged in a fluid. The force on a small surface element $dA$ of the object is:

$$d\vec{F} = -P(h) \hat{n} \, dA$$

where $\hat{n}$ is the unit normal vector pointing outward from the object's surface, and the negative sign indicates that pressure acts inward (compressive).

![Submerged Object with Pressure Forces]({{ "/assets/images/buoyancy-beyond-3d/submerged_object_schematic.png" | relative_url }})

The total force on the object is obtained by integrating over the entire surface $S$:

$$\vec{F}_b = -\oint_S P(h) \hat{n} \, dA$$

Substituting the pressure expression:

$$\vec{F}_b = -\oint_S (P_0 + \rho g h) \hat{n} \, dA$$

$$= -P_0 \oint_S \hat{n} \, dA - \rho g \oint_S h \hat{n} \, dA$$

### Applying the Divergence Theorem

For a closed surface, $\oint_S \hat{n} \, dA = 0$ (the integral of the unit normal over a closed surface is zero). Therefore:

$$\vec{F}_b = -\rho g \oint_S h \hat{n} \, dA$$

Now, let's consider the vertical component (the $z$-direction, where $z$ increases downward). The vertical component of the force is:

$$F_{b,z} = -\rho g \oint_S h (\hat{n} \cdot \hat{z}) \, dA$$

where $\hat{z}$ is the unit vector in the vertical direction.

Since $h = z$ (depth equals vertical coordinate), and using the divergence theorem:

$$F_{b,z} = -\rho g \oint_S z (\hat{n} \cdot \hat{z}) \, dA = -\rho g \int_V \frac{\partial z}{\partial z} \, dV = -\rho g \int_V dV$$

where $V$ is the volume enclosed by the surface $S$.

### The Buoyancy Force

The integral $\int_V dV$ is simply the volume of the displaced fluid, $V_{\text{displaced}}$. Therefore:

$$F_{b,z} = -\rho g V_{\text{displaced}}$$

The negative sign indicates the force is upward (opposite to the direction of increasing $z$). Taking the magnitude:

$$F_b = \rho g V_{\text{displaced}}$$

This is **Archimedes' principle**: the buoyant force equals the weight of the fluid displaced by the object.

![Buoyancy Force vs Displaced Volume]({{ "/assets/images/buoyancy-beyond-3d/buoyancy_force.png" | relative_url }})

### Vector Form

In vector notation, the buoyancy force is:

$$\vec{F}_b = -\rho g V_{\text{displaced}} \hat{g}$$

where $\hat{g}$ is the unit vector in the direction of gravity (downward), so $-\hat{g}$ points upward.

### Key Result

For a 3D object of volume $V$ completely submerged in a fluid of density $\rho$:

$$\boxed{F_b = \rho g V}$$

This elegant result shows that the buoyancy force depends only on:
- The density of the fluid ($\rho$)
- The acceleration due to gravity ($g$)
- The volume of the displaced fluid ($V$)

The shape, orientation, and material of the object are irrelevant—only the displaced volume matters!

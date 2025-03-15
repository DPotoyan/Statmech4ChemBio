
### Monoatomic ideal gas

**Quantum density of states of an ideal gas**

![](./figs/pib-states.png)

$$E({\bf n}) = \frac{h^2}{8mL^2} {\bf n^2}$$

$$\Omega(N,V, E) = \int_{E(n)=E} dn = \frac{C_{3N-1}}{2^{3N}} \int \delta \Big(\frac{(8mE)^{1/2}L}{h}-{\bf n}  \Big) d {\bf n}$$

- A sum over all total quantum number of N 3D particles in a box ends up being a problem of finding the volume of an N-dimensional sphere

**Classical density of states of an ideal gas**

$$H(p,q) =\frac{p^2}{2m} = E$$

$${\Omega(E) = \frac{1}{N! h^{3N}}\int_{p^N,q^N} dp^N dq^N \delta(H(p,q) -E) =\frac{V^N}{N! h^{3N}} \int dp^N \delta(p^2/2m -E)}$$

$$ \Omega(E) = \frac{V^N}{N! h^{3N}} \delta V(R)$$

Where $\delta V(R)$ is a volume of a spherical shell with radius $R = (2mE)^{1/2}$ and thickness $\delta R = 1/2 (2m/E)^{1/2} \delta E$

**Volume of a sphere in N dimesnional space**

$$V(R) = \frac{\pi^{D/2}}{(D/2)!} R^D$$

For $D\rightarrow \infty$ we discover that most of the volume of the sphere is concentrated at its surface!
<br>

$$\delta V(R) = V(R) -V(R-\delta R) = C [R^D - (R-\delta R)^D] = CR^D [1-(1- (\delta R/R)^D)] = CR^D = V(R)$$

### Classical density of states of an ideal gas

$$\boxed{\Omega(E) = \frac{V^N}{h^{3N} N!} \cdot \frac{(2m\pi E)^{3N/2}}{(3N/2)!}}$$
 
$$\boxed{ S = log \Omega(E) = k_B N \cdot  \Big [ log \Big(\frac{V}{N \lambda^3}\Big) + \frac{5}{2}\Big]}$$

- Note linear dependence on N. Entropy is an extensive quantity!

- exponent 3/2 reflexts that each particle has 3 degrees of freedom

- $\lambda = \Big(\frac{3h^2 N}{4\pi m E}\Big)^{1/2}$ thermal de Broglie wavelength.

- This result know as "Sackur Tetrode equation" was known long before statistical mechanics. 


#### Equations of state for ideal gas

$$\frac{1}{T} = \frac{\partial S}{\partial E} = \frac{3}{2}k_B \frac{N}{E}$$

<br>

$$\frac{p}{T} =  \frac{\partial S}{\partial V} = k_B N \frac{1}{V}$$

<br>

$$\frac{\mu}{T} = -\frac{\partial S}{\partial N} = k_B T \cdot log \frac{N}{V} \lambda^3$$


### More Examples of using statistical Ensembles

::::{admonition} **Exercise: Random polymer chain**
:class: note

- Consider 1D polymer where $N$ monomers are randomly oriended with $+l$ and $-l$ orientation along the $x$ axis.
- Microcanonical ensmeble here is defined as all possible microstates given fixed value of end to end distance $X$ of this polymer. 
- Compute entropy $S(X)$ and argue that if polymer length is free to move most likely configuraiton would be where the polymer remains compact with nearly equal numbers of $ +l $ and $ -l $ orientations.

:::{dropdown} **Solution**

- We consider a 1D polymer consisting of $ N $ monomers, where each monomer can be oriented either in the $ +l $ or $ -l $ direction along the $ x $-axis. The total end-to-end distance of the polymer is given by:

$$
X = \sum_{i=1}^{N} s_i l
$$

- where $ s_i = \pm 1 $ represents the orientation of the $ i $th monomer.

**Microcanonical Partition Function**

- The total number of microstates corresponding to a given end-to-end distance $ X $ is determined by the number of ways to distribute $ N_+ $ monomers in the $ +l $ direction and $ N_- $ monomers in the $ -l $ direction, such that:

$$
N_+ + N_- = N, \quad N_+ - N_- = \frac{X}{l}
$$

- Solving for $ N_+ $ and $ N_- $,

$$
N_+ = \frac{N + X/l}{2}, \quad N_- = \frac{N - X/l}{2}
$$

- The number of microstates corresponding to a given $ X $ is given by the binomial coefficient:

$$
\Omega(X) = \binom{N}{N_+} = \frac{N!}{N_+! N_-!}
$$

- For large $ N $, we approximate using **Stirling’s approximation**:

$$
\ln \Omega(X) \approx N \ln N - N_+ \ln N_+ - N_- \ln N_-
$$

**Entropy Calculation**


$$
S(X) = k_B \ln \Omega(X)
$$

- Using Stirling's approximation and expressing $ N_+ $ and $ N_- $ in terms of $ X $,

$$
S(X) \approx k_B \left[ N \ln N - \frac{N+X/l}{2} \ln \frac{N+X/l}{2} - \frac{N-X/l}{2} \ln \frac{N-X/l}{2} \right]
$$

- To simplify, define the **normalized displacement** $ x = X / (N l) $

$$
S(X) \approx k_B N \left[ \ln N - \frac{1+x}{2} \ln \frac{1+x}{2} - \frac{1-x}{2} \ln \frac{1-x}{2} \right]
$$

- For small $x$, we can approximate using a Taylor expansion:

$$
S(X) \approx k_B N \left[ \ln 2 - \frac{x^2}{2} \right]
$$

- Thus, the entropy has a **maximum** at $X = 0 $, meaning the most probable configuration is one where the polymer remains compact with nearly equal numbers of $ +l $ and $ -l $ orientations.

- This shows a decrease in entropy as the polymer is more stretched ($|X|$ increases), reflecting fewer accessible configurations.


:::

::::
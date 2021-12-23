#!/usr/bin/env python
# coding: utf-8

# # NVE

# ## What is the relationship between StatMech and Thermo?

# - Equilibirum statistical physics reconciles macroscopic properties of matter in equilibirum states **(Thermodynamics)** with the microspic dynamics of consitutent atoms/molecules **(Probabilistic descirption of mechanics).** 
# 
# - Equilibrium statistical mechanics shows the molecular basis of thermodynamics giving us tools to calculate substance specific thermodynamic quantities from the first principles, such as heat capcities, free energy differences. These quanties serve as an input for thermodynamics becasue thermodynamics makes no refernce of microscopic world.  
# 
# > When learning statistical mechanics It is important to not have any illlusion about the role and value of thermodynamics and certainly not think that statistical mechanics is replacing thermodynamics! After all statistical mechanics is constructed for making a link between probabilistic world of micrrosopic particles and the deterministic world of thermodynamics. Within its domain of applicability (large systems, so called thermodynamic limit) Thermodynamics rules as an undipsuted theory agnostic to molecular realities which has never been defeated by any experiment to date. Statistical mechanical predictions obey the rules of thermodynamics and often thermodynamic arguments (second law, linear scaling of extensive quantities, Gibbs-duhem) is used to validate statistical mechanics claims. 

# ### Boltzmann's equation: "A bridge from probabilistic microscopic world to the thermodynamic world of macro(meso) systems"

# $$\boxed{S = k_B log \Omega}$$
# 
# - $S(N, V, E)$ is the entropy of an isolated system (we are in the NVE). Yes, it is the very same entropy that appears in thermdoynamic relations (Carnot engines, irreversibility and all that)!
# - $k_B =1.380649\cdot 10^{-23} J/K$,  Boltzmann's constant 
# - $\Omega$ quantifies number of micro-states **consistent with a macrostate of our system**. For instance number of states that in their totallity still have macroparameters $N, V, E$

# ### Lessons we learned from thermodynamics that can now be understood in new light
# 
# 1. Isolated systems eventually come to a terminal state of **equilibrium.**  System stays in equilibrium "forver" untill pertrubed from the outside.
# 
# 2. A few macrosocpic variables are sufficient for describing equilibirum, e.g $(E,N,V)$
# 
# 3. An extensive thermodynamic variable called entropy $S(E, N, V)$ exists which is a globally concave funcion and predicts thermodynamic equilibrium as a state with vanishing entropy variation $\delta S=0$ 
# 
# 4. Thermodynamic space is structured into non-crossing adiabats corresponding to $S=const$ planes on qhich system can be transformed quasistatically and reversibly (e.g stay in equilibrium). Leaving the adiabatic plane is posisble only through heat exchange (cooling or heating)! 

# ## How to quantify the micro states $\Omega$  for an isolated system? 

# ### Microstates in QM

# #### A collection of up/down spins
# 1. Consider a spin-1 particle with spin $|\uparrow \rangle$ and $|\downarrow\rangle$, hence this is a two state system. 
# > For an electron we have the magnetic moment $\mu = eh/2mc$, energy $E = −2\mu H$ Hmz and spin $m_z = \pm 1/2$. Where $H$ is the external magnetic field. 
# 
# 2. Now consider N non-interacting spin-1 particles. Now the system has $2N$ possible states. The 2 energy of the system is then given as $E = \sum^N_i  E_i$
# > The question boils down to partitioning $N_1$ up and $N_2$ down indistinguishable spin states. $N_1+N_2=N$ and $E = -\mu H N_1 -\mu H N_2$

# $$\boxed{\Omega (E,N)=\frac{N!}{N_1! N_2!} = \frac{N!}{\Big[\frac{1}{2}(N-E/H\mu)\Big]! \Big[\frac{1}{2}(N+E/H\mu)\Big]!}}$$
# 
# > Compare this expression to an expression for partitioning gas molecules into left and right regions of a container. Or to a porblme of random walk after N states. Notice any patterns :) 

# ### A collection of harmonic oscilaltors
# 1. 1D harmonic oscillator $E_n = \hbar \omega (n+1/2)$ with $n = 0, 1, 2, ...$ This system has infinitely many but still countable number of states. 
# 
# 2. Now consider  N harmonic oscillators. This can describe N atoms in a crystal, each vibrating around its mechanical equilibrium state independet of each other("Einstein model"). Although these are infinitely many states in this system they can be counted easily.
# 

# > The question boils down to finding how many states correspond to $n_1+n_2+...n_N = M$. In other words what is the degeneracy of the state correspodning to the total quantum number M? 
# 
# $$E(n_1,n_2,...n_N) = \sum^N_{i=1} \hbar \omega \Big(n_i+\frac{1}{2}\Big) = \sum^N_{i=1} n_i +\frac{N}{2}\hbar \omega
# $$

# The question is answered by partitioning M quanta of energy among N oscillators.  This is slightly different from previous example. The partitioning is analogus to putting M ideantical balls into N identical boxes. 
# 
# $$\boxed{\Omega(E,N) = \frac{(N+M-1)!}{M!(N-1)!} = \frac{(E/\hbar\omega+N/2-1)!}{(E/\hbar\omega-N/2)!(N-1)!}}$$

# ### A collection of particles in a box
# 
# 1. A 1 particle in a box. $E_n = \frac{\hbar^2 \pi^2}{2mL^2}(n^2_x+n^2_y+n^2_z)$. 
# 
# 2. Now consider N particles in a box. How many states can system have?
# > The question boils down to determining degeneracy of states with total quanta $n_1+n_2+...+n_{3N}$. 
# 
# $$\sum_{E=const} 1 = \int_{E=const} dn$$

# ### Microstates in (Quasi)Classical Mechanics. 
# 
# In Quantum mechanics we simply count the number of states which is natural and easy due to discretness of energy levels.  
# The question now is how to deal with the classical systems which have continuous energy functions?
# We clarify this issue using the example of 1D harmonic oscillator with an objective to find an expression coinciding with QM description.

# $$E=\Big(N+\frac{1}{2}\Big)\hbar\omega$$
# 
# - For a single harmonic oscillator in  the number of states correpsonding to E is obtained simply as:
# 
# $$N_E \approx \frac{E}{\hbar \omega} $$

# $$H(p,q) = \frac{p^2}{2m}+ \frac{m\omega^2 q^2}{2} = E$$
# 
# In CM, not having discrete count of states we are forced to somehow quantify the "volume" of states occupied by the harmonic oscillator at E as a measure of number of states
# 
# $$\Big[\frac{p}{(2mE)^{1/2}}\Big]^2 + \Big[\frac{q}{(2E/m\omega)^{1/2}}\Big]^2 = 1$$ 
# 
# 
# $$V = \pi  \cdot (2mE)^{1/2} \cdot (2E/m\omega)^{1/2} =\frac{2\pi E}{\omega}$$
# 
# We see that we are missing an important factor of $h$ which does not exist in CM! Otherwise the expression is identical to QM expression. Hence weintroduce a rule to divide the number of states in CM by $h$ 

# $$N_E = \frac{V}{h}$$
# 
# Generalizing the epxression for a collection of objects with 3N degrees of freedom we obtain:
# 
# $$\boxed{N_E = \frac{1}{h^{3N}}\int_{H(p^N,q^N)\leq E} dp^N dq^N}$$

# ### Density of States is more convenient to use than number of states

# $$\Omega(E) =\frac{d N(E)}{d E}$$
# 
# We will show that for macroscopic system it is convenient to work with denisty of states because number of states in outer thin shell $\Delta E$ is an excellent approximation to total number of states
# 
# $$N(E)\sim \Omega(E)\Delta E$$

# $$\boxed{N_E = \frac{1}{h^{3N}}\int dp^N dq^N \theta(H(p^N,q^N) -E)} $$
# 
# $$\boxed{\Omega(E) = \frac{1}{h^{3N}}\int dp^N dq^N \delta(H(p^N,q^N) -E)}$$
# 
# <br>
# 
# > Where $\theta(x-a)$ is a step function (Heviside function) derivative of which gives rise to delta function $\delta(x) =\frac{d}{dx}\theta(x-a)$

# ### Watch out for N! The indistingushability of the particles has consequences for thermodynamics
# 
# Since we are using classical mechanics where all particles can be distingushed and labeled, we need to correct for this artifact if we want to study large N collection of identical atoms and molecules:
# 
# $$\boxed{\Omega(E) = \frac{1}{N! h^{3N}}\int_{p^N,q^N} dp^N dq^N \delta(H(p,q) -E)}$$

# ## Microcanonical Ensemble and "equal a priori probabilities" postulate.  

# $$\boxed{P(E) = \frac{1}{\Omega(E)}=const}$$
# 
# - Each state in the $NVE$ ensemble is sampled with equal probabilities. Why? Becasue no microstate has any more priviledged status than the other. 
# 
# - The task of quantifying probabilities in the thermodynamic processes under $NVE$ conditions reduces to quantifying changes in the number(density) of states.

# ## Examples of using NVE ensemble to derive fundmental equation 

# ### Example-1: A three spin state
# 
# 3 spin state can adopt many different states with different energies. 
# 
# If we know the total energy is $E = -\mu H$ Then we have microcanonican ensemble with three states 
# 
# $$N(E) = \{++-, +-+, -++, \}$$
# 
# $$P(E) = \frac{1}{N(E)} = \frac{1}{3}$$
# 
# $$S(E=-3\mu H) = k_B log 3$$
# 
# > Can you write down entropy for other energy values?

# ### Example-2: Monoatomic ideal gas

# $$H(p,q) =\frac{p^2}{2m} = E$$
# 
# $${\Omega(E) = \frac{1}{N! h^{3N}}\int_{p^N,q^N} dp^N dq^N \delta(H(p,q) -E) =\frac{V^N}{N! h^{3N}} \int dp^N \delta(p^2/2m -E)}$$
# 
# $$ \Omega(E) = \frac{V^N}{N! h^{3N}} \delta V(R)$$
# 
# Where $\delta V(R)$ is a volume of a spherical shell with radius $R = (2mE)^{1/2}$ and thickness $\delta R = 1/2 (2m/E)^{1/2} \delta E$

# **Volume of a sphere in N dimesnional space**
# 
# $$V(R) = \frac{\pi^{D/2}}{(D/2)!} R^D$$
# 
# For $D\rightarrow \infty$ we discover that most of the volume of the sphere is concentrated at its surface!
# <br>
# 
# $$\delta V(R) = V(R) -V(R-\delta R) = C [R^D - (R-\delta R)^D] = CR^D [1-(1- (\delta R/R)^D)] = CR^D = V(R)$$
# 

# ### Classical density of states of an ideal gas
# 
# $$\boxed{\Omega(E) = \frac{V^N}{h^{3N} N!} \cdot \frac{(2m\pi E)^{3N/2}}{(3N/2)!}}$$
#  
# $$\boxed{ S = log \Omega(E) = k_B N \cdot  \Big [ log \Big(\frac{V}{N \lambda^3}\Big) + \frac{5}{2}\Big]}$$
# 
# - Note linear dependence on N. Entropy is an extensive quantity!
# 
# - exponent 3/2 reflexts that each particle has 3 degrees of freedom
# 
# - $\lambda = \Big(\frac{3h^2 N}{4\pi m E}\Big)^{1/2}$ thermal de Broglie wavelength.
# 
# - This result know as "Sackur Tetrode equation" was known long before statistical mechanics. 

# ### Quantum density of states of an ideal gas
# 
# ![](./figs/pib-states.png)

# $$E({\bf n}) = \frac{h^2}{8mL^2} {\bf n^2}$$
# 
# - ${\bf n} = \sum^{i=N}_{i=1} n_i^2$. A sum over all total quantum number of N 3D particles in a box

# $$\Omega(N,V, E) = \int_{E(n)=E} dn = \frac{C_{3N-1}}{2^{3N}} \int \delta \Big(\frac{(8mE)^{1/2}L}{h}-{\bf n}  \Big) d {\bf n} \approx \frac{V^N E^{3N/2}}{h^{3N}}$$

# ## Thermal, Mechanical and chemical equilibrium
# 
# $$\Omega(E) = \sum_{E_1} \Omega_1(E_1) \Omega_2 (E-E_1)$$
# 
# $$log \Omega(E) = log \Omega_1(E_1) + log \Omega_2(E-E_1)$$
# 
# Recall that for ideal gas we have $\Omega(E) = C V^N E^{3/2 N}$. And now consider a probability $P(E_1) = \Omega_1(E_1) \Omega_2 (E-E_1)$ for a one particular energy partitioning among systems with $E_1$ going to first subsystem and $E-E_1$ to second.
# 
# $$\frac{\partial logP(E_1)}{\partial E_1} \Big |_{E_1=U_1}= \frac{3}{2}\frac{N_1}{U_1} - \frac{3}{2}\frac{N_2}{U_2} = 0$$
# 
# Using definition of entropy we get the most probable value of energy $(U_1)$ corresponding to the equilibirum state 
# $$\frac{1}{k_B T} = \frac{3}{2}\frac{N_1}{U_1} = \frac{3}{2}\frac{N_2}{U_2}$$
# 
# 
# 

# ### Equations of state for ideal gas
# 
# $$\frac{1}{T} = \frac{\partial S}{\partial E} = \frac{3}{2}k_B \frac{N}{E}$$
# 
# <br>
# 
# $$\frac{p}{T} =  \frac{\partial S}{\partial V} = k_B N \frac{1}{V}$$
# 
# <br>
# 
# $$\frac{\mu}{T} = -\frac{\partial S}{\partial N} = k_B T \cdot log \frac{N}{V} \lambda^3$$
# 
# 
# ### Quasistatic process and Irreversibility
# 
# From the NVE esnsemble reasoning we can now state that quasistatic process corresponds to process which does not change in the number of microstates. That is removal of a constraint keeps the "volume" of microstates intact.  
# 
# $$\Delta S = k_B log \frac{\Omega_f}{\Omega_i} = 0$$
# 
# On the other hand once the number of microstates grows upon removal of a constraint then re-instating the constraint will not shrink the "volume" of microstate space. 
# 
# $$\Delta S = k_B log \frac{\Omega_f}{\Omega_i} > 0$$

# ### Problems

# #### Problem-1
# Write a python code to quantify the number of states of particle in a box at energy $E = C(n^2_x +n^2_y+n^2_z)$ where C is a constant which you can set  to 1. You can do this by generating three integer numbers satisfying $n^2_x +n^2_y+n^2_z < E$.
# 
# - Try differnet energy values, $E = 10, 20, 50, 100$
# 
# - Can you think of some Monte Carlo ideas to estimate number of states?

# ##### Problem-2: 2D Spin lattice
# - Generate  16 by 16 lattice with spin up and down states. This can be done by using 
# 
# ```python
# np.random.choice([-1,1],size=(16,16))
# ``` 
# 
# Visualize the lattice via plt.imshow(latttice)
# 
# - Write a function to compute the total energy by using $E_{ij} = -\sum_{ij} s_i s_j$ where the summation runs only between nearest neighbours of the lattice. E.g each spin has only four neighbours to interact with. 
# 
# - Generate 1000 states by randomly flipping spins in batches of 1,2,4,8. E.g pick random spins and flip the sign. Plot the distribution of energies that results. Comment on the number of states as a function of energy. 
# 
# - What is the probability of observing each configuration? What are the total number of states? Can you comment on efficiency of estimating total energy via random sampling. 
# 
# - Enforce periodic boundary conditions, e.g allow each spin at the endge to interact with spin on the other side. E.g spin at $(5,16)$ now can interact with spin at (5,1). Can you comment on the contribution of energy that results from inclduing the surface spins?
# 

# ### Problem-3: Shottky defects in NVE: Computing number of states via lattice models 
# 
# Schotky defects are vacancies in a lattice of atoms. Creating a single vacancy costs an energy. Consider NVE ensemble of lattice with n vacacnies(defects) in an N-lattice model of solid material. The total energy is solely a function of defects in this model $E=n\epsilon$
# 
# - Write down number of states in NVE ensemble and compute the entropy via Boltzman formula. Plot number of states as a function of energy. You can use log of number of states for plotting. 
# 
# - Compute how the temperature would affect the fraction of vacancies on the lattice. Plot fraction of vacancies as a function of temperature. 
# 
# - How would the total energy depend on temperature $T$. Derive expression for the high temeprature limit ($\frac{\epsilon}{k_b T} \gg 1$). 
# - Plot total energy as a function of temperature E(T)

# #### Problem-4: Lattice gas
# 
# Consider a lattice gas of N particles distributed among V cells (with $N\geq V$). Suppose that each cell may be either empty or occupied by a single particle. The number of microscopic states of this syste will be given by:
# 
# $$\Omega (N, V) = \frac{V!}{N! (V-N)!}$$
# 
# - Obtain an expression for the entropy per particle $s(v)=\frac{1}{N} \cdot S(N,V)$ where $v=\frac{V}{N}$. 
# - From this simple fundamental equation, obtain an expression of equation of state $p/T$. - Write an expansion of $p/T$ in terms of density $1/v$. Show that the first term gives Boyle law of ideal gases. 
# - Sketch a graph of $\mu/T$, where $\mu(\rho)$ is a chemical potential as a function of density. Comment on $\rho\rightarrow 0$ and $\rho\rightarrow 1$ limits
# 

# #### Problem-5: Entropic origin of polymer elasticity
# 
# > Solve the problem 3.3 from the book.

#!/usr/bin/env python
# coding: utf-8

# # NPT

# ### Open systems 
# ![](./figs/bottleocean.jpg)

# $NVT \rightarrow \mu VT$ by releasing N=const constraint to get $\mu=const$
# 
# In the $\mu VT$ ensemble, the system samples different number of particles $N$ consistent with $\mu =const$ constraint imposed by putting system in contact with infinitely large chemostat.  
# 
# $$E_{tot} = E_r + E_i$$
# 
# $$N_{tot} = N_r + N_i$$
# 
# 
# $$\Omega_{tot}(E_{tot}, N_{tot}) = \sum_N \sum_i \Omega_r(E_{tot}-E_i, N_{tot}-N_i) \cdot \Omega(E_i, N_i)$$

# ### $\mu V T Ensemble$

# Let us single out one micro-state $E_i, N$ of our system $\Omega(E_i, N) =1$ and see what would be its probability in $\mu VT$ ensemble.
# 
# $$p(E_i, N_i) = \frac{\Omega_r(E_{tot}-E_i, N_{tot}-N_i)}{\Omega_{tot} (E_{tot}, N_{tot})} = \frac{e^{S_r(E_{tot}-E_i, N_{tot}-N_i)/k_B}}{e^{S_{tot}(E_{tot}, N_{tot})/k_B}}$$
# 
# Where we have used use the microcanonical ensemble of **system+reservoir** to cast the problem in terms of probabilities of **the system**.

# ### Deriving probability distribution (complete analogy with NVT). 
# 
# A more revealing is the expansion around system's average energy $\delta E = E-U \sim O(N^{1/2})$  and average particle number  fluctuations  $\delta N = N-\bar{N} \sim O(N^{1/2})$ around which are small:  
# 
# **Entropy of reservoir**
# 
# 
# 
# $$S_r(E_{tot}-E_i, N_{tot}-N) = S_r(E_{tot}-U + \color{blue}{ [U-E_i]}, N_{tot}-\bar{N} + \color{green}{[\bar{N}-N_i]})$$
# 
# 
# $$S_r(E_{tot}-U + \color{blue}{ \delta E}, N_{tot}-\bar{N} + \color{green}{\delta N}) \approx S_r(E_{tot}-U, N_{tot}-\bar{N}) +\frac{\partial S_r(E, N)}{\partial E} \color{blue}{\delta E} + \frac{\partial S_r(E, N)}{\partial N} \color{green}{\delta N}$$
# 
# $$ S_r =  S_r(E_{tot}-U, N_{tot}-\bar{N}) + \frac{1}{T}\color{blue}{ \delta E} - \frac{\mu}{T} \color{green}{\delta N}$$
# 
# **Entropy of total system**
# 
# Let us now use additivity of entropy of the combined syste+resoervioir in equilibrium: 
# 
# $$S_{tot}(E_{tot}, N_{tot}) = S_r(E_{tot}-U, N_{tot}-\bar{N})+S(U, \bar{N})$$
# 
# 
# Combining the expressions of total and reservoir entropies we get the probability distirbution of system's energy and particle numbers 
# 
# $$p(E_i, N_i) =\frac{e^{S_r(E_{tot}-E_i, N_{tot}-N_i)/k_B}}{e^{S_{tot}(E_{tot}, N_{tot})/k_B}} = \frac{e^{-\beta E_i} e^{\beta \mu N}}{e^{-\beta \Psi}}$$

# **Grand-Canonical distribution**
# 
# $$\boxed{p(E_i, N_i) = \frac{e^{-\beta(E_i -\mu N_i)}}{Z_G}}$$
# 
# **Grand-Canonical Partiation Function**
# 
# $$\boxed{Z_G = \sum_i E^{-\beta (E_i-\mu N_i)}}$$ 
# 
# **Free Energy** 
# 
# $$\boxed{Z_G = e^{-{\beta \Psi}}}$$ 
# 
# $$\boxed{\Psi = -\beta^{-1} log Z_G}$$

# ### Connections with $NVE$ and $NVT$

# **Grand canonical partition function**
# 
# $$Z_G = \sum^{N=\infty}_{N=0} \Big [ \sum_i e^{-\beta E_i}  \Big ]e^{\beta \mu N} = \sum^{N=\infty}_{N=0} Z(N,V,T)e^{\beta \mu N}$$
# 
# Hence why we call partition function **Grand canononical** as it is expresed as exponentially  weighted (by $e^{\beta \mu N}$) summation of canonical parition functions over all values of N. 
# 
# **Laplace and Legendre transform connection with NVE and NVT**
# 
# $$\boxed{p(E,N) = \frac{1}{Z_G} \Omega(E,N) e^{-\beta(E-\mu N)} = \frac{1}{Z_G} e^{-\beta \Psi(T,V,\mu))}}$$
# 
# $$\boxed{\Psi(T,V, \mu) = E- TS -\mu N}$$
# 
# The free energy in grand canonical parition function is obtained by legendre transforming microcanonical ensemble over conjugate variables: $(S, T)$ and $(N, \mu)$.
# 
# **Using Euler's relation**
# 
# $$\boxed{\Psi(T,V, \mu) = -PV}$$

# ### Grand-canonical potential

# **Recall Gibbs equation of thermodynamics**
# 
# $$dE = TdS -pdV +\mu dN$$
# 
# **Free energy minimization with $(T,V, \mu)$**
# 
# Using Gibbs-Duhem we get the connection with the rest of the intensive variable changes
# 
# $$\boxed{d\Psi(\mu, V, T) = -SdT -p dV -Nd \mu}$$
# 
# For constant temperature and chemical potential we have a simple connection with pressure and volume
# 
# $$\boxed{d\Psi_{\mu, T} = d (E-TS-\mu N) = -pdV}$$
# 
# 
# **Equations of state**
# 
# - $$S = -\frac{\partial \Psi}{\partial T}$$
# 
# - $$p = -\frac{\partial \Psi}{\partial V}$$
# 
# - $$N = -\frac{\partial \Psi}{\partial \mu}$$

# ### Fluctuations
# 
# $$\langle N \rangle  = \sum_i p_i N_i = \frac{\partial log Z_G}{\partial (\beta \mu)}$$
# 
# $$\sigma^2_N =\langle N^2\rangle - \langle N \rangle^2 = \frac{\partial^2 log Z_G}{\partial (\beta \mu)^2} = \frac{\partial \langle N \rangle}{\partial (\beta \mu)}$$
# 
# $$\sigma^2_N = \frac{N^2 k_B T \kappa_T}{V} \sim O(N)$$
# 
# > Notice anology with NVT where we found $\sigma^2_E = k_B T^2 C_v$ for energy fluctuations with $C_v\geq 0$ implying stability. For particle fluctuataions instead of heat capacity we have the isothermal compressibility $\kappa_T = -\frac{1}{V}\frac{\partial V}{\partial p} \geq 0$
# 
# $$\frac{\sigma_N}{\langle N \rangle} \sim O(N^{-1/2})$$

# ### Ideal Gas

# 
# $$Z(T,V,N) = \frac{1}{N!} \Big( \frac{V}{\lambda^3} \Big)^N\,\,\,\,$$
# 
# - **Thermal wavelength** $\lambda = \frac{h}{(2 \pi mk_B T)^{1/2}}$
# 
# $$Z_G = \sum^{N=\infty}_{N =0} Z(T,V,N) e^{\beta \mu N} = \sum^{N=\infty}_{N =0} \frac{1}{N!} \Big( e^{\beta \mu} \frac{V}{\lambda^3} \Big)^N = exp\Big(z \frac{V}{\lambda^3} \Big)$$
# 
# 
# - **Fugacity** $z = e^{\beta \mu}$
# 
# $$\langle N \rangle = \frac{\partial log Z_G}{\partial (\beta \mu)} = \frac{V}{\lambda^3} e^{\beta \mu}$$
# 
# $$\mu  = k_B T log \frac{N \lambda^3}{V} = k_B T log [(k_B T)\lambda^3 \cdot p ] = \mu^0 (T) + k_B Tlog p $$
# 
# $$\sigma^2_N = \frac{N^2 k_B T \kappa_T}{V} = N$$
# 
# $$\kappa_T = \frac{NV }{N^2 k_B T} = \frac{1}{p} \geq 0$$

# #### System of dilute uncorrelated particles = ideal gas
# 
# $$\sigma^2_N = \langle N \rangle$$

# ### Molecular adsorption on the surface
# 
# ![](./figs/adsorption.png)

# $$Z_G = z^N_G$$

# #### One site one molecule model
# 
# $$z_G = 1 +e^{-\beta (\epsilon-\mu)}$$
# 
# $$\langle n \rangle =\frac{0+1\cdot e^{-\beta(\epsilon - \mu)}}{Z_G} = \frac{1}{e^{-\beta(\mu-\epsilon)}+1}$$
# 
# $$\langle E \rangle =\frac{0+\epsilon\cdot e^{-\beta(\epsilon - \mu)}}{Z_G} = \epsilon \langle n \rangle $$
# 
# For the idea gas $\mu  = k_B T log \frac{p}{p_0}$
# 
# $$\langle n \rangle = \frac{p}{p_0e^{\beta \epsilon}+p}$$
# 
# > This is known as Langmuir isotherm. 

# #### Multi-stide binding of molecular gas with internal states
# 
# 1. Molecule A binds to one site and adopts 2 conformations. 
# 2. Two molecules of B can bind one site. When one molecle is bound it has one conformation and when two bound there are 5 conformations.  
# 
# 

# $$z_G = 1 + 2 e^{-\beta(\epsilon_A - \mu_A)}+ e^{-\beta(\epsilon_B - \mu_B)} +5 e^{-2\beta(\epsilon_B - \mu_B)}$$

# ## Problems

# ###  $NVT-NVE-\mu V T$ 
# 
# 1. Consider a three level single particle system with five microstates with energies 0, ε, ε, ε, and 2ε. What is $\Omega(\epsilon n)$  n=0,1,2 for this system? What is the mean energy of the system if is in equilibrium with a heat bath at temperature T ?
# 
# 2. Derive an expression for the chemical potential of an ideal gas using clssical mechanics model for energy $E=\frac{p^2}{2m}$ in the $\mu VT$ ensemble evaluate the fluctuations in particle number. 
# 
# 3. Consider a system in equilibrium with a heat bath at temperature $T$ and a particle reservoir at chemical potential $\mu$. The system can have a minimum of one and a maximum of four distinguishable particles. The particles in the system do not interact and can be in one of two states with energies zero or $\Delta$. Determine the (grand) partition function of the system.
# 
# 4. Combine the Gibbs formula of Entropy $S=-k_B \sum_i p_i log p_i$ with the Grand canonical prbability distribution $P(E_i,N_i)=\frac{e^{-\beta E_i+\mu N_i}}{Z_G}$ to show that $\beta PV=log Z_G$<br>
# 
# 5. Derive partition function for a pressure ensemble $(T, p, N)$ and show its connection with microcanonical ensemble $N V E$
# 
# 6. At a given temperature T a surface with N_0 adsorption centers has $N\neq N_0$ adsorbed molecules. Suppose hat there are no interactions between molecules. 
# 
#     - Show that the chemical potential of adsoprbed gas is given by: $\mu  = k_B T log \frac{N}{N_0 - N a(T)}$
# 
#     - What is the meaning of $a(T)$

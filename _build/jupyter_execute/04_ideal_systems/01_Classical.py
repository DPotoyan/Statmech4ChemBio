#!/usr/bin/env python
# coding: utf-8

# # Classical gases

# ## Maxwell-Boltzmann statistics

# **Distingusihable vs indistingusihable particles**
# 
# $$Z_N = \frac{1}{N!} Z^{dist}_N$$
# 
# 
# $$\Omega_N = \frac{1}{N!} \Omega^{dist}_N$$
# 
# - Treat particles as distinguishable but divide in the end by $N!$ to get the correct extensive entropy and free energies.
# 
# - This way of handling parititon functions is called "Maxwell-Boltzmann" statistics which is widely applicalble in the "classical regime"

# **Example of MB statistics** 
# 
# Consider 2 particles each having 3 energy levels $\epsilon_1, \epsilon_2, \epsilon_3$
# 
# $$Z_2 = \frac{1}{2!}(e^{-\beta \epsilon_1}+e^{-\beta \epsilon_2}+e^{-\beta \epsilon_3})^2$$
# 
# $$Z_2 = \frac{1}{2} \big[e^{-2\beta \epsilon_1}+e^{-2\beta \epsilon_2}+e^{-2\beta \epsilon_3}\big]+\big[e^{-2\beta (\epsilon_1+\epsilon_2)}+e^{-2\beta (\epsilon_1+\epsilon_3)}+e^{-2\beta (\epsilon_2+\epsilon_3)}\big]$$
# 
# 
# - **Multiply occupied states** are unphysically suppressed.
# 
# - **Single occupied states** are nicely weighted which removes the double-counting.
# 

# ### Occupation numbers representation of a microstate
# 
# Preparing ground for the quantum statistics we adopt an **occupation number representation of a microstate**. Occupation number or orbital representation explicitely tracks the occupation of single particle eigenvelues. In this representation a **microstate** is idenitfied with the  occupancy vector $[n_1, n_2, ... n_N]$ specifiying number of particles populating every fixed energy level.  
# 
# $$E= \sum_i n_i \epsilon_i$$
# 
# $$N = \sum_i n_i$$

# ### In classical mechanics particles are distinguishable
# 
# The number of different ways to distribute occupation numbers are 
# 
# $$\Omega(n_1, n_2, ...) = \frac{N!}{n_1! n_2!... n_N!}$$
# 
# $$Z_N = \sum_{n_1, n_2, ... n_N} \Omega(n_1, n_2, ...) e^{-\beta (n_1 \epsilon_1 +n_2 \epsilon_2 + ...)} = \sum_{n_1, n_2, ... n_N} \frac{N!}{n_1! n_2!... n_N!} [e^{-\beta \epsilon_1}]^{n_1} [e^{-\beta \epsilon_2}]^{n_2} ...$$
# 
# The last expeansion is seen as a a polynomial expenasion leading to the factorization of partiion function as we would expect for the non-interacting nature of the system
# 
# $$Z =(e^{-\beta \epsilon_1}+e^{-\beta \epsilon_2}+ ...)^N= Z^N_1 $$
# 
# $$Z_1 =\sum_j e^{-\beta \epsilon_j}  $$
# 
# We this recover canonical partition function for N non-interatice particles. The partion function however needs to be mulitpled by $N!$ to account for the indistinguishability. 
# 
# $$Z = \frac{1}{N!}Z^N_1$$

# ## Boltzman gas and the original derivation of Boltzman distribution
# 
# Boltzmann's original derivation of canonical distirbution has followed the same argument despite the absence of quantum mechanics and understanding of discretnesss of energy levels. Boltzman realized that fluctuations around the average $U$ are expected to be very small $O(N^{1/2})$. To find the peak of the distirbution, that is most likely distribution of average energy among members of ensemble ${n_1, n_2, ... n_k}$ given the constant number of particles $N$ average energy $U$. Thus the problem is reduced to maximizing number of microstates under given constraints:
# 
# $$\sum_{k} n_{k}=N$$
# 
# $$ \sum_k n_k E_k = N U$$
# 
# Recall that we every configuration in the $NVE$ ensemble is equally likely. Therefore the set of ${n_1,n_2,...}$that maximizes $\Omega(U)$ is the most likely to occur. This is the eseence of Boltzmann's original derivation. 
# 
# $$\Omega(U) = \frac{N!}{n_1! n_2! n_3! ... }$$
# 
# <br>
# 
# $$log \Omega(U) \approx  NlogN -\sum_k n_k log n_k = N \Big[ -\sum_k \frac{n_k}{N}log\frac{n_k}{N} \Big] = \frac{1}{k_B}S(U)$$
# 
# Last equality, we will come to recognize as a general expression for the entropy (first derived by J W Gibbs)! Notice that it is an extensive quantity propotional to N where $p_i = \frac{n_i}{N}$ can bee seen as probabilities of states in the ensemble.   
# 
# $$\boxed{S = -\sum_i p_i log p_i}$$
# 
# ### Maximizing number of states with Lagrange multipliers
# 
# Constrained optimization is done via Lagrange multipliers. Here we also threw away constant facotrs $NlogN$ keeping only terms dependening on $n_k$ explicitely. 
# 
# $$I(n_1, n_2,...n_k...) = -\sum_k n_k log n_k - \lambda_1 \sum n_k -\lambda_2 \sum_k n_k E_k $$
# 
# $$\frac{\partial }{\partial n_k} I = 0  = -log n_k -\lambda_1 -\lambda_2 E_k$$
# 
# $$n_k = e^{-(1+\lambda_1)} e^{-\lambda_2 E_k}$$
# 
# After normalization we eliminate $\lambda_1$ and identify $\lambda_2$ with $\beta =\frac{1}{k_B T}$ which has units of inverse energy. 
# 
# $$ p_k = \frac{n_k}{N} = \frac{e^{-\beta E_k}}{Z} $$

# ### Average and fluctuations of occupancy numbers
# 
# $$\langle n_i \rangle = - \frac{1}{\beta}\frac{\partial log Z}{\partial \epsilon_i}$$
# 
# $$p_i = \frac{n_i}{N} = \frac{e^{-\beta \epsilon_i}}{Z_i}$$

# ### Validity of the classical regime
# 
# - A sufficient conditon for the validity of the classical regime is the low mean occuopanyc of energy levels $\epsilon_i$. 
# 
# $$\bar{n}_i \ll 1\,\,\,\,\, for\,\,\,\, all\,\,\,\, i$$ 
# 
# Using translational partition function for a free particle in a box $Z_1 = V \Big(\frac{2\pi m k_B T}{h^2} \Big)^{3/2}$ we express low mean occupancy limit in terms of microsocipic parameters: 
# 
# $$\bar{n}_i = N e^{-\beta \epsilon_i}/Z_1 \ll 1$$
# 
# $$\frac{N}{V} \Big(\frac{h^2}{2\pi m k_B T} \Big)^{3/2} \ll 1$$ 
# 
# $$\lambda^3_T \ll \frac{N}{V} = l^3$$
# 
# - Classical limit is the limit where thermal wavelength is much smaller than interatomic distances. 

# ## Non-interacting molecular gases 
# 
# ### Translational degrees of freedom: particle in a box
# 
# $$E_{n_x, n_y, n_z} = \frac{h^2}{8m L^2}(n^2_x+n^2_y+n^2_z)^2$$
# 
# $$ Z \approx \Bigg [\int dn e^{-\beta \frac{h^2 n^2}{8m L^2}} \Bigg]^{3N} = V \Bigg[\frac{2\pi m k_B T}{h^2} \Bigg]^{3N/2}$$
# 
# ### Rotatational degrees of freedom: Rigid rotor model 
# 
# $$E = \frac{\hbar^2}{2I} J (J+1) $$
# 
# $$Z \approx \int^{J=\infty}_{J=0} (2J+1)e^{-\Big[\beta \frac{\hbar^2}{2I} J (J+1)\Big]}\approx \frac{T}{\theta_{rot}}$$
# 
# - Where $\theta_{rot} = \frac{\hbar^2}{2 I_0 k_B}$ is called rotational temperature. 
# 
# ### Vibrational degrees of freedom: Harmonic oscillator model
# 
# $$E_n = \hbar \omega (n+1/2)$$
# 
# $$z = \sum^{n=+\infty}_{n=0} = e^{-\frac{1}{2}\beta \hbar \omega} (1 + e^{-\beta\hbar\omega}+e^{-2\beta\hbar\omega}+...) = \frac{e^{-\frac{1}{2}\beta \hbar \omega}}{1-e^{-\beta\hbar\omega}}$$
# 
# $$Z = z^N$$
# 
# $$E = \frac{\partial log Z}{\partial (-\beta)} = N\hbar \omega \Big(\frac{1}{2}+ \frac{1}{1+e^{\beta\hbar\omega}} \Big) $$
# 
# - When $T \rightarrow 0$ we are left with zero point energies $E \rightarrow \frac{N \hbar \omega}{2}$
# 
# - When $T \rightarrow \infty$ we get equipartion of energy! $E \rightarrow \frac{3}{2} N k_B T$
# 
# ### Partition function for a molecular gas
# 
# <br>
# 
# $$E = E_{transl}+E_{vib}+E_{rot}+E_{elec} $$
# 
# <br>
# 
# $$Z = Z_{transl} Z_{vib} Z_{rot} Z_{elec} $$
# 
# > $\frac{1}{N!}$ must go inside $Z_{tranls}$ to account for indistinguishability

# ### Equipartion theorem
# 
# $$U(x) = U(x_0) +U^{'}(x-x_0) +\frac{1}{2}U^{''}(x-x_0)^2 +...$$
# 
# $$U_{harm}(x) = U(x_0) +  \frac{1}{2}U^{''}(x-x_0)^2 = U_0 + \frac{1}{2}\kappa (x-x_0)^2$$
# 
# $$\langle U \rangle = \int p(x) U(x) dx = \frac{\int U(x) e^{-\beta U(x)}dx}{\int e^{-\beta U(x)}dx}$$
# 
# $$U(x) = U_0 + \frac{k_B T}{2}$$
# 
# > Notice the spring constant does not figure in the average energy expression! 
# 

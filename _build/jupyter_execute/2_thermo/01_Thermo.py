#!/usr/bin/env python
# coding: utf-8

# # Review of thermodynamics principles

# ### Summary of the key principles thermodynamics
# 
# 1. Thermodynamics is a **phenomoneological** theory. Phenomoneological means that the macrosocpic phenomena are descibred terms of few quanitites which can be observed and measrued by macroscopic devices without any refernce to microscopic details.
# 2. The variables one deals in thermodynamics can be classifeid as **extensive** and **intensive**. Former depends on the size of system (volume, number of particles, energy, entropy) the latter is size independent (temperature, pressure, magnetic field, etc). **Extensive variables** are a priviledges set of variables which uniquely define the equilibrium sates. **Intensive variables** are derived from extensive ones and are conjugate pairs to extensive ones. E.g $V-P$, $S-T$, $N-\mu$ are conjugate pairs. Conjugate means one can replace extensive variables by intensive variables through legendre transformation.
# 3. **Equilibrium** is a special state of matter where the most simple descirption is possible in terms of extensive variables or properly chosen set of extensive+intensive variables. Equilibrium state is defined as a state where on the timescale of interest no measurable variable dsiplays any changes over time. In particular there are no macrosopic fluxex or flows of any form of energy or matter. In equilibrium, macroscopic matter assumes a particularly simple description in terms of **few extensive quantites**. 
# 4.  **Fundmanetal equation** in thermodynamics is the equation that binds together all extensive variables, e.g $E(U,V,S,N_1, N_2, ...)$.      
# 5. **Transformations between equilibrium states** is the central task of thermodynamics. Thermodynamics is fully equiped to predict the equilibrium state B which results form equilibrium state A through spontenous transformation upon removal of a **constraint.**  
# 6. **Quasi-static path: a dense successtion of equilibrium states** that connects A with B in the space of extensive variables is constructed in order to compute changes in thermodynamic variables between states A and B. This equilibrium path is necessarily quasistatic for ensuring that system does not at all deviate from equilibrium state during transformation. The quasistatic path can also be reversible when the path from B to A can be re-traced with zero change in the universe while the system remains in the state of equilibrium. This necessitates intoduction of Entropy which differnetiates reversible from non-reversible changes. 
# 7. Thermodynamic space is folliated into non-corssing **adiabats**. These adiabats are planes on whcih system can be transformed reversibly.  The only way to "jump" from one adiabt to another is by heating or cooling the system, e.g transfer of heat. 
# 8. The second Law establishes the directionality of processes. The first law is a reflection of conservation of "mechanical energy" in many body systems such studied in thermodynamics. 
# 9. Any change in adiabatic system is accompanied either by entropy increase (non-equilibrium change) or entropy remaining the same (equilibrium-change)

# ### Basic features of macrosystems 

# Let us list some of the most conspicious features of macroscopic systems consisting of many particles:
# 
# - **Additivitiy of Energy**
# - **Irreversibility of time evoluation.** 
# - **Simplicity and stability of equiliubrium states.**
# - **"Invisibility" of fluctuations**

# #### On Addititivty of Energy
# 
# The additivity of energy can hold if we assumed pairwise potential description between particles and that these potentials decasye with distance faster than the $r^{-3}$ in 3D. 

# In[1]:


from ipywidgets import widgets
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci


# In[2]:


def U_LJ6_12(r, sig=1, eps=1):
    '''Classic 6-12 Lennar Jones Potential
    r: interatomic distance in units sigma
    sigma: atomic/particle size
    E: energy in units of epsilon
    '''
    
    x=r/sig
    
    inv_r6  = 1/x**6
    inv_r12 = inv_r6**2
    
    return 4*eps*(inv_r12 - inv_r6)

def U_DH(r, a=1):
    '''Screened electrostatic potential
    '''
    
    return 1/r * np.exp(-a*r)


# In[3]:


fig, ax = plt.subplots(nrows=1, ncols=2,figsize=(11,4))
dist = np.linspace(1, 4,100)

ax[0].plot(dist, U_LJ6_12(dist,1,1),'--',lw=3,color='orange')
ax[0].set_xlabel('$r, [\sigma]$',fontsize=12)
ax[0].set_ylabel('$U_{LJ}(r)$',fontsize=12)

ax[1].plot(dist, U_DH(dist,1),'--',lw=3,color='green')
ax[1].set_xlabel('$r, [\sigma]$',fontsize=12)
ax[1].set_ylabel('$U_{DH}(r)$',fontsize=12)

ax[0].grid('on')
ax[1].grid('on')


# #### On Irreversibility
# 
# [Poincarre recurrence theorem](https://en.wikipedia.org/wiki/Poincar%C3%A9_recurrence_theorem)
# 
# If you play bridge long enough you will eventually be dealt any grand-slam hand, not once but several times. A similar thing is true for mechanical systems governed by Newton's laws, as the French mathematician Henri Poincare (1854-1912) showed with his recurrence theorem in 1890: if the system has a fixed total energy that restricts its dynamics to bounded subsets of its phase space, the system will eventually return as closely as you like to any given initial set of molecular positions and velocities. If the entropy is determined by these variables, then it must also return to its original value, so if it increases during one period of time it must decrease during another.
# 
# <img src="./figs/recurrence.jpg"  class="bg-primary" width="400px">
# 
# - Zermello is right for small systems. A dynamical system will alwasy return to its starting configuration hence irreversibility is not a property of micrsccopic systems.  
# 
# - Boltzman is right for large systems becasue a likelihhood of recurrence for macrosystem happening is beyond the lifetime of a universie. Case closed. 
# 

# ### Extensive vs Intensive
# 
# The **extensive variables (E,V,N)** are a priviledged set of variables in thermodynamin space becasue:
# - Proportional to the size of the system 
# - Uniquely describe macroscopic states 
# - Only mechanics/electromagnetis is needed without introdcuing derived notions of heat and temperature. 
# 
# The **intensive variables (T, P, $\mu$)** are derived from extensive variables and are therefore derived, conveient variables for controlling experiments. Thus, intensive variables do not have the same status of extenisve variables. 
# 
# - A glass of water with and without ice cube can both be under 1 atm and 0 C whereas values of energy, entropy volume will be different. 

# ### Thermodynamic coordinates and thermodynamic space. 

# - State of equilibrium is completely defined as a point in the space of thermodynamic coordinates:  $E, V, N, S$. Theese coordinates have a **unique** and well defined values for each equilirbum state irresective to how such state was created.  Weather through violent non-equilibrimu process or calm quasi-static sequence of equilibrou states. This is why the functions of extensive variables $E(S,V,N)$ or $S(E,V,N)$ are called **state functions** and their changes are given by differnee between initial or final state only $\Delta E =E_f -E_i$, $\Delta S =S_f -S_i$. The work $W$ or heat $Q$ on the other hand are process dependent characterizing the way  energy is trasnfered to the system and not characterizing equilibrium states itself.  
# 
# - Study of thermodynamic processes than boils down to study of transofrmations between equilibium A to equilibrium B in the **thermodynamic space** spanned by thermodynamic coordinates. E.g computing $\Delta E = E_B - E_A$
# 
# - To compute changes between equilirbum state A and B we construct reversible (read equilirbium) and quasistatic path connecting the two states which allwos writing down exact differntials for state changes. 

# ### Reversible, quasistatic process
# 
# <img src="./figs/adiabat.png"  class="bg-primary" width="400px">

# ### Plank's statment of 2nd law
# 
# <img src="./figs/plank.png"  class="bg-primary mb-1" width="400px">
# 
# > "Planck’s principle: For any adiabatic process with all the work coordinates returning to
# their original values $\Delta E \geq 0$ " M Plank
#  
# > In other words doing pure mechanical work on insulated(read adiabatic) system with no net change in mechanical variables results in energy either going up or remaining unchanged $\Delta E \geq 0$.  Thus we can not through mechanical work "steal" energy away from closed system wihtout any other change in the environment.    

# ### Thermodynamic space is made up of non-crossing adiabats. 
# 
# <img src="./figs/Adiabats.png"  class="bg-primary" width="400px">

# ### Nope-1
# 
# <img src="./figs/NO1.png"  class="bg-primary" width="400px">

# ### Nope-2
# 
# <img src="./figs/NO2.png"  class="bg-primary" width="400px">

# ### First Law
# 
# Mechanical energy conservation law extended to many-body thermal systems
# 
# $$dE = \delta Q +\delta W$$

# ### Second Law
# 
# For an adiabatic quasisatic process entropy always increases or remains the same (in the equilibrium state). 
# 
# $$dS \geq 0$$

# ### Gibbs relation
# 
# Given the energy as a function of extensive variables $E(S,V,N)$ we can write down its full differntial. 
# 
# 
# $$dE = \Big(\frac{\partial E}{\partial S} \Big)_{V,N}dS+ \Big(\frac{\partial E}{\partial V} \Big)_{S,N}dV+\Big(\frac{\partial E}{\partial N} \Big)_{S,V}dN$$
# 
# We identify **intensive variables** conjugate to extenive variables:
# 
# -  $$T = \Big(\frac{\partial E}{\partial S} \Big)_{V,N}$$
# 
# -  $$P = \Big(\frac{\partial E}{\partial V} \Big)_{S,N}$$
# 
# -  $$\mu = \Big(\frac{\partial E}{\partial N} \Big)_{S,V}$$
# 
# This is known as **Gibbs relation** in Thermodynamics and is a starting point for thermodynamic calculations
# 
# $$\boxed{dE=  TdS - pdV +\mu dN}$$

# ### Gibbs Duhem relation
# 
# Extensivity proeprty implies linear scaling with respect to extensive variables. In other words extensive variables are additive quantities 
# 
# $$E(\lambda S,\lambda V,\lambda N) = \lambda E(S,V,N)$$ 
# 
# $$E = \Big(\frac{\partial E}{\partial \lambda S} \Big)_{V,N}S+ \Big(\frac{\partial E}{\partial  \lambda V} \Big)_{S,N}V+\Big(\frac{\partial E}{\partial  \lambda N} \Big)_{S,V}N$$
# 
# $$E = TS -PV +\mu N$$
# 
# Now take derivative of E and compare with Gibbs relation
# 
# $$\boxed{SdT-VdP+Nd\mu =0}$$

# ### Other useful thermodynamic derivatives 

# #### Heat capacities at constnat P and V. Thermal stability requires $c_v,c_p\geq 0$
# 
# $$C_p = \Big(\frac{d Q}{dT} \Big)_{p,N}$$
# 
# $$C_v = \Big(\frac{d Q}{dT} \Big)_{v,N}$$
# 
# #### Expansion and compression coefficients. Mechanical stability requires $\kappa_T\geq 0$
# 
# - **Thermal expansion coeff:** 
# 
# $$\alpha  = \frac{1}{V}\Big(\frac{d V}{dT} \Big)_{p,N}$$
# 
# - **Isothermal compressibility coeff:** 
# 
# $$\kappa_T  = -\frac{1}{V}\Big(\frac{d V}{dP} \Big)_{T,N}$$

# ### Ideal Gas entropy example
# 
# $$dS = \frac{1}{T}dE + \frac{P}{T}dV$$
# 
# - $E = \frac{3}{2}Nk_B T$ and $PV = Nk_BT$ for monoatomic gas
# 
# $$dS = \frac{3Nk_B}{2E}dE + \frac{Nk_B}{V}dV$$
# 
# 
# $$S(E,V,T) = \frac{3}{2}Nk_B log \frac{E}{N} +Nk log \frac{V}{N} + const$$

# ### Convexity of Entropy and Concavity of Energy

# Entropy $S(E,V,N)$ of a composite system is additive over each one of the individual components. The entropy is therefore continuous, differentiable, and monotonically increasing function of the energy $S(E)$
# 
# 
# ![](./figs/concave_convex.png)
# 
# To sum up we have the follwing fundamental properties that any Entropy as a function of extensive variables should obey:
# 
# - $S(\alpha E + (1-\alpha) E^{'}, \alpha V + (1-\alpha) V^{'}) \geq \alpha S_1 (E, V) +(1-\alpha) S_2(E^{'}, V^{'})$ 
# 
# - $S(\lambda E,\lambda V, \lambda N) = \lambda S(E,V,N)$ 
# 
# - $\frac{\partial S}{\partial E} > 0$  
# 
# - $\frac{\partial E}{\partial S} = 0,\ as\ S \rightarrow 0$
# 

# 

# #### Exercise: Is it fundamental enough?
# 
# The following ten equations are purported to be fundamental equations for various thermodynamic systems. Five, however, are inconsisent with the basic postulates of a fundamental equation and are thus unphysical.  For each, plot the relationship between $S$ and $U$ and identify the five that are unacceptable. $v_0$, $\theta$, and $R$ are all positive constants and, in the case of fractional exponents, the real positive root is to be implied.
# 
# 1. $\ S = \left ( \frac{R^2}{v_0\theta} \right )^{1/3}\left ( NVU \right
# )^{1/3}$
# 
# 2. $S = \left ( \frac{R}{\theta^2} \right )^{1/3}\left ( \frac{NU}{V} \right)^{2/3}$
# 
# 3. $S = \left ( \frac{R}{\theta} \right )^{1/2}\left ( NU + \frac{R\theta V^2}{v_0^2} \right)^{1/2}$
# 
# 4. $S = \left ( \frac{R^2\theta}{v_0^3} \right ) \frac{V^3}{NU}$
# 
# 5. $S = \left ( \frac{R^3}{v_0\theta^2} \right )^{1/5}\left ( N^2U^2V \right)$
# 
# 6. $S = NR \ln \left ( \frac{UV}{N^2 R \theta v_0}  \right )$
# 
# 7. $S = \left ( \frac{NRU}{\theta} \right )^{1/2}\exp \left (-\frac{V^2}{2N^2v_0^2} \right )$
# 
# 8. $S = \left ( \frac{NRU}{\theta} \right )^{1/2}\exp
# \left (-\frac{UV}{NR\theta v_0} \right )$
# 
# 9. $U = \left ( \frac{NR\theta V}{v_0} \right ) \left ( 1+\frac{S}{NR} \right ) \exp \left (-S/NR \right)$
# 
# 10. $U = \left ( \frac{v_0\theta}{R} \right ) \frac{S^2}{V} \exp\left ( S/NR \right)$
# 

# #### Exercise: from equation of state to fundamental equation
# 
# - Obtain Helmholtz free energy of a simple pure homogenuus fluid described by the following equations of state 
# 
# $$u = \frac{3}{2}pv$$
# 
# $$p=av T^4$$

# #### Exercise: Where is my equilibrium state?
# 
# The fundamental equations of both systems $A$ and $B$ are 
# 
# $$S = \left (\frac{R^2}{v_0\theta} \right )^{1/3} \left ( N V U \right )^{1/3}$$
# 
# - The volume and mole number of system $A$ are $ 9 \times 10^{-6}\ m^3 $ and $3$ mol, respectively, 
# - and of system $B$ are $ 4 \times 10^{-6}\ m^3 $ and $2$ mol, respectively.  
# 
# First suppose $A$ and $B$ are completely isolated from one
# another.  Plot the total entropy $S_A + S_B$ as function of $U_A/(U_A + U_B)$,
# where $U_A + U_B = 80$ J. If $A$ and $B$ were connected by a diathermal wall and
# the pair allowed to come to equilibrium, what would $U_A$ and $U_B$ be?

# Call
# 
# $$ X = \frac{U_A}{U_A + U_B}$$
# 
# we know $U_A + U_B = 80$, therefore
# 
# $$ U_A = 80X,\hspace{20pt} U_B = 80(1 - X) $$
# 
# Then setting $R, v_0, \theta = 1 $ and plugging in $V_A$, $V_B$, $N_A$ and $N_B$.
# 
# $S = S_A + S_B = \left(3 \times 9 \times 10^{-6} \times 80X \right)^{1/3} + \left(2 \times 4 \times 10^{-6} \times 80(1-X)\right)^{1/3} = 0.086(1-X)^{1/3} + 0.129X^{1/3}$
# 
# Entropy is maximized when $X = 0.65$, which is where we would expect the system to go at equilibrium once the internal wall is made diathermal.

# In[4]:


import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,1,100)
S = 0.086 * (1 - X)**(1./3) + 0.129 * (X**(1./3))

plt.plot(X, S,'-o')

plt.xlabel('X')
plt.ylabel('S(X)')


# ### Free Energies: Swapping extensive variables for intensive ones
# 
# $$E(S,V,N) \rightarrow A(T,V,N)$$
# 
# $$E(S,V,N) \rightarrow G(T,p,N)$$
# 
# $$E(S,V,N) \rightarrow \Omega(T,p,\mu)$$

# ### Legendre Transform of convex functions. 
# 
# Genrally speaking legendre transform is transforming one convex function $f(x)$ into another $f^*(\alpha)$. 
# Morover, the transofmraiton is involutive, meaning it is its own inverse. If we apply legendre trnsform to a function if single variable twice we get back to orginal function! 
# 
# ![](./figs/Legendre.png)
# 
# 
# $$f^*(\alpha) = max_x  \big [{\alpha x - f(x)} \big ]$$
# 
# $$f(x) = max_{\alpha} \big [ {\alpha x - f^*(\alpha)} \big ]$$

# #### Example of Legendre transform-1
# 
# $$f(x) = x^2$$
# 
# $$a = f'(x) =2x \rightarrow x = a/2 $$
# 
# $$g(\alpha) = f^*(\alpha) = max_x \Big[ \alpha x - f(x) \Big ] = \alpha^2/2 - \alpha^2/4 = \alpha^2/4$$

# In[5]:


f = lambda x: x**2

g = lambda a: a*(a/2) - f(a/2)   # deriv f(x) = 2x = a ---> x = a/2


# In[6]:


@widgets.interact(a=(0,2,0.2))
def legendre_transf(a):
    
    fig,ax =plt.subplots(nrows=1,ncols=2, figsize = (10,4))
    
    x = np.linspace(0,1,100)
    ax[0].plot(x,f(x),lw=3) 
    ax[0].plot(x, a*x-g(a),'--')
    
    ax[0].set_title('$f(x) = x^2$')
    ax[0].legend(['f(x)', f"$y = ax-g(a)$ = {a}x -{g(a):.2f}"])    
    ax[0].set_xlim(0,1.2)
    ax[0].set_ylim(0,1.2)
    ax[0].set_xlabel('x',fontsize=20)
    ax[0].set_ylabel('f(x)',fontsize=20)
    ax[0].grid('on')
    
    ax[1].set_title('$g(a) = max_x [ax-f(x)]= a^2/2$')
    ax[1].plot(a,g(a),'o',color='orange',ms=12)
    ax[1].plot(np.linspace(0,2,10),g(np.linspace(0,2,10)),'-',lw=3, color='red')
    ax[1].set_xlim(0,1.2)
    ax[1].set_ylim(0,1.2)
    ax[1].set_xlabel('a',fontsize=20)
    ax[1].set_ylabel('g(a)',fontsize=20)
    ax[1].grid('on') 


# #### Example of Legendre transform-2
# 
# $$f(x) = e^x$$
# 
# $$a = f'(x) =e^x \rightarrow x = log a$$
# 
# $$g(\alpha) = max_x \Big[ \alpha x - f(x) \Big ] = a(log a-1)$$

# In[7]:


f2 = lambda x: np.exp(x)

g2 = lambda a: a*np.log(a) - f2(np.log(a))   # deriv f(x) = e^x = a ---> x = log a


# In[8]:


@widgets.interact(a=(1,3,0.2))
def legendre_transf(a):
    
    fig,ax =plt.subplots(nrows=1,ncols=2, figsize = (10,4))
    
    x = np.linspace(0,1,100)
    ax[0].plot(x,f2(x),lw=3) 
    ax[0].plot(x, a*x-g2(a),'--')
    
    ax[0].set_title('$f(x) = x^2$')
    ax[0].legend(['f(x)', f"$y = ax-g(a)$ = {a:.2f}x-{g2(a):.2f}"])    
    ax[0].set_xlim(0,1.2)
    ax[0].set_ylim(0,3)
    ax[0].set_xlabel('x',fontsize=20)
    ax[0].set_ylabel('f(x)',fontsize=20)
    ax[0].grid('on')
    
    ax[1].set_title('$g(a) = max_x [ax-f(x)]= a(log a-1)$')
    ax[1].plot(a,g(a),'o',color='orange',ms=12)
    ax[1].plot(np.linspace(0,3,10),g(np.linspace(0,3,10)),'-',lw=3, color='red')
    ax[1].set_xlim(0,3)
    ax[1].set_ylim(0,3)
    ax[1].set_xlabel('a',fontsize=20)
    ax[1].set_ylabel('g(a)',fontsize=20)
    ax[1].grid('on') 


# ### Legendre Transform numerically  (via numpy/scipy )

# In[9]:


def legendre_transf(f, a=1, guess_0=0):
    
    '''Legendre transform function f to g 
    
    INPUT:
    f <-- function
    a <-- value of new variable
    
    OUTPUT:
    g(a) = min_x[a*x-f(x)] legendre transform at point a
    '''
    
    min_x, = sci.optimize.fmin(lambda x: f(x)-a*x, guess_0) 
            
    return a*min_x - f(min_x)


# In[10]:


f = lambda x: x**2+x**4

#g = [legendre_transf(f, a) for a in np.linspace(0,1,100)]


# ### Problem-1
# 
# 1. Give an example of a process in which a system is not heated, but its temperature increases. Also give an example of a process in which a system is heated, but its temperature is unchanged.
#  
# 2. Which states are in an equilibrium state, a time dependent non-equilibrium state, or time independent but still non-equilibrium state (e.g steady stae). Explain your reasoning. In some cases, the state is not a true steady or equilibrium state but close to one. Discuss under what conditions it can be treated as a steady or equilibrium state. 
#     - a cup of hot tea, sitting on the table while cooling down 
#     - the wine in a bottle that is stored in a wine cellar 
#     - the sun 
#     - the atmosphere of the earth 
#     - electrons in the wiring of a flashlight switched off 
#     - electrons in the wiring of a flashlight switched on
# 3. What is meant by a constraint in thermodynamics and why its removal must always lead to increase of entropy?
# 4. What is meant by a quasi-static process in thermodynamics and how this idealization is used for computing changes in thermodynamic variables?
# 5. What is the difference between fundemtnal equation in thermodyamics $S(E,V,N)=$ vs state equation $P(V,N,T)$ e.g like $PV=NRT$ for ideal gas. 
# 
# 6. Why during a spotneous transofrmation of systems  entropy tend to its maximum value. This is the reason why we use entropy maximization as a powerful tool to predict the final equilibrium states. 
# 
# 7. Why do we introduce Free energies of various kinds? Explain why free energy minimization is equivalent of total entropy maximization. 
# 
# 8. Can part of the entropy of a part of a total system decrease? Give some exmaples. 
# 
# 9. Does the change of the entropy depend on the path between two equilibrium states?
# 
# 10. How is adiabatic process different from quasistatic and reversible process?  
# 
# 

# ### Problem-2: Expansion of a gas into vacuum
# 
# 
# -  Suppose that a gas expands adiabatically into a vacuum. What is the work done by the gas?
# -  Suppose that the total energy of the gas is given by 
# 
# $$E = 3/2NkT −N^2 V/a$$
# 
#  Initially the gas occupies a volume $V_1$ at a temperature $T_1$. The gas then expands adiabatically into a vacuum so that it occupies a total volume $V_2$. What is the final temperature $T_2$ of the gas?

# ### Problem-3: Entropy changes
# 
# 1. kg of water (specific heat = 4.2 kJ/(kg·K)) at $0 ^oC$ is in contact with a $50 ^oC$ heat bath, and eventually reaches $50 ^oC$. What is the entropy change of the water? What is the increase of the entropy of this water plus the heat bath?
# 
# 2. Instead of (1) first the water at $0 ^oC$ is in contact with a $25 ^oC$ heat bath. Then, after reaching thermal equilibrium, the water is in contact with a $50 ^oC$ heat bath to reach the final temperature $50 ^oC$ as in (1). What is the increase of the entropy of the water plus the two heat baths?
# 
# 3. Show that in the two-step heating process whatever the first heat bath temperature T is between $0^oC$ and $50^oC$, the total change of entropy of the water plus heat baths is less than the case of (1)

# ### Problem-4: Legendre transforms
# 
# Carry out the following transformations and plot the resulting function with matploltib. 
# 
# - From $f(x) = x^2+x^4$ to $g(a)$ 
# 
# - From $f(x,y,z) = x^2+y^4+logz$ to $g(a,b,c)$
# 
# - From $G(T,p,N)$ to $A(S,p,N)$
# 
# - From $\Omega(T,p,\mu)$ to $E(S,V,N)$
# 
# 
# 

# ### Problem-5: manipulate derivatives
# 
# Derive the following identities: 
# 
# - $$\Big( \frac{\partial C_p}{\partial P} \Big)_T = - T \Big( \frac{\partial^2 V}{\partial T^2} \Big)_P$$
# 
# - $$\Big( \frac{\partial C_v}{\partial V} \Big)_T =  T \Big( \frac{\partial^2 P}{\partial T^2} \Big)_V$$
# 

# In[ ]:





import numpy as np
from numpy.random import choice, rand, randint
from numba import jit, njit

######## Main Code ###########

@njit
def ising2d_mcmc(N,J,B,T, n_steps=10**7, out_freq = 10**4):

    #Initialize
    spins    =  np.ones((N,N))   # choice([-1,1], (N,N))

    #Empty array/matrix for recording
    confs       = []
    M, E        = [], []
    
    for step in range(n_steps):

        #Pick random spin
        i, j = randint(N), randint(N)

        #Compute energy change
        z  = spins[(i+1)%N, j] + spins[(i-1)%N, j] + spins[i, (j+1)%N] + spins[i, (j-1)%N]
        dE = 2*spins[i,j]*(J*z + B)

        #Metropolis condition
        if dE <= 0 or np.exp(-dE/T) > rand():
            
            spins[i,j] *= -1 

        #Store the spin configuration
        if step % out_freq == 0:
            
            confs.append(spins.copy())
            M.append(getM(spins))
            E.append(getE(spins,N,J,B))

    return confs, M, E


####### Thermo Output  #######
@njit
def getM(spins):
    
    return np.mean(spins)


@njit
def getE(spins,N,J,B):    
    
    E = 0
    
    for i in range(N):
        for j in range(N):   
            
            z = spins[(i+1)%N, j] + spins[(i-1)%N, j] +\
                spins[i,(j+1)%N] +  spins[i,(j-1)%N]
            
            E += -J*z*spins[i,j]/4 # Since we overcounted interactions 4 times divide by 4.

    return E - B*np.sum(spins) #Field contribution added


####### Print  #######


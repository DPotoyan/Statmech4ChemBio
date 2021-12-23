import numpy as np
from numpy.random import choice, rand, randint
from numba import jit, njit

######## Main Code ###########

@njit
def us_mcmc(spins, J, B, T, W, n_steps = 10000, out_freq = 100):
    
    '''mcmc takes spin configuration and samples with given N,J,B,T 
    for n_steps outputing results every out_freq'''
    
    N = len(spins)
    confs = [] 
    Ms    = []
    
    for step in range(n_steps):
        
        #Pick random spin
        i, j = randint(N), randint(N)

        #Change in bulk energy due to spin flip
        z            = spins[(i+1)%N, j] + spins[(i-1)%N, j] + spins[i, (j+1)%N] + spins[i, (j-1)%N]
        dE_bulk      = 2*spins[i,j]*(J*z + B)
        
        #Change in magnetizaton coordinate
        m_try        = getM(spins)   - (2/N)*spins[i,j] 
        dE_umb       = U_hard(W, m_try) 
    
        #Compute energy change
        dE = dE_bulk + dE_umb 
        
        
        #Metropolis condition
        if dE <= 0 or np.exp(-dE/T) > rand():
            
            spins[i,j] *= -1 
        

        #Store the spin configuration
        if step % out_freq == 0:
            
            confs.append(spins.copy())
            Ms.append(getM(spins))
    
    return confs, np.array(Ms)

@jit
def initalize(N, mode='ones'):
    
    if mode =='random':
        spins = choice([-1,1],(N,N))
        
    if mode == 'ones':
        spins = np.ones((N,N))
        
    return spins

@jit
def U_hard(W, m):
    
    if min(W) <= m <= max(W): U = 0
    else:  U = 1e6
        
    return U

@jit
def U_soft(W, m):
        
    return 0.5*W[1]*(W[0]-m)**2

@njit
def getM(spins):
    
    return np.mean(spins)


@njit
def getE(spins,J,B):    
    
    N = len(spins)
    E = 0
    
    for i in range(N):
        for j in range(N):   
            
            z = spins[(i+1)%N, j] + spins[(i-1)%N, j] +spins[i,(j+1)%N] +  spins[i,(j-1)%N]
            
            E += -J*z*spins[i,j]/4 # Since we overcounted interactions 4 times divide by 4.

    return E - B*np.sum(spins) #Field contribution added


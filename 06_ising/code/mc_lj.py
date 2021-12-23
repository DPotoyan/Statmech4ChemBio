import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
from numpy.random import rand, randint, uniform, choice, normal 
from numba import jit, njit


######### Main MCMC loop for simulating LJ fluid #################

@njit
def doMC_LJ(particles, rho=0.1, T=2.5, sig=1, eps=1, trunc=3, steps=10000, freq=1000):

    N      = len(particles)
    L      = (N/rho)**(1/3)
    
    E_tot       = getE_tot(particles, L, sig, eps, trunc) 
    confs, es   = [particles.copy()], [E_tot]
    
    #Loop through MC steps
    
    for step in range(0, steps):
        
        # Randomly choose some particle i in  
        i = randint(N)
    
        #Position and Energy of particle i
        pos_i      = particles[i]
        eng_i      = getE_one(particles, i, pos_i, L, sig, eps, trunc)
    
        #Give a particle i a random push:
        pos_i_new  = particles[i] + (rand(3)-0.5)
        eng_i_new  = getE_one(particles, i, pos_i_new, L, sig, eps, trunc)
        
        # Evaluate change in energy
        dE = eng_i_new - eng_i

        # Metropolis acceptance/rejection conditions
        if  np.exp(-dE/T) > rand():
            
            particles[i] = pos_i_new
            E_tot       += dE
            
        if step % freq ==0:
            
            confs.append(particles.copy())
            es.append(E_tot)
                    
    return confs, es
    

########## Helper functions ####################
    
@njit
def pbc_wrap(pp, L):
    
    ''' (a) if pp = (x,y,z) position; wraps it back to box (with origin in the center!) 
        (b) if pp = (dr_x, dr_y, dr_z) distances; uses nearest image convension'''
    
    if pp[0] >  L/2:  pp[0] = pp[0] - L     
    if pp[0] <= -L/2: pp[0] = pp[0] + L
        
    if pp[1] >  L/2:  pp[1] = pp[1] - L     
    if pp[1] <= -L/2: pp[1] = pp[1] + L
    
    if pp[2] >  L/2:  pp[2] = pp[2] - L     
    if pp[2] <= -L/2: pp[2] = pp[2] + L
    
    return pp

@njit
def get_r2(p1, p2, L):
    
    ''' Compute squared distance between two particles 
   p1(x,y,z) and p2(x,y,z) while enforcing PBC.'''
    
    p1, p2 = pbc_wrap(p1, L), pbc_wrap(p2, L)  # position wrap back into box
   
    dr     = p2 - p1
    
    dr     = pbc_wrap(dr, L)                   # distance via minimum image 
    
    return dr[0]**2 + dr[1]**2 + dr[2]**2


@njit
def get_e2(pos_i, pos_j, L, sig, eps, trunc ):
    
    pair_e  = 0
    
    dist_sq = get_r2(pos_i, pos_j, L)
                
    if dist_sq <= trunc**2:
                
        pair_e += (sig/dist_sq)**6 - (sig/dist_sq)**3
        
    return 4*eps*pair_e
  
    
@njit
def getE_tot(particles, L, sig, eps, trunc):
    
    '''Compute Total energy 
    by summing all pairwise interactions'''
    
    N = len(particles)
    energy = 0
    
    for i in range(0, N-1):
        for j in range(i+1, N):
            
                energy += get_e2(particles[i], particles[j], L, sig, eps, trunc)
                    
    return energy
    
    
@njit
def getE_one(particles, j, tag_j, L, sig, eps, trunc):
    
    '''Compute energy of a tagged particle j 
    by summing all pairwise interactions with j'''
    
    N = len(particles)
    energy = 0
        
    for i in range(N):
        if i!=j:
                
            energy += get_e2(particles[i], tag_j, L, sig, eps, trunc)
    
    return energy 

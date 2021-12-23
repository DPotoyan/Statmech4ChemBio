#!/usr/bin/env python
# coding: utf-8

# # Plotting

# Matplotlib is a standard plotting library of python. We begin by importing it first along with numpy.

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# The most widely used function in `matplotlib` is plot, which allows you to plot 1D and 2D data. Here is a simple example:

# In[2]:


# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# Plot the points using matplotlib
plt.plot(x, y)


# We can easily customize the style of plots for poster/talk/paper

# In[3]:


print(plt.style.available)


# In[4]:


plt.style.use(['seaborn-white'])
plt.plot(x, y)


# if we want to customize plots it is better to plot by first defining fig and ax objecs which have manuy methods for customizing figure resolution and plot related aspects respecticely. 

# In[5]:


fig, ax = plt.subplots()

y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
ax.plot(x, y_sin)
ax.plot(x, y_cos)

# Specify labels
ax.set_xlabel('x axis label')
ax.set_ylabel('y axis label')
ax.set_title('Sine and Cosine')
ax.legend(['Sine', 'Cosine'])

#fig.savefig("myfig.pdf")


# ## A gallery of useful examples
# 
# **For a greater variety of plotting examples check out [Matploltib Gallery!](https://matplotlib.org/3.1.1/gallery/index.html)**

# 1D plotting is conveniently done by creating fig and ax objects which allow coutom styling plots and figure properties separately. 

# In[6]:


fig, ax = plt.subplots()          # Create fig and ax objects

t = np.arange(0.0,  2*np.pi, 0.1) # create x values via np.arange or np.linspace

s = np.sin(t)                     # create y values

ax.plot(t, s, '-o')                     # make the plot

#fig.savefig('myFIG.png')         # save figure


# #### fig and ax objects
# For customizing plots it is more convenient to define **fig** and **ax** objects.  One can then use ax object to make veriety of subplots then use fig to save the entire figure as one pdf. Try changing fig size, number of columns and rows.

# In[7]:


t = np.arange(0.0,  2*np.pi, 0.1) # create x values
s = np.sin(t)                     # create y values

fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(6,3))          

ax[0].plot(t, s,'-o', color='purple', lw=1.0)  # plot on subplot-1
ax[1].plot(t, s**2,'-o', color='green',  lw=1.0)  # plot  on subplot-2

#fig.savefig('sd.png')             # save the figure


# ### Plotting in 2D

# To make 2D plots we need to generate 2D grid $(x,y)$ of points and pass it to our function $f(x,y)$
# 
# $$f(x,y) = sin(x) \cdot cos(x) \,\,\,$$

# In[8]:


x = np.arange(0.0,  2*np.pi, 0.1)   # create x values
y = np.arange(0.0,  2*np.pi, 0.1)   # create y values

X, Y = np.meshgrid(x,y)             # tunring 1D array into 2D grids of x and y values

Z = np.sin(X) * np.cos(Y)           # feed 2D grids to our 2D function f(x,y)

fig, ax = plt.subplots()            # Create fig and ax objects
ax.pcolor(X, Y, Z,cmap='RdBu')                  # plot 

# try also ax.contour, ax.contourf


# ### 3D plots with matplotlib

# In[9]:


from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D

# Create fig and ax objects for 3d plotting
fig = plt.figure()
ax = fig.add_subplot(projection='3d')  

# Using X,Y,Z grid of points in previous step 
ax.plot_surface(X, Y, Z, cmap='RdYlBu')


# ### Plotting histograms with matplotlib

# In[10]:


fig, ax = plt.subplots()

# Make up some random data
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# Plot 1D histogram of the data
hist = ax.hist(x, bins=40, density=True)


# In[11]:


fig, ax = plt.subplots()

# Make up some random data
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
y = mu + 2*sigma * np.random.randn(10000)

# Plot 2D histogram of the data
hist = ax.hist2d(x, y, bins=40, density=True, cmap='RdBu_r')


# ### Statistical visualizations with seaborn

# - [Seaborn](https://seaborn.pydata.org/index.html) For visualizing statistical plots there is a specialized library build on top of matplotlib that simplifies many intermediate steps that are needed to go from data to beautiful and polished visualization.

# In[12]:


import seaborn as sns
from scipy import stats


# In[13]:


# Make up some random data
mu, sigma = 100, 15

x = mu + sigma * np.random.randn(10000)

sns.displot(x, kind="kde")


# ## Pandas and seaborn! a power couple for multivariate statistics visualization

# In[14]:


# Normal distribution of points 
n_points=200

df = pd.DataFrame({ 'X':    1*np.random.randn(n_points), 
                    'Y':    5*np.random.randn(n_points), 
                    'Z':    1+5*np.random.randn(n_points),
                    'time': np.linspace(0,n_points,n_points)
                  })


# In[15]:


sns.jointplot(data=df, x='X', y='Z',
              kind="kde", cmap='RdBu_r')


# ## Interactive plots

# In[16]:


import plotly.express as px


# ### Plotly
# 
# - [Plotly](https://plotly.com/python/) is large multi-language  interactive graphing library that covers Python/Julia/R. 
# 
# - [Plotly-dash](https://dash.plotly.com/introduction) is a framework for building web dashborads with itneractive plotly graphs.
# 
# - [Plotly-express](https://plotly.com/python-api-reference/plotly.express.html) is a high level library for quick visualizations whihc is similiar to seaborn vs matploltib in its philosophy
# 
# > Check out [this cool website](https://biapss.chem.iastate.edu/) built using Dash-Plotly

# In[17]:


df = pd.DataFrame({ 'X':    1*np.random.randn(500), 
                    'Y':    5*np.random.randn(500), 
                    'Z':    1+5*np.random.randn(500),
                    'time':  np.arange(500)
                  })

px.density_heatmap(df, x='X', y='Y')
#px.line(df, x='X', y='Y')
#px.scatter(df, x='X', y='Y')
#px.area(df, x='X', y='Y')
#px.histogram(df, x="X")


# In[18]:


fig = px.scatter(df, x="X", y="Y", size=20*np.ones(len(df)), 
                 animation_frame="time", animation_group='Y', color='Y',
                 range_x=[-20,20], range_y=[-20,20]
                 )
fig.show()


# ### Holoviews
# 
# > Stop plotting your data - annotate your data and let it visualize itself
# 
# Too many libraries for visualization in pyviz universe? Enter Holoviews! We all can agree there are just too many options for visualizing data and sometimes it is impossible to pick one and stick with becaue different libaries have different strengths when it comes visualizing different kinds of data. Plotly does a gread job with 3D visualization while matploltib is mostly desinged for 2D plots. Seaborn has everying one needs to genreate statistical plots while plotly may cover ony a subgroup of seaborn, etc. One emerging idea in scientific software desing is to create library agnostic tools. E.g if you want to plot histogram you can do it either using several different libraries or using a library agnsotic tool by specifiying the particular library interface for the visualization. 
# 
# - [Holoviews](http://holoviews.org/#) 
# - [Example of Holoviews Elements](http://holoviews.org/reference/index.html)
# 

# In[19]:


import holoviews as hv


# In[ ]:


hv.extension('matplotlib') # try 'bokeh' or 'matplotlib'
data = [1,2,4,8,16,25]

#hv.Curve(data) + hv.Scatter(data) # adding crates subplots
hv.Curve(data) * hv.Scatter(data) # multiplying creates overlay


# In[ ]:


import numpy as np
import pandas as pd
df = pd.DataFrame({'X':np.random.randn(1000),'Y':np.random.randn(1000), 'Z':np.random.randn(1000)})

data = df[['X', 'Y']].values

#hv.Curve(data)
hv.Scatter(data) + hv.Curve(data) + hv.Points(data) + hv.Bivariate(data)
#hv.Histogram(df['X'], density=True, bins=50)


# In[ ]:


#Example of 3D plot

Z = np.sin( np.random.randn(40,40) )

hv.Surface(Z, bounds=(-5, -5, 5, 5))


# ### Using interactive widgets
# 
# Suppose we would like to explore how the variation of parameter $\lambda$ affects the following function of a standing wave:
# 
# $$f(x) = sin (\omega *x +p)$$
# 
# - Make a python-function which creates a plot as a function of a parameter(s) of interest.
# 
# - Add an interactive widget on top to vary the parameter.

# In[ ]:


from ipywidgets import widgets


# In[ ]:


@widgets.interact(phase=(0,2*np.pi), freq = (0.1,5))  
def wave(phase=0, freq=0.5):          
    
    x  = np.linspace(0,10,1000)
    y  = np.sin(freq*x+phase)
        
    plt.plot(x, y)


# In[ ]:


def wave(phase, freq):
    
    x  = np.linspace(0,10,100)
    y  = np.sin(freq*x+phase)
    
    return hv.Curve((x, y))


# In[ ]:


#hv.extension('bokeh')

## Option-1: Define ranges of variables and pass to DynamicMap
#hv.DynamicMap(wave, kdims=['phase', 'freq']).redim.range(phase=(0.0,2*np.pi), freq=(0.1, 5))
hv.DynamicMap(wave, kdims=['phase', 'freq']).redim.values(phase=np.linspace(0.0,2*np.pi,20), freq=np.linspace(0.1, 5,20))

## Option-2: make dictionary of data points and pass to HoloMap
#data = {(phase, freq): wave(phase, freq) for (phase, freq) in zip(np.linspace(0.0,2*np.pi,20), np.linspace(0.1, 5, 20)) }
#hv.HoloMap(data, kdims=['phase', 'freq'])


# ### Interactive visualization of a Reaction-Diffusion system

# In[ ]:


def laplacian(Z, dx):
    """
    Function to computes the discrete Laplace operator of
    a 2D variable on the grid (using a five-point stencil
    finite difference method.)
    """
    Ztop = Z[0:-2,1:-1]
    Zleft = Z[1:-1,0:-2]
    Zbottom = Z[2:,1:-1]
    Zright = Z[1:-1,2:]
    Zcenter = Z[1:-1,1:-1]
    return (Ztop + Zleft + Zbottom + Zright - 4 * Zcenter) / dx**2


def reaction_diffusion(a=2.8e-4, b=5e-3, tau=0.1, k=-0.005, samples=10):
    """
    We simulate the PDE with the finite difference method.

    The samples value is the number of equally spaced samples
    to collect over the total simulation time T.
    """
    size = 100         # size of the 2D grid
    dx = 2./size       # space step
    T = 10.0           # total time
    dt = 4.5 * dx**2    # simulation time step
    n = int(T/dt)

    result = []
    U = np.random.rand(size, size)
    V = np.random.rand(size, size)

    sample_times = [int(el) for el in np.linspace(0, n, samples)]

    for i in range(n):
        # We compute the Laplacian of u and v.
        deltaU = laplacian(U, dx=dx)
        deltaV = laplacian(V, dx=dx)
        # We take the values of u and v inside the grid.
        Uc = U[1:-1,1:-1]
        Vc = V[1:-1,1:-1]
        # We update the variables.
        U[1:-1,1:-1], V[1:-1,1:-1] =             Uc + dt * (a * deltaU + Uc - Uc**3 - Vc + k),             Vc + dt * (b * deltaV + Uc - Vc) / tau
        # Neumann conditions: derivatives at the edges
        # are null.
        for Z in (U, V):
            Z[0,:] = Z[1,:]
            Z[-1,:] = Z[-2,:]
            Z[:,0] = Z[:,1]
            Z[:,-1] = Z[:,-2]

        if i in sample_times:
            result.append((i * dt,U.copy()))
            
    return result


# In[ ]:


sim1 = reaction_diffusion()


# In[ ]:


hv.HoloMap({time: hv.Image(array) for (time, array) in sim1}, kdims=['Time'])


# ## Additional resoruces. 
# 
# Matplotlib has a huge scientific user base. This means that you can always find a good working template of any kind of visualization which you want to make. With basic understanding of matplotlib and some solid googling skills you can go very far. Here are some additional resources that you may find helpful
# 
# - [Matplotlib](https://matplotlib.org/index.html)
# 
# - [Matplotlib gallery](https://matplotlib.org/3.1.1/gallery/index.html)
# 
# - [Matplotlib Blog](https://matplotlib.org/matplotblog/)
# 
# - [PyViz universe](https://pyviz.org/index.html)
# 
# - [The Python Graph Gallery](https://python-graph-gallery.com/)
# 
# - [Plotly documentaiton](https://plotly.com/python/)

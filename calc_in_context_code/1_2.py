#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:39:23 2022

@author: gracemcgrath
"""
from pylab import plot, show

t = 0

# initial conditions
S = 45400
I = 2100
R = 2500

# make arrays in order to graph
t_list = [t]
s_list = [S]
i_list = [I]
r_list = [R]


#stepsize = h = deltat
delta_t = 1
print("initial conditions for t = ",t, "\n S = ", S, "\n I = ", I, "\n R = ", R)

for k in range(3):
    #System of ODE
    s_prime = -0.00001*S*I
    i_prime = .00001*S*I - I/14
    r_prime = I/14
    
    #Approximate the rate of change 
    delta_s = s_prime*delta_t
    delta_i = i_prime*delta_t
    delta_r = r_prime*delta_t
    
    # Update all values as the loop iterates
    t += delta_t
    S += delta_s
    I += delta_i
    R += delta_r
    
    # append updated valuess to array for plotting
    t_list.append(t)
    s_list.append(S)
    r_list.append(R)
    i_list.append(I)
    
    
    #print("updated conditions for t = ",t,"\n S = ", round(S,1), "\n I = ", round(I,1), "\n R = ", round(R,1))
    
# plot the functions 
plot(t_list,s_list)
plot(t_list,i_list)
plot(t_list,r_list)
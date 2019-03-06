"""
Created on Fri Sep 29 16:47:14 2017

@author: DivyaRamesh
"""


###10/22/2017

import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt
from scipy.optimize import fsolve
#import numdifftools as nd
from numpy import linalg
##########################################################


def predpreysig (b,trange,k0,k1,phi,p, t, h):
    """

    b - behaviours signal and attack
    s - prey resident signalling probability
    a - predator attack probability
    k0 - predator's chance of successfully killing a prey that has not detected it
    k1 - predator's chance of successfully killing a prey when there is a signal (whether prey1 or prey2 signals)
    phi - prey cost of signalling
    p - prey probability of detecting predator
    t - predator travel time
    h - predator handling time
    """
    s = b[0]
    a = b[1]


    ds = (1-p)*p*(((0.5)*k1) - a*k1*(0.5+phi)) + (p**2.)*(s*(1-(0.5)*a*k1) \
            + (1-s)*(1-a*k1*(0.5+phi)) - s*(1-a*k1*(0.5-phi)) - (1-s)*(1-k1*(0.5)))

    if s >= 1. and ds > 0.:
            ds = 0.
    if s <= 0. and ds < 0.:
        ds = 0.


    da = (k1*(t+h-(2.*h*p*s))) - (h*((((1.-p)**2.)*k0) + (p*k1*(1.-s))  \
             + (p*k0*(1.-p)*(1.-s)) + ((p**2.)*s*k1)))

    if a >= 1. and da > 0.:
        da = 0.

    if a <= 0. and da < 0.:
        da = 0.




    return [ds, da]

##############################################################


def ds(b,k0,k1,phi,p,t,h):
    """
    time derivative of signalling probability
    """
    s = b[0]
    a = b[1]

    ds = (1-p)*p*(((0.5)*k1) - a*k1*(0.5+phi)) + (p**2.)*(s*(1-(0.5)*a*k1) \
        + (1-s)*(1-a*k1*(0.5+phi)) - s*(1-a*k1*(0.5-phi)) - (1-s)*(1-k1*(0.5)))
    return ds

def da(b,k0,k1,phi,p,t,h):
    """
    time derivative of attack probability
    """
    s = b[0]
    a = b[1]

    da = (k1*(t+h-(2.*h*p*s))) - (h*((((1.-p)**2.)*k0) + (p*k1*(1.-s))  \
         + (p*k0*(1.-p)*(1.-s)) + ((p**2.)*s*k1)))
    return da

def pderiv(f,x,index, *args):
    """
    Simple partial derivative function
    f:   function
    x:   parameter values at which partial der is evaluated
    index: the index of the parameter for deriv
    * args : other function parameters (coefficients, etc.)
    """
    h = .00001
    x0 = list(x)
    x0[index]=x[index]+h
    d = np.diff([f(x,*args),f(x0,*args)])/h
    return d


#b = [0.25,0.75]
#k0 = 0.4
#k1 = 0.1
#phi = 0.4
#p = 0.3
#t = 2.5
#h = 1.

b = [0.8, 0.99]
k0 = 0.4
k1 = 0.1
phi = 0.2
p = 0.3
t = 2.0
h = 1.0

trange = np.arange(0,20000)


result = integrate.odeint(predpreysig,b,trange,args=(k0,k1,phi,p,t,h))
tresult = np.transpose(result)

#11Nov2016, using fsolve to solve for roots/equilibrium point
roots = fsolve(predpreysig, b, args=(trange, k0, k1, phi, p, t, h))


plt.subplot(111)
plt.plot(tresult[0],tresult[1])       # plot prey and predator behaviours
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
#plt.title("Dynamics of signal evolution", fontsize='15')
plt.xlabel("probability of signaling, s")
plt.ylabel("probability of post-signal attack, a")
plt.grid(True)
plt.plot(tresult[0][-1],tresult[1][-1],'ro',markersize=8)  #plot endpoint
plt.plot(roots[0],roots[1],'o',mfc='k',markersize=5)  #plot equilibr
plt.show()

print "equilibr: ", roots
print "endpoint: ", result[-1]
print "result(n-1) =", result[-1]    #should be the same as endpoint
print "result(n-500) =", result[-500]
print "b =", b
print "k0 =", k0
print "k1 =", k1
print "phi =", phi
print "p =", p
print "t =", t
print "h =", h
print "trange =", len(trange)



#print "da at equil: ", da(roots, k0,k1,phi,p,t,h)
#print "ds at equil: ", ds(roots, k0,k1,phi,p,t,h)
#print
jac00 = pderiv(ds,roots,0,k0,k1,phi,p,t,h)[0]
jac01 = pderiv(ds,roots,1,k0,k1,phi,p,t,h)[0]
jac10 = pderiv(da,roots,0,k0,k1,phi,p,t,h)[0]
jac11 = pderiv(da,roots,1,k0,k1,phi,p,t,h)[0]

jacobian = np.matrix([[jac00,jac01],[jac10,jac11]])
print "jacobian: "
print jacobian

print "eigenvalues: ", linalg.eigvals(jacobian)


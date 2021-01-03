#%%
from __future__ import print_function, absolute_import, division
import sys
sys.path.append('../')
import numpy as np
import tt
import random
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
import pandas as pd
from scipy.stats import norm
from scipy.stats import multivariate_normal
import time

import matplotlib.pyplot as plt


import tt.cross.rectcross as rect_cross


d = 5
n = 10
b = 1E3
#x = np.arange(n)
#x = np.reshape(x, [2] * d, order = 'F')
#x = tt.tensor(x, 1e-12)
x = tt.xfun(n, d)
#x = tt.ones(n, d)

#sf = lambda x : x[0]+x[1]+x[2]+x[3]+x[4] #Should be rank 2

#y = tt.multifuncrs([x,x,x,x,x], sf, 1e-6, y0=tt.ones(n, d))
#y1 = tt.tensor(sf(x.full()), 1e-8)

#print("pi / 2 ~ ", tt.dot(y, tt.ones(2, d)) * h)
#print (y - y1).norm() / y.norm()
# %%
x.full().shape
# %%
xfull=x = tt.xfun(5, 2).full()
# %%
xfull
# %%
sf = lambda x : x[0]+x[1]+x[2]+x[3]+x[4] #Should be rank 2
# %%
sf([1,2,3,4,5])
# %%
y = tt.multifuncrs(x, sf, 1e-6, y0=tt.ones(n, d))
# %%
a = tt.tensor(np.random.rand (3, 3),1e-4)
b = tt.tensor(np.random.rand (3, 3),1e-4)
c = tt.multifuncrs([a, b], lambda x: np.sum(x, axis=1), eps=1E-6)

# %%
a
# %%
a
# %%
a.full()
# %%
b
# %%
c.full()
# %%
a.full()+b.full()-c.full()
# %%
#from __future__ import print_function, absolute_import, division
#import numpy as np
#import tt


#%%
#Tested function
def myfun(x):
    return np.sin((x.sum(axis=1))) #** 2
    #return 1.0 / ((x.sum(axis=1)) + 1e-3)

    #return (x + 1).prod(axis=1)
    #return np.ones(x.shape[0])

def sumFun(x):
    thesum=x.sum(axis=1)
    print("x=",x.shape,x,thesum)
    return thesum

d = 3
n = 5
r = 2

#sz = [n] * d
#ind_all = np.unravel_index(np.arange(n ** d), sz)
#ind_all = np.array(ind_all).T
#ft = reshape(myfun(ind_all), sz)
#xall = tt.tensor(ft, 1e-8)
#x0 = tt.tensor(ft, 1e-8)


x0 = tt.rand(n, d, r)

x1 = rect_cross.cross(sumFun, x0, nswp=5, kickrank=1, rf=2)

# %%
x1
#%%
def unit(n, d=None, j=None, tt_instance=True):
    ''' Generates e_j _vector in tt.vector format
    ---------
    Parameters:
        n - modes (either integer or array)
        d - dimensionality (integer)
        j - position of 1 in full-format e_j (integer)
        tt_instance - if True, returns tt.vector;
                      if False, returns tt cores as a list
    '''
    if isinstance(n, int):
        if d is None:
            d = 1
        n = n * np.ones(d, dtype=np.int32)
    else:
        d = len(n)
    if j is None:
        j = 0
    rv = []

    j = ind2sub(n, j)

    for k in range(d):
        rv.append(np.zeros((1, n[k], 1)))
        rv[-1][0, j[k], 0] = 1
    if tt_instance:
        rv = tt.vector.from_list(rv)
    return rv


def ind2sub(siz, idx):
    '''
    Translates full-format index into tt.vector one's.
    ----------
    Parameters:
        siz - tt.vector modes
        idx - full-vector index
    Note: not vectorized.
    '''
    n = len(siz)
    subs = np.empty((n))
    k = np.cumprod(siz[:-1])
    k = np.concatenate((np.ones(1), k))
    for i in range(n - 1, -1, -1):
        subs[i] = np.floor(idx / k[i])
        idx = idx % k[i]
    return subs.astype(np.int32)

def lin_ind(n0,ind):
    d=len(n0)
    ni = float(n0[0])
    ii=ind[0]
    for i in range(1, d):
        ii+=ind[i]*ni
        ni *= n0[i]
    return ii

t=(1,0,2)
print (lin_ind([2,3,5],t))
print(tt.xfun([2,3,5]).full()[t])
print(tt.xfun([2,3,5]).full())



#%%
##
def bs1(a):
    S,K,T,r,sigma = a
    return bs(S,K,T,r,0,sigma,'call')

def bs(S, K, T, r, q, sigma, option = 'call'):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #q: rate of continuous dividend paying asset 
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    if option == 'call':
        result = (S * np.exp(-q * T) * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == 'put':
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * np.exp(-q * T) * si.norm.cdf(-d1, 0.0, 1.0))
        
    return result


Strikes = np.arange(80,100,5)
Ts = np.arange(0.1,1,0.1)
Ss = np.arange(80,100,5)
sigmas = np.arange(0.2,0.7,0.1)
rs = np.arange(0.01,.05,0.01)

A = [Ss,Strikes,Ts,rs,sigmas]

shape = [len(x) for x in A]

def index_to_var(x):
    s_i,k_i,t_i,r_i,sig_i = x[:,0],x[:,1],x[:,2],x[:,3],x[:,4]
    Aa=np.array([A[0][s_i],A[1][k_i],A[2][t_i],A[3][r_i],A[4][sig_i]]).T
    return Aa

ind1=np.array([[0,0,0,0,0],[1,0,0,1,0]])
index_test= index_to_var(ind1)
print()
def testf(a):
    print("a=",a)
    return a[3]

def bsFun(x):
    pv=np.apply_along_axis(bs1,1,x)
    return pv

print("bs=",bsFun(index_test))

def bs_ind(x):
    y = x.astype(int)
    return bsFun(index_to_var(y))

print("bs_ind=",bs_ind(ind1))
#sz = [n] * d
#ind_all = np.unravel_index(np.arange(n ** d), sz)
#ind_all = np.array(ind_all).T
#ft = reshape(myfun(ind_all), sz)
#xall = tt.tensor(ft, 1e-8)
#x0 = tt.tensor(ft, 1e-8)
#%%

class TrainBSData:
    def __init__(self,strikes,ts,Ss,sigmas,rs):
        self.Strikes = strikes
        self.Ts = ts
        self.Ss = Ss
        self.sigmas = sigmas
        self.rs = rs
        self.A = [self.Ss,self.Strikes,self.Ts,self.rs,self.sigmas]
        self.shape = [len(x) for x in self.A]
    


class TrainBS:
    def __init__(self,bsData : TrainBSData, r : int):
        self.bsData=bsData
        self.r=r
    
    def index_to_var(self,x):
        A=self.bsData.A
        s_i,k_i,t_i,r_i,sig_i = x[:,0],x[:,1],x[:,2],x[:,3],x[:,4]
        Aa=np.array([A[0][s_i],A[1][k_i],A[2][t_i],A[3][r_i],A[4][sig_i]]).T
        return Aa

    def bs_ind(self,x):
        y = x.astype(int)
        return bsFun(self.index_to_var(y))


    def train(self):
        d = 5
        n = self.bsData.shape
        r = self.r
        x0 = tt.rand(n, d, r)
        x1 = rect_cross.cross(self.bs_ind, x0, nswp=5, kickrank=1, rf=2)
        return x1

    def test(self,p,train_res):
        data = self.bsData
        print("shape=",data.shape)
        #p=[1,0,65,23,15]
        print("p    =",p)
        bs_data=[data.A[j][p[j]] for j,k in enumerate(p)]
        print("[Ss,Strikes,Ts,rs,sigmas]=\n",bs_data)
        u1=unit(data.shape,5,lin_ind(data.shape,p))
        print("tt-cross=",tt.dot(train_res,u1))
        print("bs      =",bs1(bs_data))

#%%
Strikes = np.arange(50,150,5)
Ts = np.arange(0.1,1,0.01)
Ss = np.arange(50,150,5)
sigmas = np.arange(0.1,0.7,0.01)
rs = np.arange(0.01,.25,0.01)

data=TrainBSData(Strikes,Ts,Ss,sigmas,rs)
#%%
train = TrainBS(data,10) 
train_res=train.train()
#%%
print("1. preparing .....")
Strikes = np.arange(50,250,1)
Ts = np.arange(0.1,5,0.01)
Ss = Strikes
sigmas = np.arange(0.1,0.7,0.01)
rs = np.arange(0.01,.45,0.01)

data1=TrainBSData(Strikes,Ts,Ss,sigmas,rs)
train1 = TrainBS(data1,10)
print("2. training ......") 
train_res1=train1.train()
print('3. all done, you can tes!')




#%%
np.prod(data1.shape)
#%% 
##############3333 Testing .... #################
p=[60,60,100,0,20]
print(train_res1.core.shape)
print(train_res1.core.shape/np.prod(data1.shape))
train1.test(p,train_res1)
print(train_res1.__getitem__(p))

#print(tt.dot(tt.ones(data1.shape,5),train_res1))
print(tt.sum(train_res1[:,0,0,0,0]))

#%%
############### Testing fit #########
print("shape=",data.shape)
p=[1,0,65,23,15]
print("p    =",p)
bs_data=[data.A[j][p[j]] for j,k in enumerate(p)]
print("[Ss,Strikes,Ts,rs,sigmas]=\n",bs_data)
u1=unit(data.shape,5,lin_ind(data.shape,p))
print("tt-cross=",tt.dot(train_res,u1))
print("bs      =",bs1(bs_data))
#%%

'''
train = TrainBS(data,10) ...
swp: 0/4 er_rel = 2.8e+00 er_abs = 6.7e+05 erank = 15.0 fun_eval: 44472
swp: 1/4 er_rel = 3.2e-03 er_abs = 7.7e+02 erank = 20.0 fun_eval: 129680
swp: 2/4 er_rel = 7.9e-04 er_abs = 1.9e+02 erank = 25.7 fun_eval: 273300
swp: 3/4 er_rel = 2.9e-04 er_abs = 6.9e+01 erank = 31.4 fun_eval: 494640
swp: 4/4 er_rel = 3.6e-06 er_abs = 8.6e-01 erank = 36.9 fun_eval: 809956
'''

fun_evals=\
[44472,
129680,
273300,
494640,
809956]

sum(fun_evals)

print("sum_evals    ",1752048)
print("total params ",np.prod(data.shape))
print("tt params    ",train_res.core.shape[0])

#%%
d = 5
n = shape
r = 3
x0 = tt.rand(n, d, r)
x1 = rect_cross.cross(bs_ind, x0, nswp=5, kickrank=1, rf=2)
#%%

#%%
# x1 contains approximation

print("shape=",shape)
p=[2,0,5,0,0]
print("p    =",p)
u1=unit(shape,5,lin_ind(shape,p))
print("tt-cross=",tt.dot(x1,u1))
#[A[0][0],A[1][0],A[2][0],A[3][0],A[4][0]]

print("bs      =",bs1([A[j][p[j]] for j,k in enumerate(p)]))

# %%
x1.full()
# %%
xf=tt.xfun([3,2,3],1)
# %%
xf.full()
# %%
u1=unit((3,2,3),2,[0,0,0])
print(u1.full())
print(tt.dot(xf,u1))
# %%
###########################33
# 
# try to approximate payoff*density and then calcaulate inegral by summing up
#%%
#%%
class BlackScholesMCInput:
    def __init__(self,s,k,r,t,sigma,N):
        self.S=s
        self.r=r
        self.K=k
        self.T=t
        self.sigma=sigma
        self.N = N

class BlackScholesMC:

    def price(self,inp : BlackScholesMCInput):
        nAssets=1
        w=np.random.normal(0.0,size=[nAssets,inp.N])
        S=inp.S*np.exp((inp.r-.5*inp.sigma**2)*inp.T + np.sqrt(inp.T)*inp.sigma*w)
        payoff = np.maximum(S-inp.K,0)
        pv = payoff*np.exp(-inp.r*inp.T)
        p = np.mean(pv)
        return p#S,payoff,pv,p

class BlackScholesIntegration:

    def price(self,inp : BlackScholesMCInput):
        nAssets=1
        density=norm.pdf
        x = np.linspace(norm.ppf(0.00001),
                norm.ppf(0.99999), 100000)
        dx = x[1:]-x[:-1]
        dP = density(x[1:])*dx
        payoff = lambda s : np.maximum(s-inp.K,0)
        S=inp.S*np.exp((inp.r-.5*inp.sigma**2)*inp.T + np.sqrt(inp.T)*inp.sigma*x[1:])
        integral = np.dot(payoff(S),dP)
        pv = integral*np.exp(-inp.r*inp.T)
        return pv

class BlackScholesMCInputMA(BlackScholesMCInput):
    
    def __init__(self,s,k,r,t,sigma,C,N):
        super().__init__(s,k,r,t,sigma,N)
        self.C=C
    
class BlackScholesMCMA:

    def price(self,inp : BlackScholesMCInputMA):
        nAssets=len(inp.S)
        rr = inp.r*np.ones(nAssets)
        mean=np.zeros(nAssets)
        mean = mean+ (rr - .5*np.array(inp.sigma)**2)*inp.T
        cov = inp.C
        sigs=np.concatenate([sig*np.ones([nAssets,1]) for sig in inp.sigma],axis=1)
        cov=cov*sigs*sigs.T*inp.T
        #print(mean)
        #print(cov)
        w=np.random.multivariate_normal(mean,cov,size=inp.N) 
        S = np.array(inp.S)*np.exp(w)
        Karr=np.array(inp.K)
        SminusK=S-Karr
        payoff = np.amax(np.maximum(SminusK,0,),axis=1)
        pv = np.mean(payoff)*np.exp(-inp.r*inp.T)
        return pv

class BlackScholesIntegralMA:

    def price(self,inp : BlackScholesMCInputMA):
        nAssets=len(inp.S)
        rr = inp.r*np.ones(nAssets)
        mean=np.zeros(nAssets)
        mean = mean+ (rr - .5*np.array(inp.sigma)**2)*inp.T
        cov = inp.C
        sigs=np.concatenate([sig*np.ones([nAssets,1]) for sig in inp.sigma],axis=1)
        cov=cov*sigs*sigs.T*inp.T

        dist = multivariate_normal(mean,cov)
        
        u=np.random.uniform(-10,10,size=(nAssets,inp.N)).T
        #print(u)
        S = np.array(inp.S)*np.exp(u)
        mu=dist.pdf(u)
        print("mu=",mu)
        #print(S)
        Karr=np.array(inp.K)
        SminusK=S-Karr
        payoff = np.amax(np.maximum(SminusK,0,),axis=1)*mu
        pv = np.mean(payoff)*np.exp(-inp.r*inp.T)*((20)**nAssets)
        return pv


#%%
class PayoffInp:
    def __init__(self,strikes):
        self.strikes = strikes


class VariableRange:
    def __init__(self,low,high,dx):
        self.low = low
        self.high = high
        self.dx = dx

class BSVariableRanges:
    def __init__(self,\
        s0 : VariableRange,\
        sig : VariableRange,\
        r : VariableRange,\
        t : VariableRange):
        
        self.s0=s0
        self.sig=sig
        self.r=r
        self.t=t


class TTDiscretization:
    def __init__(self,num_assets, bsRanges : BSVariableRanges):
        self.num_assets = num_assets
        self.ranges = bsRanges
    
    def get_discretization(self,x : VariableRange):
        factor = self.get_discretization1(x)
        return np.array(self.num_assets*[factor])

    def get_discretization1(self,x : VariableRange):
        factor = np.arange(x.low,x.high,x.dx)
        return factor


    def get_arrays(self):
        factor = np.arange(-6,6,self.get_dx())
        s0=self.get_discretization(self.ranges.s0)
        return {\
            "spot_base":np.array(self.num_assets*[factor]),\
            "s0":s0,\
            "r":self.get_discretization1(self.ranges.r),\
            "t":self.get_discretization1(self.ranges.t),\
            "sigma":self.get_discretization(self.ranges.sig)}

    def get_dx(self):
        return 0.5
    
    def get_dvol(self):
        return self.get_dx()**self.num_assets

    
class TTDiscretizationIndex:
    def __init__(self,s : np.array,dvol :float):
        self.disc_arrays=s
        self.dvol1=dvol
        
    
    def dvol(self):
        return self.dvol1

    def get_n(self):
        s=self.disc_arrays['spot_base'].shape
        s0=self.disc_arrays['s0'].shape
        sig=self.disc_arrays['sigma'].shape
        r=self.disc_arrays['r'].shape
        t=self.disc_arrays['t'].shape
        gn=sig[0]*[sig[1]]+s0[0]*[s0[1]]+s[0]*[s[1]]+[r[0]]+[t[0]]

        
        return gn

    def get_d(self):
        return len(self.get_n())
        
    def index_to_var(self,index) -> dict:
        # index structure: 
        
        s = self.disc_arrays['spot_base']
        d = len(s)
        spot_base = [s[j][ind] for j,ind in enumerate(index[2*d:3*d])]
        
        s = self.disc_arrays['s0']
        s0 = [s[j][ind] for j,ind in enumerate(index[d:2*d])]
        
        s = self.disc_arrays['sigma']
        sigma = [s[j][ind] for j,ind in enumerate(index[0:1*d])]
        
        s = self.disc_arrays['r']
        r = [s[ind] for j,ind in enumerate(index[3*d:3*d+1])]

        s = self.disc_arrays['t']
        t = [s[ind] for j,ind in enumerate(index[3*d+1:3*d+2])]

        return {'spot_base':spot_base,'s0':s0,'sigma':sigma,'r':r,'t':t}


class BlackScholesTTMA:

    def __init__(self,r,payoff_inp : PayoffInp, indexing : TTDiscretizationIndex):
        self.r = r
        self.payoff_inp = payoff_inp
        self.indexing = indexing
        

    def index_to_var(self,x):
        return self.indexing.index_to_var(x)
    
    def get_payoff_times_density_ind(self,inp):
        Karr=np.array(self.payoff_inp.strikes)
        Sarr=np.array(inp.S)
        print("Sarr",Sarr,"Karr",Karr)
        nAssets=len(inp.S)
        def payoff_times_density_ind1(ind):
            ivar = self.index_to_var(ind)
            inpsigma = np.array(ivar['sigma'])#np.array(inp.sigma)#
            inpr = inp.r#np.array(ivar['r'])
            inpT = inp.T#np.array(ivar['t'])
            
            rr = inpr*np.ones(nAssets)
            mean=np.zeros(nAssets)
            mean = mean+ (rr - .5*inpsigma**2)*inpT
            cov = inp.C.copy()
            sigs=np.concatenate([sig*np.ones([nAssets,1]) for sig in inpsigma],axis=1)
            cov=cov*sigs*sigs.T*inpT

            dist = multivariate_normal(mean,cov)


            u = np.array(ivar['spot_base'])
            s0 = np.array(ivar['s0'])
            S = s0*np.exp(u)
            SminusK=S-Karr
            mu=dist.pdf(u)
            payoff = np.amax(np.maximum(SminusK,0,),axis=0)*mu
            return payoff

        
        def payoff_times_density_ind(x):
            y = x.astype(int)
            return np.apply_along_axis(payoff_times_density_ind1,1,y)

        return payoff_times_density_ind

    def fit(self,inp : BlackScholesMCInputMA):
        start = time.time()
        print("fitting TT.....")
        nAssets=len(inp.S)
        d = self.indexing.get_d()
        n = self.indexing.get_n()
        r = self.r

        '''
        nAssets=len(inp.S)
        rr = inp.r*np.ones(nAssets)
        mean=np.zeros(nAssets)
        mean = mean+ (rr - .5*np.array(inp.sigma)**2)*inp.T
        cov = inp.C
        sigs=np.concatenate([sig*np.ones([nAssets,1]) for sig in inp.sigma],axis=1)
        cov=cov*sigs*sigs.T*inp.T

        dist = multivariate_normal(mean,cov)
        '''

        print("ndr=",n,d,r)
        x0 = tt.rand(n, d, 1)
        x1 = rect_cross.cross(self.get_payoff_times_density_ind(inp), x0)#, nswp=8, kickrank=1, rf=2)     

        
        endt = time.time()
        print("done fitting T={}! ".format(endt-start))
        return x1

    
    def get_tensor(self,inp : BlackScholesMCInputMA):
        # fit
        x1=self.fit(inp)
        # calculate pv
        return x1#,tt.sum(x1)*np.exp(-inp.r*inp.T)*self.indexing.dvol()
    
    def get_pv(self,inp,tensor):

        a1 = self.indexing.disc_arrays
        s0_i  = [np.abs(a1['s0'] - s).argmin() for s in inp.S]
        sig_i = [np.abs(a1['sigma'] - s).argmin() for s in inp.sigma]
        r_i,t_i = \
                np.abs(a1['r'] - r).argmin(),\
                np.abs(a1['t'] - t).argmin()

        n =self.indexing.get_n()
        self.tensor = tensor
        num_assets=len(inp.S)
        to_sum_index=[range(n[2*num_assets + l]) for l in range(num_assets)]
        to_sum_index=sig_i+s0_i+to_sum_index+[r_i]+[t_i]
        pv=tt.sum(tensor[to_sum_index])*np.exp(-inp.r*inp.T)*self.indexing.dvol()
        return pv
    
    def price(self,inp : BlackScholesMCInputMA):
        x1=self.get_tensor(inp)
        pv=self.get_pv(inp,x1)
        return x1,pv



# %%

s,k,r,t,sigma,C,N = (12,12),(11.5,10.5),0.01,1.2,(.13,.2),np.array([[1,.7],[.7,1]]),1000000
inpMA=BlackScholesMCInputMA(s,k,r,t,sigma,C,N)
s_range,sig_range,r_range,t_range = \
    VariableRange(0.0,20,1),\
    VariableRange(0.1,.4,.01),\
    VariableRange(0.01,.1,.01),\
    VariableRange(0.0,2,.1)        
bs_ranges = BSVariableRanges(s_range,sig_range,r_range,t_range)
disc=TTDiscretization(len(s),bs_ranges)
pricers = [ ]

#plt.scatter(w[0][:,0],w[0][:,1])
#print("w=",w)

#s,k,r,t,sigma,C,N = (120,100),(95,115),0.01,1.2,(.3,.2),np.array([[1,.7],[.7,1]]),1000000
inpMA=BlackScholesMCInputMA(s,k,r,t,sigma,C,N)
pricers = [BlackScholesMCMA(),\
    BlackScholesIntegralMA(),\
        BlackScholesTTMA(10,PayoffInp(k),TTDiscretizationIndex(disc.get_arrays(),disc.get_dvol()))]

w=[pr.price(inpMA) for pr in pricers]
#plt.scatter(w[0][:,0],w[0][:,1])
print("w=",w)
#%%
disc_ind=TTDiscretizationIndex(disc.get_arrays(),disc.get_dvol())
print(np.array(disc_ind.index_to_var((100,100,10,10,25,26,10,200))['sigma'] )  )
#print(disc_ind.disc_arrays['sigma'])

#%%
s,k,r,t,sigma,C,N = (12,9),(11.5,10.5),0.01,1.2,(.3,.2),np.array([[1,.7],[.7,1]]),1000000

inp2 = BlackScholesMCInputMA(s,k,r,t,sigma,C,N)
print("tt=",pricers[2].get_pv(inp2,w[2][0]))

w1=[pr.price(inp2) for pr in pricers[0:2]]
print("w=",w1)

#%%
tens=w[2][0]
#tens[]

ind1=TTDiscretizationIndex(disc.get_arrays(),disc.get_dvol())

a1=disc.get_arrays()

show_by_s=True
if show_by_s:
    inpps = [BlackScholesMCInputMA([s1,10],k,r,t,[.21,.13],C,N) for s1 in a1['s0'][0]]
    xs=a1['s0'][0]
    ys_tt=[pricers[2].get_pv(inpp,w[2][0]) for inpp in inpps]
    ys_mc=[pricers[0].price(inpp) for inpp in inpps]
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(xs)
    ax.set_yticks(np.arange(0,10,.1))
    plt.scatter(xs,ys_tt,label="tt")
    plt.scatter(xs,ys_mc,label="mc")
    plt.legend()
    plt.grid()
    fig.autofmt_xdate()
    ax.set_xticks(ax.get_xticks()[::2])
    ax.set_yticks(ax.get_yticks()[::4])
    fig.tight_layout()
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.show()



xs=a1['sigma'][0]
inpps = [BlackScholesMCInputMA([13,10],k,r,t,[sig,.23],C,N) for sig in xs]
ys_tt=[pricers[2].get_pv(inpp,w[2][0]) for inpp in inpps]
ys_mc=[pricers[0].price(inpp) for inpp in inpps]

fig = plt.figure()
ax = fig.gca()
ax.set_xticks(xs)
ax.set_yticks(np.arange(0,10,.1))
plt.scatter(xs,ys_tt,label="tt")
plt.scatter(xs,ys_mc,label="mc")
plt.legend()
plt.grid()
fig.autofmt_xdate()
ax.set_xticks(ax.get_xticks()[::2])
fig.tight_layout()
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.show()



#a=a1['s0']
#a0=np.array([12,13])
#agmin=np.abs(a - a0).argmin()
#print(agmin)
#print(a.flat[agmin])
#print(a[0][12])

s01_i,s02_i,sig1_i,sig2_i,r_i,t_i = \
    np.abs(a1['s0'] - s[0]).argmin(),\
    np.abs(a1['s0'] - s[1]).argmin(),\
    np.abs(a1['sigma'] - sigma[0]).argmin(),\
    np.abs(a1['sigma'] - sigma[1]).argmin(),\
    np.abs(a1['r'] - r).argmin(),\
    np.abs(a1['t'] - t).argmin()


print("s01_i,s02_i,sig1_i,sig2_i,r_i,t_i=",s01_i,s02_i,sig1_i,sig2_i,r_i,t_i)
print("s01_i,s02_i,sig1_i,sig2_i,r_i,t_i=",a1['s0'][0][s01_i],a1['s0'][1][s02_i],a1['sigma'][0][sig1_i],a1['sigma'][1][sig2_i],a1['r'][r_i],a1['t'][t_i])
print("sum=",tt.sum(tens[:,:,s01_i,s02_i,sig1_i,sig2_i,r_i,t_i])*ind1.dvol()*np.exp(-r*t))
#%%
s,k,r,t,sigma,N = 100,115,0.01,1.2,.2,1000000
inp=BlackScholesMCInput(s,k,r,t,sigma,N)
pricer = BlackScholesMC()
prcer_integral = BlackScholesIntegration()
o_integral = prcer_integral.price(inp)
bs_price = bs(s,k,t,r,0,sigma)
for _ in range(10):
    o=pricer.price(inp)
    print("mc={} integral={} bs={}".format(o,o_integral,bs_price))


#print(o[3])
#print(np.concatenate(o[0:3],axis=0).T)

#%%

fig, ax = plt.subplots(1, 1)
x = np.linspace(norm.ppf(0.01),
                norm.ppf(0.99), 100)
ax.plot(x, norm.pdf(x),
       'r-', lw=5, alpha=0.6, label='norm pdf')
# %%
x
# %%
[x[j]-x[j+1] for j in [1,2,3,4,5,6]]
# %%

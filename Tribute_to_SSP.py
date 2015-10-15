# (Cathryn) Yining Chen, Tribute to SSP 2013'
# Date: 2013/7/21, the Sunday after OD deadline
import math
import numpy
from numpy import matrix
from visual import *
from ephemPy import Ephemeris as Ephemeris_BC
import time

# Scene 1

for i in range(2):
    text1=text(text='SSP',font='Times',align='center', depth=-0.6, color=(1,1,1),size=10)
    rate(1)
    text1.visible=False

for i in range(2):
    text1=text(text='The most wonderful experience ever...',font='Times',align='center', pos=(-1,-1,-1),depth=-0.6, color=(1,1,1),size=5)
    rate(1)
    text1.visible=False

position=['################################################################################',
          '################################################################################',
          '##                                                                            ##',
          '##                                                                            ##',
          '##          $$$$$$$$$$              $$$$$$$$$$             $$$$$$$$$$$$       ##',
          '##         $$                      $$                     $$          $$      ##',
          '##        $$                      $$                      $$           $$     ##',
          '##       $$                      $$                       $$            $$    ##',
          '##      $$                      $$                        $$            $$    ##',
          '##     $$$                     $$$                        $$           $$     ##',
          '##     $$$                     $$$                        $$          $$      ##',
          '##      $$$                     $$$                       $$         $$       ##',
          '##        $$$                     $$$                     $$       $$$        ##',
          '##           $$$$$$$                 $$$$$$$              $$    $$$           ##',
          '##                 $$$$$                   $$$$$          $$  $$$             ##',
          '##                    $$$                     $$$         $$$$$               ##',
          '##                     $$$                     $$$        $$                  ##',
          '##                     $$$                     $$$        $$                  ##',
          '##                    $$$                     $$$         $$                  ##',
          '##                   $$$                     $$$          $$                  ##',
          '##                  $$$                     $$$           $$                  ##',
          '##                 $$                      $$             $$                  ##',
          '##               $$                      $$               $$                  ##',
          '##        $$$$$$$                 $$$$$$$                 $$                  ##',
          '##                                                                            ##',
          '##                                                                            ##',
          '################################################################################',
          '################################################################################']

textssp=[]
for i in range(3,24):
    for j in range(3,76):
        if position[i][j]!=' ':
            textssp.append(text(text='SSP',font='Times',align='center', pos=(14-i,3,40-j),depth=-0.4, color=(1,1,1),size=1))
            rate(100000000000)

l=len(textssp)
for i in range(l):
    textssp[i].visible=False

# Scene 2

for i in range(10):
    text1=text(text="Asteroids' Reunion",font='Times',align='center', depth=-0.6, color=(1,0.7,0.2),size=10)
    rate(1)
    text1.visible=False

# Scene 3

# This makes a big table of epheme data
# copied from the JPL DE405 ephem website

class Ephemeris(Ephemeris_BC):
 
    def __init__(self, *args, **kwargs):
        Ephemeris_BC.__init__(self, *args, **kwargs)
        self.AUFAC = 1.0/self.constants.AU
        self.EMFAC = 1.0/(1.0+self.constants.EMRAT)
 
    def position(self, t, target, center):
        pos = self._position(t, target)
        if center != self.SS_BARY:
            pos = pos - self._position(t, center)
        return pos
     
    def _position(self, t, target):
        if target == self.SS_BARY:
            return numpy.zeros((3,), numpy.float64)
        if target == self.EM_BARY:
            return Ephemeris_BC.position(self, t, self.EARTH)*self.AUFAC
        pos = Ephemeris_BC.position(self, t, target)*self.AUFAC
        if target == self.EARTH:
            mpos = Ephemeris_BC.position(self, t, self.MOON)*self.AUFAC
            pos = pos - mpos*self.EMFAC
        elif target == self.MOON:
            epos = Ephemeris_BC.position(self, t, self.EARTH)*self.AUFAC
            pos = pos + epos - pos*self.EMFAC
        return pos
 
 
ephem = Ephemeris('405')

arrow(pos=(0,0,0),axis=(1,0,0),shaftwidth=.1,color=(5,0,0))
arrow(pos=(0,0,0),axis=(0,1,0),shaftwidth=.1,color=(0,5,0))
arrow(pos=(0,0,0),axis=(0,0,1),shaftwidth=.1,color=(0,0,5))
label(pos=(1.25,0,0),text='x',box=0)
label(pos=(0,1.25,0),text='y',box=0)
label(pos=(0,0,1.25),text='z',box=0)
box(pos=(0,0,0),opacity=.2,axis=(1,0,0),width=.01,length=5,height=5,color=(1,1,0))

r=[vector(0.345443, -1.14274, 0.162192),vector(0.0976895, -1.34317, 0.0749987),
   vector(0.243764, -1.30646, -0.0489946),vector(0.275722, -1.23899, -0.00482837),
   vector(0.403564, -1.2852, 0.232651),vector(0.5359701224004094, -0.9867908107784090, 0.04220099957441736)]
rdot=[vector(1.09103, -0.00560825, 0.233963),vector(0.838704, -0.206117, -0.225285),
      vector(0.811069, 0.677202, 0.0407638),vector(0.998037, 0.319343, 0.137646),
      vector(0.853979, -0.243504, 0.490869),vector(0.966154843396939, 0.53320719497176700, -0.158853015910725)]
t=[2456481.72538,2456472.67676,2456478.77096,2456481.76349,2456487.66695,2456477.83333]
as_text=["1998 QE2","1999 KX4","1999 ML14","2007 TX18","1999 WC2","1627 Ivar"]

mint=t[0]
asteroid=[]
as_label=[]
for i in range(len(t)):
    if mint>t[i]:
        mint=t[i]
    asteroid.append(sphere(pos=r[i],color=(2,2,2),radius=.02))
    asteroid[i].visible=False
    as_label.append(label(pos=r[i]+(.15,.15,.15),text=as_text[i],box=0))
    as_label[i].visible=False
mint_copy=mint

trail=[curve(color=color.red),curve(color=color.magenta),curve(color=color.cyan),
       curve(color=color.orange),curve(color=color.green),curve(color=color.white)]

R=ephem.position(mint, 10, 2)
earth=sphere(pos=R,color=(0,0,1),radius=.05)
trail_e=curve(color=color.blue)
e_label=label(pos=R+(.15,.15,.15),text="Earth",box=0)

dt=.0001

def fpar(tao,r,rdot):
    f2=1-(tao**2)*.5/(mag(r)**3)
    f2+=(tao**3)*dot(r,rdot)/2/(mag(r)**5)
    f3=f2+(tao**4)/24*(3/(mag(r)**3)*(dot(rdot,rdot)/(mag(r)**2)-1/(mag(r)**3))-15*(dot(r,rdot)**2)/(mag(r)**7)+1/mag(r)**6)
    return f3

def gpar(tao,r,rdot):
    return tao-tao**3/6/(mag(r)**3)+dot(r,rdot)/4/(mag(r)**5)*(tao**4)

def taylor(dt,r,rdot):
    ans=[]
    ans.append(fpar(dt,r,rdot)*r+gpar(dt,r,rdot)*rdot)
    ans.append(rdot-dt*r/mag(r)**3)
    return ans

while mint<2460000:
    rate(1000000000)
    for i in range(len(t)):
        if t[i]>=mint_copy:
            asteroid[i].visible=True
            asteroid[i].pos=r[i]
            as_label[i].visible=True
            as_label[i].pos=r[i]+(.15,.15,.15)
            trail[i].append(pos=r[i])
            state=taylor(dt,r[i],rdot[i])
            r[i]=state[0]
            rdot[i]=state[1]
    
    earth.pos=R
    e_label.pos=R+(.15,.15,.15)
    trail_e.append(pos=R)
    mint+=dt*58  
    R=ephem.position(mint, 10, 2)


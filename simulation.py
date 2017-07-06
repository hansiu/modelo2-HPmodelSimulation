#! /usr/bin/env/python
from aminoacids import AminoAcid
from random import randint,choice,random
from math import exp
from decimal import Decimal,getcontext
from trajectoryAndStatistics import *
getcontext().prec=3

class Simulation:

    def __init__(self, chain='PHPPHPPHHPPHHPPHPPHP',K=10000,Tmax=1.0,Tmin=0.15,Tdelta=0.05,kB=1):
        self.chain=[AminoAcid(chain[i]) for i in range(len(chain))]
        self.K=K
        self.T=float(Tmax)
        self.Tmin=Decimal(Tmin)
        self.Tdelta=Decimal(Tdelta)
        self.kB=kB
        self.rotations=set([90,180,270])
        self.best=self.chain
        self.Hbest=0

        
    def Run(self):
        st=0
        print('Przed ruszaniem: ')
        for atom in self.chain:
            print(atom)
        trajectory(st,self.chain,[a.coords for a in self.chain])
        stats(0)
        Hcount=[0]
        while Decimal(self.T) >= self.Tmin:
            accepted_steps=0
            e_sum=0
            e_squared_sum=0
            i_sum=0
            st+=1
            print("temperatura "+str(self.T))
            for step in range(self.K):
                h=0
                num=randint(0,len(self.chain)-2)#bo oprocz ostatniego
                coor=self.chain[num].coords
                for a in self.chain:
                    a.SetPlace(a.coords-coor)
                rots=set()
                for l in range(3):
                    rotate=choice(list(self.rotations-rots))
                    rots.add(rotate)
                    bad=False
                    rotated=[]
                    for a1 in self.chain:
                        if a1.number<=num:
                            rotated.append(a1)
                        else:
                            rotated.append(a1.Rotate(rotate))
                    while not bad:
                        for r1 in rotated:
                            for r in rotated:
                                if (r1)!=(r):
                                    if r.coords==r1.coords:
                                        bad=True
                        break;
                    if not bad:
                        break
                if not bad:
                    x=0
                    y=0
                    for a1 in rotated:
                        for a2 in rotated:
                            if a1!=a2 and rotated.index(a1)!=rotated.index(a2)-1 and rotated.index(a1)!=rotated.index(a2)+1:
                                if a1.type=='H' and a2.type=='H':
                                    if a1.Neighbour(a2):
                                        h+=1
                        x+=a1.coords[0]
                        y+=a1.coords[1]
                    h/=2
                    if h>=Hcount[-1]:
                        for x in range(len(self.chain[(num+1):])):
                            self.chain[(num+1):][x].SetPlace(rotated[(num+1):][x].coords)
                        Hcount.append(h)
                        accepted=True
                    else:
                        prob=((exp(h/(self.kB*self.T)))/(exp(Hcount[-1]/(self.kB*self.T))))
                        if random() <= prob:
                            accepted=True
                        else:
                            accepted=False

                else:
                    accepted=False
                if accepted:
                    for x in range(len(self.chain[(num+1):])):
                        self.chain[(num+1):][x].SetPlace(rotated[(num+1):][x].coords)
                    Hcount.append(h)
                    if Hcount[-1]>self.Hbest:
                        self.Hbest=Hcount[-1]
                        self.best=[a.coords for a in self.chain]
                    contacts(self.T,accepted_steps,h)
                    accepted_steps+=1
                    e_sum+=-h
                    e_squared_sum+=(-h)**2
                    x/=len(self.chain)
                    y/=len(self.chain)
                    for a in self.chain:
                        i_sum+=(x-a.coords[0])**2 + (y-a.coords[1])**2
                Hcount=Hcount[-2:]
            trajectory(st,self.chain,self.best)
            Cv=((e_squared_sum/accepted_steps)-((e_sum/accepted_steps)**2))/(self.kB*(self.T**2))
            I=i_sum/accepted_steps
            stats(self.T,Cv,I)
            plot_contacts(self.T)
            self.Hbest=0
            self.T=float(Decimal(self.T)-self.Tdelta)
        plot_stats()
        
    def __str__(self):
        return(str(self.atoms))
        
    def __repr__(self):
        return(str(self.atoms))

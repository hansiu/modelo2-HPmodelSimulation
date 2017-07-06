#! /usr/bin/env/python

class Vector:
    dim=2
    def __init__(self,coords=None):
        if coords is None:
            self.dim=Vector.dim
            self.coords=[0 for d in range(self.dim)]
        elif isinstance(coords,list):
            self.dim=len(coords)
            self.coords=[c for c in coords]
        else: 
            self.dim=1
            self.coords=coords

    def NewCoords(self,coords):
        self.dim=len(coords)
        self.coords=[c for c in coords]
        return(self)

    def length(self):
        len=float(0)
        for i in range(self.dim):
            len+=self.coords[i]**2
        len=len**0.5
        return(len)

    def __getitem__(self,i):
        return(self.coords[i])

    def __setitem__(self,i,x):
        self.coords[i]=x
	
    def __str__(self):
        return(str(self.coords))

    def __repr__(self):
        return('Vector('+str(self.coords)+')')

    def __neg__(self):
        vsig=Vector()
        for i in range(self.dim):
            vsig.coords[i]=-self.coords[i]
        return(vsig)
        
    def __pos__(self):
        return self.coords
        
    def __add__(self,other):
        vsum=Vector()
        if isinstance(other, Vector):
            if self.dim>=other.dim:
                vsum.NewCoords(self.coords.copy())#copy zrobic
                for i in range(int(other.dim)):
                    vsum[i]+=other.coords[i]
            else:
                vsum.NewCoords(other.coords.copy())
                for i in range(int(self.dim)):
                    vsum[i]+=self.coords[i]
        elif isinstance(other,float) or isinstance(other, int):
            vsum.NewCoords(self.coords.copy())
            for i in range(int(self.dim)):
                vsum[i]+=other
        else:
            raise TypeError(other)
        return(vsum)
        
    def __radd__(self, other):
        return(self + other)
        
    def __sub__(self,other):
        vsum=Vector()
        if isinstance(other, Vector):
            if self.dim>=other.dim:
                vsum.NewCoords(self.coords.copy())
                for i in range(int(other.dim)):
                    vsum[i]-=other.coords[i]
            else:
                vsum.NewCoords(-(other.coords))
                for i in range(int(self.dim)):
                    vsum[i]+=self.coords[i]
        elif isinstance(other,float) or isinstance(other, int):
            vsum.NewCoords(self.coords.copy())
            for i in range(int(self.dim)):
                vsum[i]-=other
        else:
            raise TypeError(other)
        return(vsum)
    
    def __mul__(self,other):
        if isinstance(other, Vector):
            vmul=0
            if self.dim<=other.dim:
                for i in range(int(self.dim)):
                    vmul+=self.coords[i]*other.coords[i]
            else:
                for i in range(int(other.dim)):
                    vmul+=other.coords[i]*self.coords[i]
        elif isinstance(other,float) or isinstance(other,int):
            vmul=Vector()
            vmul.NewCoords(self.coords.copy())
            for i in range(int(self.dim)):
                vmul[i]*=other
        else:
            raise TypeError(other)
        return(vmul)
        
    def __div__(self,other):
        if other==0:
            raise ZeroDivisionError(other)
        if isinstance(other,float) or isinstance(other,int):
            vmul=Vector()
            vmul.NewCoords(self.coords.copy())
            for i in range(int(self.dim)):
                vmul[i]/=other
        else:
            raise TypeError(other)
        return(vmul)
    
    def __rdiv__(self,other):
        return(self/other)

    def __eq__(self,other):
        if isinstance(other,Vector):
            return(self.coords==other.coords)
        elif isinstance(other,list):
            return(self.coords==other)
        elif self.dim==1 and isinstance(other,int):
            return(self.coords[0]==other)
        elif self.coords==[] and not other:
            return(True)
        else:
            return(False)

#! /usr/bin/env/python
from vector import Vector
class AminoAcid():
    number=0

    def __init__(self,type):
        self.number=AminoAcid.number
        AminoAcid.number+=1
        self.type=type
        self.coords=Vector([self.number,0])
        
    def SetPlace(self,newplace):
        if isinstance(newplace,list):
            self.coords=Vector.NewCoords(newplace)
        elif isinstance(newplace,Vector):
            self.coords=newplace
        else:
            sys.exit('aa coords need to be a list')
            
    def Rotate(self,rotation):
        rot=[]
        if rotation==90:
            rot=[self.coords[1],-self.coords[0]]
        elif rotation==180:
            rot=[-self.coords[0],-self.coords[1]]
        elif rotation==270:
            rot=[-self.coords[1],self.coords[0]]
        else:
            sys.exit('wrong rotation')
        aa=AminoAcid(self.type)
        aa.coords=Vector(rot)
        return(aa)
        
    def Neighbour(self,other):
        neighbours=[[self.coords[0],self.coords[1]+1],[self.coords[0],self.coords[1]-1],[self.coords[0]+1,self.coords[1]],[self.coords[0]-1,self.coords[1]]]
        for n in neighbours:
            if other.coords==n:
                return(True)
        return(False)
        
    def __str__(self):
        return(str(self.number)+': '+self.type+' '+str(self.coords))
    def __repr__(self):
        return(str(self.number)+': '+self.type+' '+str(self.coords))
        
    
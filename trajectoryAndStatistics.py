#! /usr/bin/env/python
from matplotlib import pyplot

def trajectory(step,atoms,bestcoords):
    if step==0:
        traj=open('traj.pdb','w')
        best=open('best.pdb','w')
        traj.close()
        best.close()
    traj=open('traj.pdb','a')
    best=open('best.pdb','a')
    traj.write('MODEL '+str(step)+'\n')
    best.write('MODEL '+str(step)+'\n')
    for atom in atoms:
        if atom.type=='H':
            name='ALA'
        else:
            name='ARG'
        traj.write('ATOM  '+str(atom.number).rjust(5)+'   C  '+name+' A'+str(atom.number).rjust(4)+'    '+str(round(atom.coords[0],3)).rjust(8)+str(round(atom.coords[1],3)).rjust(8)+'0'.rjust(8)+'                       C  \n')
        best.write('ATOM  '+str(atom.number).rjust(5)+'   C  '+name+' A'+str(atom.number).rjust(4)+'    '+str(round(bestcoords[atoms.index(atom)][0],3)).rjust(8)+str(round(bestcoords[atoms.index(atom)][1],3)).rjust(8)+'0'.rjust(8)+'                       C  \n')
    traj.write('ENDMDL\n')
    best.write('ENDMDL\n')

def contacts(temp,step,H):
    if step==0:
        energy=open('Contacts'+str(temp)+'.txt','w')
        energy.close()
    energy=open('Contacts'+str(temp)+'.txt','a')
    energy.write(str(int(H))+';')
    
def stats(temp,Cv=None,I=None):
    if temp==0:
        cfile=open('Cv.txt','w')
        ifile=open('I.txt','w')
        cfile.close()
        ifile.close()
    else:
        cfile=open('Cv.txt','a')
        ifile=open('I.txt','a')
        cfile.write(str(temp)+';'+str(Cv)+'\n')
        ifile.write(str(temp)+';'+str(I)+'\n')
        
def plot_contacts(temp):
    file=open('Contacts'+str(temp)+'.txt')
    contacts=[]
    for line in file:
        line=line.split(';')[:-1]
        contacts+=[int(x) for x in line]
    pyplot.title('Liczba kontaktow H-H dla temperatury '+str(temp))
    pyplot.xlabel('liczba kontaktow H-H')
    pyplot.ylabel('Ilosc krokow')
    pyplot.hist(contacts,range=(0,10),normed=False)
    pyplot.savefig('Contacts'+str(temp)+'.png')
    pyplot.clf()
    pyplot.close
    
def plot_stats():
    ifile=open('I.txt')
    cfile=open('Cv.txt')
    temperatures=[]
    Is=[]
    Cvs=[]
    for line in ifile:
        line=line.split(';')
        temperatures.append(line[0])
        Is.append(line[1])
    for line in cfile:
        line=line.split(';')
        Cvs.append(line[1])
    pyplot.title('Moment bezwladnosci')
    pyplot.xlabel('temperatura')
    pyplot.ylabel('moment bezwladnosci')
    pyplot.plot(temperatures,Is)
    pyplot.savefig('Is.png')
    pyplot.clf()
    pyplot.close()
    pyplot.title('Cieplo wlasciwe')
    pyplot.xlabel('temperatura')
    pyplot.ylabel('cieplo wlasciwe')
    pyplot.plot(temperatures,Cvs)
    pyplot.savefig('Cvs.png')
    pyplot.clf()
    pyplot.close()
    

import math,random


class ball :
    def __init__(self,canevas,Mafenetre,balle):
        self.vitesse=random.uniform(1.8,2)*5
        self.angle=random.uniform(0,2*math.pi)

        self.DX=self.vitesse*math.cos(self.angle)
        self.DY=self.vitesse*math.sin(self.angle)

        self.H=880
        self.L=650
        self.R=15
        self.X=self.L/2
        self.Y=self.H/2
        def deplacement(self):
            global X,Y,DX,DY,R,H,L
            if self.X+self.DX+self.R > self.L :
                self.X=2*(self.L-self.R)-self.X
                self.DX=-self.DX
            if self.X-self.R+self.DX <0:
                self.X=2*self.R-self.X
                self.DX=-self.DX
            if self.Y+self.DY+self.R > self.H :
                self.Y=2*(self.H-self.R)-self.Y
                self.DY=-self.DY
            if self.Y-self.R+self.DY <0:
                self.Y=2*self.R-self.Y
                self.DY=-self.DY

            self.X=self.X+self.DX
            self.Y=self.Y+self.DY
        canevas.coords(balle,self.X-self.R,self.Y-self.R,self.X+self.R,self.Y+self.R)
        Mafenetre.after(20,deplacement)
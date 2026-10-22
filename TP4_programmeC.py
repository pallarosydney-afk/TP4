"""
Objectif : création d'un casse brique / utilisation des bonnes pratiques 
Utilisateur : Charline TALON 
Date : 08/10/2026
ToDo :
"""


class plateforme:
    def __init__(self,canevas):
        self.Canevas=canevas
        self.raquette=canevas.create_rectangle(400,600,480,610,outline='black',fill='grey')
    def Clic(self,event):
        global DETECTION_CLIC
        self.X=event.x
        self.Y=event.y
        [self.Xmin,self.Ymin,self.Xmax,self.Ymax]=self.Canevas.coords(self.raquette)
        if self.Xmin<=self.X<=self.Xmax and self.Ymin<=self.Y<=self.Ymax:
            self.DETECTION_CLIC=True 
        else :
            self.DETECTION_CLIC=False
        print("DETECTION_CLIC ->",self.DETECTION_CLIC)

    def drag(self,event):
        
        self.X=event.x
        self.Y=event.y
        if self.DETECTION_CLIC == True :
            if self.X<0:
                self.X=0
            if self.X>880:
                self.X=880
            if self.Y <0:
                self.Y=0
            if self.Y>650:
                self.Y=650
            self.Canevas.coords(self.raquette,self.X-50,self.Y-10,self.X+10,self.Y+50)


    




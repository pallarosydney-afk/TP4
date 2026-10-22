from tkinter import Button,Tk,Pack,Canvas
import TP4_programmeC as f
import TP4_mouvement as fo


class interface :
    def __init__(self):

        self.Mafenetre= Tk()
        self.Mafenetre.geometry('900x700')
        self.Mafenetre.title('casse brique')

        self.Mafenetre.config(cursor='heart')

        self.Canevas=Canvas(self.Mafenetre,width=880,height=650,bg='white')
        self.Canevas.pack(padx=5,pady=5) 
        self.l=100
        self.e=10
        self.h=30

        

        self.H=880
        self.L=650
        self.R=15
        self.X=self.L/2
        self.Y=self.H/2
        self.balle=self.Canevas.create_oval(self.X-self.R,self.Y-self.R,self.X+self.R,self.Y+self.R,outline="#000B80",fill="#1CE6DC")
        b=fo.ball(self.Canevas,self.Mafenetre,self.balle)
        for j in range(5):
            for i in range(8):
                self.X1=5+i*(self.l+self.e)
                self.X2=self.X1+self.l
                self.Y1=j*(self.h+5)+2
                self.Y2=self.Y1+self.h
                self.Canevas.create_rectangle(self.X1,self.Y1,self.X2,self.Y2,outline="#6E0D06", fill="#BB0362")

        def jouer ():
            p=f.plateforme(self.Canevas)
            self.raquette = p.raquette
            self.Canevas.bind("<Button -1>",p.Clic)
            self.Canevas.bind('<B1-Motion>',p.drag)
            self.Canevas.focus_set()
            self.deplacement=b.deplacement()
            i.deplacement()

        self.ButonLancer  = Button(self.Mafenetre, text ='jouer',command = jouer,bg="#1CE6DC",fg="#000B80",activebackground="#BB0362")
        self.ButonLancer.pack(side='left', padx=10,pady=10)

        self.Butonquitter= Button(self.Mafenetre, text='quitter',command=self.Mafenetre.destroy,bg="#BB0362",fg="#520803",activebackground='#1CE6DC')
        self.Butonquitter.pack(side='left',padx=5,pady=5)
        
        
i=interface()
i.Mafenetre.mainloop()
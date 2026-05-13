heads_="""
import pygame
import random
import sys
import time
class apps:
    #put you code here
    def __init__(self):
        #put you code here
        self.score=0
        self.fire=0
        self.live=0
        self.lives=3
        self.x=0
        self.y=0
        self.z=0
        self.w=640
        self.h=480
        self.ends=False
        self.camera=0
        self.enemy=[]
        self.enemycount=3
        self.debug=True
        self.files="log.txt"
        self.datas=""
        self.fmode="w"
        self.frmode="r"
        self.screens=None
        self.caption="applications"
        self.bcolor=(0,0,0) 
       
    def debugs(self,value):
        #put you code here
        print(value)
        time.sleep(0.1)

    def saves():
        f1=open(self.files,self.fmode)
        f1.write(self.datas)
        f1.close()

    def loads():
        f1=open(self.files,self.frmode)
        f1.write(self.datas)
        f1.close()

    def startvars(self):
        #put you code here
        self.debugs("startvars")

    def startapp(self):
        #put you code here
        self.debugs("startapps")

    def refreshscreen(self):
        #put you code here
        time.sleep(3)

    def checkgameover(self):
        #put you code here
        self.debugs("checkgameover")


"""
def saves(files,mode,value):
    f1=open(files,mode)
    f1.write(value)
    f1.close()


def heads(files,value):
    saves(files,"w",value)

print("give me the file name .txt ? ")
filesa=input().strip()


def getfiles(files):
    f1=open(files,"r")
    values=f1.read()
    f1.close()
    v=values.split("\n")
    return v
    

def defs(files,value):
    print("handle : function :"+value)
    saves(files,"a","\n"+" "*4)
    saves(files,"a","def ")
    saves(files,"a",value)
    saves(files,"a"," (self):\n")
    saves(files,"a",(" "*8)+"#put you code here\n")
    saves(files,"a",(" "*8)+ "self.debugs(\"")
    saves(files,"a",value)
    saves(files,"a","\")\n\n")

print(filesa)
gfiles=getfiles(filesa)

filesa=filesa.replace(".txt",".py")
heads(filesa,heads_)
for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs(filesa,sss)


heads__="""
    def mainloop(self):
        #put you code here
        #you can chage list events order
        clock = pygame.time.Clock()
        appsstart=True
        self.debugs("mainloop")
        while appsstart:

"""

def defs_(files,value):
    print("handle : function :"+value)
    saves(files,"a","\n"+" "*12)
    saves(files,"a","self.")
    saves(files,"a",value)
    saves(files,"a","()\n")

saves(filesa,"a",heads__)

for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs_(filesa,sss)

heads___="""
            pygame.display.flip()
            # Limita o FPS
            clock.tick(60)
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                      return False
                      gamestart=False
            if self.ends:
                 break

    def setuploop(self):
        #put you code here
        sloop=True
        while sloop:
            sloop=self.mainloop()
            
    def main(self):
        #put you code here
        pygame.init()
        self.screens=pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption(self.caption)
        self.screens.fill(self.bcolor)
        pygame.display.flip()
        self.startvars()
        self.startapp()
        self.setuploop()
        pygame.quit()
        sys.exit()


apps1=apps()
apps1.main()
"""
saves(filesa,"a",heads___)
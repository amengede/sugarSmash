import math
#Physics routines

GRAVITY = (0,0.5)

class particle:
    def __init__(self):
        self.velocity = [0,0]
        self.ke = 0;
    
    def fall(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.velocity[0] += GRAVITY[0]
        self.velocity[1] += GRAVITY[1]
    
    def bounce(self):
        self.ke = math.pow(self.velocity[0],2) + math.pow(self.velocity[1],2)
        if self.ke < 5:
            self.state = "stable"
            self.velocity = [0,0]
            self.ke = 0
            return
        norm = math.sqrt(self.ke)
        vnorm = [self.velocity[0]/norm,self.velocity[1]/norm]
        self.ke *= 0.3;
        self.velocity[0] = -math.sqrt(self.ke)*vnorm[0]
        self.velocity[1] = -math.sqrt(self.ke)*vnorm[1]
        
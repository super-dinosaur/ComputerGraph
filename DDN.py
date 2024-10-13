import cv2 as cv
import numpy as np

from icecream import ic

e = np.array([100,100])
s = np.array([500,300])

def round(x):
    return int(x+0.5)

class DDN:
    def __init__(self,s,e, W=600,H=400,offset=2):
        self.img = np.zeros((H,W,3),np.uint8)
        self.x1,self.x2 = s[0],e[0]
        self.y1,self.y2 = s[1],e[1]
        self.offset = offset
        self.l,self.b = self.init_l()

    def init_l(self):
        try:
            self.m = round((self.y2-self.y1)/(self.x2-self.x1))
        except ZeroDivisionError:
            self.m = 0
            raise ZeroDivisionError("Division by zero")
        if self.m > 1:
            self.x1,self.y1 = self.y1,self.x1
            self.x2,self.y2 = self.y2,self.x2
            self.offset = -self.offset
        elif self.m < 0:
            self.offset = -self.offset
        return lambda x: self.m*(x-self.x1)+self.y1,\
                round(-self.m*self.x1+self.y1)


    def draw(self):
        x0 = round(self.x1)
        assert type(self.x1), type(self.x2) == (int, int)
        tim = abs(round(self.x2) - x0 + 1)/abs(self.offset)
        tim = round(tim)
        temp = round(self.y1)
        for i in range(tim-1):
            if i: temp = round(temp + self.m)
            self.img[temp:temp + self.offset,
                     x0 + i * self.offset:x0 + (i+1) * self.offset] = (255,255,255)
        cv.circle(self.img,(self.x1,self.y1),5,(0,255,0),5)
        cv.circle(self.img,(self.x2,self.y2),5,(0,0,255),5)
        cv.imshow("DDN",self.img)
        cv.waitKey(0)




if __name__ == '__main__':
    d = DDN(s,e)
    d.draw()
    
import cv2 as cv
import numpy as np

from icecream import ic

s = np.array([100,120])
e = np.array([200,100])

def r(x):
    return int(x+0.5)

class DDN:
    def __init__(self,s,e, W=900,H=900,offset=2):
        self.img = np.zeros((H,W,3),np.uint8)
        self.x1,self.x2 = s[0],e[0]
        self.y1,self.y2 = s[1],e[1]
        self.offset = offset
        self.l,self.b = self.init_l()

    def init_l(self):
        try:
            self.m = (self.y2-self.y1)/(self.x2-self.x1)
        except ZeroDivisionError:
            self.m = 0
            raise ZeroDivisionError("Division by zero")
        if self.m > 1:
            self.x1,self.y1 = self.y1,self.x1
            self.x2,self.y2 = self.y2,self.x2
        elif self.m < 0:
            self.offset = -self.offset
        return lambda x: self.m*(x-self.x1)+self.y1,\
                r(-self.m*self.x1+self.y1)


    def draw(self):
        x1 = r(self.x1)
        y1 = r(self.y1)
        x2 = r(self.x2)
        y2 = r(self.y2)
        tim = (x2 - x1 + 1)/abs(self.offset)
        ic(r(tim))
        # if tim < 0:
        #     x0,self.x2 = self.x2,self.x1
        #     self.y1,self.y2 = self.y2,self.y1
        #     tim *= -1
        tim = r(tim)
        temp = y1
        for i in range(tim):
            if i: temp = r(temp + self.m)
            self.img[temp:temp + self.offset,
                     x1 + i * self.offset:x1 + (i+1) * self.offset] = (255,255,255)
        cv.circle(self.img,s,1,(0,255,0),5)
        cv.circle(self.img,e,1,(0,0,255),5)
        cv.imshow("DDN",self.img)
        cv.waitKey(0)

if __name__ == '__main__':
    d = DDN(s,e)
    d.draw()
    
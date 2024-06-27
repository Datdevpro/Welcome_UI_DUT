
import math
import tkinter as tk
import time


my_w = tk.Tk()
#my_w.tk.call('tk', 'scaling',200)
width,height=410,410 # set the variables 
c_width,c_height=width-5,height-5 # canvas width height
#d=str(width)+"x"+str(height)
my_w.geometry("500x500") 
c1 = tk.Canvas(my_w, width=c_width, height=c_height,bg='lightgreen')
c1.grid(row=0,column=0,padx=5,pady=5,columnspan=3)
dial=c1.create_oval(10, 10, 400, 400,width=10,outline='#FF0000',fill='#FFFFFF')
x,y=205,205 # center 
x1,y1,x2,y2=x,y,x,10 # second needle ( kim giây )
center=c1.create_oval(x-8,y-8,x+8,y+8,fill='#c0c0c0')
r1=180 # dial lines for one minute 
r2=130 # for hour numbers  before the lines 
in_degree = 0
h=iter(['12','1','2','3','4','5','6','7','8','9','10','11'])
for i in range(0,60):
    in_radian = math.radians(in_degree) # converting to radian
    if(i%5==0): 
        ratio=0.85 # Long marks ( lines )
        t1=x+r2*math.sin(in_radian) # coordinate to add text ( hour numbers )
        t2=x-r2*math.cos(in_radian) # coordinate to add text ( hour numbers )
        c1.create_text(t1,t2,fill='blue',font="Times 30  bold",text=next(h)) # number added
    else:
        ratio=0.9 # small marks ( lines )
    
    x1=x+ratio*r1*math.sin(in_radian)
    y1=y-ratio*r1*math.cos(in_radian)
    x2=x+r1*math.sin(in_radian)
    y2=y-r1*math.cos(in_radian)
    c1.create_line(x1,y1,x2,y2,width=1) # draw the line for segment
    in_degree=in_degree+6 # increment for next segment

my_w.mainloop()
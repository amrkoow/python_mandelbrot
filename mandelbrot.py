# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
import matplotlib
from matplotlib import cm                    #no idea, why I have to import cm seperately. ran without this line from spyder3 without any promblems, but with "module has no argument 'cm' " in normal command line window or python shell.

# =============================================================================
# Startvorgaben --> sollen später in GUI
# =============================================================================

imgwidth=200
aspectratio=1
imgheight=int(round(imgwidth/aspectratio))

lefto=-2.25
righto= 0.75
horcenter=(lefto+righto)/2

topo=1.5
bottomo=-1.5
vertcenter=(bottomo+topo)/2

# Mandelbrotmegenparameter
maxiter=60      #Anzahl der maximalen Iterationsschritte
limit=2         #Absolutwertlimit, über dem die Iteration abgebrochen wird

#Colormap
cmpa=matplotlib.cm.get_cmap('gist_ncar')

# =============================================================================
# Berechnung Bildparameter
# =============================================================================

left= horcenter-(((topo-bottomo)/2)*aspectratio)
right= horcenter+(((topo-bottomo)/2)*aspectratio)

top= vertcenter-((topo-bottomo)/2)
bottom= vertcenter+((topo-bottomo)/2)

tk=Tk()
tk.title("Mandelbrot")

canvas=Canvas(tk, width=imgwidth, height=imgheight)

# =============================================================================
# Mandelbrot Iteration
# =============================================================================

for x in range (imgwidth):
    cr=left+x*(right-left)/imgwidth
    print(x)
    for y in range (imgheight):
        ci=bottom+y*(top-bottom)/imgheight
        c=complex(cr, ci)
        z=0
        i=0
        for i in range(maxiter):
            if abs(z)>limit:
                break
            z=(z**2)+c
            
            # Zeichnen
            
        mycolor1=cmpa(i/maxiter)
        mycolor2=mycolor1[:3]
        mycolor=matplotlib.colors.rgb2hex(mycolor2)
        if i == (maxiter -1):
            mycolor='#%02x%02x%02x' % (0,0,0)
        canvas.create_line(x,y, x+1, y+1, fill= mycolor)
        canvas.pack()
            
# =============================================================================
# Bildschirmausgabe
# =============================================================================

canvas.mainloop()
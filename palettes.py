# Python>3.0
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import matplotlib.patches as pat 
import matplotlib.colors as cl  
import math 

#colors_list = list(cl._colors_full_map.values())
colors_list = cl.cnames 
fig = plt.figure(figsize=(4,3),dpi=300)
ax = fig.add_subplot(111)

ratio = 1.0/3.0
cnt = math.ceil(math.sqrt(len(colors_list)))
x_cnt = cnt * ratio
y_cnt = cnt / ratio
x = 0
y = 0
w = 1 / x_cnt
h = 1 / y_cnt

for c in colors_list:
    pos = (x / x_cnt, y / y_cnt)
    ax.add_patch(pat.Rectangle(pos,w,h,color=c))
    ax.annotate(c,xy=pos)
    if y >= y_cnt -1:
        x += 1
        y = 0
    else:
        y += 1
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#解决中文乱码问题
plt.rcParams['font.sans-serif']=['SimHei']#显示中文标签 
plt.rcParams['axes.unicode_minus']=False
sns.set(font='SimHei')

plt.style.use('default') #风格一共有default、bmh、ggplot、dark_background、fivethirtyeight、grayscale,有时需注释掉才能显示中文

fig = plt.figure(figsize=(14,8))
plt.subplots_adjust(hspace=0.3,wspace=0)

ax = fig.add_subplot(221, projection='3d')
x1 = [2000,2000]
y1 = [2,3]
z1= [29,285]
plt.plot(x1,y1,z1,color = 'green')
x2 = [2500,2500]
y2 = [2,3]
z2= [15,256]
plt.plot(x2,y2,z2,color = 'blue')
x2 = [3000,3000]
y2 = [2,3]
z2= [15,256]
plt.plot(x2,y2,z2,color = 'black')
x2 = [3500,3500]
y2 = [2,3]
z2= [15,256]
plt.plot(x2,y2,z2,color = 'purple')
x = [4000,4000]
y = [2,3]
z= [15,183]
plt.plot(x,y,z,color='deeppink')
x = [4500,4500]
y = [2,3]
z= [15,183]
plt.plot(x,y,z,color='brown')
x = [5000,5000]
y = [2,3]
z= [15,0]
plt.plot(x,y,z,color='purple')
ax.set_xlabel('Threshold1')  
ax.set_ylabel('Size_of_pattern')    
ax.set_zlabel('Number_of_GFDs')
plt.yticks([2,3],[2,3])
plt.title("(a)Exploring pattern size effect, new method",fontsize=12)

ax = fig.add_subplot(222, projection='3d')
x1 = [8000,8000]
y1 = [2,3]
z1= [14,164]
plt.plot(x1,y1,z1,color = 'orange')
x1 = [9000,9000]
y1 = [2,3]
z1= [14,162]
plt.plot(x1,y1,z1,color = 'green')
x2 = [10000,10000]
y2 = [2,3]
z2= [14,162]
plt.plot(x2,y2,z2,color = 'purple')
x2 = [11000,11000]
y2 = [2,3]
z2= [14,162]
plt.plot(x2,y2,z2,color = 'black')
x2 = [12000,12000]
y2 = [2,3]
z2= [14,162]
plt.plot(x2,y2,z2,color = 'brown')
x2 = [13000,13000]
y2 = [2,3]
z2= [14,162]
plt.plot(x2,y2,z2,color = 'red')
x2 = [13500,13500]
y2 = [2,3]
z2= [10,124]
plt.plot(x2,y2,z2,color = 'deepskyblue')
x2 = [14000,14000]
y2 = [2,3]
z2= [0,0]
plt.plot(x2,y2,z2,color = 'deeppink')
ax.set_xlabel('Threshold2')  
ax.set_ylabel('Size_of_pattern')    
ax.set_zlabel('Number_of_GFDs')
plt.yticks([2,3],[2,3])
plt.title("(b)Exploring pattern size effect, Fan method",fontsize=12)

ax = fig.add_subplot(223, projection='3d')
x1 = [2,2,2,2,2,2,2]
y1 = [2000,2500,3000,3500,4000,4500,5000]
z1= [29,15,15,15,15,15,15]
plt.plot(y1,x1,z1,color = 'green')
x2 = [3,3,3,3,3,3,3]
y2 = [2000,2500,3000,3500,4000,4500,5000]
z2= [285,256,256,256,183,183,0]
plt.plot(y2,x2,z2,color = 'blue')
ax.set_xlabel('Threshold1')  
ax.set_ylabel('Size_of_pattern')    
ax.set_zlabel('Number_of_GFDs')
plt.yticks([2,3],[2,3])
plt.title("(c)Exploring threshold effect, new method",fontsize=12)

ax = fig.add_subplot(224, projection='3d')
x1 = [2,2,2,2,2,2,2,2]
y1 = [8000,9000,10000,11000,12000,13000,13500,14000]
z1= [14,14,14,14,14,14,10,0]
plt.plot(y1,x1,z1,color = 'green')
x2 = [3,3,3,3,3,3,3,3]
y2 = [8000,9000,10000,11000,12000,13000,13500,14000]
z2= [164,162,162,162,162,162,124,0]
plt.plot(y2,x2,z2,color = 'blue')
ax.set_xlabel('Threshold2')  
ax.set_ylabel('Size_of_pattern')    
ax.set_zlabel('Number_of_GFDs')
plt.yticks([2,3],[2,3])
plt.title("(d)Exploring threshold effect, Fan method",fontsize=12)

plt.show()
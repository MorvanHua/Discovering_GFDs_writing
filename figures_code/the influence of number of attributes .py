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
plt.subplots_adjust(hspace=0.3,wspace=0.3)

ax = fig.add_subplot(231, projection='3d')
x1 = [2,3,4,5,6]
y1 = [1,1,1,1,1]
z1= [0.177,0.41,0.65,0.883,1.636]
plt.plot(x1,y1,z1,color = 'green')
x1 = [2,3,4,5,6]
y1 = [2,2,2,2,2]
z1= [0.027,0.036,0.134,0.161,0.297]
plt.plot(x1,y1,z1,color = 'blue')
x1 = [2,3,4,5]
y1 = [3,3,3,3]
z1= [0.028,0.046,0.219,0.409]
plt.plot(x1,y1,z1,color = 'black')
ax.set_xlabel('Number_of_attributes')  
ax.set_ylabel('PatternID')    
ax.set_zlabel('Time(seconds)')
plt.xticks([2,3,4,5,6],[2,3,4,5,6])    
plt.yticks([1,2,3],[1,2,3])
plt.title("(a) IMDB with 100000 nodes, 2 size of pattern",fontsize=12)

ax = fig.add_subplot(232, projection='3d')
x1 = [3,4,5,6,7,8,9]
y1 = [1,1,1,1,1,1,1]
z1= [0.334,0.445,0.571,2.286,8.555,21.691,90.473]
plt.plot(x1,y1,z1,color = 'green')
x1 = [3,4,5,6,7,8,9]
y1 = [2,2,2,2,2,2,2]
z1= [0.096,0.196,0.503,2.594,6.523,21.307,55.096]
plt.plot(x1,y1,z1,color = 'blue')
x1 = [3,4,5,6,7,8,9]
y1 = [3,3,3,3,3,3,3]
z1= [0.046,0.115,0.172,0.604,1.429,5.915,16.914]
plt.plot(x1,y1,z1,color = 'black')
ax.set_xlabel('Number_of_attributes')  
ax.set_ylabel('PatternID')    
ax.set_zlabel('Time(seconds)') 
plt.xticks([3,4,5,6,7,8,9],[3,4,5,6,7,8,9])   
plt.yticks([1,2,3],[1,2,3])
plt.title("(b) IMDB with 100000 nodes, 3 size of pattern",fontsize=12)

ax = fig.add_subplot(233, projection='3d')
x1 = [4,5,6,7,8,9,10,11,12]
y1 = [1,1,1,1,1,1,1,1,1]
z1= [0.476,0.655,1.829,4.484,11.014,41.926,86.08,225.955,759.263]
plt.plot(x1,y1,z1,color = 'green')
x1 = [4,5,6,7,8,9,10,11,12]
y1 = [2,2,2,2,2,2,2,2,2]
z1= [0.366,0.435,2.172,4.705,14.39,65.361,168.161,505.893,1767.724]
plt.plot(x1,y1,z1,color = 'blue')
x1 = [4,5,6,7,8,9,10,11,12]
y1 = [3,3,3,3,3,3,3,3,3]
z1= [0.182,0.577,1.778,4.656,14.459,65.15,167.978,506.313,1747.868]
plt.plot(x1,y1,z1,color = 'black')
ax.set_xlabel('Number_of_attributes')  
ax.set_ylabel('PatternID')    
ax.set_zlabel('Time(seconds)') 
plt.xticks([4,5,6,7,8,9,10,11,12],[4,5,6,7,8,9,10,11,12]) 
plt.yticks([1,2,3],[1,2,3])
plt.title("(c) IMDB with 100000 nodes, 4 size of pattern",fontsize=12)

ax = fig.add_subplot(234, projection='3d')
x1 = [2,3,4,5,6,7,8]
y1 = [1,1,1,1,1,1,1]
z1= [0.071,0.102,0.114,0.165,0.18,0.215,0.279]
plt.plot(x1,y1,z1,color = 'green')
x1 = [2,3,4,5,6,7,8]
y1 = [2,2,2,2,2,2,2]
z1= [0.033,0.015,0.025,0.028,0.06,0.067,0.16]
plt.plot(x1,y1,z1,color = 'blue')
x1 = [2,3,4,5,6,7,8]
y1 = [3,3,3,3,3,3,3]
z1= [0.011,0.015,0.027,0.032,0.056,0.095,0.263]
plt.plot(x1,y1,z1,color = 'black')
x1 = [2,3,4,5,6,7,8]
y1 = [4,4,4,4,4,4,4]
z1= [0.006,0.006,0.009,0.008,0.011,0.031,0.034]
plt.plot(x1,y1,z1,color = 'pink')
x1 = [2,3,4,5,6,7,8]
y1 = [5,5,5,5,5,5,5]
z1= [0.115,0.254,0.32,0.44,0.777,1.771,4.588]
plt.plot(x1,y1,z1,color = 'red')
ax.set_xlabel('Number_of_attributes')  
ax.set_ylabel('PatternID')    
ax.set_zlabel('Time(seconds)') 
plt.xticks([2,3,4,5,6,7,8],[2,3,4,5,6,7,8]) 
plt.yticks([1,2,3,4,5],[1,2,3,4,5])
plt.title("(d) yago4 with 4.5million nodes, 2 size of pattern",fontsize=12)

ax = fig.add_subplot(235, projection='3d')
x1 = [3,4,5,6,7,8,9,10,11,12]
y1 = [1,1,1,1,1,1,1,1,1,1]
z1= [0.111,0.12,0.132,0.16,0.239,0.337,0.788,1.723,6.573,19.694]
plt.plot(x1,y1,z1,color = 'green')
x1 = [3,4,5,6,7,8,9,10,11,12]
y1 = [2,2,2,2,2,2,2,2,2,2]
z1= [0.005,0.005,0.006,0.032,0.08,0.125,0.438,23.726,24.466,25.574]
plt.plot(x1,y1,z1,color = 'blue')
x1 = [3,4,5,6,7,8,9,10,11,12]
y1 = [3,3,3,3,3,3,3,3,3,3]
z1= [0.004,0.005,0.015,0.01,0.009,0.026,0.091,0.175,0.409,0.42]
plt.plot(x1,y1,z1,color = 'black')
x1 = [3,4,5,6,7,8,9,10,11,12]
y1 = [4,4,4,4,4,4,4,4,4,4]
z1= [0.011,0.005,0.018,0.043,0.069,0.128,0.352,9.545,9.449,10.12]
plt.plot(x1,y1,z1,color = 'pink')
x1 = [3,4,5,6,7,8,9,10,11,12]
y1 = [5,5,5,5,5,5,5,5,5,5]
z1= [0.01,0.01,0.033,0.09,0.236,0.565,4.838,177.762,183.935,188.039]
plt.plot(x1,y1,z1,color = 'red')
ax.set_xlabel('Number_of_attributes')  
ax.set_ylabel('PatternID')    
ax.set_zlabel('Time(seconds)') 
plt.xticks([3,4,5,6,7,8,9,10,11,12],[3,4,5,6,7,8,9,10,11,12]) 
plt.yticks([1,2,3,4,5],[1,2,3,4,5])
plt.title("(e) yago4 with 4.5million nodes, 3 size of pattern",fontsize=12)

ax = fig.add_subplot(236, projection='3d')
x1 = [4,5,6,7,8,9,10,11,12]
y1 = [1,1,1,1,1,1,1,1,1]
z1= [0.128,0.126,0.143,0.19,0.258,0.376,1.022,1.828,6.313]
plt.plot(x1,y1,z1,color = 'green')
ax.set_xlabel('Number_of_attributes')  
ax.set_ylabel('PatternID')    
ax.set_zlabel('Time(seconds)') 
plt.xticks([4,5,6,7,8,9,10,11,12],[4,5,6,7,8,9,10,11,12]) 
plt.yticks([1],[1])
plt.title("(f) yago4 with 4.5million nodes, 4 size of pattern",fontsize=12)

plt.show()
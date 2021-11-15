import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#解决中文乱码问题
plt.rcParams['font.sans-serif']=['SimHei']#显示中文标签 
plt.rcParams['axes.unicode_minus']=False
sns.set(font='SimHei')
#plt.plot? #显示函数的参数说明
#设定主题风格
plt.style.use('default') #风格一共有default、bmh、ggplot、dark_background、fivethirtyeight、grayscale,有时需注释掉才能显示中文

graph_IMDB = [7,43,93]
graph_museum = [1,2,4,14]
graph_yago4 = [18,32,41]

plt.figure(figsize=(14,3.8))
plt.subplots_adjust(hspace=0.4,wspace=0.3)
plt.subplot(1,3,1)
plt.plot([2,3,4],graph_IMDB,"+-k")
plt.title("(a) IMDB 100000 dataset",fontsize=12)
plt.ylabel("Number_of_GFDs",fontsize=12)
plt.xlabel("Pattern size",fontsize=12)
# plt.ylim(0,350) #设置y轴的范围
plt.xticks([2,3,4])
plt.yticks(graph_IMDB)

plt.subplot(1,3,2)
plt.plot([2,3,4,5],graph_museum,"+-k")
plt.title("(b) Museum dataset",fontsize=12)
plt.ylabel("Number_of_GFDs",fontsize=12)
plt.xlabel("Pattern size",fontsize=12)
# plt.ylim(0,45) #设置y轴的范围
plt.xticks([2,3,4,5])
plt.yticks(graph_museum)

plt.subplot(1,3,3)

plt.plot([2,3,4],graph_yago4,"+-k")
plt.title("(c) YAGO4 4.5million dataset",fontsize=12)
plt.ylabel("Number_of_GFDs",fontsize=12)
plt.xlabel("Pattern size",fontsize=12)
# plt.ylim(0,25) #设置y轴的范围
plt.xticks([2,3,4])
plt.yticks(graph_yago4)

plt.show()
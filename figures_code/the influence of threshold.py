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

graph_IMDB = [329,190,112,109,83,0]
graph_museum = [41,11,11,11,11,11,3]
graph_yago4_subGraph21 = [20,15,15,11,11,0]
graph_yago4_subGraph26 = [84,78,63,24,12]

plt.figure(figsize=(14,8))
plt.subplots_adjust(hspace=0.4,wspace=0.15)
plt.subplot(2,2,1)
plt.plot([16000,18000,20000,22000,24000,26000],graph_IMDB,"x-k")
plt.title("(a) IMDB 100000 dataset",fontsize=15)
plt.ylabel("Number_of_GFDs",fontsize=15)
plt.xlabel("Threshold",fontsize=15)
plt.ylim(0,350) #设置y轴的范围

plt.subplot(2,2,2)
plt.plot([1500,2500,3500,4500,5500,6500,7500],graph_museum,"x-k")
plt.title("(b) Museum dataset",fontsize=15)
plt.ylabel("Number_of_GFDs",fontsize=15)
plt.xlabel("Threshold",fontsize=15)
plt.ylim(0,45) #设置y轴的范围
plt.xticks([1500,2500,3500,4500,5500,6500,7500])
plt.yticks([45,41,11,3,0])

plt.subplot(2,2,3)

plt.plot([600,900,1200,1500,1800,2100],graph_yago4_subGraph21,"x-k")
plt.title("(c) SubGraph1 of YAGO4 4.5million dataset",fontsize=15)
plt.ylabel("Number_of_GFDs",fontsize=15)
plt.xlabel("Threshold",fontsize=15)
plt.ylim(0,25) #设置y轴的范围
plt.xticks([600,900,1200,1500,1800,2100],[600,900,1200,1500,1800,2100])

plt.subplot(2,2,4)
plt.plot([155,165,175,185,195],graph_yago4_subGraph26,"x-k",label='new method')
plt.title("(d) SubGraph2 of YAGO4 4.5million dataset",fontsize=15)
plt.ylabel("Number_of_GFDs",fontsize=15)
plt.xlabel("Threshold",fontsize=15)
plt.ylim(0,90) #设置y轴的范围
plt.xticks([155,165,175,185,195],[155,165,175,185,195])
plt.yticks([90,84,78,63,24,12,0])

plt.show()
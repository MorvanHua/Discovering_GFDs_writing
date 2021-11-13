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

graph_IMDB_20000_new = [round(100.791/3600,2),round(100.791/3600,2)];graph_IMDB_20000_Fan = [round(1541.28/3600,2),round(5244.5/3600,2)]
graph_IMDB_50000_new = [round(2304.516/3600,2),round(2304.516/3600,2)];graph_IMDB_50000_Fan = [round(11439.04/3600,2),round(37618/3600,2)]
graph_IMDB_100000_new = [round(5866.692/3600,2),round(5866.692/3600,2)];graph_IMDB_100000_Fan = [round(54490.77/3600,2),round(238937.8/3600,2)]
graph_yago4_3000_new = [round(75.469/3600,2),round(75.469/3600,2)];graph_yago4_3000_Fan = [round(3188.855/3600,2),round(8349.2/3600,2)]
graph_yago4_4500000_new = [round(35838.756/3600,2),round(35838.756/3600,2)];graph_yago4_4500000_Fan = [round(150,2),round(150,2)]
graph_museum_60000_new = [round(2598.06/3600,2),round(2598.06/3600,2)];graph_museum_60000_Fan = [round(5,2),round(5,2)]

print(graph_IMDB_50000_Fan)
nodes_compared = [0,1,2,3,4]

plt.figure(figsize=(14,8))
plt.subplots_adjust(hspace=0.4,wspace=0.3)
plt.subplot(2,3,1)
#plt.style.use('default') #风格一共有default、bmh、ggplot、dark_background、fivethirtyeight、grayscale,有时需注释掉才能显示中文
plt.plot([1,2],graph_IMDB_20000_new,"x-k",label='new method')
plt.plot([1,2],graph_IMDB_20000_Fan,"+--k",label='Fan method')
plt.title("(a) Varing n(IMDB 20000)",fontsize=15)
plt.ylabel("Time(hours)",fontsize=15)
plt.xlabel("Size of pattern(n)",fontsize=15)
plt.xlim(0,3) #设置x轴的范围
plt.ylim(0,2) #设置y轴的范围
plt.xticks([0,0.5,1,2,3],nodes_compared)
plt.yticks([graph_IMDB_20000_new[0],graph_IMDB_20000_Fan[0],graph_IMDB_20000_Fan[1],2])
plt.legend(loc='upper left',prop={'size': 9}) #显示每个对象的小图表

plt.subplot(2,3,2)
#plt.style.use('default') #风格一共有default、bmh、ggplot、dark_background、fivethirtyeight、grayscale,有时需注释掉才能显示中文
plt.plot([1,2],graph_IMDB_50000_new,"x-k",label='new method')
plt.plot([1,2],graph_IMDB_50000_Fan,"+--k",label='Fan method')
plt.title("(b) Varing n(IMDB 50000)",fontsize=15)
plt.ylabel("Time(hours)",fontsize=15)
plt.xlabel("Size of pattern(n)",fontsize=15)
plt.xlim(0,3) #设置x轴的范围
plt.ylim(0,12) #设置y轴的范围
plt.xticks([0,0.5,1,2,3],nodes_compared)
plt.yticks([graph_IMDB_50000_new[0],graph_IMDB_50000_Fan[0],graph_IMDB_50000_Fan[1],12])
plt.legend(loc='upper left',prop={'size': 9}) #显示每个对象的小图表

plt.subplot(2,3,3)
#plt.style.use('default') #风格一共有default、bmh、ggplot、dark_background、fivethirtyeight、grayscale,有时需注释掉才能显示中文
plt.plot([1,2],graph_IMDB_100000_new,"x-k",label='new method')
plt.plot([1,2],graph_IMDB_100000_Fan,"+--k",label='Fan method')
plt.title("(c) Varing n(IMDB 100000)",fontsize=15)
plt.ylabel("Time(hours)",fontsize=15)
plt.xlabel("Size of pattern(n)",fontsize=15)
plt.xlim(0,3) #设置x轴的范围
plt.ylim(0,70) #设置y轴的范围
plt.xticks([0,0.5,1,2,3],nodes_compared)
plt.yticks([graph_IMDB_100000_new[0],graph_IMDB_100000_Fan[0],graph_IMDB_100000_Fan[1],70])
plt.legend(loc='upper left',prop={'size': 9}) #显示每个对象的小图表

plt.subplot(2,3,4)
#plt.style.use('default') #风格一共有default、bmh、ggplot、dark_background、fivethirtyeight、grayscale,有时需注释掉才能显示中文
plt.plot([1,2],graph_yago4_3000_new,"x-k",label='new method')
plt.plot([1,2],graph_yago4_3000_Fan,"+--k",label='Fan method')
plt.title("(d) Varing n(yago4 3000)",fontsize=15)
plt.ylabel("Time(hours)",fontsize=15)
plt.xlabel("Size of pattern(n)",fontsize=15)
plt.xlim(0,3) #设置x轴的范围
plt.ylim(0,2.5) #设置y轴的范围
plt.xticks([0,0.5,1,2,3],nodes_compared)
plt.yticks([graph_yago4_3000_new[0],graph_yago4_3000_Fan[0],graph_yago4_3000_Fan[1],2.5])
plt.legend(loc='upper left',prop={'size': 9}) #显示每个对象的小图表

plt.subplot(2,3,5)
#plt.style.use('default') #风格一共有default、bmh、ggplot、dark_background、fivethirtyeight、grayscale,有时需注释掉才能显示中文
plt.plot([1,2],graph_yago4_4500000_new,"x-k",label='new method')
plt.plot([1,2],graph_yago4_4500000_Fan,"+--k",label='Fan method')
plt.title("(e) Varing n(yago4 4.5million)",fontsize=15)
plt.ylabel("Time(hours)",fontsize=15)
plt.xlabel("Size of pattern(n)",fontsize=15)
plt.xlim(0,3) #设置x轴的范围
plt.ylim(0,155) #设置y轴的范围
plt.xticks([0,0.5,1,2,3],nodes_compared)
plt.yticks([graph_yago4_4500000_new[0],graph_yago4_4500000_Fan[0]],[graph_yago4_4500000_new[0],'Inf'])
plt.legend(loc='center right',prop={'size': 9}) #显示每个对象的小图表

plt.subplot(2,3,6)
#plt.style.use('default') #风格一共有default、bmh、ggplot、dark_background、fivethirtyeight、grayscale,有时需注释掉才能显示中文
plt.plot([1,2],graph_museum_60000_new,"x-k",label='new method')
plt.plot([1,2],graph_museum_60000_Fan,"+--k",label='Fan method')
plt.title("(f) Varing n(museum 60000)",fontsize=15)
plt.ylabel("Time(hours)",fontsize=15)
plt.xlabel("Size of pattern(n)",fontsize=15)
plt.xlim(0,3) #设置x轴的范围
plt.ylim(0,5.2) #设置y轴的范围
plt.xticks([0,0.5,1,2,3],nodes_compared)
plt.yticks([graph_museum_60000_new[0],graph_museum_60000_Fan[0]],[graph_museum_60000_new[0],'Inf'])
plt.legend(loc='center right',prop={'size': 9}) #显示每个对象的小图表

plt.show()
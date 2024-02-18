from matplotlib import pyplot as plt

x=[5, 2, 9, 4, 7, 6, 1, 8] # x values
y=[10, 5, 8, 4, 2, 3, 7, 9] # y values

#plt.plot(x, y, marker='x') # line plot
#plt.bar(x, y) # bar plot
#plt.barh(x, y) # horizontal bar plot
#plt.hist(x) # histogram
#plt.scatter(x, y) # scatter plot
#plt.plot(x, y, linestyle='--', color='r', marker='o', label='Line 1') # formatting for line plots

labels=['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']
sizes=[20, 15, 10, 25, 20, 5, 5, 10]

#plt.title('Pie Chart')
#plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, explode=[0.2, 0.1, 0.5, 0.2, 0.3, 0.4, 0.6, 0.1], shadow=True) # pie chart

datamat=[[5, 2, 9, 4, 7, 6, 1, 8], [10, 5, 8, 4, 2, 3, 7, 9], [20, 15, 10, 25, 20, 5, 5, 10]]
plt.matshow(datamat) # matrix plot

plt.show()
import matplotlib.pyplot as plt
d_s=[5,15,25,35,45,55]
plt.hist(d_s,bins=[0,10,20,30,40,50,60],weights=[20,10,4,3,45,8],edgecolor="red")
plt.show()
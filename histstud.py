
#hist fo student data different formats,labels etc

import matplotlib.pyplot as plt
import numpy as np
d_s=[1,11,21,31,41,51]
plt.hist(d_s,bins=[0,10,20,30,40,50,60],weights=[10,1,0,33,6,8],facecolor='y',edgecolor='red')
plt.title("hist for student data")
plt.xlabel('value')
plt.ylabel('frequency')
plt.savefig('student.png')
plt.show()

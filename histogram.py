#histo using randomly selected dataset
#import matplotlib.pyplot as plt
#import numpy as np
#y=np.random.randn(1000)
#plt.hist(y)
#plt.show()


#hist using well-defined edges
#import matplotlib.pyplot as plt
#import numpy as np
#y=np.random.randn(1000)
#plt.hist(y,25,edgecolor="red")
#plt.show()

#hist to display no of students
#import matplotlib.pyplot as plt
#d_s=[5,15,25,35,45,55]
#plt.hist(d_s,bins=[0,10,20,30,40,50,60],weights=[20,10,45,33,6,8],edgecolor="red")
#plt.show()

#hist fo student data different formats,labels etc

#import matplotlib.pyplot as plt
#import numpy as np
#d_s=[1,11,21,31,41,51]
#plt.hist(d_s,bins=[0,10,20,30,40,50,60],weights=[10,1,0,33,6,8],facecolor='y',edgecolor='red')
#plt.title("hist for student data")
#plt.xlabel('value')
#plt.ylabel('frequency')
#plt.savefig('student.png')
#plt.show()


#import matplotlib.pyplot as plt
#d_s=[5,15,25,35,45,55]
#plt.hist(d_s,bins=[0,10,20,30,40,50,60],weights=[20,10,4,3,45,8],edgecolor="red")
#plt.show()

#import matplotlib.pyplot as plt
#d_s=[5,15,25,35,15,55]
#plt.hist(d_s,bins=[0,10,20,30,40,50,60],weights=[20,10,45,33,6,8],edgecolor='red')
#plt.show()

#import seaborn as s
#import matplotlib.pyplot as plt
#print(s.get_dataset_names())
#ir=s.load_dataset('iris')
#print(ir)
#s.histplot(ir['petal_length'],kde=False,color='red')


#import pandas as pd
#import seaborn as sb
#from matplotlib import pyplot as plt
#df = sb.load_dataset('iris')
#sb.distplot(df['sepal_length'],kde = False)
#plt.show()


import seaborn as s
import numpy as np
import pandas as pd
np.random.seed(1)
num_var = np.random.randn(1000)
num_var = pd.Series(num_var, name = "Numerical Variable")
s.histplot(data = num_var, kde = False)

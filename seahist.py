#seaborn hist

import seaborn as s
import matplotlib.pyplot as plt
print(s.get_dataset_names())
ir=s.load_dataset('iris')
print(ir)
s.histplot(ir['petal_length'],kde=False,color='red')

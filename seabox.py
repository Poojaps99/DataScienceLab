#seaborn boxplot
import seaborn as s
import matplotlib.pyplot as plt
print(s.get_dataset_names())
ir=s.load_dataset('iris')
print(ir)
s.boxplot(x='petal_length',y='petal_width',data=ir)
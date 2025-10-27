import pandas as pd
import matplotlib.pyplot as plt
# Sample Data
data={'Month':['Jan','Feb','Mar','Apr'],'Sales':[200, 220, 250, 280]}
df=pd.DataFrame(data)
# Line Plot
df.plot(x='Month',y='Sales',kind='line', marker='o', title='Monthly Sales')
plt.show()

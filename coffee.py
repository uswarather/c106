import pandas as pd
import numpy as np
df=pd.read_csv("C:\Users\mhrat\OneDrive\Desktop\python\c106\cups of coffee vs hours of sleep.csv")
temp=df['Temperature'].tolist()
icecream=df['Ice-cream Sales( ₹ )'].tolist()
d={"x":temp,"y":icecream}
correlation=np.corrcoef(d["x"],d["y"])
print(correlation)
#directcorrelation
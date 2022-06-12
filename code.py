
import pandas as pd
import numpy as np
df=pd.read_csv("C:/Users/mhrat/OneDrive/Desktop/python/c106/cups of coffee vs hours of sleep.csv")
coffee=df['Coffee in ml'].tolist()
sleepcycle=df['sleep in hours'].tolist()
d={"x":coffee,"y":sleepcycle}
correlation=np.corrcoef(d["x"],d["y"])
print(correlation)

#indirectcorrelation
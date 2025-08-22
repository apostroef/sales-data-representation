#Library settings
import re

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)

#Pengolahan Data
#1 Editing
print("[Editing]")
df = pd.read_csv("Electronic-Sales.csv")
print("/n") 
print(df.head())
# print(df.describe())
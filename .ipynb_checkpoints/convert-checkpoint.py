# import os
# os.getcwd()
import pandas as pd
from pandas import read_csv
import numpy as np

import pickle
import warnings
warnings.filterwarnings('ignore')

# Reading Dataset
df = read_csv('../Data/dataset/2012-18_officialBoxScore.csv')
print(df.shape)

df = df.iloc[::3, :].reset_index(drop = True)
print(df.shape)

df.to_csv('2012-18_officialBoxScore_converted.csv', index=False)
print('Done')
import os
import pandas as pd
from sklearn.datasets import load_diabetes

os.chdir(os.path.dirname(__file__))

diabetes_df = pd.read_csv("../data/diabetes.csv")

print(diabetes_df.shape)

diabetes_data = load_diabetes(as_frame=True)
df = diabetes_data.frame
print(df.shape)

print(df.info())

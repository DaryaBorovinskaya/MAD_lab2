from ucimlrepo import fetch_ucirepo 
import pandas as pd

file_path = './online_shoppers_intention.csv'


df = pd.read_csv(file_path)

print(f"Размер: {df.shape}")

print(df.describe())






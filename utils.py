import pandas as pd

def category_summary(df):
    return df.groupby('category')['amount'].sum()

def total_spent(df):
    return df['amount'].sum()
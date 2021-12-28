import pandas as pd


def get_shape(df):
    return df.shape


def get_num_unique(df):
    return df['Name'].nunique(),\
           df['Price'].nunique(),\
           df['Quantity'].nunique()


def get_statistics(df):
    return df['Price'].mean(), df['Price'].median()


def make_column(df):
    df2 = df
    df2['Cal_per_mass'] = df2.Calories/df2.Weight
    df2['Cal_per_mass'] = df2['Cal_per_mass'].round(decimals=2)
    return df2


def make_row(df, A):
    to_append = A
    df_length = len(df)
    df.loc[df_length] = to_append
    return df


def modify_col(df):
    df["Name"] = df["Name"].apply(lambda x: x.title())
    return df


def select(df):
    df2 = df[(df['Weight'] >= 250) & (df['Calories'] < 400)]
    return df2


import sys
exec(sys.stdin.read())

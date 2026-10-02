import pandas as pd
df={'one':pd.Series ([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df=pd.DataFrame(df)
print("adding a new column by passing a series to the DataFrame")
df['three'] = pd.Series([5,6,7,8], index=['a','b','c','d'])
print(df)
print("adding a new column using the existing columns in DataFrame")
df['four'] = df['one'] + df['two']
print(df)

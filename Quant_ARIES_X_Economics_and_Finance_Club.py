#week 1 submission 

#for one stock (aapl)

'''#convert text to csv file
import pandas as pd


df = pd.read_csv("aapl_stock.txt")


df.to_csv("aapl.us.csv", index=False)


df = pd.read_csv('aapl.us.csv')
print(df.tail(),df.head())


#filling the unknown daTA
import numpy as np
features  = ['Open','High','Low','Close','Volume']

#for x in features:
    #rolling_mean = df[x].rolling(window=100, center=True, min_periods=1).mean()

    #df['Open'] = df[x].fillna(rolling_mean)
    
def fill_nan_with_adjacent_mean(df, column):
    for i in df.index:
        if pd.isna(df.loc[i, column]):
            prev_idx = i - 1
            next_idx = i + 1
            
            # Handle boundary conditions
            prev_val = df.loc[prev_idx, column] if prev_idx in df.index else np.nan
            next_val = df.loc[next_idx, column] if next_idx in df.index else np.nan
            
            # Compute mean of non-null adjacent values
            values = [v for v in [prev_val, next_val] if not pd.isna(v)]
            if values:
                df.loc[i, column] = np.mean(values)
    
    return df

for x in features:
    fill_nan_with_adjacent_mean(df,x )


# Assume df is your DataFrame

# Option 1: Print names of columns with at least one NaN
print(df)





df['Date'] = pd.to_datetime(df['Date'])
filtered_df = df[(df['Date'].dt.year >= 2008) & (df['Date'].dt.year <= 2017)]

#filtered_df contains the data of 2008-2017 only

df["Daily_Return"] = ((df['Close'] -df['Open'])/df['Open'])*100

print(df.head())



df['MA_7'] = df['Close'].rolling(window=7).mean()

# 30-day moving average of 'Close' column
df['MA_30'] = df['Close'].rolling(window=30).mean()

df['STD_30'] = df['Close'].rolling(window=30).std()
print(df)







import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))

# Plot actual Close price
#plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')

# Plot 7-day moving average
plt.plot(df['Date'], df['Volume'], label='7-Day MA', color='green')

# Plot 30-day moving avera
'''plt.plot(df['Date'], df['MA_30'], label='30-Day MA', color='orange')

# Plot 30-day standard deviation
plt.plot(df['Date'], df['STD_30'], label='30-Day Std Dev', color='red', linestyle='--')'''


plt.show()
fill_nan_with_adjacent_mean(df,'STD_30' )
print(max(df['Volume']))
print(max(df['STD_30']))   


'''




#code comparing all 4 stocks 


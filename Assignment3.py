#Requirement 1
import pandas as pd
df = pd.read_csv('hw3_avocado.csv')

#Requirement 2
df.info()

#Requirement 3
print(df.nunique())

#Requirement 4
df.head()

#Requirement 5
print(df.head())
print(df.tail())
print(df.iloc[:, :4])
print(df.iloc[:, -4:])

#Requirement 6
selected_columns = df[['region', 'Total Volume', "AveragePrice"]]
print(selected_columns.head())

#Requirement 7
print(df.AveragePrice.head())

#Requirement 8
df['EstimatedRevenue'] = df['Total Volume'] * df['AveragePrice']
print(df[['Total Volume', 'AveragePrice', 'EstimatedRevenue']].head())

#Requirement 9
grouped_df = df.groupby(['region', 'type'])['AveragePrice'].mean().reset_index()
print(grouped_df.head())

#Requirement 10
import matplotlib.pyplot as plt
stats = df.groupby('year')['Total Volume'].agg(['mean', 'median', 'std'])
stats.plot(kind='bar', figsize=(10, 6))
plt.title('Mean, Median, and Standard Deviation of Total Volume by Year')
plt.ylabel('Total Volume')
plt.show()

#Requirement 11
bags_columns = ['Small Bags', 'Large Bags', 'XLarge Bags']
bags_total = df.groupby('type')[bags_columns].sum()
print(bags_total)

#Requirement 12
bags_total.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Total Bags by Type (Small, Large, XLarge)')
plt.ylabel('Total Bags')
plt.show()

#Requirement 13
plt.scatter(df['Total Volume'], df['AveragePrice'], alpha=0.5)
plt.title('Total Volume vs Average Price')
plt.xlabel('Total Volume')
plt.ylabel('Average Price')
plt.show()
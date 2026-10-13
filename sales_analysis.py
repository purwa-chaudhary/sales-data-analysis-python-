import pandas as pd
import matplotlib.pyplot as plt

# Load the sales dataset
df = pd.read_csv('sales_data.csv')

# Display the first five rows
print('Sales Data:')
print(df.head())

# Calculate total sales
print('\nTotal Sales:', df['Sales'].sum())

# Find the best-selling product
product_sales = df.groupby('Product')['Sales'].sum()
print('\nSales by Product:')
print(product_sales)

# Create a bar chart
product_sales.plot(kind='bar', title='Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.show()

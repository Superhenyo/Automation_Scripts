import pandas as pd

inputFile = './Generate a Monthly Sales Report.xlsx'
data = pd.read_excel(inputFile)

data['Total'] = data['Quantity'] * data['Price']

summary = data.groupby('Product').agg({'Total': 'sum'}).reset_index()
summary.rename(columns={'Total': 'Total Sales'}, inplace=True)

outputFile = 'monthlyReport.xlsx'
summary.to_excel(outputFile, index=False)

print(f"Monthly sales report Save to {outputFile}")
#---------------------- DATASET CLEANING USING PYTHON PANDAS ------------------------------------ 

# import pandas as pd

# df = pd.read_csv("C:/Users/VIJAY/Desktop/VJ/PROJECTS/sales_project/Sample - Superstore.csv")

# df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
# print("first five rows values in this dataset:")
# print(df.head())
# print("inforation about datatypes:")
# print(df.info())
# print("null values  count in the given data set:")
# print(df.isnull().sum())
# print("duplicate values count in given dataset:")
# print(df.duplicated().sum())
# df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

# df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

# df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

# df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")

# print("decribe the values /summerizations of the given dataset:")
# print(df.describe())
# print("unique values in the REGION cilumn:")
# print(df["Region"].unique())
# print("Count of each value in coumns ")
# print(df["Region"].value_counts())
# print("Sales by Region :")
# sales_by_region = df.groupby("Region")["Sales"].sum()
# print("profit by REgion :")
# profit_by_state = df.groupby("State")["Profit"].max()

# print(sales_by_region)

# print(profit_by_state)
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Sales over time
# sns.lineplot(data=df, x='Order Date', y='Sales')
# plt.show()

# # Profit by category
# sns.barplot(data=df, x='Category', y='Profit', estimator=sum)
# plt.show()

# # Distribution of discounts
# sns.histplot(df['Discount'], bins=10, kde=True)
# plt.show()

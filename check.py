# i=2
# n=int(input())
# while i<=n:
#     print(i)
#     i+=2


# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
# print(sum)
# sum=0
# res=[]
# for i in range(1,101):
#     count=0
#     for j in range(1,i):
#         if i%j==0:
#             count+=1
#     if count==2:
#         res.append(i)
#         sum+=j
# print(res)
# print(sum)


# a=[122,9089,565,8768,939,1221,430]
# for i in a:
#     s=str(i)
#     if s[0]==s[-1]:
#         print(i)



# n=[-9,-5,-6,2,3,0,1,0,3,-8,"hi"]
# l=["zero" if i==0 else "pos" if i>0 else "neg" for i in n]
# print(l)


# # set  comprehencsion
# l={i for i in n if type(i)== int}
# print(l)
# res={i for i in n if isinstance(i,int) and i>0}

# ==============================
# 1. IMPORT LIBRARIES
# # ==============================
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # ==============================
# # 2. LOAD DATASET
# # ==============================
# df = pd.read_csv("C:/Users/VIJAY/Desktop/VJ/PROJECTS/sales_project/Sample - Superstore.csv")

# # ==============================
# # 3. DATA CLEANING
# # ==============================

# # Convert date columns
# df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
# df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# # Convert numeric columns
# df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
# df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
# df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
# df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")

# # Check nulls & duplicates
# print("Null Values:\n", df.isnull().sum())
# print("Duplicate Rows:", df.duplicated().sum())

# # ==============================
# # 4. BASIC INFO
# # ==============================
# print(df.head())
# print(df.info())
# print(df.describe())

# # ==============================
# # 5. FEATURE ENGINEERING
# # ==============================
# df["Year"] = df["Order Date"].dt.year
# df["Month"] = df["Order Date"].dt.month

# # ==============================
# # 6. EDA (ANALYSIS)
# # ==============================

# # Sales by Region
# sales_region = df.groupby("Region")["Sales"].sum()
# print("\nSales by Region:\n", sales_region)

# # Profit by Category
# profit_category = df.groupby("Category")["Profit"].sum()
# print("\nProfit by Category:\n", profit_category)

# # Profit by State
# profit_state = df.groupby("State")["Profit"].max()
# print("\nProfit by State:\n", profit_state)

# # Discount impact
# discount_profit = df.groupby("Discount")["Profit"].mean()
# print("\nDiscount vs Profit:\n", discount_profit)

# # Sales Trend
# sales_year = df.groupby("Year")["Sales"].sum()
# sales_month = df.groupby("Month")["Sales"].sum()

# # ==============================
# # 7. VISUALIZATION
# # ==============================

# # Barplot: Sales by Region
# plt.figure()
# sns.barplot(x=sales_region.index, y=sales_region.values)
# plt.title("Sales by Region")
# plt.show()

# # Barplot: Profit by Category
# plt.figure()
# sns.barplot(x=profit_category.index, y=profit_category.values)
# plt.title("Profit by Category")
# plt.xticks(rotation=45)
# plt.show()

# # Line Plot: Sales by Year
# plt.figure()
# sales_year.plot()
# plt.title("Sales Trend by Year")
# plt.show()

# # Line Plot: Sales by Month
# plt.figure()
# sales_month.plot()
# plt.title("Sales Trend by Month")
# plt.show()

# # Heatmap: Correlation
# plt.figure()
# sns.heatmap(df.corr(numeric_only=True), annot=True)
# plt.title("Correlation Heatmap")
# plt.show()

# # Boxplot: Detect Outliers
# plt.figure()
# sns.boxplot(x=df["Sales"])
# plt.title("Sales Outliers")
# plt.show()

# # ==============================
# # 8. FINAL INSIGHTS (PRINT)
# # ==============================
# print("\n--- FINAL INSIGHTS ---")

# print("Top Region (Sales):", sales_region.idxmax())
# print("Top Category (Profit):", profit_category.idxmax())
# print("Most Profitable State:", profit_state.idxmax())

# print("Observation: Higher discounts tend to reduce profit (check discount vs profit data).")

# # ==============================
# # END OF PROJECT
# # ==============================
# import matplotlib.pyplot as plt

# Data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Create plot
# plt.plot(y)

# # Add title and labels
# plt.title("Basic Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# # Show the plot
# plt.show()
# plt.plot([1,3,6,4.3,4])
# plt.show()

# l1=[1,2,3,4,5]
# l2=[5,3,1,4,3]
# plt.plot(l1,l2)
# plt.show()
  

# a=[1,2,3,4,5]
# b=[10,10,20,30,70]
# plt.bar(a,b)
# plt.show()


# import matplotlib.pyplot as plt

# # Sample data
# data = [1,2,2,3,4,5,5,5,5,4]

# # Create histogram
# plt.hist(data)

# # Add title and labels
# plt.title("Simple Histogram")
# plt.xlabel("Values")
# plt.ylabel("Frequency")

# # Show plot
# plt.show()


# =======================================
#           IMPORT LIBRARIES
# =======================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================================
#           LOADING DATASET
# =====================================
df = pd.read_csv("C:/Users/VIJAY/Desktop/VJ/PROJECTS/sales_project/Sample - Superstore.csv")

# ==========================================
#            DATA CLEANING 
# ==========================================
df["Ship Date"]=pd.to_datetime(df["Ship Date"],errors="coerce")
df["Order Date"]=pd.to_datetime(df["Order Date"],errors="coerce")
df["Sales"]=pd.to_numeric(df["Sales"])
df["Quantity"]=pd.to_numeric(df["Quantity"])
df["Discount"]=pd.to_numeric(df["Discount"])
df["Profit"]=pd.to_numeric(df["Profit"])

# =============================================
#  FEATURE ENGINEERING
# =============================================
df["Month"]=df["Order Date"].dt.month
df["Year"]=df["Order Date"].dt.year
df["Month"]=pd.to_numeric(df["Month"],errors="coerce")
df["Year"]=pd.to_numeric(df["Year"],errors="coerce")

# ===========================================
#       EDA (SAME AS YOUR CODE)
# ===========================================
sales_by_region=df.groupby("Region")["Sales"].sum()
profit_by_category=df.groupby("Category")["Profit"].sum()
profit_by_sate=df.groupby("Region")["Profit"].sum()
discount=df.groupby("Discount")["Profit"].mean()
sales_montly=df.groupby("Month")["Sales"].sum()
sales_yearly=df.groupby("Year")["Sales"].sum()

# ==========================================
#           DASHBOARD (ONLY ARRANGEMENT)
# ==========================================
fig, axes = plt.subplots(3, 2, figsize=(16, 12))
fig.suptitle("SALES DASHBOARD", fontsize=20)

# ==========================================
# 1. SALES BY REGION
# ==========================================
sns.barplot(x=sales_by_region.index, y=sales_by_region.values, ax=axes[0,0])
axes[0,0].set_title("SALES BY REGION")

# ==========================================
# 2. PROFIT BY CATEGORY
# ==========================================
axes[0,1].bar(profit_by_category.index, profit_by_category.values, color="green")
axes[0,1].set_title("PROFIT BY CATEGORY")

# ==========================================
# 3. PROFIT BY REGION
# ==========================================
axes[1,0].plot(profit_by_sate.index, profit_by_sate.values, linestyle="--", marker=".", color="red")
axes[1,0].set_title("PROFIT BY REGION")

# ==========================================
# 4. DISCOUNT IMPACT
# ==========================================
sns.lineplot(x=discount.index, y=discount.values, ax=axes[1,1])
axes[1,1].set_title("DISCOUNT IMPACT")

# ==========================================
# 5. MONTHLY SALES
# ==========================================
sns.lineplot(x=sales_montly.index, y=sales_montly.values, ax=axes[2,0])
axes[2,0].set_title("MONTHLY SALES")

# ==========================================
# 6. YEARLY SALES
# ==========================================
sns.barplot(x=sales_yearly.index, y=sales_yearly.values, ax=axes[2,1],color="red")
axes[2,1].set_title("YEARLY SALES")

# ==========================================
# FINAL TOUCH
# ==========================================
plt.tight_layout()
plt.show()
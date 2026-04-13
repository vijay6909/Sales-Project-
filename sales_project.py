# =======================================
# #           IMPOERT LIBRARIES
#======================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# # ======================================
# #           LEADING DATASET
# =====================================
df=pd.read_csv("C:/Users/VIJAY/Desktop/VJ/PROJECTS/sales_project/Sample - Superstore.csv")
# ==========================================
#            DATA CLEANING 
# ==========================================
print(df.isnull().sum())
print(df.duplicated().sum())
df["Ship Date"]=pd.to_datetime(df["Ship Date"],errors="coerce")
df["Order Date"]=pd.to_datetime(df["Order Date"],errors="coerce")
df["Sales"]=pd.to_numeric(df["Sales"])
df["Quantity"]=pd.to_numeric(df["Quantity"])
df["Discount"]=pd.to_numeric(df["Discount"])
df["Profit"]=pd.to_numeric(df["Profit"])
#  =============================================
#  FEATURE ENGINEERING : Creating new columns by using existing data
# ================================================
df["Month"]=df["Order Date"].dt.month
df["Year"]=df["Order Date"].dt.year
df["Month"]=pd.to_numeric(df["Month"],errors="coerce")
df["Year"]=pd.to_numeric(df["Year"],errors="coerce")
# ==============================================
#         BASIC INFO AFTER CLEANING
# ==========================================
print(df)
print(df.info())
print("SHAPE OF THE DATSET:",df.shape)
# ===========================================
##      EDA-Explatory Data Analsys (ANALSYS)
# ==========================================
#  SALES BY REGION
sales_by_region=df.groupby("Region")["Sales"].sum()
print("\nSales by Region:\n",sales_by_region)
#  PROFIT BY CATEGORY
profit_by_category=df.groupby("Category")["Profit"].sum()
print("\nprofit_by_category:\n",profit_by_category)
#  PROFIT BY REGION
profit_by_sate=df.groupby("Region")["Profit"].sum()
print("\nProfit by State:\n",profit_by_sate)
#  DISCOUNT IMPACT 
discount=df.groupby("Discount")["Profit"].mean()
print("Discount Impact",discount)
# SALES TREND YEARLY AND MONTLYU
sales_montly=df.groupby("Month")["Sales"].sum()
sales_yearly=df.groupby("Year")["Sales"].sum()
print("\nMonthly Sales:\n",sales_montly)
print("\n Yearsly Sales:\n",sales_yearly)

# ==========================================
            #   VISUALIZATIONS 
# ============================================
plt.figure(figsize=(10, 8))
# ==========================================
# 1. SALES BY REGION
# ==========================================
plt.subplot(3,2,1)
plt.bar(sales_by_region.index, sales_by_region.values)
sns.barplot(x=sales_by_region.index, y=sales_by_region.values)
plt.title("SALES BY REGION")
# ==========================================
# 2. PROFIT BY CATEGORY
# ==========================================
plt.subplot(3,2,2)
plt.bar(profit_by_category.index, profit_by_category.values, color="green")
plt.title("PROFIT BY CATEGORY")
# ==========================================
# 3. PROFIT BY REGION
# ==========================================
plt.subplot(3,2,3)
plt.plot(profit_by_sate.index, profit_by_sate.values, linestyle="--", marker=".", color="red")
plt.title("PROFIT BY REGION")
# ==========================================
# 4. DISCOUNT IMPACT
# ==========================================
plt.subplot(3,2,4)
sns.lineplot(x=discount.index, y=discount.values)
plt.title("DISCOUNT IMPACT")
# ==========================================
# 5. MONTHLY SALES
# ==========================================
plt.subplot(3,2,5)
sns.lineplot(x=sales_montly.index, y=sales_montly.values)
plt.title("MONTHLY SALES")
# ==========================================
# 6. YEARLY SALES
# ==========================================
plt.subplot(3,2,6)
sns.barplot(x=sales_yearly.index,y=sales_yearly.values,color="red",height=10)
plt.title("YEARLY SALES")
# ==========================================
# FINAL
# ==========================================
plt.tight_layout()
plt.show()



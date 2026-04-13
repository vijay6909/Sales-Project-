# =======================================
#           IMPORT LIBRARIES
# =======================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn style
sns.set_style("whitegrid")

# ======================================
#           LOADING DATASET
# ======================================
df = pd.read_csv("C:/Users/VIJAY/Desktop/VJ/PROJECTS/sales_project/Sample - Superstore.csv")

# ==========================================
#            DATA CLEANING 
# ==========================================
print(df.isnull().sum())
print(df.duplicated().sum())

df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

df = df.dropna()

# =============================================
#  FEATURE ENGINEERING
# =============================================
df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year

# ==============================================
#         BASIC INFO
# ==============================================
print(df.head())
print(df.info())
print("SHAPE:", df.shape)

# ===========================================
#       EDA - ANALYSIS
# ===========================================

sales_by_region = df.groupby("Region")["Sales"].sum()
profit_by_category = df.groupby("Category")["Profit"].sum()
profit_by_region = df.groupby("Region")["Profit"].sum()
discount = df.groupby("Discount")["Profit"].mean()

sales_monthly = df.groupby("Month")["Sales"].sum()
sales_yearly = df.groupby("Year")["Sales"].sum()

# ==========================================
#               VISUALIZATIONS 
# ==========================================

# SALES BY REGION (Seaborn)
plt.figure()
sns.barplot(x=sales_by_region.index, y=sales_by_region.values)
plt.title("Sales by Region")
plt.show()

# PROFIT BY CATEGORY (Seaborn)
plt.figure()
sns.barplot(x=profit_by_category.index, y=profit_by_category.values)
plt.title("Profit by Category")
plt.show()

# PROFIT BY REGION (Matplotlib)
plt.figure()
plt.plot(profit_by_region.index, profit_by_region.values, marker="o")
plt.title("Profit by Region")
plt.show()

# DISCOUNT IMPACT (Seaborn)
plt.figure()
sns.lineplot(x=discount.index, y=discount.values)
plt.title("Discount vs Profit")
plt.show()

# MONTHLY SALES (Seaborn)
plt.figure()
sns.lineplot(x=sales_monthly.index, y=sales_monthly.values)
plt.title("Monthly Sales Trend")
plt.show()

# YEARLY SALES (Matplotlib)
plt.figure()
plt.plot(sales_yearly.index, sales_yearly.values, marker="o")
plt.title("Yearly Sales Trend")
plt.show()

# SALES DISTRIBUTION (Seaborn)
plt.figure()
sns.histplot(df["Sales"], kde=True)
plt.title("Sales Distribution")
plt.show()

# SALES VS PROFIT (Seaborn)
plt.figure()
sns.scatterplot(x="Sales", y="Profit", data=df)
plt.title("Sales vs Profit")
plt.show()

# BOXPLOT (IMPORTANT 🔥)
plt.figure()
sns.boxplot(x="Category", y="Profit", data=df)
plt.title("Profit Distribution by Category")
plt.show()

# HEATMAP (Correlation 🔥)
plt.figure()
sns.heatmap(df[["Sales","Profit","Discount","Quantity"]].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# TOP PRODUCTS (Matplotlib)
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure()
plt.barh(top_products.index, top_products.values)
plt.title("Top 10 Products")
plt.show()

# ==========================================
#               INSIGHTS
# ==========================================

print("\n=========== INSIGHTS ===========")
print("Highest Sales Region:", sales_by_region.idxmax())
print("Highest Profit Category:", profit_by_category.idxmax())
print("Most Profitable Region:", profit_by_region.idxmax())
print("Best Month:", sales_monthly.idxmax())
print("Best Year:", sales_yearly.idxmax())

# ==========================================
#               END
# ==========================================

print("PROJECT COMPLETED")
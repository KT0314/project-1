import numpy as np
import csv

products = []
stock_quantity = []
sales_volume = []
unit_price = []

# 讀取 hw.csv
with open("hw.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        # 商品名稱
        products.append(row["Product_Name"])

        # 庫存數量
        stock_quantity.append(float(row["Stock_Quantity"]))

        # 銷售量
        sales_volume.append(float(row["Sales_Volume"]))

        # 單價（去掉 $）
        price = row["Unit_Price"].replace("$", "").strip()
        unit_price.append(float(price))

# 轉成 numpy array
products = np.array(products)
stock_quantity = np.array(stock_quantity)
sales_volume = np.array(sales_volume)
unit_price = np.array(unit_price)

# (1) 每個商品總庫存價值
total_inventory_value = stock_quantity * unit_price

# (2) 找出最暢銷商品（可能不只一個）
max_sales = np.max(sales_volume)

# 找出所有最大銷售量的位置
best_indices = np.where(sales_volume == max_sales)[0]

# 找出所有最暢銷商品名稱
best_products = products[best_indices]

print("最暢銷商品：", best_products)

# (3) 9折後收入
revenue_90_discount = sales_volume * unit_price * 0.9

# 輸出 hw_ok.csv
with open("hw_ok.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)

    # 欄位名稱
    w.writerow([
        "Product_Name",
        "Stock_Quantity",
        "Unit_Price",
        "Sales_Volume",
        "Total_Inventory_Value",
        "Revenue_90_Discount",
        "Best_Seller"
    ])

    # 寫入資料
    for i in range(len(products)):
        w.writerow([
            products[i],
            stock_quantity[i],
            unit_price[i],
            sales_volume[i],
            total_inventory_value[i],
            revenue_90_discount[i],
            i in best_indices
        ])

print("已成功輸出 hw_ok.csv")
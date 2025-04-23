import pandas as pd

#Load CSVs
customers = pd.read_csv('data/customers.csv')
orders = pd.read_csv('data/orders.csv')
products = pd.read_csv('data/products.csv')

print("Customers:")
print(customers.head(3))
print("\nOrders:")
print(orders.head(3))
print("\nProducts:")
print(products.head(3))

# Preview Data
print("Customers:")
print(customers.head(3))
print("\nOrders:")
print(orders.head(3))
print("\nProducts:")
print(products.head(3))

# Add full_name column to customers
customers["full_name"] = customers["first_name"] + " " + customers["last_name"]

print("\nCustomers with full_name:")
print(customers[["customer_id", "full_name", "email"]].head(3))

# Merge customers and orders on customer_id
customer_orders = pd.merge(orders, customers, on="customer_id", how="left")

# Preview the joined data
print("\nCustomer Orders:")
print(customer_orders[["order_id", "full_name", "email", "product_id", "price"]].head(3))

# Join with products to get product details
final_data = pd.merge(customer_orders, products, on="product_id", how="left")

# Preview final enriched dataset
print("\nFinal ETL Output:")
print(final_data[["order_id", "full_name", "product_name", "category", "price_y"]].head(3))

# Save final output to CSV
final_data.to_csv("data/final_customer_orders.csv", index=False)
print("\nData saved to data/final_customer_orders.csv ✅")

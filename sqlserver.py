import sqlite3
import pandas as pd

apt = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\apartment.csv')
car_sales = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\car_sales_tax.csv')
food = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\food.csv')
heal_ins = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\health_insurance.csv')
sq_f = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\house_square_footage.csv')
homes = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\houses.csv')
income_tax = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\income_tax.csv')
income = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\income.csv')
auto = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\insurance.csv')
sales_tax = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\sales_tax.csv')
property_tax = pd.read_csv(r'C:\Users\Blake Dennett\Downloads\CostOfLiving\property_tax.csv')


conn = sqlite3.connect('costofliving.db')

cur = conn.cursor()

# cur.execute("""CREATE TABLE apartment (
#     state string,
#     average_rent integer,
#     average_apartment_size integer
# )""")

# cur.execute("""DROP TABLE apartment;""")

# apt.to_sql('apartment', conn, if_exists='replace')

# print(pd.read_sql_query("""SELECT * From apartment LIMIT 5""", conn))



# print(pd.read_sql_query("PRAGMA table_info('apartment');", conn))


# food.to_sql('food', conn, index=False)
# heal_ins.to_sql('health_insurance', conn, index=False)
# sq_f.to_sql('apartment_size', conn, index=False)
# homes.to_sql('houses', conn, index=False)
# income_tax.to_sql('income_tax', conn, index=False)
# income.to_sql('income', conn, index=False)
# auto.to_sql('auto', conn, index=False)
# sales_tax.to_sql('sales_tax', conn, index=False)
# property_tax.to_sql('property_tax', conn, index=False)



# print(pd.read_sql_query("""SELECT * FROM car_sales LIMIT 5""", conn))

# print(pd.read_sql_query("""PRAGMA table_info('car_sales');""", conn))
conn.close()
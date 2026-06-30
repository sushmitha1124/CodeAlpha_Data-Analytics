import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("car_data.csv")


print("FIRST 5 ROWS")
print(df.head())


print("\nDATASET INFO")
print(df.info())


print("\nMISSING VALUES")
print(df.isnull().sum())


print("\nBASIC STATISTICS")
print(df.describe())


print("\nHIGHEST CAR PRICE")
print(df["Selling_Price"].max())


print("\nFUEL TYPE COUNT")
print(df["Fuel_Type"].value_counts())


df["Selling_Price"].plot(kind="hist")
plt.title("Car Price Distribution")
plt.xlabel("Selling Price")
plt.ylabel("Number of Cars")
plt.show()


df["Fuel_Type"].value_counts().plot(kind="bar")
plt.title("Fuel Type Count")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Cars")
plt.show()


print("\nAnalysis Completed Successfully")
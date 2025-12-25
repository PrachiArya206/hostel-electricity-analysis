import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("electricity.csv")

print("Complete Data:")
print(data)

data.columns = data.columns.str.strip()
print("\nColumn Names:")
print(data.columns)

block_usage = data.groupby("Block")["Electricity_Usage"].sum()
print("\nElectricity Usage Block-Wise:")
print(block_usage)

plt.figure()
block_usage.plot(kind="bar")
plt.title("Student Hostel Electricity Usage Analysis")
plt.xlabel("Block")
plt.ylabel("Electricity Usage (kWh)")
plt.tight_layout()
plt.show()
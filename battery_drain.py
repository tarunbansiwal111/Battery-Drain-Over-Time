
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create battery data

time = ["9 AM", "10 AM", "11 AM",
        "12 PM", "1 PM", "2 PM", "3 PM"]

battery = [100, 92, 83, 72, 60, 49, 35]

# Step 2: Create DataFrame

df = pd.DataFrame({
    "Time": time,
    "Battery": battery
})

print("Battery Data:")
print(df)

# Step 3: Calculate battery drain

df["Battery Drain"] = df["Battery"].shift(1) - df["Battery"]

df["Battery Drain"] = df["Battery Drain"].fillna(0)

print("\nBattery Drain:")
print(df)

# Step 4: Calculate total battery usage

total_drain = battery[0] - battery[-1]

print("\nTotal Battery Drain:", total_drain, "%")

# Step 5: Create line chart

plt.figure(figsize=(10, 5))

plt.plot(time, battery,
         marker='o',
         color='red',
         linewidth=2,
         label='Battery Level')

# Step 6: Add title and labels

plt.title("Battery Drain Over Time")
plt.xlabel("Time")
plt.ylabel("Battery Percentage (%)")

plt.ylim(0, 110)

plt.grid(True)
plt.legend()

# Step 7: Display chart

plt.show()

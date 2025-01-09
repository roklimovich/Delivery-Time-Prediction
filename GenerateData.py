import random
import pandas as pd

n_samples = 25000

data = {
    "DeliveryID": [f"D{str(i).zfill(3)}" for i in range(1, n_samples + 1)],
    "Distance (km)": [round(random.uniform(1, 20), 1) for _ in range(n_samples)],
    "Package_Weight (kg)": [round(random.uniform(0.5, 10), 1) for _ in range(n_samples)],
    "Weather_Conditions": random.choices(["Sunny", "Rainy", "Cloudy", "Foggy", "Snowy"], k=n_samples),
    "Traffic_Level": random.choices(["Low", "Medium", "High"], k=n_samples),
    "Start_Time_Delivery": [f"{random.randint(6, 20)}:{str(random.randint(0, 59)).zfill(2)}"
                            for _ in range(n_samples)],
    "Delivery_Time (mins)": [random.randint(10, 120) for _ in range(n_samples)],
}

df = pd.DataFrame(data)

df["Delivery_Difficulty"] = df["Distance (km)"] * df["Package_Weight (kg)"]
df["Distance_Category"] = pd.cut(
    df["Distance (km)"], bins=[0, 5, 10, 20], labels=["Short", "Medium", "Long"]
)
df["Start_Hour"] = df["Start_Time_Delivery"].str.split(":").str[0].astype(int)
df["Peak_Hours"] = df["Start_Hour"].apply(lambda x: 1 if 7 <= x <= 9 or 17 <= x <= 19 else 0)
df["Combined_Condition"] = df["Weather_Conditions"] + " + " + df["Traffic_Level"]
df["Efficiency"] = df["Delivery_Time (mins)"] / df["Distance (km)"]

df.to_csv("delivery_dataset5.csv", index=False)

print("Dataset generated and saved as 'delivery_dataset.csv'")
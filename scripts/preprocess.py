import pandas as pd

data = pd.read_csv("../data/drinkWaterApp_data.csv", parse_dates=["Date"])

data = data[["Date", "Time", "Water(ml)"]]

time_bins = [0, 11, 18, 21, 24]
time_labels = ['Morning', 'Noon', 'Evening', 'Night']
data['Time_of_day'] = pd.cut((pd.to_datetime(data['Time']).dt.hour), bins=time_bins, labels=time_labels, right=False)

data["Time"] = pd.to_datetime(data["Time"]).dt.time
data["Month"] = data["Date"].dt.month
data["Day"] = (data["Date"].dt.day).astype("category")
data["Week"] = data["Date"].dt.isocalendar().week
data["Weekday_name"] = data["Date"].dt.strftime('%a')


month_names = {11: "November", 12: "December", 1: "January", 2: "February", 3: "March"}
data["Month"] = data["Month"].map(month_names)

water_data = data[data["Date"].dt.year == 2024]

water_data.to_csv('drink_water_data.csv', index=False)

import pandas as pd

GY_data = pd.read_csv('Global YouTube Statistics.csv', encoding="ISO-8859-1")



#Top creators' subscriber counts, video views, upload frequency

df = GY_data[['subscribers','video views','uploads']]

# Head 5 rows
print("=== Dataset Overview ===")
print(df.head())
print("\n")

# Summary statistics using the describe method
summary_stats = df.describe()
print("=== Descriptive Statistics Overview ===")
print(summary_stats)
print("\n")

# Mean, Median and Mode
print("=== Mean, Median and Mode Overview ===")
mean = df.mean()
median = df.median()
mode = df.mode().iloc[0]  # In case there are multiple modes
print("Mean:\n", mean)
print("Median:\n", median)
print("Mode:\n", mode)
print("\n")

# Variance and standard deviation
variance = df.var()
std_deviation = df.std()
print("=== Variance and standard deviation Overview ===")
print("Variance:\n", variance)
print("Standard Deviation:\n", std_deviation)
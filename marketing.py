import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------- 1️⃣ Generate Dummy Data -----------------
# Define marketing channels
channels = ['Paid Search', 'Display Ads', 'Social Media', 'Email', 'Direct', 'Organic']

# Set random seed for reproducibility
np.random.seed(42)

# Number of customer interactions
n_samples = 5000

# Generate dataset
df = pd.DataFrame({
    'customer_id': np.random.randint(10000, 50000, n_samples),
    'timestamp': pd.date_range(start='2024-01-01', periods=n_samples, freq='min'),
    'channel': np.random.choice(channels, n_samples),
    'conversion': np.random.choice([0, 1], n_samples, p=[0.8, 0.2]),  # 20% conversion rate
    'revenue': np.random.randint(50, 500, n_samples) * np.random.choice([0, 1], n_samples, p=[0.8, 0.2])
})

# Save dummy data
df.to_csv("marketing_data.csv", index=False)
print("✅ Dummy marketing data saved as 'marketing_data.csv'")

# ----------------- 2️⃣ Last-Click Attribution Logic -----------------
# Load data
df = pd.read_csv("marketing_data.csv")

# Sort by customer and timestamp
df = df.sort_values(by=['customer_id', 'timestamp'])

# Filter only customers who converted
converted_users = df[df['conversion'] == 1]['customer_id'].unique()

# Filter data for converted users
converted_df = df[df['customer_id'].isin(converted_users)]

# Get last touchpoint before conversion
last_click_df = converted_df.groupby('customer_id').last().reset_index()

# Aggregate conversion & revenue per channel
channel_performance = last_click_df.groupby('channel').agg(
    total_conversions=('conversion', 'sum'),
    total_revenue=('revenue', 'sum')
).reset_index()

# Save attribution results
channel_performance.to_csv("last_click_attribution.csv", index=False)
print("✅ Last-click attribution results saved as 'last_click_attribution.csv'")

# ----------------- 3️⃣ Visualization: Attribution Insights -----------------
# Load results
channel_performance = pd.read_csv("last_click_attribution.csv")

# Plot the data
plt.figure(figsize=(10, 6))
sns.barplot(data=channel_performance, x='channel', y='total_conversions', palette="viridis")
plt.title("Last-Click Attribution: Conversions by Marketing Channel")
plt.xticks(rotation=45)
plt.ylabel("Total Conversions")
plt.xlabel("Marketing Channel")
plt.show()

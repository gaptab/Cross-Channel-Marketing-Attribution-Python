![alt text](https://github.com/gaptab/Cross-Channel-Marketing-Attribution-Python/blob/main/489.png)

**Data Generation (Marketing Data Simulation)**

We first generate a synthetic dataset to mimic real-world marketing interactions. Each row represents a customer’s engagement with a marketing channel, including:

Customer ID: A unique identifier for each user

Timestamp: The exact time the interaction occurred

Marketing Channel: Where the user engaged (e.g., Paid Search, Social Media, Email, etc.)

Conversion: Whether the user made a purchase (1 = Yes, 0 = No)

Revenue: The amount of money generated if a purchase occurred

This simulated dataset gives us 5,000 records of customer interactions with different marketing campaigns.


**Implementing the Last-Click Attribution Model**

Once we have the data, we apply Last-Click Attribution using the following logic:

Identify customers who made a purchase (converted users).

Filter out only their interactions and sort them by timestamp.

Find the last recorded interaction (channel) before purchase for each customer.

Count the total conversions & revenue per channel to see which channels contributed the most.

This process ensures we accurately attribute sales to the final marketing touchpoint before purchase.

**Visualizing the Results**

After running the attribution model, we generate a bar chart showing:

Which marketing channels drive the most conversions?

How many purchases are attributed to each channel?

This visualization helps business teams make data-driven decisions on:

✅ Where to increase marketing spend (high-performing channels)

✅ Which channels need optimization (low-converting channels)

✅ How to improve campaign strategies


**Business Impact of the Project**

🔹 Optimize Marketing Budget: Allocate more budget to high-converting channels

🔹 Improve ROI Measurement: Understand which channels drive actual revenue

🔹 Enhance Marketing Strategy: Focus on customer journey insights to refine campaigns

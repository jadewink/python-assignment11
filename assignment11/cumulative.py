# Task 2: A Line Plot with Pandas
# Create a file called cumulative.py. The boss wants to see how money is rolling in. 
# You use SQL to access ../db/lesson.db again. You create a DataFrame with the order_id and the total_price for each order. 
# This requires joining several tables, GROUP BY, SUM, etc.

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to a new SQLite database
with  sqlite3.connect("../../python_homework/db/lesson.db") as conn: 
    print("Database created and connected successfully.")

cursor = conn.cursor()
# Load a DataFrame
# Select Statement
query = "SELECT o.order_id, SUM(p.price * li.quantity) AS total_price FROM orders AS o JOIN line_items AS li ON li.order_id = o.order_id JOIN products AS p ON p.product_id = li.product_id GROUP BY o.order_id"
cumulative_df = pd.read_sql_query(query, conn)

# Add a "cumulative" column to the DataFrame. This is an interesting use of apply():
def cumulative(row):
   totals_above = cumulative_df['total_price'][0:row.name+1]
   return totals_above.sum()

# cumulative_df['cumulative'] = cumulative_df.apply(cumulative, axis=1)
cumulative_df['cumulative'] = cumulative_df['total_price'].cumsum()

# Line Plot
cumulative_df.plot(x="order_id", y=["cumulative"], kind="line", title="Cumulative Revenue vs. Order ID")
plt.show()

# Task 3: Interactive Visualizations with Plotly
# Load the Plotly wind dataset, via the following:
import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type='pandas')

# Clean the data. You need to convert the 'strength' column to a float.
df['strength'] = df['strength'].str.replace(r'[^\d\.]', '', regex=True).astype(float)

print("First 10 rows:\n", df.head(10))
print("\nLast 10 rows:\n", df.tail(10))

# Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
df = pldata.wind(return_type='pandas') # Returns a DataFrame.  plotly.data has a number of sample datasets included.
fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Strength vs. Frequency")
                #  , hover_data=["petal_length"])
fig.write_html("wind.html", auto_open=True)

# Do not try fig.show()!  This sometimes works, but usually it just hangs.
# Save and load the HTML file, as wind.html. Verify that the plot works correctly.
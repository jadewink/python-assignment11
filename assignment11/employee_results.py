# Task 1: Plotting with Pandas
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to a new SQLite database
with  sqlite3.connect("../../python_homework/db/lesson.db") as conn: 
    print("Database created and connected successfully.")

cursor = conn.cursor()
# Load a DataFrame called employee_results using SQL. You connect to the ../db/lesson.db database.
# Select Statement
query = "SELECT last_name AS 'Last Name', SUM(price * quantity) AS Revenue FROM employees e JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id"
employee_results = pd.read_sql_query(query, conn)

# Use the Pandas plotting functionality to create a bar chart where the x axis is the employee last name and the y axis is the revenue.
# Give appropriate titles, labels, and colors.
# Show the plot.

# Bar Plot
employee_results.plot(x="Last Name", y="Revenue", kind="bar", color="skyblue", title="Revenue by Employee")
plt.show()
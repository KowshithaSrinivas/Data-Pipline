import duckdb
import pandas as pd

# Connect to DuckDB
con = duckdb.connect()

# Query 1: Sample Data
print("▶ Sample Data:")
result = con.execute("""
    SELECT * FROM 'data/retailstore_large.csv'
    LIMIT 5
""").df()
print(result)

# Query 2: Average salary by gender
print("\n▶ Average Salary by Gender:")
result = con.execute("""
    SELECT Gender, AVG(Salary) AS Avg_Salary
    FROM 'data/retailstore_large.csv'
    GROUP BY Gender
""").df()
print(result)

# Query 3: Average salary by country
print("\n▶ Average Salary by Country:")
result = con.execute("""
    SELECT Country, AVG(Salary) AS Avg_Salary
    FROM 'data/retailstore_large.csv'
    GROUP BY Country
    ORDER BY Avg_Salary DESC
""").df()
print(result)

# Query 4: Salary by age group
print("\n▶ Average Salary by Age Range:")
result = con.execute("""
    SELECT 
        CASE 
            WHEN Age < 25 THEN 'Under 25'
            WHEN Age BETWEEN 25 AND 40 THEN '25-40'
            ELSE 'Over 40'
        END AS Age_Group,
        AVG(Salary) AS Avg_Salary
    FROM 'data/retailstore_large.csv'
    GROUP BY Age_Group
""").df()
print(result)

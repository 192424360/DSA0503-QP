import sqlite3

# Connect to database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Department (
    DeptID INTEGER PRIMARY KEY,
    DeptName TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    EmpID INTEGER PRIMARY KEY,
    EmpName TEXT,
    DeptID INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Salary (
    EmpID INTEGER,
    Salary INTEGER
)
""")

# Clear old data
cursor.execute("DELETE FROM Department")
cursor.execute("DELETE FROM Employee")
cursor.execute("DELETE FROM Salary")

# Insert data
cursor.executemany("INSERT INTO Department VALUES (?, ?)", [
    (1, "HR"),
    (2, "IT"),
    (3, "Finance")
])

cursor.executemany("INSERT INTO Employee VALUES (?, ?, ?)", [
    (101, "Asha", 1),
    (102, "Ravi", 1),
    (103, "Teja", 2),
    (104, "Kiran", 2),
    (105, "Divya", 3)
])

cursor.executemany("INSERT INTO Salary VALUES (?, ?)", [
    (101, 40000),
    (102, 50000),
    (103, 70000),
    (104, 60000),
    (105, 80000)
])

conn.commit()

print("===== Merged Tables =====")
cursor.execute("""
SELECT e.EmpID, e.EmpName, d.DeptName, s.Salary
FROM Employee e
JOIN Department d ON e.DeptID = d.DeptID
JOIN Salary s ON e.EmpID = s.EmpID
""")

for row in cursor.fetchall():
    print(row)

print("\n===== Employees Earning Above Department Average =====")
cursor.execute("""
SELECT e.EmpID, e.EmpName, d.DeptName, s.Salary
FROM Employee e
JOIN Department d ON e.DeptID = d.DeptID
JOIN Salary s ON e.EmpID = s.EmpID
WHERE s.Salary >
(
SELECT AVG(s2.Salary)
FROM Employee e2
JOIN Salary s2 ON e2.EmpID = s2.EmpID
WHERE e2.DeptID = e.DeptID
)
""")

for row in cursor.fetchall():
    print(row)

print("\n===== Department-wise Highest Salary =====")
cursor.execute("""
SELECT d.DeptName, MAX(s.Salary)
FROM Employee e
JOIN Department d ON e.DeptID = d.DeptID
JOIN Salary s ON e.EmpID = s.EmpID
GROUP BY d.DeptName
""")

for row in cursor.fetchall():
    print(row)

conn.close()

-- Create Department table
CREATE TABLE Department (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

-- Create Employee table
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    DeptID INT,
    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
);

-- Create Salary table
CREATE TABLE Salary (
    EmpID INT PRIMARY KEY,
    Salary DECIMAL(10,2),
    FOREIGN KEY (EmpID) REFERENCES Employee(EmpID)
);

-- Insert sample departments
INSERT INTO Department VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');

-- Insert sample employees
INSERT INTO Employee VALUES
(101, 'Asha', 1),
(102, 'Ravi', 1),
(103, 'Teja', 2),
(104, 'Kiran', 2),
(105, 'Divya', 3);

-- Insert salaries
INSERT INTO Salary VALUES
(101, 40000),
(102, 50000),
(103, 70000),
(104, 60000),
(105, 80000);


SELECT e.EmpID,
       e.EmpName,
       d.DeptName,
       s.Salary
FROM Employee e
JOIN Department d
ON e.DeptID = d.DeptID
JOIN Salary s
ON e.EmpID = s.EmpID;

SELECT e.EmpName,
       d.DeptName,
       s.Salary
FROM Employee e
JOIN Department d
ON e.DeptID = d.DeptID
JOIN Salary s
ON e.EmpID = s.EmpID
WHERE s.Salary > (
    SELECT AVG(s2.Salary)
    FROM Employee e2
    JOIN Salary s2
    ON e2.EmpID = s2.EmpID
    WHERE e2.DeptID = e.DeptID
)
SELECT d.DeptName,
       MAX(s.Salary) AS Highest_Salary
FROM Employee e
JOIN Department d
ON e.DeptID = d.DeptID
JOIN Salary s
ON e.EmpID = s.EmpID
GROUP BY d.DeptName;

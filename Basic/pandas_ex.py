import pandas as pd
#print(pd.__version__)

# Example - 2
# nums = [10,20,30,40,50]
# res = pd.Series(nums)
# print(res)

# Example -3
# data = ["Python,"ML","DL"]
# res = pd.Series(data,index=["a","b","c"])
# print(res)

# Example - 4
# marks = [80,90,95]
# res = pd.Series(marks,index=["Std1","Std2","Std3"])
# print(res)
# print(res["Std3"])

# Example -5 
# emp = {
#     "EmpId": [101,102,103],
#     "Department": ["IT","HR","Finance"],
#     "Salary": [5000,6000,7000]
# }
# df = pd.DataFrame(emp,index=["a","b","c"])
# print(df)

# Example -6
df = pd.read_csv("employees.csv")
#print(df)
#print(df.head(3)) # read 3 rows
#print(df.head(10)) # read 10 rows
#print(df.head()) # read 5 rows

#print(df.tail()) # read last 5 rows
#print(df.tail(10)) # read last 10 rows

#print(df.shape) # displays rows and columns
#print(df.columns) # displays all the column names 

#print(df.info()) # displaying - col name , datatype , null values

#print(df["Salary"].describe()) # mathematical calculation

#print(df["Name"]) # display single column

#print(df[["Name,"Age"]].head()) # display more than one column

#print(df[df["Salary"]>70000]) # display employees whose salary > 70000

#print(df[df["Departmet"]=="IT"]) # display only IT Department

#print(df.groupby("Department")["Salary"].mean()) # find mean salary department wise

#print(df.sort_values("Salary",ascending=False)) # find employee with highest salary in descending order

#print(df.sort_values("Salary",ascending=False).head(1)[["Name","Department"]]) # find highest salary employee name and department

#print(df[(df["Salary"]>70000) & (df["Department"]=="IT")]) # apply multiple conditions to filter data

# Load the CSV file with null values
dff = pd.read_csv("employees_null.csv")
#print(dff)  

# missed value displays with "True"
#print(dff.isnull()) 

# missed value displays with "False"
#print(dff.isnotnull())

# count of null values in each column
#print(dff.isnull().sum()) 

# percentage of null values in each column
# percentage of null values in each 
#null_pct=print(dff.isnull().sum()/len(dff)*100) 
#print(null_pct)

# fill null values with 0
#print(dff.fillna(0)) 

# fill null values with mean of age column
#print(dff.fillna(dff["age"].mean())) 

# fill null values with mean of salary column
#print(dff.fillna(dff["salary"].mean())) 

#print(dff)
# forward fill - fill null values with previous non-null value
#print(dff.ffill()) 

# backward fill - fill null values with next non-null value
#print(dff.bfill()) 

# fill null values with linear interpolation
#dff[["age","salary"]]=dff[["age","salary"]].interpolate() 
#print(dff)

# drop rows with any null values
#print(dff.dropna()) 

# drop rows where all values are null
#print(dff.dropna(how="all")) 

# drop rows where age is null
#print(dff.dropna(subset=["age"])) 

# drop rows with at least 2 non-null values
#print(dff.dropna(thresh=2)) 




import pandas as pd

students = pd.read_csv(r"../CSV FILES/students.csv")

#                         groupby()
#used to group rows having similar values

# Group students according to City.

for city,group in students.groupby("City"):
  print("City: ",city)
  print(group)

# Group students according to Department

for dept, rows in students.groupby("Department"):
  print("Department: ",dept )
  print(rows)

# Group students according to Marks
for marks,stud in students.groupby("Marks"):
  print("Marks: ",marks)
  print(stud)

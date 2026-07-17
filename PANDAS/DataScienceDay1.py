import pandas as pd


#                       Series
#         A Series is a one-dimensional labeled array.


# Example 1 :

# marks = [85,78,39,87,13]
# data = pd.Series(marks)
# print(data)


# Example 2:
# names = ["Karan", "Anas", "Harsh"]
# print(pd.Series(names))


# example 3: Custom Index and Accessing Series
marks =[85,78,39]
data = pd.Series(marks, index=["Karan", "Anas","Harsh"])
print(data)

# Accessing by index name
print(data["Anas"])

# Accessing by position
print(data[2])


#                  DataFrame
#       A DataFrame is a two-dimensional table.

# Example 1:
# students = {
#   "names": ["Karan","Anas","Harsh","Saad","Aman","Arnold","Devda"],
#   "marks": [74,66,49,35,25,30,8]
# }

# print(pd.DataFrame(students))


# Example 2: DF using list of lists
data = [
  ["Karan",22],["Anas",66],["Harsh",49]
]

# print(pd.DataFrame(data, columns=["Name", "Age"]))


# Example 3: DF using List of Dictionary
sheet = [
  {"Name": "Karan", "Age":22},
  {"Name": "Anas", "Age":23},
  {"Name": "Harsh", "Age":20}
]

print(pd.DataFrame(sheet))

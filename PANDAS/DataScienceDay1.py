import pandas as pd
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

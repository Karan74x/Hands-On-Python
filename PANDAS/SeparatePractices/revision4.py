import pandas as pd


#                       4.Sorting

# sort_values() is used to arrange rows based on the values of one or more columns.


df = pd.DataFrame({
    "Patient_Name": ["Karan", "Rahul", "Anas", "Aman", "Karan", "Anas"],
    "Age": [22, 34, 18, 35, 21, 16],
    "Fee": [800, 500, 1200, 700, 600, 400]
})


# Sorts the rows based on the Fee column.
# ascending=True means smallest value comes first.
#           1. Sort ascending

print(df.sort_values(by="Fee", ascending=True))



# Sort descending
print(df.sort_values(by="Age", ascending=False))


#                   Sorting by multiple columns

# Sort Name in ascending order (A → Z)
# and Age in descending order (High → Low) within each Name
print(df.sort_values(by=["Patient_Name", "Age"], ascending=[True, False]))



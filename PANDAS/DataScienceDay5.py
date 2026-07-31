import pandas as pd
df = pd.read_csv(r"D:/students.csv")


#               sort_values()
# used to sort the DataFrame by one or more columns in ascending or descending order.

# sort_values(by,axis,ascending,inplace,na_position,ignore_index,key)

# 1) by  -> Specifies which column(s) to sort by.


#              Sorting by ONE Column

#Sort everyone by their Marks, from smallest to biggest.
# print(df.sort_values(by="Marks"))

#Sort everyone by their Name, from smallest to biggest.
# print(df.sort_values(by="Name"))

#Sort everyone by their Age, from biggest to lowest.
# print(df.sort_values(by="Age",ascending=False))


#               Sorting by MULTIPLE Columns
# Rule 1 (First Priority): Sort by City alphabetically (A to Z).
# Rule 2 : If two people live in the same city, sort them by Marks (lowest to highest).

# Sort by City A-Z first. If cities match, lowest mark comes first
# print(df.sort_values(by=["City","Marks"]))

# Sort by City A-Z first. If cities match, highest mark comes first becasue of ascending is set to False
#print(df.sort_values(by=["City", "Marks"], ascending=[True,False]))


#print(df.sort_values(by=["Age","City"]))

#print(df.sort_values(by=["Age","City"], ascending=[True,False]))


#               axis (0 vs 1)
# axis=0 or 'index' (Default): Sorts Rows up-and-down based on column values.
#axis=1 or 'columns': Sorts Column Names / Headers left-to-right.

# Sort rows vertically using the values inside "Marks"
# print(df.sort_values(by="Marks",axis=0))


# Sort column names alphabetically: City $\rightarrow$ Marks $\rightarrow$ Name.
# print(df.sort_values(axis=1))



#                   inplace (False vs True)
# Controls whether to overwrite the existing DataFrame or return a brand-new copy.

# Leaves original df untouched and returns a new sorted DataFrame.
print(df.sort_values(by="Marks", inplace=False))
print(df)

# Overwrites df directly in memory and returns None.
print(df.sort_values(by="City", inplace=True))
print(df)

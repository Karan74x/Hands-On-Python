import pandas as pd
df = pd.read_csv(r"D:/students.csv")


#               sort_values()
# used to sort the DataFrame by one or more columns in ascending or descending order.

# sort_values(by,axis,ascending,inplace,na_position,ignore_index,key)

# 1) by  -> Specifies which column(s) to sort by.


#              Sorting by ONE Column

#Sort everyone by their Marks, from smallest to biggest.
print(df.sort_values(by="Marks"))

#Sort everyone by their Name, from smallest to biggest.
print(df.sort_values(by="Name"))

#Sort everyone by their Age, from biggest to lowest.
print(df.sort_values(by="Age",ascending=False))


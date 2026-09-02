import pandas as pd


#              1.   Data Cleaning & Conversion


df = pd.DataFrame({
    "Age": ["21", "22", "twenty three", "25", "unknown"],
    "Marks": ["85", "90", "Absent", "78", "95"]
})


# pd.to_numeric(column, errors = 'coerce') -> Converts values into numbers.
# errors="coerce" is important

# Age converted to numeric form
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
# print(df)

# Age converted to numeric form
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
# print(df)




# pd.to_datetime(column, error='coerce', dayfirst=True) -> converts values into datetime format
# NaT -> Not a Time / invalid date

df2 = pd.DataFrame({
    "Appointment_Date": [
        "12-08-2026",
        "2026-08-15",
        "20/08/2026",
        "bad date",
        "25-08-2026"
    ],
     "Order_Time": [
        "12-08-2026",
        "2026/08/15",
        "20/08/2026",
        "bad date",
        "25-08-2026"
    ]
})

# Converted invalid date to proper format
df2["Appointment_Date"] = pd.to_datetime(df2["Appointment_Date"], errors="coerce", dayfirst=True)

df2["Order_Time"] = pd.to_datetime(df2["Order_Time"], errors="coerce", dayfirst=True)
# print(df2)



#      Method	                      What it does

#    .str.strip()     	Removes spaces from beginning/end
#   .str.replace()          	Replaces text



# df["column"].str.strip() -> remove spaces from start and end


df3 = pd.DataFrame({
   "Product": [
        " Laptop Stand ",
        "Wireless Mouse",
        " Office Chair ",
        "Notebook Pack  ",
        "  USB Hub"
    ]
})

df3["Product"] = df3["Product"].str.strip()

# for product in df3["Product"]:
#    print(repr(product))


# df["column"].str.replace("old_Value", "new_Value") -> replace specific text inside a column

print(df3["Product"].str.replace("Mouse", "Speaker"))
print(df3["Product"].str.replace("Chair", "Computer"))



df4 = pd.DataFrame({
  "Age":[
    23,56,"45", "76", "98", "74","999"
  ]
})

# df["column"].astype(int) -> Used to change the data type of a column to int.
print(df4["Age"].astype(int))

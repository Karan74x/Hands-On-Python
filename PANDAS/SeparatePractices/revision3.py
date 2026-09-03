import pandas as pd

#             3.Duplicate Handling


# duplicated() -> checks whether a row is a duplicate of a previous row.
# True  -> duplicate row
# False ->  unique row

df = pd.DataFrame({
  "Appointment_ID" : ["A101", "A102", "A103","A102", "A105"],
  "Patient_Name":["Karan", "Anas", "Harsh", "Anas", "Aman"],
  "Fee":[500, 600, 800, 600, 600]
})

print(df.duplicated())

# to see duplicate rows
print(df[df.duplicated()])


#                 drop_duplicates()
#            remove duplicate rows from dataFrame


# By default, it keeps the first occurrence.

print("\nBefore:\n", df)
df = df.drop_duplicates()

print("\nAfter:\n", df)



# → remove duplicates based on a particular column.
print(df.drop_duplicates(subset=["Appointment_ID"]))



import pandas as pd

df = pd.DataFrame({
    "Age": ["21", "22", "twenty three", "25", "unknown"],
    "Marks": ["85", "90", "Absent", "78", "95"]
})


# pd.to_numeric(column, errors = 'coerce') -> Converts values into numbers.
# errors="coerce" is important

# Age converted to numeric form
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
print(df)

# Age converted to numeric form
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
print(df)

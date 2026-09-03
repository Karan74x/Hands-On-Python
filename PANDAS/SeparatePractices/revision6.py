import pandas as pd


#          6. Supporting Operations

# Operation	                  Simple meaning

# unique()	             What different values exist?
# value_counts()	       How many times does each value appear?
# reset_index()	         Convert index → normal column
# copy()	                Make an independent copy




df = pd.DataFrame({
    "Name": ["Karan", "Rahul", "Amit", "Karan", "Rahul"],
    "City": ["Ahmedabad", "Mumbai", "Delhi", "Ahmedabad", "Mumbai"],
    "Age": [22, 25, 21, 22, 25]
})


# 1. Question: What different cities are present?
# unique() = show unique values
print(df["City"].unique())



# 2. Question: How many people are from each city
# value_counts() = count how many times each value appear
print(df["City"].value_counts())


# reset_index() ->  turn the index back into a normal column
result = df.groupby("City")["Age"].mean()
print("Here, City is the index.\n",result) #->Here, City is the index.

result = result.reset_index()
print("\n\nAfter reset_index().\n",result)



# copy() = create a separate copy so changes don't affect the original

df_clean = df.copy()
print(df_clean)

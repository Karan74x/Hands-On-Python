arr = [3,1,6,9,]
largest = 0
secLargest = 0

for i in arr:
  if i > largest:
    print("before: ",largest, secLargest)
    secLargest = largest
    largest = i
    print("After: ",largest, secLargest)

print("Largest: ",largest)
print("Second Largest",secLargest)

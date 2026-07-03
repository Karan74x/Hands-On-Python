arr = [100,200,300,400,500]
revarr = []
print("BEFORE REVERSE: ", arr)
for i in reversed(range(len(arr))):
  revarr.append(arr[i])

print("AFTER REVERSE: ", revarr)

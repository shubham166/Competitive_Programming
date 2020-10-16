import array

arr = array.array('i', [1, 2, 3])
print(arr.tolist())

arr.append(4)
print(arr.tolist())

arr.insert(2, 5)
print(arr.tolist())

arr.pop(3)
print(arr.tolist())

# Remove the element 2 from the array.
arr.remove(2)
print(arr.tolist())


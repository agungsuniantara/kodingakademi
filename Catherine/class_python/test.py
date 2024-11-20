combine = {
    1: [2],
    4: [5, 6],
    4: [8]  # This would be overwritten in a dictionary. This is just for demonstration
}

# Create an empty dictionary to store the final result
new = {}

# Iterate through the dictionary (with fixed duplicate keys)
for key, value in combine.items():
    if key not in new:
        new[key] = sum(value)
    else:
        new[key] += sum(value)

print(combine)
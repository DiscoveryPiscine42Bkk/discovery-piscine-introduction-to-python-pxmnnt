original_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []

for i in original_arr:
    if(i > 5):
        new_arr.append(i+2)

new_arr = set(list(new_arr))

print(f"Original array: {original_arr}")
print(f"New array: {new_arr}")
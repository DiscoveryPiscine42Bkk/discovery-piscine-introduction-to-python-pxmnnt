def find_the_redheads(family):
    arr = []

    for (key, value) in family.items():
        if (value == 'red'):
            arr.append(key)

    return arr

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
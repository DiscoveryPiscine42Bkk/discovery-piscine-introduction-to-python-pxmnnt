
def array_of_names(names):
    arr = []

    for(key, value) in names.items():
        key = key.capitalize()
        value = value.capitalize()
        arr.append(f"{key} {value}")

    return arr

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
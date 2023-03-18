people = [
    {"name": "Steve", "Favorite": "Real Madrid"},
    {"name": "Chris", "Favorite": "Los Angles Lakers"},
    {"name": "Ice", "Favorite": "Roma"}
]


people.sort(key=lambda person: person["name"])
print(people)

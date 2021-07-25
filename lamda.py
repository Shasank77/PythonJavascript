people = [
    {"name": "Shasank", "house":"sydney"},
    {"name": "Mayank", "house":"Darwin"},
    {"name": "Sandeep", "house":"pearth"},
]

def f(person):
    return person["name"]

people.sort(key=lambda person: person["name"])

print(people)
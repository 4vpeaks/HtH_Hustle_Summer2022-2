full_name = "Phong Trang"
nickname = "John"
age = 16
has_used_python = False

hobbies = [
    "editing",
    "gameing",
    "eating good food",
]

fav_things = {
    "movie": "Tenet",
    "food": "french fries",
    "hobby": hobbies[0],
    "show/anime": "Moonknight",
    "number": 33
}

print(
    f"Hello world! My name is {full_name}, but many of my friends call me {nickname}. I am {age} years old."
)
print()
print(f"Has Python Experience: {has_used_python}")
print()

for key in fav_things.keys():
    print(f"My favorite {key} is {fav_things[key]}.")

print()
print(f"Here are some of my other hobbies: {hobbies}")
print()

all_vars = dict(vars())

import random

goat1 = random.randint(1, 3)
goat2 = random.randint(1, 3)

while goat1 == goat2:
    goat2 = random.randint(1, 3)


success = 0
tries = 1_000_000
for _ in range(tries):
    options = [1, 2, 3]
    choice = random.randint(1, 3)
    options.remove(choice)
    if choice == goat1:
        options.remove(goat2)
    else:
        options.remove(goat1)

    choice = options[0]

    if choice != goat1 and choice != goat2:
        success = success + 1

print(success / tries)

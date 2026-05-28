#peyton mcadams
#madlibs story

import random
def madlibs():

    user = []
    plurnouns = ["cats", "dogs", "houses", "buses", "boxes", "tomatoes", "children", "men", "women", "feet", "mice"]
    locations = ["house", "doghouse", "school", "police station", "train station", "cafe", "jail", "airport", "convenience store", "diner", "city hall"]
    plurfoods = ["eggs", "hot dogs", "peas", "oranges", "poptarts", "waffles", "ice cubes", "chocolate bars", "s'mores", "bagels", "protein bars"]
    nouns = ["cardboard cutout", "candy bar", "plunger", "lightbulb", "t-shirt", "flag", "football", "toothbrush", "golf club", "sock", "apple"]
    liquids = ["orange juice", "protein shake", "diet coke", "smoothie", "matcha", "chai latte", "chocolate milk", "milk", "water", "sparkling water", "cider"]

    plurnoun = input("Please enter a plural noun: ")
    if plurnoun == "random":
        user.append(random.choice(plurnouns))
    else:
        user.append(plurnoun)
    location = input("Please enter a location: ")
    if location == "random":
         user.append(random.choice(locations))
    else:
        user.append(location)
    plurfood = input("Please enter a plural food: ")
    if plurfood == "random":
         user.append(random.choice(plurfoods))
    else:
        user.append(plurfood)
    noun = input("Please enter a noun: ")
    if noun == "random":
         user.append(random.choice(nouns))
    else:
        user.append(noun)
    liquid = input("Please enter a liquid: ")
    if liquid == "random":
         user.append(random.choice(liquids))
    else:
        user.append(liquid)
    plurnoun = input("Please enter a plural noun: ")
    if plurnoun == "random":
         user.append(random.choice(plurnouns))
    else:
        user.append(plurnoun)
    location = input("Please enter a location: ")
    if location == "random":
         user.append(random.choice(locations))
    else:
        user.append(location)
    noun = input("Please enter a noun: ")
    if noun == "random":
         user.append(random.choice(nouns))
    else:
        user.append(noun)
    plurnoun = input("Please enter a plural noun: ")
    if noun == "random":
        user.append(random.choice(nouns))
    else:
        user.append(noun)

    user = [item.upper() for item in user]

    print(f"""A group of \033[1m{user[0]}\033[0m once went to the \033[1m{user[1]}\033[0m.
The first girl ordered \033[1m{user[2]}\033[0m. They came with extra \033[1m{user[3]}\033[0m!
The boys bought a large glass of \033[1m{user[4]}\033[0m. Afterward, they exchanged
\033[1m{user[5]}\033[0m at the \033[1m{user[6]}\033[0m. The first boy opened up a \033[1m{user[7]}\033[0m.
Awwww said everyone. The next girl opened up a huge \033[1m{user[8]}\033[0m. Everyone
laughed.""")

madlibs()

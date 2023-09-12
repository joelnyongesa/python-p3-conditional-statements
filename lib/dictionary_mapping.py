# used if there is a long set of conditions inside our if/else statements.
# Python does not have the switch/case unlike JS, so it looks to solve this inside if else statements. Dictionary mapping is key as it comes in handy.


dog = "sleeping"

dict_map = {
    "hungry": "Refilling food bowl",
    "thirsty": "Refilling water bowl",
    "playful": "Playing tug-of-war",
    "cuddly": "Snuggling",
}

# A dictionary's .get() method lets us set a default value
owner = dict_map.get(dog, "Reading newspaper")

print(owner)
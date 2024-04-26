import random

#Define  a class for validator nodes
class Validator:
    def __init__(self, name, stake):
        self.name = name
        self.stake = stake

#Function to select a validator for the next block
def select_validator(validators):
    #Randomly choose a validator based  on the stake(higher stake, higher chance)
    total_stake = sum(validator.stake for validator in validators)
    probability = [validator.stake / total_stake for validator in validators]
    return random.choices(validators, weights=probability)[0]

#Create some validator nodes
validators = [
    Validator('Olawale', 100),
    Validator('Babatunde', 70),
    Validator('Mustapha', 80),
]

#Simulate block creation
new_block = f"Block created by {select_validator(validators).name}"

#Print the newly created block
print(new_block)
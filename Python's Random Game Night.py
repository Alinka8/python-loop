import random
list_items=["book", "pen", "pencil", "bubble gum", "paper"]
user_guess=(input("Guess the item? "))
guess_item= random.choice(list_items)
print(f"Guess item was {guess_item}")
if guess_item == user_guess:
    print("You guested correctly")
else:
    print("Not correct")

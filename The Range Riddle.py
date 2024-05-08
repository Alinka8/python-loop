# task 1 part 1 Your Mood Today
import random
mood_list=["happy","sad", "energetic", "calm"]
days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
for day in days:
    selected_mood = random.choice(mood_list)
    print(f"{day} we will be {selected_mood}")
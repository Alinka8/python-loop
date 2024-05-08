# task 2 part 1
# record 3 times per day for each day of the week
# outer loop should iterate over the days
# the inner loop should iterate over the times of the day
# For each time, randomly select a mood from a predefined list and print it.

import random

days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
times=["morning", "afternoon", "evening"]
mood_list=["happy","sad", "energetic", "calm"]
for day in days:
     for time in times:
        selected_day=random.choice(days)
        selected_time=random.choice(times)
        selected_mood=random.choice(mood_list)
        print(f" On {selected_day}, {selected_time} you were {selected_mood}")

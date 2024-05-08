# task 5 part 1
# Our playlist of genres
import random 
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
message = ['is my favorite', 'doesnt like', 'sometimes listen', 'rarely listen']
for genre in genres:
    custom_message=random.choice(message)
    print(f"{genre} {custom_message}")

# task 5 part 2 The Remix Artist with while
import random 
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
index= 0
while index < len(genres):
    genre = genres[index]
    print(f"My favourite genre is {genre}")

    if genre == 'Hip-hop':
        break
    index +=1

# task 5 part 3 Light Show Technician Loop
import random
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for index in range(len(genres)):
    if genres[index] == "Classical":
        continue
    print("Track"+ str(index+1)+ ":"+ genres[index]+ "  - light show is on!")
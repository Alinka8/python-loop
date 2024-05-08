# task 6 part 1  The Selective DJ
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for genre in genres[2:4]:  
    print(f"Sublese of genres is {genre}")

# task 6 part 2 The One-Liner Band with List Comprehensions
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
new_list=[genre + ' Music' for genre in genres]
print(new_list)

# task 6 part 3 Numerical Beats with range
countdown = 10
for number in range (countdown,0,-1):
    print(number)
    print("The beats drop now!")
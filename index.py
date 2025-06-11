import random
range_start=int(input("Enter the range start: "))
range_end=int(input("Enter the range end: "))

print(f'Your range start from {range_start} to {range_end}. Okay, Lets start the game')

random_num=random.randint(range_start, range_end)

chance = 7
chance_used = 0
while chance>chance_used:
    chance_used=chance_used+1
    user_input= int(input("Guess the number: "))
    if chance_used >=chance and user_input!=random_num:
        print(f'Sorry! Better luck next time. Your number is {random_num}')
        break

    if user_input>random_num:
        print("Too high! Try a lower number")
    
    elif user_input<random_num:
        print("Too Low! Try a higher number")
    
    elif user_input == random_num:
        print(f"Correct answer. You have guess the right answer in {chance_used} attempt ")
        break


    


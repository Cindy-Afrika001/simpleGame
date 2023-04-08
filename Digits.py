import random 

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
   top_of_range = int(top_of_range)  

   if top_of_range <=5:
    print("Boss!Something better next😁😁")
    quit()
else:
    print("What!!")
    quit() 

random_number = random.randrange(5, 11)
print(random_number)
while True:
    guess_work = input ("Type a guess: ")
if guess_work.isdigit():
    guess_work = int(guess_work)
else:
    print("warning!! a number next time")
if guess_work == top_of_range:
    print("There you go baby!!")
    breakpoint
else:
    print("another trial please")


 


def check_guess(guess,answer):
    
    global score
    still_guessing=True
    attempt=0

    while still_guessing and attempt<3:
        
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing=False
            
        else:

            if attempt<2:
                guess= input("Wrong Answer Try Again..!! ")
            attempt=attempt + 1

        if attempt==3:
            print("The Correct Answer is", answer)
            
            
 
        
score=0
guess1= input("Which bear lives at the North Pole? ")
check_guess(guess1,"polar bear")

guess2 = input("Which is the fastest land animal? ")
check_guess(guess2,"cheetah")

guess3= input("Which is the large animal? ")
check_guess(guess3,"blue whale")

guess4= input("Who is Rohan? ")
check_guess(guess4,"hero")

guess5=input("Where Is Islington Located? ")
check_guess(guess5,"Kamalpokhari")

print("Your Score is ",str(score))

        

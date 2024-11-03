import random 

#empty flashcard
flashcard={}


#Adding flashcard
def addflashcard():
    question=input("Enter the question for flashcard")
    answer=input("Enter the answer for flashcard")
    flashcard[question]=answer
    print("Flashcard Added")
    print("      ")


#Reviewing flashcard
def reviewflashcard():
    if not flashcard:
        print("No flashcard to review.")
        return

    
    print("Here are all your flashcards")
    for question, answer in flashcard.items():
        print(f"QUESTION:",[question])
        print(f"ANSWER:",[answer])
    print()
 

#Taking a Test
def quiz():
    if not flashcard:
        print("There are no flashcards to start the quiz")
        return

    print("Let's start the quiz!")
    print("Type 'exit' to leave the quiz.")
    questions=list(flashcard.keys())
    random.shuffle(questions)


    correct=0
    total=len(questions)

    for question in questions:
        user_A=input(f"Q={question}\n Your Answer:")
        if user_A.lower()=='exit':
            break
        elif user_A.lower()==flashcard[question].lower():
            print("Correct")
            correct+=1
        else:
            print(f"Your answer's incorrect. The correct answer is: {flashcard[question]}")

    print(f"you got {correct} out of {total} correct.")
    print("Congrats!!!")
    
#Creating a main function
def main():
    while True:
        print("   ")
        print("FLASHCARDS")
        print("1.Add flashcard")
        print("2.Review flashcard")
        print("3.Quiz Yourself")
        print("4.Exit")

        choice=input("Choose an option:")

        if choice=='1':
            addflashcard()
        elif choice=='2':
            reviewflashcard()
        elif choice=='3':
            quiz()
        elif choice=='4':
            print("You are leaving, GoodBye")
            break
        else:
            print("Invalid option. Please enter a VALID option")

#Run the main function
if __name__=="__main__":
    main()
    
        

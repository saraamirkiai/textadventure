start = '''
Today is the day of your interview! You are applying for a job at a startup to help support your family.  You don't know who is interviewing you until you walk in...
'''


print(start)


print("Type 'male' if you are male or 'female' if you are female.")
user_input = input()
if user_input == "male":
    print("You find out that you are being interviewed by a well known guy-friend.  Do you wish to continue this interview? yes or no?")
    user_input = input()
    if user_input == "yes":
        print("He asks you if you are interested working with the startup. Are you? yes or no?" )
        user_input = input()
        if user_input == "yes":
            print("Congratulations! You got the job. Your starting pay will be $20 an hour.")
        elif user_input == "no":
            print ("Oh ok.  Find another job.")
        else:
            print("No job for you.  Bad choice")
    elif user_input == "no":
        print("No job for you.  Bad choice")
elif user_input == "female":
            print("UH OH! You have found that you are getting interviewed by a sexist man.  Do you wish to continue your interview? ")
            user_input = input()
            if user_input == "yes":
                print ("He decides to walk you to your car.  Did you take your carseat out? yes or no?")
                user_input = input ()
                if user_input == ("yes"):
                    print ("You got the job! You will be paid only $16.00... because you are a girl. If you chose to be a man you would be paid $20 because of the wage gap. ")
                elif user_input == ("no"):
                    print ("There was a better candidate.....  Employees often walk their potential employees to their car to see if they have a carseat.  The carseat implies that the person has a kid.  Although illegal, the man interviewing you did not choose you for the job because you have a child and he assumed that you will be less focused on the job. ")
else:
    print("What gender is that?????")

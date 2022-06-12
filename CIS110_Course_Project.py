print("Hello, there! I have a cool story to tell you about this stray cat.")
print("Before I tell you, I must ask you a few questions.")
print("Press enter after your finished.")
input("\nPress enter to continue")

keepPlaying ="yes"
while keepPlaying.lower() == "yes":

    catName = input("\nWhat is the cat's name:    ")
    while (len(catName) == 0):
        catName = input("Please enter a cat's name:    ")

    catBreed = input("What is the cat's breed:    ")
    while (len(catBreed) == 0):
        catBreed = input("Please enter a cat's breed:    ")

    favoriteNumber = input("What is your favorite number:    ")
    while not favoriteNumber.isdigit():
        favoriteNumber = input("Please enter a number:    ")

    cityName = input("What city do you live near:    ")
    while (len(cityName) == 0):
        cityName = input("Please enter a city you live near:    ")

    forestName = input("What forest do you live near:    ")
    while (len(forestName) == 0):
        forestName = input("Please enter a forest you live near:    ")

    ownerName = input("What is your name:    ")
    while (len(ownerName) == 0):
        ownerName = input("Please enter your name:    ")

    print("\nHere we go!")

    print("\nOnce upon a time on a cold night in", cityName, "there was a stray", catBreed, "named", catName + ".")
    print( catName, "needed somewhere to hide from the cold so it jumped in the back of a pickup truck with tarp covering half the bed.")
    print(catName, "went to sleep and when", catName, "woke up it had no idea where it is")


    leave_Truck =  input("\n Does the cat leave the truck?  Yes or No:   ")
    while leave_Truck.lower() != "yes" and leave_Truck.lower() != "no":
        leave_Truck =  input("\nPlease enter yes or no:   ")

    if leave_Truck.lower() == ("yes"):

        print("\n", catName, "leaves the truck and runs towards", forestName + ".")
        print(catName, "starts to look around and smell the new environment in", forestName, "and approaches a skunk.")
        print("The skunk shoots", catName, "and", catName, "runs further into", forestName + ".")

    if leave_Truck.lower() == ("no"):
            print("the sleepy", catBreed, "attempts to look around the back of the truck, but", catName, "suddenly hears something in the distance")
            print("The truck owner spots", catName, "and screams “get out of my truck!”", catName, "runs out of the truck and far into", forestName + ".")

    print("\n", catName, "stops in front of a stream.")

    cross_Stream = input("\n Should the cat cross the stream? Yes or No:   ")
    while cross_Stream.lower() != "yes" and cross_Stream.lower() != "no":
        cross_Stream =  input("\nPlease enter yes or no:   ")

    if cross_Stream.lower() == ("yes"):
        print( "\n", catName, " attempts to cross the stream using the rocks that are sticking out of it.")
        print(favoriteNumber, "fish start to swim downstream towards", catName + ".")
        print(catName, "continues through", forestName + "." )

    if cross_Stream.lower() == ("no"):
        print(catName, "starts to clean themselves but suddenly notices", favoriteNumber, "fish start to swim down the middle of the stream.")
        print(catName, "rushes to the rocks sticking out the water to catch the fish but is to late.")
        print(catName, "jumps to the other side of the stream and continues through", forestName + ".")

    if leave_Truck.lower() == ("yes") and cross_Stream.lower() == ("yes"):
        print("\n After getting sprayed by a skunk and falling into a stream in", forestName, catName, "finally reached", cityName +  ".")
        print(catName, "walks up to a vent blowing hot air to dry off.")
        print(ownerName, "walks past", catName, "and says, I always wanted a", catBreed, "and picks up", catName + ".")
        print(catName, "purrs and returns home with", ownerName + ".")

    if leave_Truck.lower() == ("no") and cross_Stream.lower() == ("no"):
        print("\nAfter escaping", forestName, catName, "finally reached", cityName + "." )
        print(catName, "runs past a vent blowing hot almost hitting", ownerName, "in the legs.")
        print(ownerName, "says “hey, I’m walking here!” And", catName, "runs down an alley and starts eating food out of the trash.")

    if leave_Truck.lower() == ("yes") and cross_Stream.lower() == ("no"):
        print("\nAfter getting sprayed by a skunk", catName, "finally reached", cityName + ".")
        print(catName, "walks up to a vent blowing hot air to dry off.")
        print(ownerName, "walks past", catName, "and says “That cat stinks”.")
        print(catName, "runs down an alley and starts eating food out of the trash.")

    if leave_Truck.lower() == ("no") and cross_Stream.lower() == ("yes"):
        print("\nAfter falling into a stream in", forestName, catName, "finally reached", cityName + ".")
        print(catName, "walks up to a vent blowing hot air to dry off.")
        print(ownerName, "walks past", catName, "and says 'I always wanted a", catBreed, "'" , "and picks up", catName)
        print(catName, "purrs and returns home with", ownerName + ".")
    keepPlaying = input("\nDo you want to play again? Enter yes or no:     ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
            keepPlaying = input("Please enter yes or no:    ")

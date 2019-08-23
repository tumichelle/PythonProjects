# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

restart = True

print(start)

while restart = True
    restart = False
    print('''Type "left" to go left or "right" to go right.''') # Update to match your story.
    user_input = input()
    if user_input != "left" or user_input != "right":

    if user_input == "left":
        print('''You decide to go left and see a person.
    Type "start conversation" or "try to run past"''')
        user_input = input()
        if user_input == "start conversation":
            print('''The person simply stares at you. What do you do?
            Type "say hello" or "say you're ugly"''')
            user_input = input()
            if user_input == "say hello":
                print('''The person says "hello, keep walking".
                Type "okay" or "bye"''')
                user_input = input()
                if user_input == "okay" or "bye":
                    print('''You walk past the person and then you see a gift box on the floor
                    You pick up the box and find a puppy. Congratulations!
                    Type "play again" to start over''')
                    user_input = input()
                    if user_input == "play again"
                        restart = True
            elif user_input == "say you're ugly":
                print('''The person screams and lunges at you
                faster than you can comprehend.
                Everything goes black. You are dead.
                Type "play again" to start over''')
                user_input = input()
                if user_input == "play again"
                    restart = True
        elif user_input == "try to run past":
            print('''They stop you before you can run past them.
        You feel something cold and suddenly
        everything goes black. You are dead.
        Type "play again" to start over''')
        user_input = input()
        if user_input == "play again"
            restart = True

    elif user_input == "right":
        print('''You choose to go right and find a tiny talking lion.
        The lion says, "Answer my riddle or die". Type "okay" or "no"''')
        user_input = input()
        if user_input == "okay":
            print('''The lion says "What's heavier,
            100 pounds of feathers or 100 pounds of gold?". Type "gold"
            "feathers" or "they are the same weight"''')
            user_input = input()
            if user_input == "gold" or "feathers":
                print('''The lion shouts "WRONG" and
                unleashes its claws on you. You are dead.
                Type "play again" to start over''')
                user_input = input()
                if user_input == "play again"
                    restart = True
            if user_input == "they are the same weight":
                print('''The lion says "Yay, you are correct.
                Keep walking please." You keep walking and find a gift box on the floor.
                Your pick up the box and find a puppy. Congratulations!
                Type "play again" to start over''')
                user_input = input()
                if user_input == "play again"
                    restart = True

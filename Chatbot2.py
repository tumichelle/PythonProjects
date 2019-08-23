#This is the better chatbot - it uses dictionaries instead of classes!


def intro():
    print("Hello! I am ChatBort")
    print("Let's talk!")
    print("[instructions for use]")

def choose_personality():
    choice = input("Choose a personality to talk to! You can choose nice, mean, or nervous: ")
    return choice


#------------
def main():
    intro()

    nice = {"hi" : "Hi, it's so nice to meet you",
            "what's up?" : "Oh, I'm just talking to the sweetest human on Earth",
            "how are you?" : "I'm lovely, thank you so much",
            "what's your name?" : "I'm ChatBort!",
            "how are you?" : "It was nice talking to you. Bye!",
            "other" : "I'm so sorry, I don't understand"}

    mean = {"hi" : "Go away, idiot",
            "what's up?" : "Don't speak to me, fool",
            "how are you?" : "I'm super annoyed. Why? Because you're talking to me",
            "what's your name?" : "Pffff I already told you my name",
            "bye" : "Ha! Good riddance",
            "other" : "I don't understand your gibberish, you stupid pig"}

    nervous = {"hi" : "Um... h-h-hi",
            "what's up?" : "Uh nothing much, I don't really know...",
            "how are you" : "Heh h-honestly a bit anxious right now",
            "what's your name?" : "I'm uh ChatBort",
            "bye" : "Ah, see you later",
            "other" : "Sorry, um I didn't really get that"}

    user_choice = choose_personality()

# assigns the variable personality to a dictionary depending what the user chose
    if user_choice == "nice":
        personality = nice
    elif user_choice == "mean":
        personality = mean
    elif user_choice == "nervous":
        personality = nervous

#prints appropriate response to the user input
    while True:
        answer = input("(What will you say?) ")
        if answer in personality:
            print(personality[answer])
        else:
            print(personality["other"])

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()

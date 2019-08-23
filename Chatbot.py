#choose a personality
#make a personality an object
#setup the personality
#use the personality

class Personality:
    hi_response = ""
    whats_up_response = ""
    how_response = ""
    other_response = ""

    def process_input(self, response):
        if response == "hi":
            print(self.hi_response)
        elif response == "what's up?":
            print(self.whats_up_response)
        elif response == "how are you?":
            print(self.how_response)
        elif response == "what's your name?":
            print(self.name_response)
        elif response == "bye"
            print(self.bye_response)
        else:
            print(self.other_response)

def intro():
    print("Hello! I am ChatBort")
    print("Let's talk!")
    print("[instructions for use]")

def choose_personality():
    choice = input("Choose a personality to talk to! You can choose nice, mean, or nervous: ")
    return choice

def main():
    intro()
    user_choice = choose_personality()

    nice_robot = Personality()
    nice_robot.hi_response = "Hi, it's so nice to meet you"
    nice_robot.whats_up_response = "Oh, I'm just talking to the sweetest human on Earth"
    nice_robot.how_response = "I'm lovely, thank you so much"
    nice_robot.name_response = "I'm ChatBort!"
    nice_robot.bye_response = "It was nice talking to you. Bye!"
    nice_robot.other_response = "I'm so sorry, I don't understand"

    mean_robot = Personality()
    mean_robot.hi_response = "Go away, idiot"
    mean_robot.whats_up_response = "Don't speak to me, fool"
    mean_robot.how_response = "I'm super annoyed. Why? Because you're talking to me"
    mean_robot.name_response = "Pffff I already told you my name"
    mean_robot.bye_response = "Ha! Good riddance"
    mean_robot.other_response = "I don't understand your gibberish, you stupid pig"

    nervous_robot = Personality()
    nervous_robot.hi_response = "Um... h-h-hi"
    nervous_robot.whats_up_response = "Uh nothing much, I don't really know..."
    nervous_robot.how_response = "Heh h-honestly a bit anxious right now"
    nervous_robot.name_response = "I'm uh ChatBort"
    nervous_robot.bye_response = "Ah, see you later"
    nervous_robot.other_response = "Sorry, um I didn't really get that"

    while True:
        answer = input("(What will you say?) ")
        if (user_choice == "nice"):
            nice_robot.process_input(answer)
        elif (user_choice == "mean"):
            mean_robot.process_input(answer)
        elif (user_choice == "nervous"):
            nervous_robot.process_input(answer)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()

import random
start = '''Welcome to the random haiku generator!
Type "generate" for a haiku.
Type "stop" to stop the program'''
print(start)

fiveone = ["Welcome! Keep reading",
"Hi! Nice to meet you",
"The sun in the sky",
"What is life? It's death"]

seven = ["This is an awesome haiku",
"Leaves falling from trees each Spring",
"How do you end a haiku?",
"Everybody is special"]

fivetwo = ["This is now the end",
"Refrigerator",
"Bye! See you later",
"This was so easy to code"]

user_input = input()

if user_input == "generate" and user_input != "stop":
    print(random.choice(fiveone))
    print(random.choice(seven))
    print(random.choice(fivetwo))

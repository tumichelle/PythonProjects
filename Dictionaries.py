hair_colors = ["Brown", "Blue", "Red", "Blonde", "Black", "Purple"]

print(hair_colors[2])

people = ["Bob Ross", "Kendra", "Liv", "Taylor Swift", "Lil Nas X", "Kat"]

print(people[1] + " has: " + hair_colors[1] + " hair.")

#a dictionary is a list of pairs connected with a colon

people_and_colors = {"Bob Ross" : "Brown", "Kendra" : "Blue", "Liv" : "Red",
                     "Taylor Swift" : "Blonde", "Lil Nas X" : "Black",
                     "Kat" : ["Purple", "Blue"]}

#Bob Ross and Brown are associated
#Bob Ross is the key, and Brown is the value
#order matters in a dictionary


print("Bob Ross has: " + people_and_colors["Bob Ross"] + " hair.")

name = "Lil Nas X"

print(name + " has: " + people_and_colors[name] + " hair")

print(people_and_colors["Kat"][1])

print(list(people_and_colors.keys()[3]))

print("Katy Perry" in people_and_colors)
#you can only look for keys like this
print("Brown" in people_and_colors.values)
#you can look for values like this
#more than one key can have the same values
#one key cannot have more than one value unless you make a list


people_and_colors.update({"Ed Sheeran" : "Red"})
#to add stuff to dictionary

people_and_colors.pop("Ed Sheeran")
#to take away stuff from the dictionary

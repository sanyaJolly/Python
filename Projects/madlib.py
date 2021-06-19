adjectives=[]
x=0
while(x<2):
    x+=1
    adjective=input("enter an adjective: ")
    adjectives.append(adjective)

typeOfBird=input("enter a type of bird: ")
roomInAHouse=input("enter a room in a house: ")
verbPastTense=input("enter a verb-past tense: ")
verb=input("enter a verb: ")
relativeName=input("enter a relative's name: ")

nouns=[]
for i in range(2):
    noun=input("enter a noun: ")
    nouns.append(noun)

aLiquid=input("enter a liquid: ")
verbIng=[]
t=0
while(t<2):
    verbInIng=input("enter a verb in 'ing' form: ")
    verbIng.append(verbInIng)
    t+=1

partBodyPlural=input("enter a part of the body-plural: ")
pluralNoun=input("enter a plural noun: ")
print(f'It was a {adjectives[0]}, cold November day. I woke up to the {adjectives[1]} smell of {typeOfBird} roasting in the {roomInAHouse} downstairs. I {verbPastTense} down the stairs to see if I could help {verb} the dinner. My mom said, "See if {relativeName} needs a fresh {nouns[0]}." So I carried a tray of glasses full of {aLiquid} into the {verbIng[0]} room. When I got there,I could not believe my {partBodyPlural}! There were {pluralNoun} {verbIng[1]} on the {nouns[1]}!')

electronic_points = 0
pop_points = 0
alt_points = 0
rap_points = 0
randb_points = 0

print("hey..this is a quiz on what genre of music that i listen to that i think you would like!")
input()
answer1 = input("do you like A upbeat music, B mellow/soft music, or C energetic music? ")
if answer1 == "A":
    pop_points += 1
elif answer1 == "B":
    alt_points += 1
    randb_points += 1
elif answer1 == "C":
    electronic_points += 1
    rap_points += 1

answer2 = input("do you like A rainy days, B sunny days, or C cloudy days? ")
if answer2 == "A":
    alt_points += 1
elif answer2 == "B":
    pop_points += 1
    randb_points += 1
elif answer2 == "C":
    electronic_points += 1
    rap_points = 1
    alt_points = 1

answer3 = input("do you like A fast music, or B slow music? ")
if answer3 == "A":
    electronic_points += 1
    rap_points += 1
    pop_points += 1
elif answer3 == "B":
    randb_points += 1
    alt_points += 1

answer4 = input("almost finished, would you prefer A hanging out with friends, B reading a book and looking scarily mysterious, or C going to a nightclub? ")
if answer4 == "A":
    pop_points += 1
    randb_points += 1
elif answer4 == "B":
    alt_points += 1
elif answer4 == "C":
    electronic_points += 1
    rap_points += 1
answer5 = input("lastly, where would you rather live? A mountains, B beach, or C city? ")
if answer5 == "A":
    alt_points += 1
    randb_points += 1
elif answer5 == "B":
    pop_points += 1
    electronic_points += 1
elif answer5 == "C":
    rap_points += 1
    electronic_points += 1

print("that was great! are you ready for results?")
input()
if electronic_points > pop_points and electronic_points > alt_points and electronic_points > rap_points and electronic_points > randb_points:
    print("you would probably like electronic music! some electronic artists that i like are aphex twin, crystal castles, and daft punk!")
elif pop_points > electronic_points and pop_points > alt_points and pop_points > rap_points and pop_points > randb_points:
    print("you would probably like pop music! some pop artists i like are pinkpantheress and lady gaga!")
elif alt_points > electronic_points and alt_points > pop_points and alt_points > rap_points and alt_points > randb_points:
    print("you would probably like alt pop! some alt pop artists i like are lana del rey, clairo, and lorde!")
elif rap_points > electronic_points and rap_points > pop_points and rap_points > alt_points and rap_points > randb_points:
    print("you would probably like rap music! some rap artists i enjoy are a$ap rocky and travis scott!")
elif randb_points > electronic_points and randb_points > pop_points and randb_points > alt_points and randb_points > rap_points:
    print("you would probably like r&b music! some r&b artists that i enjoy are sza and the weeknd!")
input()
print("great job!")
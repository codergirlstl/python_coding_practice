season = "Fall"

print(season)

for x in range(len(season)):
    print(season[x])

subseason = "all"
if subseason in season:
    print("That is a substring of Fall")
if subseason not in season:
    print("That is not a substring of Fall")

user_answer = input("What is your favorite season?")

if user_answer in season:
    print("That is a substring of Fall")
if user_answer not in season:
    print("That is not a substring of Fall")

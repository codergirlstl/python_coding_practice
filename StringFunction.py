def substring_check(myseason, yourseason):
    season1 = str(myseason)
    season2 = str(yourseason)
    if season1 in season2:
        answer = "True"
    if season1 not in season2:
        answer = "False"
    return answer

myseason = ("My favorite season is Summer.")

yourseason = input("What is your favorite season")

substring_check(myseason, yourseason)

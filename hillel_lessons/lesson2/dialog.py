import datetime
now = datetime.datetime.now()
name = input("Привет меня зовут Николай, а тебя как?\n")
age = int(input("Сколько тебе лет, "+name+"?\n"))
print("Значит ты родился в "+str(now.year - age)+" году.", end=' ')
print("Замечательное было время!")

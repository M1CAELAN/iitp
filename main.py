from random import randint
print("вы хотите бросить д20, д10, д8, д6 ил д4?")
a = input()
if a == "д20":
    print(randint(1, 20))
elif a == "д10":
    print(randint(1, 10))
elif a == "д8":
    print(randint(1, 8))
elif a == "д6":
    print(randint(1, 6))
elif a == "д4":
    print(randint(1, 4))
else:
    print("правильно вводи, а не это ваше")
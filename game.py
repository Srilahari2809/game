import random
print("Enter your name: ")
name = input()
print("Hi", name,"let's start the game")
digits = list(range(10))
random.shuffle(digits)
if digits[0] == 0:
    digits[0], digits[1] = digits[1], digits[0]
num = digits[0] * 100 + digits[1] * 10 + digits[2]


sn = str(num)
print("You have 8 chances to guess the correct number")
for i in range (8):
    count = 0
    sum = 0
    print("chance no:",i+1)
    c = input()
    if(c == sn):
        print('Congrats you cracked it')
        break
    else:
        if sn[0] == c[0]:
            count+=1
        if sn[1] == c[1]:
            count+=1
        if sn[2] == c[2]:
            count+=1
        if count == 1:
            print('1 bull')
        elif count > 1:
            print(count, 'bulls')
        else:
            print('No bulls')
        if sn[0] == c[0] or sn[0] == c[1] or sn[0] == c[2]:
            sum+=1
        if sn[1] == c[0] or sn[1] == c[1] or sn[1] == c[2]:
            sum+=1
        if sn[2] == c[0] or sn[2] == c[1] or sn[2] == c[2]:
            sum+=1
        if sum == 1:
            print('1 cow')
        elif sum > 1:
            print(sum, 'cows')
        else:
            print('No cows')
else:
    print("Oops you lost\nBetter luck next time\nThe correct number is:",num)
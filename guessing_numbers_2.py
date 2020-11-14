
min = 0
max = 1000
# checking is a number is integer
try:
    user_number = int(input("Give me the number i range 1-1000 and i I will guess it in max. 10 steps : "))
    test=0
    while True:

        if test < 10:
            guess = int((max - min) / 2) + min
            print(f"({test+1})Guessing :{guess}")
            answer_1= input("for to big press 'TB', to small 'TS', if I guessed pres 'G': ")
            if answer_1 == 'G' or answer_1 == 'g':
                print("I win !!")
                break
            elif answer_1 == 'TB' or answer_1 == 'tb':
                max = guess
                test += 1
            elif answer_1 == 'TS' or answer_1 == 'ts':
                min = guess
                test += 1
            else:
                print("Don't cheat me")
                break
        else:
            print("Don't cheat me !!")
            break
except ValueError:
    print("It's not a number. Give me integer !")

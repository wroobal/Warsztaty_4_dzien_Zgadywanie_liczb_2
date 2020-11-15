
min = 0
max = 1000
# checking is a number is integer
try:
    user_number = int(input("Give me the number i range 1-1000 and i I will guess it in max. 10 steps : "))
    test = 0    # constant for counting number of lops
    while True:
        if test < 10:
            guess = int((max - min) / 2) + min
            print(f"({test+1})Guessing :{guess}")
            # taking information to next loop
            answer_1= input("for to big press 'TB', to small 'TS', if I guessed pres 'G': ")
            # verifying is the correct number, if yes press 'G' or 'g'
            if answer_1 == 'G' or answer_1 == 'g':
                print("I win !!")
                break
            # if it's to big press 'TB' or 'tb'
            elif answer_1 == 'TB' or answer_1 == 'tb':
                max = guess
                test += 1
            # if it's to small press 'TS' ot 'ts'
            elif answer_1 == 'TS' or answer_1 == 'ts':
                min = guess
                test += 1
            # if loops was more than 10, someone cheated
            else:
                print("Don't cheat me")
                break
        else:
            print("Don't cheat me !!")
            break
except ValueError:
    print("It's not a number. Give me integer !")

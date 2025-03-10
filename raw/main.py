import random
from collections import Counter

allNames = '''abirami anbarasu anusiya boobesh darshankrishnakumar darshwana deepika devdharsan dhanuja dharani dharsan dhayalini gopikashri gowtham gowthaman hareini harikishore harish hayagirivan hemaprakash jayadharshini karthikraja kishore kowsigashri madhavan manjari manjuparkavi marikarkuvelraj mathavan mohammedthanseem moniha monish nihash nisanth nithish nivethika parthiban praveen priyadharshini rejinavinnarasi sabinaparveen sanjayraj sanjay sanjeev saran sathyasri shanmugapriya sivanesh sivikshaa sowmiya sridharshan subishclarie sujith surya tharaneesh tharanitharan tulsidevi vimalraj vishnukarthik vishnukumar viswanathan yasvand yogeshkanna devadharshini dhanasekar harish naveenkumar vasanth'''

allNames = allNames.split(' ')

name = random.choice(allNames)

if __name__ == '__main__':
    print("Guess the Name of your classmate!!!!")

    for i in name:
        print('_',end=' ')
    print()

    playing = True

    letterGuessed = ''
    chances = len(name)+2
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:
            print()
            chances -=1

            try:
                guess = str(input('Enter the letter to guess:'))
            except:
                print('Enter only a letter!!!!')
                continue
            if not guess.isalpha():
                print('Enter only a letter')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE LETTER')
            elif guess in letterGuessed:
                print('you have already guessed that letter')
                continue

            if guess in name:
                k = name.count(guess)

                for _ in range(k):

                     letterGuessed += guess


            for char in name:

                if char in letterGuessed and (Counter(letterGuessed) != Counter(name)):
                        print(char, end=' ')

                        correct += 1

                elif (Counter(letterGuessed) == Counter(name)):

                    print("The Name is: ",end=' ')
                    print(name)

                    flag = 1

                    print("Congratulations, you Won")

                    break
                    break
                else:
                    print('_',end=' ')


        if chances <= 0 and (Counter(letterGuessed) != Counter(name)):
            print()
            print("Ohhhhh You Lost! Try Again.....")
            print()
            print('The Name Was {}'.format(name))

    except KeyboardInterrupt:
        print()
        print('Try Again.')
        exit()



                        

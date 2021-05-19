from questions import QUESTIONS
import random

def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    correct = question["answer"]
    return True if answer == correct else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    count = 2
    temp = 1
    while(count):
      if ques["answer"] != temp:
          choice = "option" + str(temp)
          ques[choice] = ""
          count -= 1
          temp = int(temp)
      temp += 1    

    return ques   


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print("Welcome to KBC")
    TOTAL = 15
    index = 0
    min_reward = 0
    money = 0
    has_used_lifeLine = False

    while(index < TOTAL):
        if not has_used_lifeLine:
            print("You also have 50-50 lifeline. Type `L` to use it")

        print(f'\tQuestion {index}: {QUESTIONS[index]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[index]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[index]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[index]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[index]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        # check for the input validations
        if(ans == 'quit'):
            print("You have won {}".format(money))
            break

        if ord(ans) not in range(49, 53):
            if ans != 'L':
                print("not a valid answer! please Enter a number b/w 1 to 4")
                continue
            else:        
                if(ans == 'L'):
                  if not has_used_lifeLine and (index != 14):
                    has_used_lifeLine = True
                    question = lifeLine(QUESTIONS[index])
                    print(f'\tQuestion {index}: {question["name"]}' )
                    print(f'\t\tOptions:')
                    print(f'\t\t\tOption 1: {question["option1"]}')
                    print(f'\t\t\tOption 2: {question["option2"]}')
                    print(f'\t\t\tOption 3: {question["option3"]}')
                    print(f'\t\t\tOption 4: {question["option4"]}')
                  elif not has_used_lifeLine and (index == 14):
                    print("You can't use lifeline at this stage!")
                  else:
                    print("You have used your only lifeLine!!!")            
                
                  ans = input('Your choice ( 1-4 ) : ') 

                  if(ans == 'quit'):
                    print("You have won {}".format(money))
                    break

                  try:
                    int(ans)
                  except:
                    print("Invalid Input!!!")
                    continue                   


        if isAnswerCorrect(QUESTIONS[index],int(ans)):
                print('\nCorrect !')
                if(index == 5):
                    min_reward = 10000
                    print("You are now at level 1 and you minimum reward is {}".format(min_reward))
                if(index == 10):    
                    min_reward = 320000  
                    print("You are now at level 2 and you minimum reward is {}".format(min_reward))                       
                money = money + QUESTIONS[index]["money"] 
                print("Total Money won by you is {}".format(money))
                # See if the user has crossed a level, print that if yes

        else:
                # end the game now.
                # also print the correct answer
                print("Correct Answer: {}".format(QUESTIONS[index]["answer"]))
                print('\n Your Incorrect answer!')
                print("You have won {}".format(min_reward))
                break

        index += 1


kbc()

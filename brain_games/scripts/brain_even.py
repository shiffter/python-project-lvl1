from random import randint
import prompt
from brain_games.cli import welcome_user


a = []
diction = {}
name = welcome_user()



def generate_list():
    for i in range(3):
        a.append(randint(1, 100))
    return a
    

def generate_dict():
    for i in a:
        if i % 2 == 0:
            diction[i] = 'yes'
        else:
            diction[i] = 'no'
            
            
def play_games(name):
    print("Answer 'yes' if the number is even, otherwise answer 'no'")
    counter = 0
    for i in a:
        print("Question: " + str(i))
        user_answer = prompt.string("Your answer: ")
        if user_answer == diction[i]:
            print('Correct')
            counter += 1
            if counter == 3:
                print("Congratulations, {}!".format(name))
        else:
            print('Uuups, right answer was {}, try again!'.format(diction[i]))
            break
            
            
def main():
	generate_list()
	generate_dict()
	play_games(name)

            
if __name__ == '__main__':
	main()

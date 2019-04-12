import random

answer_list = [ 'It is certain',
'It is decidedly so',
'Without a doubt',
'Yes definitely',
'You may rely on it',
'As I see it, yes',
'Most likely',
'Outlook good',
'Yes',
'Signs point to yes',
'Reply hazy try again',
'Ask again later',
'Better not tell you now',
'Cannot predict now',
'Concentrate and ask again',
'Do not count on it',
'My reply is no',
'My sources say no',
'Outlook not so good',
'Very doubtful']

def say_answer():
	# pick a random number from 0 to N
	# where N is the length of answer options
	rand_num = random.randint(0,len(answer_list)-1)
	print(answer_list[rand_num])

random.seed() # initialize the random number generator

# what needs to be True for our program to end?
# answer: the user must say they don't have any more questions for the magic 8-ball
has_questions_for_eight_ball = True

while has_questions_for_eight_ball:
	print("Please ask a question.")
	question = input()
	say_answer()
	yes_no = input("Do you have another question for the Magic 8-Ball? (y/n)")
	if str.lower(yes_no) == 'n':
		has_questions_for_eight_ball = False

print("Thank you for playing!")

# generating random quiz program 
import random 
# sacing a dic. of the state and their capital
# you can use this program to generate any mcq test 
# but first you should make a dictionary of your questions as keys and answers as value of the dictionary 
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# generate 35 forms with 50 questions 
# also answer key for each form 
for i in range(35): 
    # opening files to write questions and answers 
    QuizFile = open('QuizFile %s' %(i+1), 'w' )
    AnswerKey = open('AnswerKey %s' %(i+1), 'w')
    # writing header of the form and answer key 
    QuizFile.write('name:\n\n'+'date:\n\n'+'period:\n\n')
    QuizFile.write(' '*20 + 'capital quiz form %s' %(i+1))
    QuizFile.write('\n\n')
    AnswerKey.write('answers for form %s \n '%(i+1))
    z= list(capitals.keys())
    # shuffleing list of states ot add it to the questions in a random way 
    random.shuffle(z)
    for i in range(50):
        # adding 50 questions  
        QuizFile.write('\t' + str(i+1)+'.'+'the capital of '+ str(z[i]) + ' is :\n')
        # arranging answers
        correct_answer = capitals[z[i]]
        wrong_answer = list(capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_options = random.sample(wrong_answer,3)
        options = [correct_answer] + wrong_options 
        # shuffling options 
        random.shuffle(options)
        AnswerKey.write(str(i+1) + '.' + correct_answer+ '\n')
         
        for i in range(0,4): 
            QuizFile.write(('ABCD'[i] + '.' + options[i] + '\n'))
            
    QuizFile.close()
    AnswerKey.close() 

# you can change number of forms and number of questions 
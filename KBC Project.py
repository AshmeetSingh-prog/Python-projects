# this is KBC programme
# work on 50 : 50 life line by removing any two elements of list in in OPTIONS
#  use vip for VIP person if their any answer is wrong
# press ENter time by Time 
def hintcorrect():
    global money
    if answer == correct_answer:
        print("Correct!",)
        print ('CONGRATULATION you won' ,money, 'rupees')
        print ()
        print ('------------------')
        print ()
        money = money * 2
                        

QUESTIONS = [
    ("Who was the first Prime Minister of India?", "c"),
    ("Who is the first citizen of India?", "a"),
    ("How many days a February month have in the leap year?", "d"),
    ("Which is the tallest mountain in the world?", "c"),
    ("Name the hardest substance available on Earth?", "b"),
    ("Name a natural satellite of Earth?", "a"),
    ("Who is known as the Father of our Nation?", "d"),
    ("Name the first man to walk on the Moon?", "b"),
    ("Name the densest jungle in the world?", "a"),
    ("Which is the National Aquatic Animal of India?", "c"),
     ]

OPTIONS = [ 
           ['a : Motilal Nehru ','b : Indhra Gandhi','c : Pandit Jawaharlal Nehru ','d : Dr. BR Ambedkar'],
           ['a : President Of India ','b : Prime Minister Of India ','c : MLA ','d : MP '],
           ['a : 28 days ','b : 27 days','c : 30 days','d : 29 days '],
           ['a : Himalayas ','b : Anna purna ','c : Mount Everest','d : Dhaula Giri '],
           ['a : Boron ','b : Diamond ','c : Steel ','d : Concrete'],
           ['a : Moon ','b : Mangalyan ','c : Chandrayan ','d : None '],
           ['a : Dr. Rajendra Prasad ','b : Subash Chandra Bose','c : ','d : Mahatma Gandhi '],
           ['a : John Glen ','b : Neil Amstrong ','c : Sally Ride','d :  Chris Hand Field'],
           ['a : Amazon ','b : Sundarbans ','c : Gir Forest ','d : kanha National Park '],
           ['a : Star Fish ','b : Sea Horse','c : River Dolphin ','d : White Shark'],
           ]
print ('Enter your details : ')
name = input ('Enter your name : ')
name = name.upper()
age = input ('Enter your age : ')
city = input ('In which city do you live : ')
sub = input ('Press ENTER to SUBMIT form  : ')
if sub == '':
    print ()
    print ("FORM SUBMITTED")
    print ()


quesno = 1
money = 1000
inp = input('To start the quiz press enter : ')
if inp == '':
    for (question,correct_answer),option,i in zip(QUESTIONS,OPTIONS,range(quesno,len(QUESTIONS)+1)) :
        print ()
        print ('Your ',i, 'question is for ',money, 'RUPEES')
        inpif = input ()
        if inpif == '':
            print ()
            print (i,question)
            print (option)
            answer = input('Enter your option : ') 
            if answer == correct_answer:
                print("Correct!",)
                print ('CONGRATULATION you won' ,money, 'rupees')
                print ()
                print ('------------------')
                print ()
                money = money * 2
                continue           
            if answer == 'quit'.upper():
                break
            
            # LIFE LINES    
            if answer == 'hint':
                if i == 1 :
                    print ('Hint : Childrens Day which is on 14th November is celebrated on his birth date')
                    answer = input('Enter your option : ')
                    
                    hintcorrect()
                    if answer != correct_answer :
                        print("The answer is ",correct_answer, 'not' , answer)
                        inpi = input('')
                        if inpi == 'vip' :
                            continue
                        else:
                            break        
                    continue
                
                if i == 2:
                    print ('Hint : He is not elected by citizens')
                    answer = input('Enter your option : ')
                    
                    hintcorrect()
                    if answer != correct_answer :
                        print("The answer is ",correct_answer, 'not' , answer)
                        inpi = input('')
                        if inpi == 'vip' :
                            continue
                        else:
                            break        
                    continue
                
                if i == 3:
                    print ('Hint : Normal February month have 28 days \tadd 1 to it')
                    answer = input('Enter your option : ')
                    
                    hintcorrect()
                    if answer != correct_answer :
                        print("The answer is ",correct_answer, 'not' , answer)
                        inpi = input('')
                        if inpi == 'vip' :
                            continue
                        else:
                            break        
                    continue
                
                if i == 4:
                    print ('Hint : It is located between Nepal and China')
                    answer = input('Enter your option : ')
                    
                    hintcorrect()
                    if answer != correct_answer :
                        print("The answer is ",correct_answer, 'not' , answer)
                        inpi = input('')
                        if inpi == 'vip' :
                            continue
                        else:
                            break        
                    continue
                
                if i == 5:
                    print ('Hint : That substance is also very Expensive')
                    answer = input('Enter your option : ')
                    
                    hintcorrect()
                    if answer != correct_answer :
                        print("The answer is ",correct_answer, 'not' , answer)
                        inpi = input('')
                        if inpi == 'vip' :
                            continue
                        else:
                            break        
                    continue  
                  
                if i == 6:
                    print ('Hint : It reflect light from sun to earth')
                    answer = input('Enter your option : ')
                    
                    hintcorrect()
                    if answer != correct_answer :
                        print("The answer is ",correct_answer, 'not' , answer)
                        inpi = input('')
                        if inpi == 'vip' :
                            continue
                        else:
                            break        
                    continue 
                   
                if i == 7:
                    print ('Hint : His picture is also printrd on Indian rupees')
                    answer = input('Enter your option : ')
                    
                    hintcorrect()
                    if answer != correct_answer :
                        print("The answer is ",correct_answer, 'not' , answer)
                        inpi = input('')
                        if inpi == 'vip' :
                            continue
                        else:
                            break        
                    continue  
                  
                if i == 8:
                    print ("Hint : 'REMEMBER' you studied it in junior class")
                    answer = input('Enter your option : ')
                    
                    hintcorrect()
                    if answer != correct_answer :
                        print("The answer is ",correct_answer, 'not' , answer)
                        inpi = input('')
                        if inpi == 'vip' :
                            continue
                        else:
                            break        
                    continue
                    
                if i == 9:
                    print ('Hint : It is also known as the lungs os Earth')
                    answer = input('Enter your option : ')
                    
                    hintcorrect()
                    if answer != correct_answer :
                        print("The answer is ",correct_answer, 'not' , answer)
                        inpi = input('')
                        if inpi == 'vip' :
                            continue
                        else:
                            break        
                    continue 
                   
                if i == 10:
                    print ('Hint : That is an Aquatic Mammel')
                    answer = input('Enter your option : ')
                    
                    hintcorrect()
                    if answer != correct_answer :
                        print("The answer is ",correct_answer, 'not' , answer)
                        inpi = input('')
                        if inpi == 'vip' :
                            continue
                        else:
                            break        
                    continue    
            # if answer is incorrect
            if answer != correct_answer :
                print("The answer is ",correct_answer, 'not' , answer)
                inpi = input('')
                if inpi == 'vip' :
                    continue
                else:
                    break
                
print ('CONGRATULATIONS')
print (name,'won ', money//2 ,'rupees')       
questions=[
   [
        'who was first prime minister of India ?:','Jawaharlal Nehru','Mahatma gandhi','Sardar vallabhbhai patel','Rajendra prasad',1 ],
   [
       "Which is the capital of India?","Delhi","Mumbai","Bangalore","Hyderabad",1],
   [
    "Who is the CEO of Tesla?","Elon Musk","Jeff Bezos","Mark Zuckerberg","Satan Nadella",1],
   ["What is the highest mountain in the world?","Mount Everest","K2","Kangchenjunga","Mauna Kea",2],
   ["Which planet has the most moons?","Venus","Earth","Mars","Pluto"],
   ["What is the largest living species of lizard?","Gila monster","Green anole","Black widow spider","Northwestern skink",3],
   ["Who created Facebook?","Dave McClure","Mark Zuckerberg","Eric Schmidt","The Rock",2],
   ["At what speed does light travel?","299792 km/h","386600 km/h","4215000 km/h","186264 km/h",4],
   ["What is the largest state in the US by area?","Alaska","California","Texas","Montana",2],
   ["Who was the first president of the United States?","George Washington","Thomas Jefferson","James Madison","Abraham Lincoln",1],
   ["What is the smallest country in the world by population?","Vatican City","Monaco","Nauru","Tuvalu",1]
]

levels=[1000,2000,4000,8000,16000,32000,64000,128000,256000,512000,1000000]
i=0
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print('\n\nQuestion:\n',question[0])
    print(f'Question for Rs.{levels[i]}')
    print(f'A.{question[1]}                               B.{question[2]}')
    print(f'C.{question[3]}                               C.{question[4]}')

    reply=int(input('Enter your answere[1-4]: or a quit'))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print(f'Correct ans you have won Rs.{levels[i]}')
    elif(i==4):
        money=16000
    elif(i==8):
        money=512000
    elif(i==11):
        money=1000000
    else:
        print('Wrong answere!')
        break
print(f'finaly you have won {levels[i]}')

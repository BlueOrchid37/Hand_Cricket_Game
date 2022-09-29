#Hand Cricket Project

#Toss Section
import random
toss=["Head","Tail"]
comChoice=["Batting","Bowling"]
playScore=[0,1,2,3,4,5,6]
score=0
comSumScore=0
sumScore = 0
bowlScore = 0

playOrNot=int(input('''
Play Hand Cricket?
1 Yes
2 No
'''))
print("You select: ", playOrNot)
if playOrNot==1:
    tossChoiceByUser=int(input('''
    1 Head
    2 Tail
    '''))
    comTossHT=random.choice(toss)
    print(comTossHT)
    if (tossChoiceByUser==1 and comTossHT=="Head") or (tossChoiceByUser==2 and comTossHT=="Tail"):
        print("You won the toss!")
        
        #Match Starts

        tossChoice=int(input('''
        1. Batting
        2. Bowling
        
        '''))   
        if tossChoice==1:
            print("You chose Batting!")
            score=int(input("Enter score: "))
            comScore=random.choice(playScore)
            
            while score!=comScore:
                sumScore=sumScore+score
                score=int(input("Enter Run: "))
                comScore=random.choice(playScore)
            print("Out!")
            print("Total Run: ", sumScore)
            print("Target: ", sumScore + 1)
            while bowlScore!=comScore and comSumScore<=sumScore:
                comSumScore=comSumScore+bowlScore
                bowlScore=int(input("Enter Bowl: "))
                comScore=random.choice(playScore)
                print(comScore) #1
            if (bowlScore==comScore):
                print("Computer Out!")
            print("Total Run: ", comSumScore)         
            if sumScore>comSumScore:
                print("You won!")
            elif comSumScore>sumScore:
                print("Computer won!")
            else:
                print("Match draw!!")
            
            

        elif tossChoice==2:
            print("You chose to Bowling!")
            bowlScore=int(input("Enter Bowl: "))
            comScore=random.choice(playScore)
            print("Computer Run:", comScore)
            while bowlScore!=comScore:
                comSumScore=comSumScore+bowlScore
                bowlScore=int(input("Enter Bowl: "))
                comScore=random.choice(playScore)
                print("Computer Run: ", comScore)
            print("Computer Out!")
            print("Total Run: ", comSumScore)
            print("Target: ", comSumScore + 1)
            score=int(input("Enter Run: "))
            comScore=random.choice(playScore)
            while score!=comScore and sumScore<=comSumScore:
                sumScore=sumScore+score
                score=int(input("Enter Run: "))
                comScore=random.choice(playScore)
            if (score==comScore):
                print("Out!")
            print("Total Run: ", sumScore)
            if sumScore>comSumScore:
                print("You won!")
            elif comSumScore>sumScore:
                print("Computer won!")
            else:
                print("Match draw!!")
            
            
            
            
        else:
            print("Invalid Input! Match dismissed!!")
        
    else:
        print("Computer won the toss!")
        comToss=random.choice(comChoice)
        comScore=random.choice(playScore)
        if comToss==comChoice[0]:
            print("Computer chose Batting!")
            bowlScore=int(input("Enter Bowl: "))
            comScore=random.choice(playScore)
            print("Computer Run: ", comScore)
            while bowlScore!=comScore:
                comSumScore=comSumScore+bowlScore
                bowlScore=int(input("Enter Bowl: "))
                comScore=random.choice(playScore)
                print("Computer Run: ", comScore)
                print(comScore)
            print("Computer Out!")
            print("Computer Total Run: ", comSumScore)
            print("Target: ", comSumScore + 1)
            score = int(input("Enter Run: "))
            comScore = random.choice(playScore)
            while score!=comScore and sumScore<=comSumScore:
                sumScore=sumScore+score
                score=int(input("Enter Run: "))
                comScore=random.choice(playScore)
            if (score==comScore):
                print("Out!")
            print("Your Total Run: ", sumScore)
            if sumScore>comSumScore:
                print("You won!")
            elif comSumScore>sumScore:
                print("Computer won!")
            else:
                print("Match draw!!")
            
            
            
            
        elif comToss==comChoice[1]:
            print("Computer chose Bowling!")
            score=int(input("Enter Run: "))
            comScore=random.choice(playScore)
            while score!=comScore:
                sumScore=sumScore+score
                score=int(input("Enter Run: "))
                comScore=random.choice(playScore)
            print("Out!")
            print("Your Total Run: ", sumScore)
            print("Target: ", sumScore + 1)
            bowlScore = int(input("Enter Bowl: "))
            comScore = random.choice(playScore)
            print("Computer Run: ", comScore)
            while bowlScore!=comScore and comSumScore<=sumScore:
                comSumScore=comSumScore+bowlScore
                bowlScore=int(input("Enter Bowl: "))
                comScore=random.choice(playScore)
                print("Computer Run: ", comScore)
            if (bowlScore==comScore):
                print("Computer Out!")
            print("Computer Total Run: ", comSumScore)
            if sumScore>comSumScore:
                print("You won!")
            elif comSumScore>sumScore:
                print("Computer won!")
            else:
                print("Match draw!!")
            
            
    
else:
    print("Exit")





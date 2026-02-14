import random

def players(n):
    play=[]
    for i in range(0,n):
        player1 = list(map(int, input(f"Player-{i+1}: Enter 5 numbers (1 to 10)  ").split()))
        play.append(player1)
    return play
        
    


while True:
    

   
    n=int(input("enter the number of players wants to play"))
    play=players(n)

    
    random_numbers = random.sample(range(1, 10), 5)
    print("\nRandom numbers are:", random_numbers)

    print("Check the numbers are matching or not")
    l=[]
    for i in range(len(play)):
        flag=0
        for j in range(0,5):
            if play[i][j] in random_numbers:  
              flag=flag+1
        l.append(flag)
   
    print("Do you want me to show the winner?")
    winner= input("Enter 'yes' to see the winner: ")
    if winner.lower() == 'yes':
       for i in l:
            if i==5:
             print("Player",l.index(i)+1,"is the winner")
             
            else:
                print("Player",l.index(i)+1,"is not the winner")
                
                
        
    n=input("Do you want to play again")
    if n!='yes':
        print("thanks for playing")
        break
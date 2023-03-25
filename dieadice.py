import random

print("Kaç tane zar atmak istersin?")

while True:
    try:
        numberpicked= int(input("1 ile 10 arası bir sayı girin.\n"))
        if(numberpicked>0 and numberpicked < 10):
          break
        else:
          print("yanlış sayı girdiniz")
    except:
        print("Lütfen sayı giriniz.")
        
                
def rolladice(amountofdice):
    totalSum= 0 
    possiblefaces= [1,2,3,4,5,6]
    for die in range(amountofdice):
        roll = random.choice(possiblefaces)
        print("Die" , die+1 , ":", roll )
        totalSum += roll
        average = totalSum/amountofdice
    print("Total sum: ", totalSum)
    print("Average roll: ", average)
    
            
rolladice(numberpicked)           
            
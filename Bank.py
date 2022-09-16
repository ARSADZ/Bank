# Muhammad Falihul Abad Arsyil Adzim Karim / 220535603278 / Teknik Informatika B

greet=input("What's your greeting : ").lower().strip()
x = greet.split(',')

if(greet=='hello'):
    money=0
elif(x[0]=='hello'):
    money=0
elif(greet[0]=='h'):
    money=20
else :
    money=100

print ('$',money)
import random
d=1
array =["rock","paper","scissors"]
class rps:
    def ran(self):
        n=random.randint(0, 2)
        a = array[n]
        return a
while d:
    data = input("rock, paper, scissors ")
    b = rps()
    if (b.ran() == data):
        print('you make it')
    else:
        print('ne munji daaa myre aaa')
    
    d = input("press 0 to stop")
    if(d == 0):
        break
import random

skolko = int(input("How many proxies to generate?: "))
port = int(input("Port proxy: ")) 
f1 = open("proxy generate " + str(skolko) +".txt", 'w')

for i in range(0, skolko):
    chisloone = random.randint(1, 255)
    chislotwo = random.randint(1, 255)
    chislotree = random.randint(1, 255)
    chislofour = random.randint(1, 255)
    
    f1.write(str(chisloone) + "." + str(chislotwo) + "." + str(chislotree) + "." + str(chislofour) + ":" + str(port) + "\n")

print("Pedras de um dominó sem repetição")
for domino1 in range(0,6+1,1):
    for domino2 in range(domino1,6+1,1):
        print(domino1,"-",domino2)
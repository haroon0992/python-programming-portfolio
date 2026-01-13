#while loop program
orders = ['wedding cakes', 'birthday cakes']

finished_cakes = []

while orders:
    current_cakes= orders.pop()
    print ("im preparing your " + current_cakes )
    finished_cakes.append(current_cakes)
print ("\n")
for cakes in finished_cakes:
    print("i made a "+ cakes )
    
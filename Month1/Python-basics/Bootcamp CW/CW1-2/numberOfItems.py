clients= []

for i in range(5):
    name = input("Enter client name: ")
    clients.append(clients[i])
print("Number of clients: ", len(clients))
print("First client: ", clients[0])
print("Last client: ", clients[-1])
names = []
lastnames = []
contact_numbers = []
num = int(input("Enter the total number of contacts you want to save: "))
for i in range(num):
    name = input("Name: ")
    lastname = input("lastname: ")
    contact_number = int(input("Contact Number: ")) 
    names.append(name)
    lastnames.append(lastname)
    contact_numbers.append(contact_number)
print("\nName\t\t\tLast name\t\t\tContact number\t\t\t")
for i in range(num):
    print("{}\t\t\t{}\t\t\t\t\t{}".format(names[i],lastnames[i], contact_numbers[i]))

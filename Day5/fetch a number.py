with open("phone_number.txt", "r") as file:
    data = file.readlines()
    for line in data:
        phone_number = line.split()
        for number in phone_number:
            if len(number) == 10:
                print(number)




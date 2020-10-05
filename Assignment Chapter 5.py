num_list = []
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    else:
        try:
            number = int(number)
            num_list.append(number)
        except:
            print("Invalid input")

print("Maximum is", max(num_list))
print("Minimum is", min(num_list))
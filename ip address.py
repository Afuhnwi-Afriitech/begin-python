ip_address = (input("Enter your ip address: "))


fullstop = 0
for j in range(0, len(ip_address)):
    if ip_address[j] in '.':
        fullstop += 1
if (fullstop < 1) or (fullstop > 4):
    print("Enter a valid ip address")
else:
    for number in ip_address:
        if number in '1234567890':
            print(number, end="")
    numberOfSymbols = ''
    for symbol in range(0, len(ip_address)):
        if ip_address[symbol] in '.':
            numberOfSymbols += ip_address[symbol]

    print("")
    print("Your ip address has {} segments".format(len(numberOfSymbols) + 1))

    # alternative solution
    length = 0
    segment = 1
    for i in range(0, len(ip_address)):
        if ip_address[i] in '.':
            segment += 1
        if ip_address[i] in '1234567890':
            length += 1

    print("The ip address you entered has {} segments".format(segment))
    print("Your ip address has {} numbers".format(length))

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        ival= int(num)
    except:
        print('Invalid input')

    if ival > largest:
            largest = ival

    if smallest is None:
        smallest = ival
    elif ival < smallest:
        smallest = ival


print("Maximum is", largest)
print("Minimum is", smallest)

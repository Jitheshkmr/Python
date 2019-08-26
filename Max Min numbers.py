largest = None
smallest = None
while True:
    num = input("Enter a number(enter done to exit): ")
    if num == "done": 
        break
    try:
        num_cast=int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest=num_cast
    if smallest is None:
        smallest=num_cast
    if num_cast>largest:
        largest=num_cast
    if num_cast<smallest:
            smallest=num_cast
print("Maximum is", largest)
print("Minimum is",smallest)
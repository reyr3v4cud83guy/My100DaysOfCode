def control_structures():
    # Define variables
    x = 10
    y = 5

    # Demonstrate if-else statement
    if x > y:  
        print(f"{x} is greater than {y}")
    elif x == y:
        print(f"{x} is equal to {y}")
    else:
        print(f"{x} is less than {y}")

    # Demonstrate for loop
    print("\nFor Loop:")
    for i in range(5):
        print(i)

    # Demonstrate while loop
    print("\nWhile Loop:")
    i = 0
    while i < 5:
        print(i)
        i += 1

    # Demonstrate nested if-else statement
    print("\nNested If-Else Statement:")
    if x > y:  
        if x > 10:
            print(f"{x} is greater than 10")
        else:
            print(f"{x} is less than or equal to 10")
    else:
        print(f"{x} is less than or equal to {y}")

    # Demonstrate break and continue statements
    print("\nBreak and Continue Statements:")
    for i in range(5):
        if i == 3:
            break
        print(i)

    print("\nContinue Statement:")
    for i in range(5):
        if i == 3:
            continue
        print(i)

control_structures()


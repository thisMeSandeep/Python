let = str(input('Enter first letter of the day'))

match let.strip():
    case 's':
        print("sunday")
    case 'm':
        print("monday")
    case 't':
        print("tuesday")
    case 'w':
        print("wednesday")
    case 't':
        print("thursday")
    case 'f':
        print("friday")
    case 's':
        print("saturday")
    case _:
        print("invalid")
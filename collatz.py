def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result 

    else:
        result = 3 * number + 1
        print(result)
        return result

number = int(input('Enter any number'))


while number != 1:
   number = collatz(number)
def digitSum(myString):

    length = len(myString)
    oddSum = 0
    evenSum = 0

    if (length == 0):
        return 0

    else:
        if length % 2 == 0:
            last = int(myString[-1])
            evenSum += last
            return evenSum + digitSum(myString[:-1])
        else:
            last = int(myString[-1])
            last = 2 * last
            part_sum = last // 10 + last % 10
            oddSum += part_sum

            return oddSum + digitSum(myString[:-1])

def CardVerifier():
    myString = input('Enter 16 digit card number: ')
    total = digitSum(myString)
    if (total % 10 == 0):
        print('Valid Card')
    else:
        print('Invalid Card')


CardVerifier()

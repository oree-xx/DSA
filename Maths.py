def digits(num):
    while num > 0:
        digit = num % 10
        print(digit)
        num = num // 10

#digits(1234)

def count_digits(num):
    count = 0
    while num > 0:
        #last_digit = num % 10
        count += 1
        num = num // 10
    return count

#count_digits(344)

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

#reverse_number(1234)

def palindrome_number(num):
    rev = 0
    dup = num
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return dup == rev
       
#palindrome_number(121)

def armstrong_number(num):
    len_num = count_digits(num)
    count = 0
    for i in range(num):
        count += count + i ** len_num
    return count == num

armstrong_number(153)
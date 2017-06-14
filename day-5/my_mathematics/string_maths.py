def sum_digits(number):
       s = str(number)
       sum = 0
       for e in s:
           sum = sum + int(e)
       return sum

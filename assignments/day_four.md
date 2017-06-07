---

# Problem 1 : Study following a few Lambda Functions   

---
## HCF Function 
```
gcd = lambda m,n: m if not n else gcd(n,m%n)

```
## Factorial 

```
factorial = lambda x: x and x * factorial(x - 1) or 1 

```
## Power 

```
power = lambda x,y: y and x * power(x,y - 1) or 1 

```

## Fibonacci Numbers

```

fibonacci = lambda x : 1 if x <= 2 else fibonacci(x-1) + fibonacci(x-2)


```


---

# Problem 2: Write a script to find the sum of it's digits.  Example: 1234 number has 1, 2, 3 & 4 as it's digits. it's sum is 10. 
 
## Task
* Name the script as - *sum_digits.py* 
* The script takes numbers as input from user. The scripts quit if you provide input as "Q"

## Sample Input 
```
$ sum_digits.py
Enter Q to quit else number>
100

```

## Sample Output 
```
Enter Q to quit else number>
100
The sum of digists of 100 is: 1
111111
The sum of digists of 111111 is: 6
999999999999999999999999999999
The sum of digists of 999999999999999999999999999999 is: 270
Q
Thank you for Using Program!

```
---

# Problem 3: Develop a class called -  Point. This has two attributes x & y (representing coridinates). 
             Write a function to take two points as arguments and calculate the distance between them

## Task
* Name the script as - *Point.py* 
* The script will have Point as class. 
* The attributes will be x and y
* The class has methods - getX & getY 

---


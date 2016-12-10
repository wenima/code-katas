#Summary

the repository *code-katas* includes the following completed coding challenges from the [CodeWars Python challenges] (http://wwww.codewars.com)

# Python coding challenges:

## Mandatory coding challenges at various levls to sum up to 16 where kyu8 counts for 1pt, kyu7 for 2pts and kyu6 for 3pts.

* kata_string_to_array
* Taking a Vacaction --> Vacation.py
* A Day at the Supermarket --> DayAtSupermarket.py
* Student Becomes The Teacher --> StudentBecomesTeacher.py
* Battleship! --> Battleship.py

## Details for each kata completed
Descripton of Kata: Write a function to split a string and convert it into an array of words.
Module: kata_string_to_array
Tests: test_katas_8thkyu8.py
Link: https://www.codewars.com/kata/convert-a-string-to-an-array/train/python
Most interesting solution/best practice:
```python
def string_to_array(string):
    return string.split(" ")
```

Description: Given a string of digits, function will replace each char with 0 if char < 5 or 1 if char >=5
Module: kata_fake_bin.py
Tests: test_kata_fake_bin.py
Link: https://www.codewars.com/kata/fake-binary/train/python
Most interesting solution/best practice:
```python
#using generator expression
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
```

Description: Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
Module: kata_even_or_odd.py
Tests: test_kata_even_or_odd.py
Link: https://www.codewars.com/kata/even-or-odd/python
Most interesting solution/best practice:
```python
#interesting solution, have to admit I don't understand why this works
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]


## Optional at level lower than kyu8

* AreaCalculator.py
* rockpaperscissors.py

# Motivation

* the completed coding challenges were part of the Codefellows 401 Python Course snow-day assignment

# General comments

*

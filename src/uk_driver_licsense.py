"""Module to solve code wars kata:
https://www.codewars.com/kata/driving-license/train/python
"""
import time

def driver(data):
    surname = data[2]
    if len(surname) < 5:
        pad = ['9' for i in range(5 - len(surname))]
        surname = surname + ''.join(pad)
    try:
        birthdate = time.strptime(data[3].replace('-', ' '), '%d %B %Y')
    except ValueError:
        birthdate = time.strptime(data[3].replace('-', ' '), '%d %b %Y')
    decade = data[3][-2]
    month = '{:02d}'.format(birthdate.tm_mon) if data[4] == 'M' else birthdate.tm_mon + 50
    day = '{:02d}'.format(birthdate.tm_mday)
    year = data[3][-1]
    first_initial = data[0][0]
    middle_initial = data[1][0] if data[1] else '9'
    initials = first_initial + middle_initial
    arb_digit = '9'
    check_digits = 'AA'
    return '{0}{1}{2}{3}{4}{5}{6}{7}'.format(surname[:5], decade, month, day, year, initials, arb_digit, check_digits).upper()

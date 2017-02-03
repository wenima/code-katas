#Summary

the repository code-katas includes the following completed coding challenges from the CodeWars Python challenges

## Description:
The UK driving number is made up from the personal details of the driver. The individual letters and digits can be code using the below information

```
1–5: The first five characters of the surname (padded with 9s if less than 5 characters)

6: The decade digit from the year of birth (e.g. for 1987 it would be 8)

7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)

9–10: The date within the month of birth

11: The year digit from the year of birth (e.g. for 1987 it would be 7)

12–13: The first two initials of the first names, padded with a 9 if no middle name

14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9

15–16: Two computer check digits. We will always use "AA"
```

Your task is to code a UK driving license number using an Array of data. The Array will look like

```
data = ["John","James","Smith","01-Jan-2000","M"]
```

Where the elements are as follows

```
0 = Forename
1 = Middle Name (if any)
2 = Surname
3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)
4 = M-Male or F-Female
```

You will need to output the full 16 digit driving license number.


# Difficulty: kyu7

# Link: https://www.codewars.com/kata/driving-license/train/python

# Example test:
```
data = ["John", "James", "Smith", "01-Jan-2000", "M"]
test.it("Should return SMITH001010JJ9AA")
test.assert_equals(driver(data), "SMITH001010JJ9AA")

data = ["Johanna", "", "Gibbs", "13-Dec-1981", "F"]
test.it("Should return GIBBS862131J99AA")
test.assert_equals(driver(data), "GIBBS862131J99AA")

data = ["Andrew", "Robert", "Lee", "02-September-1981", "M"]
test.it("Should return LEE99809021AR9AA")
test.assert_equals(driver(data), "LEE99809021AR9AA")
```

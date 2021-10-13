import pandas as pd

#1 demensional############################################################
grades = pd.Series([87, 100, 94])

# print(grades)

grades2 = pd.Series(98.6, range(3))

# print(grades2)


grades = pd.Series([87, 100, 94], index=['Walley', 'Eva', 'Sam'])

grades = pd.Series({'Walley': 87, 'Eva': 100, 'Sam': 94})

# print(grades['Eva'])

# print(grades.Walley)
# print(grades.dtype)
# print(grades.values)
# print(type(grades.values))


hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

print(hardware.str.contains('a'))


print(hardware.str.upper())

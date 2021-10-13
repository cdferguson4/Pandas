import pandas as pd
#2 Dimensional array#############################################
grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test 1', 'Test 2', 'Test 3']

# print(grades)


# print(grades['Eva'])


# print(grades.Sam)


# Using the Loc and Iloc methods

# print(grades.loc['Test 2'])
# print(grades.iloc[1])

# For consecutive Rows
# print(grades.loc['Test 1': 'Test 3'])
# print(grades.iloc[0:3])


# For non-Consecutive Rows
# print(grades.loc[['Test 1', 'Test 3']])
# print(grades.iloc[[0, 2]])

# View Only Eva's and Katie's grades for Test1 and Test 2

##print(grades.loc[:'Test 2', ['Eva', 'Katie']])

# View only Sam's THRU Bob's Grades for Test 1 and Test 3
##print(grades.loc[['Test 1', 'Test 3'], 'Sam': 'Bob'])


grades_a = grades[grades >= 90]

print(grades_a)

# Create a dataframe for everyone with a B grade
grades_B = [(grades >= 80) & (grades < 90)]


# Create a data frame fro everyone with a A or B grade

grades_a_or_b = [(grades >= 90) | (grades >= 80)]

print(grades_a_or_b)

pd.set_option('precision', 2)
print(grades.describe())

print(grades.T.describe())

print(grades.sort_index(ascending=False))

print(grades.sort_index(axis=1, ascending=False))


print(grades.sort_values(by='Test 1', axis=1, ascending=False))

print(grades.T.sort_values(by='Test 1', ascending=False))


print(grades.loc['Test 1'].sort_values(ascending=False))

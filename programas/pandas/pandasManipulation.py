# import module
import pandas as pd
 
#############################################################################
### Assign dataset from file
df = pd.read_csv("country_code.csv")
#############################################################################
### Basic manipulations
print('*** print(type(df))')
print(type(df))
print('*** print(df)')
print(df)
print('*** print(df.head(10))')
print(df.head(10))
print('*** print(df.shape)')
print(df.shape)
print('*** print(df.describe())')
print(df.describe())
print('*** print(df.dropna())') #remove os valores NaN
print(df.dropna())
print('*** print(df.dropna(axis=1))') #remove todas as colunas que possuírem valores NaN
print(df.dropna(axis=1))
#############################################################################
### Merge dataframes
# Assign new dataset
df1 = pd.read_csv("country_code.csv")
print('*** print(pd.merge(df, df1, on=\'Name\')')
print(pd.merge(df, df1, on='Name'))
country_code = df.rename(columns={'Name': 'CountryName','Code': 'CountryCode'},inplace=False)
print('*** print(df.rename(columns={\'Name\': \'CountryName\',\'Code\': \'CountryCode\'},inplace=False))')
print(df.rename(columns={'Name': 'CountryName','Code': 'CountryCode'},inplace=False)) #'inplace = False' não altera o original
#############################################################################
### Assign dataset Manually
student = pd.DataFrame({'Name': ['Rohan', 'Rahul', 'Gaurav',
                                 'Ananya', 'Vinay', 'Rohan',
                                 'Vivek', 'Vinay'],
                        'Score': [76, 69, 70, 88, 79, 64, 62, 57]})
# Display					
print('*** print(student)')
print(student)
#############################################################################
### Sorting
print('*** print(student.sort_values(by=[\'Score\'], ascending=True))')
print(student.sort_values(by=['Score'], ascending=True))
print('*** print(student.sort_values(by=[\'Name\', \'Score\'], ascending=[True, False]))')
print(student.sort_values(by=['Name', 'Score'], ascending=[True, False]))
#############################################################################
# New column
student['Percentage'] = (student['Score'] / student['Score'].sum()) * 100
print('*** print(student) - with new column')
print(student)
##############################################################################
### Logical operators
# Selecting rows where score is greater than 70
print('*** print(student[student.Score>70])')
print(student[student.Score>70])
# Selecting rows where score is greater than 60 AND less than 70
print('*** print(student[(student.Score>60) & (student.Score<70)])')
print(student[(student.Score>60) & (student.Score<70)])
# Selecting rows where score is less than 60 OR greater than 70
print('*** print(student[(student.Score<60) | (student.Score>70)])')
print(student[(student.Score<60) | (student.Score>70)])
##############################################################################
### Indexing and Slicing
# Printing five rows with name column only, i.e. printing first 5 student names
print('*** print(student.loc[0:4, \'Name\'])')
print(student.loc[0:4, 'Name'])
# Printing all the rows with score column only i.e. printing score of all the students
print('*** print(student.loc[:, \'Score\'])')
print(student.loc[:, 'Score'])
 # Printing only first rows having name, score columns i.e. print first student name & their score
print('*** print(student.iloc[0, 0:2]')
print(student.iloc[0, 0:2])
# Printing first 3 rows having name,score & percentage columns i.e. printing first three student name,score & percentage
print('*** print(student.iloc[0:3, 0:3])')
print(student.iloc[0:3, 0:3])
# Printing all rows having name & score columns i.e. printing all student name & their score
print('*** print(student.iloc[:, 0:2])')
print(student.iloc[:, 0:2])
##############################################################################
### External function
def double(a):
    return 2*a 
student['Score'] = student['Score'].apply(double)
print('*** print(student) - with score changed by a external function')
print(student)
#############################################################################
### Assign dataset Manually wiht names for indexes. The index access is still numeric.
menu = pd.DataFrame({'calorias':[200, 350, 550]},
						index = ['morango', 'pastel', 'hamburguer'])
# Display					
print('*** print(menu)')
print(menu)


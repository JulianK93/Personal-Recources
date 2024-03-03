import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from openpyxl import load_workbook
-------------------------------------
df = pd.read_csv("pokemon_data.csv",)
df = pd.read_excel("pokemon_data.xlsx")
df = pd.read_csv(“pokemon_data.txt”, delimiter=”\t”)  

with open('Dank_Central_Cleaned.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
table = xls_file.parse('Sheet1')

# More Advanced
sheet_name = 'Sheet1'                     #Set a custom sheet name, can be a name (string), index (integer), a list of sheets or 'None' (= all)
header_row = 1                            #Specifies wich row will be used as column names. It can be an integer or a list of integers.
column_names = ['Name', 'Age', 'City']    #Sets the column names
index_column = 'Name'                     #Specifies wich columns to use as indexes
selected_columns = ['Name', 'Age']        #Specifies a sub selection of columns to read from the file
data_types = {'Age': int}                 #Specify the data types of the columns
skip_rows = 2                             #Skyps a number o rows at the beginning of the document
num_rows_to_read = 100                    #Specify the numbers of rows to read from the file
parse_date_cols = ['Birthdate']           #Data logic, setting a column to a specific data type, in this case dates
date_parser_func = lambda x: pd.to_datetime(x, format='%Y-%m-%d')
-------------------------------------
df.to_csv(“Modified_csv”, index=False) 		    #Exports data after mutations, index=False optional
df.to_excel(“Modified.xlsx”, index=False)	    #Exports data to excel after mutations
df.to_csv(“Modified.txt, index=False, sep=’\t’)	#Look at documentation for options
-------------------------------------
# OFTEN USED
df.columns   				                        #reads headers
df.sort_values(“Name”, ascending=False)             #Sorts
df.sort_values([“Type1”, “HP”], ascending = [1,0])	#Sorts multiple values, 0 is descending
df.describe()						#Makes a table of avarage values
df.head(5)
df.tail(5)
df.shape
df.size

# Creating the Dataframe, setting columns
df = pd.DataFrame(data)                                        #Creates the DF
df = pd.DataFrame(data, columns="year", "state", "pop")        #Creates the DF and sets the order of columns
df = pd.Dataframe(data, columns="year", "state", "pop", "debt") #creates an empty debt column, NA values

#FILTER and SLIM
sub_df = df [ (df ["Sex"] == "M") & (names["Year"].between(1920,1960)) ]
sub_df = df[df['Age'] > 25]  
sub_df = df[['Name', 'Age']]  #Creates a new DF with only the columns Name and Age

#TRANSFORM
df.T  

##REORDER
desired_order = ['Name', 'Productivity', 'Month', 'teamlead']
df_reordered = df[desired_order
]
#RENAME
df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)
df.rename(columns={"year": "year of birth"})
df.index.name = 'year'; df.columns.name = 'state'  # sets index and column name

#ADD
df["births/5"] = df["births"] / 5
df["debt"] = 16          #Sets all column values to 16
df["debt"] = np.arange(5.)  #sets all column values 0-5
df['eastern'] = df.state == 'Ohio' #adds a new False/True column based on logic

#REMOVE
df.drop(columns=['column_to_remove'], inplace=True)
df.drop(columns=[("births/5"), ("births*2")])
del df["eastern"]     #deletes the column

# Bigs: UNIQUE, SORT, ISNULL, DROPNA, FILL NA
unique_states = df['state'].unique()
sorted = df["Name"].sort()
df["empty"] = df.isnull()
df.dropna(axis=1, how='all')  # How, drops only columns/rows that are ALL NA. Axis=1 is optional, rows ins. columns.
df.fillna(method='ffill', limit=2)
df.fillna(df.mean())

#MATHS
df.sum() Sums all columns
df.sum(axis=1) Sums all rows
df.mean()  avarages all columns
df.idxmin()  returns the index with lowest value 
df.idxmax()  returns the index with highest value

#CALCULUS
pd.count Number of non-NA values
pd.min, max Compute minimum and maximum values
pd.argmin, argmax Compute index locations (integers) at which minimum or maximum value obtained, respectively
pd.idxmin, idxmax Compute index values at which minimum or maximum value obtained, respectively
quantile Compute sample quantile ranging from 0 to 1
pd.sum Sum of values
pd.median Arithmetic median (50% quantile) of values
pd.mad Mean absolute deviation from mean value
pd.var Sample variance of values
pd.std Sample standard deviation of values
pd.skew Sample skewness (3rd moment) of values
pd.kurt Sample kurtosis (4th moment) of values
pd.cumsum Cumulative sum of values
pd.cummin, cummax Cumulative minimum or maximum of values, respectively
pd.cumprod Cumulative product of values
pd.diff Compute 1st arithmetic difference (useful for time series)
pd.pct_change Compute percent changes

-------------------------------------
pandas.pivot_table(data, values=”None”, index=”None”, columns=”None”, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')

data: #The DataFrame to be used for creating the pivot table.
values: #The column to aggregate.
index: #Columns to group by (pivot on).
columns: #Columns to pivot on.
aggfunc: #Function to use for aggregation. Default is 'mean'.
fill_value: #Replace missing values in the result.
margins: #Add all row/column margins (subtotals).
dropna: #If True, do not include columns whose entries are all NaN.
margins_name: #Name of the row/column that will contain the totals when margins is True.
Parameters:
data: #DataFrame: The input data.
values:# column or list of columns: The values to aggregate.
index: #column, Grouper, array, or list: Column to group by. If a Grouper is passed, it must be the same length as the data.
columns: #column, Grouper, array, or list: Column or group of columns to pivot.
aggfunc:# function, dict, default 'mean': If a function, it is used to aggregate the data. If a dictionary, mapping columns to aggregate functions.
fill_value: #scalar, default None: Value to replace missing values with.
margins: #bool, default False: Add all row/column margins (subtotals).
dropna: #bool, default True: Do not include columns whose entries are all NaN.
margins_name:# str, default 'All': Name of the row/column that will contain the totals when margins is True.
-------------------------------------
mylist = []              #Creates empty list, [brackets]
mylist.append("julian")  #Appends the list mylust with "Julian", append = at the end, expand

# Very basic function with return
def function3(x, y):
    return x + y
print(function3(3, 7))

# BMI Calculater ------------------------
name1 = "Julian"
height_m1 = 1.75
weight_kg1 = 70

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("Name: %s" % name)
    print("bmi: %s" % bmi)
    if bmi <25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
        
result1 = bmi_calculator(name1, height_m1, weight_kg1)
print(result1)
-------------------------------------
# For Loop
for y in range(1,100,9):
    print(y)

# Count Loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
-------------------------------------
Main functions: 
plt.plot(x, y)   #Makes a scatter or line plot of the given data, add plt.show()
plt.figure()     # Makes a figure that's adjustable, customazible graphs
# > Figure is neededwhen:
# You want multiple plots in one figure
# You want to adjust background, size, or grid
# You want to create multiple subplots

# Example data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]

# Create a new figure with specified arguments
plt.figure(
    figsize=(8,6),            #sets the width to 8 inches, height to 6 inches
    dpi=100,                  #optional, sets dots per inch (resolution)
    facecolor="lightblue",    #Background color of the figure, names, hexadecimal color codes or RGB tuples
    edgecolor="navy",         #border color of the figure
    fameon=true,             #if False, doesnt draw a frame. Normal = True
    #Subplotbars
    #tight_layout=True
    #constrained_layout=true
    #subplots
)
plt.xlabel('Year')
plt.ylabel('Number of Births')
plt.title("Number of Births in the US for {}".format(listnames))
plt.legend()
plt.show()

plt.grid(
    which="both",    #Specify which grid lines to draw. Options are 'major' (default), 'minor', or 'both'.
    axis="both",     #Set the axis on which to draw the grid. Options are 'both' (default), 'x', or 'y'.
    color="gray",    #Set the color of the grid lines.
    linestyle="--",  #linestyle: Set the line style of the grid lines. Options include '-', '--', '-.', ':', etc.
    linewidth=0.5,   #set the linewidth
    alpha=0,5        #Set the transparency of the grid lines (between 0 and 1).
)

plt.xlim(1, 12)  # Set x-axis limits from 1 to 12
plt.ylim(0, 20)   # Set y-axis limits from 0 to 20
plt.axis([1, 12, 0, 20])  # Set x-axis limits from 1 to 12, and y-axis limits from 0 to 20
-------------------------------------
y_list = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10]

for i, y in enumerate(y_list, start=1):
    plt.plot(x, y, label = f"y{i}")

listnames = ["Anne", "Valters", "Walter", "Julian"]     
for name in listnames:
    name_data = names[(names['name'] == name)]
    name_counts = name_data.groupby('year')['births'].sum()
    plt.plot(name_counts.index, name_counts, label=name)

for name in list_names:
    name_data = memes_per_month_df.loc[name]
    plt.plot(name_data.index, name_data, marker='o', label=name)
-------------------------------------
years = range(1880, 2011)  #creates a range of years under the variable "years"
pieces = []                #creates an empty list called pieces
columns = ['name', 'sex', 'births']    #creates the variable columns we will call later
for year in years:          # creates a loop that itterstes 
 path =  "yob%d.txt" % year   #constructs a file path for every year in %d position
 frame = pd.read_csv(path, names=columns)   #reads the csv files for every path, asign the column vairable. call it frame
 frame['year'] = year            #adds a new column to your data base called 'year' and fills it with var.year
 pieces.append(frame)          #adds the current frame, based on year, to the data list pieces (append is add at end)        
names = pd.concat(pieces, ignore_index=True)    #puts the strings together
print(names)
-------------------------------------
# New dimension table
dimension_table = {
    "+31 6 21460367": 'Tobit',
    'Bob Fwiend': 'Rest',
    'Dion Fwiend': 'Rest',
    'Donovan': 'Rest',
    'Enne Fwiend': 'Enne',
    'Erik Fwiend': 'Rest',
    'Hannah Famiglia': 'Rest',
    'Julian': 'Julian',
    'Mehdi Fwiend': 'Rest',
    'Ramon Fwiend': 'Rest',
    'Sam Famiglia': 'Rest',
    'lennart fam': 'Rest',
}

# Update team mapping with the new dimension table
team_mapping.update(dimension_table)

# Assign team types to the DataFrame
df['Team'] = df['Sender'].map(team_mapping)

# Check the DataFram
-------------------------------------
import pandas as pd

# Create a simple DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 15, 25, 12, 18, 8, 30]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Use transform to calculate the sum within each category and broadcast it back to each row
df['Sum_By_Category'] = df.groupby('Category')['Value'].transform('sum')
df["Total_for_catagory"] = df.groupby("Category")["Value"].transform("sum")
df["Total_for_year"] = df.groupby("Year")["Value"].transform("sum")

# Display the DataFrame with the new column added
print("\nDataFrame with Sum_By_Category column:")
print(df)
-------------------------------------
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d-%m-%Y %H:%M')
df['MonthNumber'] = df['DateTime'].dt.strftime('%Y-%m')
df['WeekNumber'] = df['DateTime'].dt.strftime('%Y-%U')
df['DayNumber'] = df['DateTime'].dt.strftime('%Y-%m-%d')
df["Hour"] = df["DateTime"].dt.strftime("%H")
df["Weekday"] = df["DateTime"].dt.strftime("%a")
df["Count"] = 1
-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------

-------------------------------------
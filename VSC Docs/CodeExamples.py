x = np.array([1, 2, 3, 4, 5])
y1 = np.array([10, 15, 7, 12, 9])
y2 = np.array([5, 8, 11, 6, 14])
y3 = np.array([12, 9, 5, 8, 11])
y4 = np.array([8, 13, 6, 11, 7])
y5 = np.array([14, 7, 10, 8, 12])
y6 = np.array([9, 12, 15, 6, 10])
y7 = np.array([11, 8, 14, 9, 5])
y8 = np.array([7, 10, 12, 5, 14])
y9 = np.array([13, 6, 9, 11, 8])
y10 = np.array([10, 14, 8, 12, 7])
###############################################################################
data = {'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
        'Population': [8_398_748, 3_979_576, 8_398_748, 2_705_994, 3_979_576],
        'Area': [468.9, 1_302, 468.9, 606.1, 1_302]}
df = pd.DataFrame(data)
###############################################################################
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'B', 'A', 'B', 'C'],
    'Value': [10, 20, 15, 25, 12, 18, 8, 30, 14, 22, 11, 25, 20, 9, 16, 28],
    'Year': [2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021, 2021, 2021]
}
###############################################################################
df = pd.read_csv("https://bit.ly/3kGDuKx", na_values="?")
---------------------------
plt.figure(
    figsize=(10,3), 
    facecolor="green",
    edgecolor="purple",
)

y_list = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10]

for i, y in enumerate(y_list, start=1):
    plt.plot(x, y, label = f"y{i}")

plt.grid(
    which="major",
    axis="both",
    color="red",
    linestyle="--",
    linewidth=0.5,
    alpha= 0.9    
)
plt.legend()
plt.xlabel("xlegend")
plt.ylabel("ylegend")
plt.xlim(1, 12)
plt.ylim(0, 20)
plt.show()
----------------------------
years = range(1880, 2011)
pieces = []
columns = ["name", "sex", "births"]
for year in years:
    path = "yob%d.txt" % year
    parts = pd.read_csv(path, names=columns)
    parts["year"] = year
    pieces.append(parts)
names = pd.concat(pieces, ignore_index=True)
print(names)

df_males = names[(names["sex"] == "M") & (names["year"].between(1920,1960))]

df_femalesn = names[(names["sex"] == "F") & (names["name"].str.endswith("n"))]


male_names = names[names['sex'] == 'M']
female_names = names[names['sex'] == 'F']

merged_names = pd.merge(male_names, female_names, on=['name', "year"], suffixes=('_male', '_female'), how='inner')
merged_names['total_Births'] = merged_names['births_male'] + merged_names['births_female']
merged_names['absolute_Difference'] = abs(merged_names['births_male'] - merged_names['births_female'])
merged_names['relative_Difference'] = merged_names['absolute_Difference'] / merged_names['total_Births']
result_df = merged_names[
    (merged_names['total_Births'] > 200) &
    (merged_names['relative_Difference'] <= 0.1)
]
print(result_df)

pivot_table = pd.pivot_table(result_df, values ="total_Births", index="name", aggfunc="sum")
sorted_pivot_table = pivot_table.sort_values(by="total_Births", ascending=False)
print(sorted_pivot_table)


df_more1000 = names[names["births"]>30000]
print(df_more1000)
table_30000 = pd.pivot_table(df_more1000, values = "births", index = "name", aggfunc = "sum")
table_30000_sorted = table_30000.sort_values(by = "births", ascending=False)
print(table_30000_sorted)

df_less50 = names[names["births"]<50]

jnamespivot = pd.pivot_table(df_namejn, values = "births", index = "name", aggfunc = "sum")
jnamespivot_sorted = jnamespivot.sort_values(by= "births", ascending = False)

only_10years_pieces = []
for year in names["year"].unique():
    if year % 10 == 0:
        part = names[names["year"] == year]
        only_10years_pieces.append(part)
only_10years = pd.concat(only_10years_pieces)
print(only_10years)

names["births/5"] = names["births"] / 5

new_order = ["births", "births/5", "name", "sex", "year"]
names_reorder = names[new_order]
print(names_reorder)

names.rename(columns={"year": "year of birth"})

names.drop(columns=['births/5'], inplace=True)

df_females2005 = names[(names["sex"]=="F") & (names["year"] > 2004)]
df_males2005 = names[(names["sex"]=="M") & (names["year"] > 2004)]

excel_file_path = "separated3.xlsx"

with pd.ExcelWriter(excel_file_path, engine='xlsxwriter', mode="a") as writer:
    df_females2005.to_excel(writer, sheet_name='Female2', index=False)

with pd.ExcelWriter(excel_file_path, engine='xlsxwriter', mode='a') as writer:
    df_males2005.to_excel(writer, sheet_name='Male2', index=False)

---------------------------
with open('roadtrip_clean.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

data = []
for line in lines:
    parts = line.split(" - ")
    date_time = parts[0]
    sender_and_message = parts[1]
    
    # Further split sender_and_message using ":"
    sender_message_parts = sender_and_message.split(":")
    
    # Extract sender and message
    if len(sender_message_parts) > 1:
        sender = sender_message_parts[0].strip()
        message = sender_message_parts[1].strip()
        data.append([date_time, sender, message])
        
################################
df = pd.DataFrame(data, columns=['DateTime', 'Sender', 'Message'])
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d-%m-%Y %H:%M')
df['MonthNumber'] = df['DateTime'].dt.strftime('%Y-%m')
df['WeekNumber'] = df['DateTime'].dt.strftime('%Y-%U')
df['DayNumber'] = df['DateTime'].dt.strftime('%Y-%m-%d')
df["Hour"] = df["DateTime"].dt.strftime("%H")
df["Weekday"] = df["DateTime"].dt.strftime("%a")
df["Count"] = 1

###################################
total = pd.pivot_table(df, values="count", index ="Sender", aggfunc=("sum"))
per_month = pd.pivot_table(df, values="count", index ="Sender", columns="MonthNumber", aggfunc=("sum"))
per_week = pd.pivot_table(df, values="count", index ="Sender", columns = "WeekNumber", aggfunc=("sum"))
per_day = pd.pivot_table(df, values="count", index ="Sender", columns = "DayNumber", aggfunc=("sum"))

##################################
plt.figure(figsize=(16, 8))
for sender in per_week.index:
    plt.plot(per_week.columns, per_week.loc[sender], label=sender, marker='o')

# Set labels and title
plt.xlabel('Week Number')
plt.ylabel('Number of Messages')
plt.title('Number of Messages per Sender per Week')

# Show the legend
plt.legend(title='Sender', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()
------------------------
import pandas as pd
import numpy as np

years = range(1880, 2011)
pieces = []
columns_names = ["name", "sex", "births"]

for year in years:
    path = "yob%d.txt" % year
    frame = pd.read_csv(path, names=columns_names)
    frame["year"] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)

total_births = names.groupby(['year', 'sex'])['births'].transform("sum")

names['proportional_birth_fraction'] = names['births'] / total_births
-------------------------------

-----------------------------
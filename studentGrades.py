import csv, time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import csv
df = pd.read_csv("cs4222_students_list.csv")
df.rename(columns={"UID": "id", "Last Name": "last-name", "First Name" : "first-name"}, inplace=True)

# a : sort names 
def insertion_sort(df, column):
    for i in range(1, len(df)):
        key_item = df.loc[i, column]
        j = i - 1
        while j >= 0 and df.loc[j, column] > key_item:
            df.loc[j + 1], df.loc[j] = df.loc[j], df.loc[j + 1].copy()
            j -= 1
        df.loc[j + 1, column] = key_item
    return df

sorting_start = time.time()
sorted_df = insertion_sort(df, "last-name")
sorting_end = time.time()
sorting_time = sorting_end - sorting_start

#b : make new dataframe with just hackathon Big-O members
codes = ["#23375868","#23327944","#23365978","#23383674","#23329831","#23381914"]
df1 = sorted_df[sorted_df['id'].isin(codes)]

# add grades of Big-O members in new columns 
df1["CS4221"] = [71, 86, 88, 44, 85, 76]
df1["CS4222"] = [77, 75, 90, 89, 31, 42]
df1["CS4141"] = [33, 92, 93, 16, 57, 18]
df1.reset_index(drop=True, inplace=True) 

searching_top5_start = time.time()

# sort the code based on CS4221 grades here
print("\n These are the top 5 \"Foundations Of Computer Science 1\" grades")
df2 = insertion_sort(df1, "CS4221")
top_5_CS4221 = df2[1:]
Sorted_CS4221_Grades = top_5_CS4221[["id","last-name","first-name", "CS4221"]]
# print(Sorted_CS4221_Grades)

# sort the code based on CS4222 grades here
print("\n These are the top 5 \"Software Development\" grades")
df3 = insertion_sort(df1, "CS4222")
top_5_CS4222 = df3[1:]
Sorted_CS4222_Grades = top_5_CS4222[["id","last-name","first-name", "CS4222"]]
# print(Sorted_CS4222_Grades)

# sort the code based on CS4141 grades here
print("\n These are the top 5 \"Into To Programming\" grades")
df4 = insertion_sort(df1, "CS4141")
top_5_CS4141 = df4[1:]
Sorted_CS4141_Grades = top_5_CS4141[["id","last-name","first-name", "CS4141"]]
# print(Sorted_CS4141_Grades)

searching_top5_end = time.time()
searching_top5_time = searching_top5_end - searching_top5_start


#plot_distributionOfMarks

student_ids = df1["id"]
colors = [ '#0a445c', '#0f668a', '#1488b8', '#19aae6','#47bbeb', '#a3ddf5']

# DISTRIBUTION OF MARKS: 1 PLOT, 5 STUDENTS, 3 BARS EACH

# Plot 1: CS4221
plt.subplot(1, 3, 1)
plt.bar(student_ids, df2["CS4221"], color=colors)
plt.title('CS4221')
plt.xticks(rotation=45)
plt.xlabel('Student ID')
plt.ylabel('Student Grade')

# Plot 2: CS4222
plt.subplot(1, 3, 2)
plt.bar(student_ids, df3["CS4222"], color=colors)
plt.title('CS4222')
plt.xticks(rotation=45)
plt.xlabel('Student ID')
plt.ylabel('Student Grade')

# Plot 3: CS4141
plt.subplot(1, 3, 3)
plt.bar(student_ids, df4["CS4141"], color=colors)
plt.title('CS4141')
plt.xticks(rotation=45)
plt.xlabel('Student ID')
plt.ylabel('Student Grade')

# Plot time (in a different window)
fig, ax = plt.subplots()
x = ["Sorting", "Searching"]
y = [sorting_time, searching_top5_time]
ax.bar(x, y, color=[colors[0], colors[-1]])
ax.set_ylabel('Time (seconds)')
ax.set_title('Time Taken')

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)  

plt.show()

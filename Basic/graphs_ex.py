import matplotlib.pyplot as plt
import pandas as pd

# Example-1 (Line Plot)
# x=[1,2,3]
# y=[10,20,30]
# plt.plot(x,y)
# plt.show()

# Example-2 (Line Plot)
# x=[1,2,3,4]
# y=[10,20,15,25]
#plt.plot(x,y)
#plt.plot(x,y,color="red",linestyle=":",marker="o") # linestyles: -,--,: marker = o,x,*
# plt.plot(x,y,'bo--')
# plt.title("Line Chart")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# Example-3 (Line Plot with pandas)
# df = pd.read_csv("chart.csv")
# x=df["age"]
# y=df["salary"]
# plt.plot(x,y,'bo--')
# plt.title("Age & Salary")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.show()

# Example-4 (Bar Chart)
# x=["A","B","C"]
# y=[10,20,15]
# plt.bar(x,y)
# plt.show()

# Example-5 (Bar Chart)
# x=["A","B","C"]
# y=[10,20,15]
# plt.bar(x,y,color=["red","blue","green"],width=0.5,edgecolor="black")
# plt.title("Bar Chart")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# Example-6 (Bar Chart)
# x=["A","B","C"]
# y=[10,20,15]
# bars = plt.bar(x,y,color=["red","blue","green"],width=0.5,edgecolor="black")
# plt.title("Bar Chart")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# for bar in bars:
#     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),bar.get_height(),ha="center",va="bottom")
# plt.show()


# subjects = ["Math", "Science", "English", "History"]
# marks = [85, 90, 78, 92]
# colors = ["red", "blue", "green", "orange"]
# explode = (0,0,1,0)
# plt.figure(figsize=(8,8))
# plt.pie(marks,
#         labels=subjects,
#         colors=colors,
#         explode=explode,
#         autopct='%1.1f%%',
#         shadow=True,
#         startangle=90)
# plt.title("Marks Distribution")
# plt.title("Student Marks Distribution")
# plt.legend(title="Subjects")
# plt.show()



# Scatter Plot
# study_hours = [1,2,3,4,5,6,7,8]
# marks = [35,40,50,60,65,70,85,95]
# sizes = [100,120,140,160,180,200,220,240]
# colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow']
# plt.figure(figsize=(10,6))
# plt.scatter(study_hours,marks,s=sizes,c=colors,alpha=0.5,edgecolor='black',marker='o')
# plt.title("Study Hours vs Marks Analysis",fontsize=16)
# plt.xlabel("Study Hours",fontsize=12)
# plt.ylabel("Marks",fontsize=12)
# plt.annotate('Top Student',xy=(8,95),xytext=(8,80),arrowprops=dict(facecolor='red', shrink=0.10))
# plt.grid(True)
# plt.show()

#Histo Graph
# marks = [35,40,42,45,50,55,58,60,62,65,68,70,72,75,78,80,82,85,88,90,92,95]
# plt.figure(figsize=(10,6))

# #bins = 5
# # 95 - 35 = 60/5 = 12
# # 35 - 47 (Bin1) 4
# # 47 - 59 (Bin2) 3
# # 59 - 71 (Bin3) 5
# # 71 - 83 (Bin4) 5
# # 83 - 95 (Bin5) 5

# plt.hist(marks,bins=5,color='lightblue',edgecolor='black',alpha=0.5)
# plt.title("Marks Distribution",fontsize=16)
# plt.xlabel("Marks",fontsize=12)
# plt.ylabel("Students",fontsize=12)
# plt.grid(True)
# plt.show()

# Multiple Graphs in One Dashboard
# subjects = ["Math", "Science", "English", "History"]
# marks = [85, 90, 78, 92]
# attendance = [90, 95, 85, 92]
# plt.figure(figsize=(10,6))
# plt.subplot(2,2,1)
# plt.plot(subjects,marks,'ro--')
# plt.title("Marks")

# plt.subplot(2,2,2)
# plt.bar(subjects,marks,color='skyblue')
# plt.title("Bar Grapph")

# plt.subplot(2,2,3)
# plt.pie(marks,labels=subjects,autopct='%1.1f%%')
# plt.title("Pie Chart")

# plt.subplot(2,2,4)
# plt.hist(marks,bins=2,color='lightgreen',edgecolor='black',alpha=0.7)
# plt.title("Histograph")


# plt.show()






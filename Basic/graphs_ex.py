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







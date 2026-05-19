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




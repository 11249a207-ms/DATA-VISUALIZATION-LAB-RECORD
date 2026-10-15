# Experiment No. 2: Basic Visualization in Python
# Aim: Create line, bar, pie, scatter and histogram visualizations.

import matplotlib.pyplot as plt

# Line graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.plot(x, y, marker="o")
plt.title("Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Bar chart
subjects = ["Python", "Java", "R", "Tableau"]
marks = [85, 75, 80, 90]
plt.bar(subjects, marks)
plt.title("Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.show()

# Pie chart
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Technology Usage")
plt.show()

# Scatter plot
hours = [1, 2, 3, 4, 5, 6]
student_marks = [45, 50, 58, 65, 72, 80]
plt.scatter(hours, student_marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# Histogram
all_marks = [45, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90]
plt.hist(all_marks, bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

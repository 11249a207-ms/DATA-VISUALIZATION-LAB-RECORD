# Experiment No. 3: Basic Visualization in R
# Aim: Create line, bar, pie, scatter and histogram visualizations.

# Line graph
x <- c(1, 2, 3, 4, 5)
y <- c(10, 20, 15, 25, 30)
plot(x, y, type="o", main="Line Graph", xlab="X Values", ylab="Y Values")

# Bar chart
marks <- c(85, 75, 80, 90)
subjects <- c("Python", "Java", "R", "Tableau")
barplot(marks, names.arg=subjects, main="Marks by Subject", xlab="Subject", ylab="Marks")

# Pie chart
pie(marks, labels=subjects, main="Technology Usage")

# Scatter plot
hours <- c(1, 2, 3, 4, 5, 6)
student_marks <- c(45, 50, 58, 65, 72, 80)
plot(hours, student_marks, main="Study Hours vs Marks", xlab="Study Hours", ylab="Marks", pch=19)

# Histogram
all_marks <- c(45, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90)
hist(all_marks, breaks=5, main="Distribution of Marks", xlab="Marks", ylab="Frequency")

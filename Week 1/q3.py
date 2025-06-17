import pandas as pd
import numpy as np

names = ['Ananya', 'Babitha', 'cherry', 'devi', 'akshara', 'akshitha', 'Sandhya', 'Rama', 'Gita', 'Sita']
subjects = ['Math', 'Science', 'History', 'English', 'Math', 'Science', 'History', 'English', 'Math', 'Science']

scores = np.random.randint(50, 101, size=10)

df = pd.DataFrame({
    'Name': names,
    'Subject': subjects,
    'Score': scores,
    'Grade': '' 
})

def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Score'].apply(assign_grade)

print("Student DataFrame with Grades:\n")
print(df)

sorted_df = df.sort_values(by='Score', ascending=False)
print("\nStudents sorted by Score (highest first):\n")
print(sorted_df)

avg_scores = df.groupby('Subject')['Score'].mean()
print("\nAverage score by subject:\n")
print(avg_scores)

def pandas_filter_pass(dataframe):
    return dataframe[dataframe['Grade'].isin(['A', 'B'])]

passed_students = pandas_filter_pass(df)
print("\nStudents with Grade A or B:\n")
print(passed_students)

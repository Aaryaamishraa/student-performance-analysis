
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('student_performance_data.xlsx')

# Display basic info
print("First 5 records:")
print(df.head())

# Average marks overall
average_marks = df['Marks'].mean()
print(f"\nAverage Marks: {average_marks:.2f}")

# Top scorer(s)
top_score = df['Marks'].max()
top_students = df[df['Marks'] == top_score][['Student Name', 'Marks']]
print(f"\nTop Scorer(s):")
print(top_students)

# Subject-wise average marks
subject_avg = df.groupby('Subject')['Marks'].mean()
print("\nAverage Marks by Subject:")
print(subject_avg)

# Plot subject-wise average marks
subject_avg.plot(kind='bar', color='skyblue', title='Average Marks by Subject')
plt.ylabel('Marks')
plt.tight_layout()
plt.savefig('subject_avg_marks.png')
plt.show()

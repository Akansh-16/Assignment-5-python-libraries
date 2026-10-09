import math
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def demonstrate_math():
    print("\n========== MATH LIBRARY ==========")
    number = 25

    print(f"Square root of {number}: {math.sqrt(number)}")
    print(f"Power (2^5): {math.pow(2, 5)}")
    print(f"Factorial of 5: {math.factorial(5)}")
    print(f"Value of PI: {math.pi}")
    print(f"Ceiling of 4.3: {math.ceil(4.3)}")
    print(f"Floor of 4.7: {math.floor(4.7)}")


def demonstrate_numpy():
    print("\n========== NUMPY LIBRARY ==========")
    marks = np.array([65, 72, 80, 75, 90])

    print("Marks:", marks)
    print("Sum:", np.sum(marks))
    print("Mean:", np.mean(marks))
    print("Median:", np.median(marks))
    print("Standard Deviation:", np.std(marks))
    print("Maximum:", np.max(marks))
    print("Minimum:", np.min(marks))
    return marks


def demonstrate_scipy(marks):
    print("\n========== SCIPY LIBRARY ==========")
    z_scores = stats.zscore(marks)
    mode_result = stats.mode(marks, keepdims=True)

    print("Z-Scores:", np.round(z_scores, 2))
    print("Mode:", mode_result.mode[0])


def create_student_dataframe():
    print("\n========== PANDAS LIBRARY ==========")
    data = {
        "Student": ["Amit", "Neha", "Rahul", "Sneha", "Priya"],
        "Maths": [78, 85, 72, 90, 88],
        "Python": [82, 90, 75, 95, 86],
        "AI": [80, 88, 70, 92, 90],
    }

    df = pd.DataFrame(data)
    print("\nStudent Data:")
    print(df.to_string(index=False))

    # Add a new column containing each student's average marks.
    df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1)

    print("\nData with Average Marks:")
    print(df.round(2).to_string(index=False))

    print("\nSummary Statistics:")
    print(df[["Maths", "Python", "AI", "Average"]].describe().round(2))
    return df


def visualize_with_matplotlib(df):
    print("\n========== MATPLOTLIB VISUALIZATION ==========")
    plt.figure(figsize=(8, 5))
    plt.bar(df["Student"], df["Average"])
    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.title("Average Marks of Students")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig("average_marks.png", dpi=150)
    plt.show()


def visualize_with_seaborn(df):
    print("\n========== SEABORN VISUALIZATION ==========")

    # Scatter plot: compare Maths and Python marks.
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="Maths", y="Python", s=100)
    plt.title("Maths Marks vs Python Marks")
    plt.xlabel("Maths Marks")
    plt.ylabel("Python Marks")
    plt.tight_layout()
    plt.savefig("maths_vs_python.png", dpi=150)
    plt.show()

    # Heatmap: show correlation between subject marks.
    plt.figure(figsize=(7, 5))
    correlation = df[["Maths", "Python", "AI"]].corr()
    sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Correlation Between Subjects")
    plt.tight_layout()
    plt.savefig("subject_correlation_heatmap.png", dpi=150)
    plt.show()


def main():
    demonstrate_math()
    marks = demonstrate_numpy()
    demonstrate_scipy(marks)
    df = create_student_dataframe()
    visualize_with_matplotlib(df)
    visualize_with_seaborn(df)

    print("\nAssignment completed successfully.")
    print("Charts saved as PNG files in the current directory.")


if __name__ == "__main__":
    main()

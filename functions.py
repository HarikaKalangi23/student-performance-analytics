
import numpy as np


SUBJECTS = ["Python", "Mathematics", "AI"]


def calculate_total(data):
    """Calculate total marks for each student."""
    data["Total_Marks"] = data[SUBJECTS].sum(axis=1)
    return data


def calculate_average(data):
    """Calculate average marks using NumPy."""
    data["Average_Marks"] = np.round(
        np.mean(data[SUBJECTS].to_numpy(), axis=1), 2
    )
    return data


def assign_grade(average):
    """Assign a grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def determine_result(row):
    """A student passes only if every subject mark is at least 40."""
    for subject in SUBJECTS:
        if row[subject] < 40:
            return "Fail"
    return "Pass"


def process_students(data):
    """Calculate totals, averages, grades and results."""
    data = calculate_total(data)
    data = calculate_average(data)

    data["Grade"] = data["Average_Marks"].apply(assign_grade)
    data["Result"] = data.apply(determine_result, axis=1)

    return data


def display_class_summary(data):
    """Display overall class performance."""
    print("\n========== CLASS SUMMARY ==========")
    print("Total students:", len(data))
    print("Class average:", round(data["Average_Marks"].mean(), 2))
    print("Highest average:", data["Average_Marks"].max())
    print("Lowest average:", data["Average_Marks"].min())

    print("Students passed:", (data["Result"] == "Pass").sum())
    print("Students failed:", (data["Result"] == "Fail").sum())


def display_subject_analysis(data):
    """Display average marks for each subject."""
    print("\n======= SUBJECT-WISE ANALYSIS =======")

    subject_averages = data[SUBJECTS].mean()

    for subject, average in subject_averages.items():
        print(f"{subject} average: {average:.2f}")

    best_subject = subject_averages.idxmax()
    print("Best-performing subject:", best_subject)


def display_top_performers(data):
    """Display the top five students by average marks."""
    print("\n========== TOP PERFORMERS ==========")

    top_students = data.sort_values(
        by=["Average_Marks", "Name"],
        ascending=[False, True]
    ).head(5)

    print(
        top_students[
            ["Student_ID", "Name", "Average_Marks", "Grade"]
        ].to_string(index=False)
    )

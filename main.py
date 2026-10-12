
import pandas as pd

from functions import (
    process_students,
    display_class_summary,
    display_subject_analysis,
    display_top_performers,
)


def main():
    """Run the Student Performance Analytics System."""
    try:
        # Step 1: Load the dataset
        data = pd.read_csv("students.csv")

        # Step 2: Validate required columns
        required_columns = [
            "Student_ID", "Name", "Department",
            "Python", "Mathematics", "AI", "Attendance"
        ]

        missing_columns = [
            column for column in required_columns
            if column not in data.columns
        ]

        if missing_columns:
            print("Missing columns:", missing_columns)
            return

        if data.empty:
            print("The student dataset is empty.")
            return

        if data[required_columns].isnull().any().any():
            print("The dataset contains missing values. Please correct them.")
            return

        mark_columns = ["Python", "Mathematics", "AI", "Attendance"]

        for column in mark_columns:
            if not data[column].between(0, 100).all():
                print(f"Invalid values found in {column}. Use 0–100.")
                return

        # Step 3: Display dataset information
        print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
        print("=" * 60)
        print("\nSTUDENT DATA")
        print(data.to_string(index=False))
        print("\nNumber of records:", len(data))
        print("\nDATASET INFORMATION")
        data.info()

        # Step 4: Process student records
        data = process_students(data)

        # Step 5: Display individual student results
        print("\n========== STUDENT RESULTS ==========")
        print(
            data[
                [
                    "Student_ID", "Name", "Department",
                    "Total_Marks", "Average_Marks",
                    "Grade", "Result", "Attendance"
                ]
            ].to_string(index=False)
        )

        # Step 6: Display class and subject analysis
        display_class_summary(data)
        display_subject_analysis(data)
        display_top_performers(data)

        # Step 7: Save the analyzed results
        data.to_csv("student_analysis_results.csv", index=False)
        print("\nAnalysis saved to student_analysis_results.csv")
        print("\nProject executed successfully!")

    except FileNotFoundError:
        print("Error: students.csv was not found in the project folder.")
    except pd.errors.EmptyDataError:
        print("Error: students.csv is empty.")
    except (ValueError, TypeError) as error:
        print("Please check your dataset:", error)


if __name__ == "__main__":
    main()

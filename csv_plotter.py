import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("=== CSV Plotter Utility ===")

    # 1. Load CSV file
    file_path = input("Enter the path to your CSV file: ").strip()
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # Show available columns
    print("\nAvailable columns:")
    for i, col in enumerate(df.columns):
        print(f"{i+1}. {col}")

    # 2. User chooses X and Y axes
    try:
        x_col = input("\nEnter column name for X-axis: ").strip()
        y_col = input("Enter column name for Y-axis: ").strip()

        if x_col not in df.columns or y_col not in df.columns:
            print("Invalid column names. Please try again.")
            return
    except Exception as e:
        print(f"Error: {e}")
        return

    # 3. Choose chart type
    chart_type = input("\nChoose chart type (line/bar): ").strip().lower()
    if chart_type not in ["line", "bar"]:
        print("Invalid chart type. Defaulting to line chart.")
        chart_type = "line"

    # 4. Plot data
    plt.figure(figsize=(8, 6))
    if chart_type == "line":
        plt.plot(df[x_col], df[y_col], marker="o", linestyle="-", color="blue")
    elif chart_type == "bar":
        plt.bar(df[x_col], df[y_col], color="green")

    plt.title(f"{chart_type.capitalize()} Chart of {y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
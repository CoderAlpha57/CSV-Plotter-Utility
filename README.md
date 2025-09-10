# CSV-Plotter-Utility
This is a simple Python utility that allows users to visualize CSV data by choosing X and Y columns and selecting either a line chart or bar chart.
It was built as part of the AI Intern Assignment.

### Requirements
Python 3.8 or higher
Libraries:
pandas
matplotlib
You can install all requirements using the provided requirements.txt file.

### Setup & Running

1. Install dependencies
   Open a terminal in the project folder and run:
   
   pip install -r requirements.txt

2. Run the script
   Execute the Python file:

   python.exe csv_plotter.py

   If using a specific conda environment, activate it first then run the above script:

   conda activate venv

3. Provide CSV file path

    When prompted it will show in terminal:
   
    Enter the path to your CSV file:(Enter the path of the csv file)

4. Choose X and Y columns
   The script will display all available columns in the CSV. Example:

   Available columns:
1. Name
2. Age
3. Score
4. Hours_Studied

Enter column name for X-axis: Name
Enter column name for Y-axis: Score

5. Select chart type
   You will be asked:

   Choose chart type (line/bar): bar

6. View the result
   A matplotlib window will open showing the chart of your selected columns.

   Example use cases:
   Plot Name vs Score (bar chart).
   Plot Hours_Studied vs Score (line chart).

### Notes
 The script automatically validates column names and chart type.
 If you enter invalid input, it will ask again or use defaults.

**AI Tools Used**
 ChatGpt(OpenAI-GPT5)

## Manual Edits Made

While the initial version of the script was generated using ChatGPT, I made the following manual improvements:

1. **Error Handling**
   - Added try/except blocks for CSV loading and invalid column names.
   - Ensured that if the user enters an invalid chart type, the script defaults to "line" chart.

2. **User Experience**
   - Printed available column names before asking for X and Y axes.
   - Added clear instructions and prompts for better usability.

3. **Code Readability**
   - Reformatted code with proper indentation and spacing.
   - Used meaningful variable names (`x_col`, `y_col`, `chart_type`) instead of generic names.

4. **Flexibility**
   - Allowed both uppercase/lowercase input for chart type (`Line`, `line`, `Bar`, `bar`).
   - Tightened layout using `plt.tight_layout()` so charts render cleanly without overlapping labels.

5. **Testing**
   - Created and tested the script with a custom `sample.csv` file to verify functionality.
   - Checked both small datasets (students’ scores) and larger datasets for robustness.



https://github.com/user-attachments/assets/6cafc5dc-158a-4f13-8ec3-a349922b97ca


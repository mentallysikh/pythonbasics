import csv
import os

def visualize_csv_as_table(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = list(csv.reader(f))
            if not reader:
                print("The CSV file is empty.")
                return

            # Clean up whitespace from each cell
            data = [[cell.strip() for cell in row] for row in reader]

            # 1. Calculate the maximum width needed for each column
            # This ensures the borders align perfectly
            col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]

            # 2. Define the horizontal border line
            # Format: +------------+-------+
            border_line = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

            print("\nOutput:\n")
            print(border_line)

            for i, row in enumerate(data):
                # 3. Format each row with pipe separators and padding
                formatted_row = "| " + " | ".join(str(val).ljust(col_widths[j]) for j, val in enumerate(row)) + " |"
                print(formatted_row)

                # 4. Add a separator line after the header
                if i == 0:
                    print(border_line)

            # 5. Add the bottom border
            print(border_line)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create a dummy CSV for the demo if it doesn't exist
    demo_file = "data.csv"
    if not os.path.exists(demo_file):
        with open(demo_file, "w") as f:
            f.write("Name,Age,Department\nAlice,30,HR\nBob,25,Engineering\nCharlie,35,Marketing\nDiana,28,Sales")
    
    visualize_csv_as_table(demo_file)
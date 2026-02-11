import tkinter as tk

# Each inner list represents one row of buttons
button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

# Operators on the right side
right_symbols = ["+", "-", "*", "/"]

# Special buttons at the top
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])


color_light_gray = "#f0f0f0"
color_black = "#000000"
color_dark_gray = "#a9a9a9"
color_orange = "#ff9500"
color_white = "#ffffff"

# set up main window
window = tk.Tk()                 # Create main window
window.title("Calculator")      # Set window title
window.resizable(0, 0)          # Prevent resizing

frame = tk.Frame(window)        # Create frame
frame.pack()                    # Place frame

# Display label (screen of the calculator)
label = tk.Label(
    frame,
    text="0",
    font=("Arial", 45),
    bg=color_black,
    fg=color_white,
    anchor="e",
    width=column_count
)

# Place label at the top
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

# calculator memory
A = "0"          # First number
B = None         # Second number
operator = None # Operator (+, -, *, /)

# function to remove .0 from numbers like 5.0 -> 5
def remove_zero_decimal(num):
    """
    Removes .0 from numbers like 5.0 -> 5
    """
    if num % 1 == 0:
        num = int(num)
    return str(num)


def clear_all():
    """
    Resets the calculator memory
    """
    global A, B, operator
    A = "0"
    B = None
    operator = None

def button_clicked(value):
    """
    Handles all button click logic
    """
    global A, B, operator

    # If operator pressed
    if value in right_symbols:
        A = label["text"]
        operator = value
        label["text"] = "0"

    # If equals pressed
    elif value == "=":
        if operator:
            B = label["text"]

            numA = float(A)
            numB = float(B)

            # Perform calculation
            if operator == "+":
                result = numA + numB
            elif operator == "-":
                result = numA - numB
            elif operator == "*":
                result = numA * numB
            elif operator == "/":
                result = numA / numB

            # Display result
            label["text"] = remove_zero_decimal(result)

            # Reset memory
            clear_all()

    # If top buttons pressed
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    # If number or decimal pressed
    else:
        if value == ".":
            # Only allow one decimal point
            if "." not in label["text"]:
                label["text"] += value
        else:
            # Replace starting zero
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value

# create buttons based on the button_values layout
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]

        # Skip empty spaces
        if value == "":
            continue

        # Create button
        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 20),
            width=4,
            height=2,
            command=lambda v=value: button_clicked(v)
        )

        # Place button in grid
        button.grid(row=row + 1, column=column)

        # Style buttons
        if value in top_symbols:
            button.config(bg=color_light_gray)
        elif value in right_symbols or value == "=":
            button.config(bg=color_orange, fg=color_white)
        else:
            button.config(bg=color_dark_gray)

# Start the main event loop
window.mainloop()


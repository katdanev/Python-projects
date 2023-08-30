# This program is written by Kateryna Danevych
# Date written 22/07/2023

# Graph


# Import required libraries
# import matplotlib.pyplot as plt (you asked to wrote used libraries)
import matplotlib.pyplot as plt


x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = []

# Main program

while True:
    for month in x_axis:
        y_axisAmt = float(input(f"Enter total sales for {month}: "))
        y_axis.append(y_axisAmt)

    plt.figure(figsize=(10, 6))
    plt.bar(x_axis, y_axis, color="skyblue")

    plt.xlabel("Months")
    plt.ylabel("Total Sales in $ ")
    plt.title("Total Sales by Month ")

    plt.show()

    while True:
            Continue = input("Do you want to continue (Y/N)? ").upper()
            if Continue == "":
                print("Error - Continue cannot be blank. ")
            elif Continue != "Y" and Continue != "N":
                print("Error - Continue must be Y or N. ")
            else:
                break

    if Continue == "N":
        break

# Housekeeping
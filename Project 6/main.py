# Description - Sprint # 2
# Authors: Ellen Dalton, Corina Jewer, Matthew Menchinton, Bradley Hiscock, Patrick Layman and Kateryna Danevych
# Date started: August 4, 2023
# Date finished:

# Import required libraries
import math
import datetime
import FormatValues as FV
from tqdm import tqdm
import time
curr_date = datetime.datetime.now()

# Open defaults file and read values into variables

f = open('Defaults.dat', 'r')

NEXT_TRANSACTION_NUM = int(f.readline())
NEXT_DRIVER_NUM = int(f.readline())
MONTHLY_STAND_FEE = float(f.readline())
DAILY_RENTAL_FEE = float(f.readline())
WEEKLY_RENTAL_FEE = float(f.readline())
HST_RATE = float(f.readline())

f.close()

# Define required functions


def new_employee():
    # Option 1 - Enter a new employee (driver)

    global NEXT_DRIVER_NUM
    global NEXT_TRANSACTION_NUM

    while True:
        # Inputs
        while True:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
            first_name = input("Enter the first name: ").title()
            if first_name == "":
                print("Error - employee's first name cannot be blank.")
            elif not set(first_name).issubset(allowed_char):
                print("Error - employee's first name contains invalid characters.")
            else:
                break

        while True:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
            last_name = input("Enter the last name: ").title()
            if last_name == "":
                print("Error - employee's last name cannot be blank.")
            elif not set(last_name).issubset(allowed_char):
                print("Error - employee's last name contains invalid characters.")
            else:
                break

        street_address = input("Enter the street address: ").title()

        city = input("Enter the city: ").title()

        while True:
            province_lst = ["NL", "NS", "PE", "NB", "QB", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
            province = input("Enter the province (LL): ").upper()
            if province == "":
                print("Error - province cannot be blank.")
            elif len(province) != 2:
                print("Error - province must be 2 letters only.")
            elif province not in province_lst:
                print("Error - not a valid province.")
            else:
                break

        postal_code = input("Enter the postal code (A1A2B2): ").upper()

        while True:
            allowed_char = set("0123456789")
            phone_num = input("Enter the phone number (9999999999): ")
            if phone_num == "":
                print("Error - phone number cannot be blank.")
                break
            elif len(phone_num) != 10:
                print("Error - phone number must be 10 digits only.")
            elif not set(phone_num).issubset(allowed_char):
                print("Error - phone number contains invalid characters.")
            else:
                break

        drivers_licence_num = input("Enter the drivers licence number: ").upper()

        while True:
            allowed_char = set("0123456789/")
            exp_date = input("Enter the expiry date (YYYY/MM/DD): ")
            if exp_date == "":
                print("Error - expiry date cannot be blank.")
            elif len(exp_date) != 10:
                print("Error - expiry date must be 10 characters long, in the YYYY/MM/DD format.")
            elif not set(exp_date).issubset(allowed_char):
                print("Error - expiry date contains invalid characters.")
            elif exp_date[4] != "/" and exp_date[7] != "/":
                print("Error - expiry date must be in the YYYY/MM/DD format.")
            elif not exp_date[0:4].isdigit() and exp_date[5:7].isdigit() and exp_date[8:10].isdigit():
                print("Error - expiry date must be in the YYYY/MM/DD format.")
            else:
                break

        insurance_company = input("Enter the insurance policy company: ")

        policy_num = input("Enter the insurance policy number: ")

        f = open("rentalcars.dat", "r")
        avail_car_num_lst = []  # Make available_car_num_list that includes n/a
        # values for cars that aren't available.
        car_data_lst = []  # Make car_data_lst that includes all car data.
        rental_status_lst = [] # Make a rental_status_lst that includes all rental status data.
        for cars_data_line in f:
            cars_line = cars_data_line.split(",")
            car_num = cars_line[0].strip()
            car_year = cars_line[1].strip()
            car_make = cars_line[2].strip()
            car_model = cars_line[3].strip()
            car_VIN = cars_line[4].strip()
            car_purchase_price = cars_line[5].strip()
            car_rental_status = cars_line[6].strip()

            if car_rental_status == "Available":
                avail_car_num = cars_line[0].strip()
                avail_car_num_lst.append(avail_car_num)
            if car_rental_status == "Rented":
                avail_car_num_lst.append("n/a")

            car_data_lst.append(car_num)
            car_data_lst.append(car_year)
            car_data_lst.append(car_make)
            car_data_lst.append(car_model)
            car_data_lst.append(car_VIN)
            car_data_lst.append(car_purchase_price)
            car_data_lst.append(car_rental_status)

            rental_status_lst.append(car_rental_status)

        f.close()

        while True:
            allowed_char = set("OR")
            own_or_rental = input("Enter the type of car you will use (O for own car or R for rental): ").upper()
            if own_or_rental == "":
                print("Error - Type of car used cannot be blank")
            elif len(own_or_rental) != 1:
                print("Error - Type of car used must be O or R only.")
            elif not set(own_or_rental).issubset(allowed_char):
                print("Error - Type of car used must be O or R only.")
            else:
                if own_or_rental == "R" and rental_status_lst[0] == "Rented" and rental_status_lst[1] == "Rented" and \
                        rental_status_lst[2] == "Rented" and rental_status_lst[3] == "Rented":
                    print("Error - There are no rental cars available at this time. Please re-enter.")
                else:
                    break

        if own_or_rental == "R":
            while True:
                try:
                    num_days_for_rental = int(input("Enter the number of days a rental is needed (must be 1 or more): "))
                    num_weeks_for_rental = num_days_for_rental / 7
                except:
                    print("Number is not a valid number - please re-enter.")
                else:
                    if num_days_for_rental < 1:
                        print("Number must be 1 or more - please re-enter.")
                    else:
                        break

        # Calculations

        if own_or_rental == "R" and num_days_for_rental < 7:
            balance_due = num_days_for_rental * DAILY_RENTAL_FEE
        elif own_or_rental == "R" and num_days_for_rental % 7 == 0:
            balance_due = num_weeks_for_rental * WEEKLY_RENTAL_FEE
        elif own_or_rental == "R" and num_days_for_rental > 7 and num_days_for_rental % 7 != 0:
            rounded_num_weeks_for_rental = math.floor(num_weeks_for_rental)
            decimal_portion_of_week = num_weeks_for_rental - rounded_num_weeks_for_rental
            days = decimal_portion_of_week * 7
            balance_due = (rounded_num_weeks_for_rental * WEEKLY_RENTAL_FEE) + (days * DAILY_RENTAL_FEE)
        else:
            balance_due = MONTHLY_STAND_FEE

        hst_on_bal = balance_due * HST_RATE

        total_balance_due = balance_due + hst_on_bal

        # Output
        print("-----------------------------------------------------------")
        print(f"                  Employee Information")
        print("-----------------------------------------------------------")
        print(f"Date: {curr_date.strftime('%Y-%m-%d')}                        Driver Number: {NEXT_DRIVER_NUM:>4d}")
        print()
        driver_name = first_name + " " + last_name
        phone_num_dsp = f"{phone_num[0]}{phone_num[1]}{phone_num[2]}-{phone_num[3]}{phone_num[4]}{phone_num[5]}-{phone_num[6]}{phone_num[7]}{phone_num[8]}{phone_num[9]}"

        print(f"Name:    {driver_name:<20s}    Phone Number: {phone_num_dsp:>12s}")
        print()
        print(f"Address: {street_address:<20s}    Licence Number: {drivers_licence_num:>10s}")
        city_prov_dsp = f"{city}, {province}"
        print(f"         {city_prov_dsp:<20s}    Expiry Date:    {exp_date:>10s}")
        print(f"         {postal_code:<6s}")
        print()
        if own_or_rental == "O":
            own_or_rental = "Own"
            print(f"Insurance Company: {insurance_company:<10s}                 Car Type: {own_or_rental:>3s}")
            print(f"Policy Number: {policy_num:<10s}")
        if own_or_rental == "R":
            own_or_rental = "Rental"
            print(f"Insurance Company: {insurance_company:10s}            Car Type:   {own_or_rental:>6s}")
            print(f"Policy Number: {policy_num:<10s}                Duration: {num_days_for_rental:>3d} days")
            for i in avail_car_num_lst:
                if i != "n/a":
                    car_num_rented = i
                    print(f"                                         Car Number: {car_num_rented}")
                    break
        print("-----------------------------------------------------------")
        print(f"                Subtotal:   ${balance_due:>8.2f}")
        print(f"                HST:        ${hst_on_bal:>8.2f}")
        print(f"                Total:      ${total_balance_due:>8.2f}")
        print("-----------------------------------------------------------")

        # Write the employee data to a text file.
        f = open("Employees.dat", "a")

        f.write(f"{curr_date.strftime('%Y-%m-%d')}, ")
        f.write(f"{NEXT_DRIVER_NUM}, ")
        f.write(f"{first_name}, ")
        f.write(f"{last_name}, ")
        f.write(f"{street_address}, ")
        f.write(f"{city}, ")
        f.write(f"{province}, ")
        f.write(f"{postal_code}, ")
        f.write(f"{phone_num}, ")
        f.write(f"{drivers_licence_num}, ")
        f.write(f"{exp_date}, ")
        f.write(f"{insurance_company}, ")
        f.write(f"{policy_num}, ")
        f.write(f"{own_or_rental}, ")
        if own_or_rental == "Rental":
            f.write(f"{num_days_for_rental} days, ")
            f.write(f"{car_num_rented}, ")
        if own_or_rental == "Own":
            f.write("n/a, ")
            f.write("n/a, ")
        f.write(f"{balance_due:.2f}, ")
        f.write(f"{hst_on_bal:.2f}, ")
        f.write(f"{total_balance_due:.2f}\n")

        f.close()

        # Create a progress bar...
        # Define the total number of iterations
        total_iterations = 100

        # Create a loop and wrap it with tqdm
        for i in tqdm(range(total_iterations), bar_format="{desc}: Saving in progress: {bar} {percentage:3.0f}%", ncols=57):
            # Simulate some work
            time.sleep(0.03)
        print()
        print("Employee information has been saved.")
        print()

        # If it is the first of the month, add monthly stand fee & associated transaction info to the revenue table.
        if curr_date.day == 1:
            revenue = MONTHLY_STAND_FEE
            hst_on_revenue = revenue * HST_RATE
            total_revenue = revenue + hst_on_revenue

            f = open("Revenues.dat", "a")

            f.write(f"{NEXT_TRANSACTION_NUM}, ")
            NEXT_TRANSACTION_NUM += 1
            f.write(f"{curr_date.strftime('%Y-%m-%d')}, ")
            if own_or_rental == "Rental":
                f.write(f"{car_num_rented}, ")
            if own_or_rental == "Own":
                f.write("n/a, ")
            f.write("Monthly Stand Fees, ")
            f.write(f"{NEXT_DRIVER_NUM}, ")
            f.write(f"{MONTHLY_STAND_FEE}, ")
            f.write(f"{hst_on_revenue}, ")
            f.write(f"{total_revenue}\n")

            f.close()
            print("monthly stand fee & associated transaction info has been added to the revenue table.")


        NEXT_DRIVER_NUM += 1

        # Re-write the Defaults.dat file

        f = open("Defaults.dat", "w")

        f.write(f"{str(NEXT_TRANSACTION_NUM)}\n")
        f.write(f"{str(NEXT_DRIVER_NUM)}\n")
        f.write(f"{str(MONTHLY_STAND_FEE)}\n")
        f.write(f"{str(DAILY_RENTAL_FEE)}\n")
        f.write(f"{str(WEEKLY_RENTAL_FEE)}\n")
        f.write(f"{str(HST_RATE)}\n")

        f.close()

        print("Defaults.dat file has been re-written")

        # # Change the availability to "Rented" in the rentalcars.dat file (re-write).

        # Open the rentalcars.dat file in write mode
        f = open("rentalcars.dat", "w")

        # Make separate lists for each of the cars.
        target_lst_1 = []
        target_lst_2 = []
        target_lst_3 = []
        target_lst_4 = []

        target_lst_1.append(car_data_lst[0])
        target_lst_1.append(car_data_lst[1])
        target_lst_1.append(car_data_lst[2])
        target_lst_1.append(car_data_lst[3])
        target_lst_1.append(car_data_lst[4])
        target_lst_1.append(car_data_lst[5])
        target_lst_1.append(car_data_lst[6])

        target_lst_2.append(car_data_lst[7])
        target_lst_2.append(car_data_lst[8])
        target_lst_2.append(car_data_lst[9])
        target_lst_2.append(car_data_lst[10])
        target_lst_2.append(car_data_lst[11])
        target_lst_2.append(car_data_lst[12])
        target_lst_2.append(car_data_lst[13])

        target_lst_3.append(car_data_lst[14])
        target_lst_3.append(car_data_lst[15])
        target_lst_3.append(car_data_lst[16])
        target_lst_3.append(car_data_lst[17])
        target_lst_3.append(car_data_lst[18])
        target_lst_3.append(car_data_lst[19])
        target_lst_3.append(car_data_lst[20])

        target_lst_4.append(car_data_lst[21])
        target_lst_4.append(car_data_lst[22])
        target_lst_4.append(car_data_lst[23])
        target_lst_4.append(car_data_lst[24])
        target_lst_4.append(car_data_lst[25])
        target_lst_4.append(car_data_lst[26])
        target_lst_4.append(car_data_lst[27])

        if own_or_rental == "Rental" and car_num_rented == "1":
            f.write(f"{target_lst_1[0]}, {target_lst_1[1]}, {target_lst_1[2]}, {target_lst_1[3]}, {target_lst_1[4]},"
                    f" {target_lst_1[5]}, Rented\n")
            f.write(
                f"{target_lst_2[0]}, {target_lst_2[1]}, {target_lst_2[2]}, {target_lst_2[3]}, {target_lst_2[4]},"
                f" {target_lst_2[5]}, {target_lst_2[6]}\n")
            f.write(
                f"{target_lst_3[0]}, {target_lst_3[1]}, {target_lst_3[2]}, {target_lst_3[3]}, {target_lst_3[4]},"
                f" {target_lst_3[5]}, {target_lst_3[6]}\n")
            f.write(
                f"{target_lst_4[0]}, {target_lst_4[1]}, {target_lst_4[2]}, {target_lst_4[3]}, {target_lst_4[4]},"
                f" {target_lst_4[5]}, {target_lst_4[6]}\n")
            target_lst_1.pop(6)
            target_lst_1.insert(6, "Rented")

        if own_or_rental == "Rental" and car_num_rented == "2":
            f.write(f"{target_lst_1[0]}, {target_lst_1[1]}, {target_lst_1[2]}, {target_lst_1[3]}, {target_lst_1[4]},"
                    f" {target_lst_1[5]}, {target_lst_1[6]}\n")
            f.write(
                f"{target_lst_2[0]}, {target_lst_2[1]}, {target_lst_2[2]}, {target_lst_2[3]}, {target_lst_2[4]},"
                f" {target_lst_2[5]}, Rented\n")
            f.write(
                f"{target_lst_3[0]}, {target_lst_3[1]}, {target_lst_3[2]}, {target_lst_3[3]}, {target_lst_3[4]},"
                f" {target_lst_3[5]}, {target_lst_3[6]}\n")
            f.write(
                f"{target_lst_4[0]}, {target_lst_4[1]}, {target_lst_4[2]}, {target_lst_4[3]}, {target_lst_4[4]},"
                f" {target_lst_4[5]}, {target_lst_4[6]}\n")
            target_lst_2.pop(6)
            target_lst_2.insert(6, "Rented")

        if own_or_rental == "Rental" and car_num_rented == "3":
            f.write(f"{target_lst_1[0]}, {target_lst_1[1]}, {target_lst_1[2]}, {target_lst_1[3]}, {target_lst_1[4]},"
                    f" {target_lst_1[5]}, {target_lst_1[6]}\n")
            f.write(
                f"{target_lst_2[0]}, {target_lst_2[1]}, {target_lst_2[2]}, {target_lst_2[3]}, {target_lst_2[4]},"
                f" {target_lst_2[5]}, {target_lst_2[6]}\n")
            f.write(
                f"{target_lst_3[0]}, {target_lst_3[1]}, {target_lst_3[2]}, {target_lst_3[3]}, {target_lst_3[4]},"
                f" {target_lst_3[5]}, Rented\n")
            f.write(
                f"{target_lst_4[0]}, {target_lst_4[1]}, {target_lst_4[2]}, {target_lst_4[3]}, {target_lst_4[4]},"
                f" {target_lst_4[5]}, {target_lst_4[6]}\n")
            target_lst_3.pop(6)
            target_lst_3.insert(6, "Rented")
        if own_or_rental == "Rental" and car_num_rented == "4":
            f.write(f"{target_lst_1[0]}, {target_lst_1[1]}, {target_lst_1[2]}, {target_lst_1[3]}, {target_lst_1[4]},"
                    f" {target_lst_1[5]}, {target_lst_1[6]}\n")
            f.write(
                f"{target_lst_2[0]}, {target_lst_2[1]}, {target_lst_2[2]}, {target_lst_2[3]}, {target_lst_2[4]},"
                f" {target_lst_2[5]}, {target_lst_2[6]}\n")
            f.write(
                f"{target_lst_3[0]}, {target_lst_3[1]}, {target_lst_3[2]}, {target_lst_3[3]}, {target_lst_3[4]},"
                f" {target_lst_3[5]}, {target_lst_3[6]}\n")
            f.write(
                f"{target_lst_4[0]}, {target_lst_4[1]}, {target_lst_4[2]}, {target_lst_4[3]}, {target_lst_4[4]},"
                f" {target_lst_4[5]}, Rented\n")
            target_lst_4.pop(6)
            target_lst_4.insert(6, "Rented")
        if own_or_rental == "Own":
            f.write(
                f"{target_lst_1[0]}, {target_lst_1[1]}, {target_lst_1[2]}, {target_lst_1[3]}, {target_lst_1[4]},"
                f" {target_lst_1[5]}, {target_lst_1[6]}\n")
            f.write(
                f"{target_lst_2[0]}, {target_lst_2[1]}, {target_lst_2[2]}, {target_lst_2[3]}, {target_lst_2[4]},"
                f" {target_lst_2[5]}, {target_lst_2[6]}\n")
            f.write(
                f"{target_lst_3[0]}, {target_lst_3[1]}, {target_lst_3[2]}, {target_lst_3[3]}, {target_lst_3[4]},"
                f" {target_lst_3[5]}, {target_lst_3[6]}\n")
            f.write(
                f"{target_lst_4[0]}, {target_lst_4[1]}, {target_lst_4[2]}, {target_lst_4[3]}, {target_lst_4[4]},"
                f" {target_lst_4[5]}, {target_lst_4[6]}\n")
        f.close()

        print("rentalcars.dat has been re-written.")

        while True:
            allowed_char = set("YN")
            Continue = input("Do you want to continue (Y/N)? ").upper()
            if Continue == "":
                print("Error - you must enter Y or N.")
            elif len(Continue) != 1:
                print("Error - you must enter Y or N only.")
            elif not set(Continue).issubset(allowed_char):
                print("Error - you must enter Y or N only")
            else:
                break
        if Continue == "N":
            break

def driver_financial_listing():
    #  Option #7 - Driver Financial Listing

    import datetime
    import FormatValues as FV
    # Initialize variables for analytics
    stand_fees_total = 0
    cab_fare_total = 0
    car_num_one_total = 0
    car_num_two_total = 0
    car_num_three_total = 0
    car_num_four_total = 0
    car_owned_by_driver_total = 0

    # List to store transaction data
    transactions = []

    # Read data from the "Revenues.dat" file
    with open("Revenues.dat", "r") as file:
        lines = file.readlines()

    # Process each line of data from the file
    for line in lines:
        data = line.strip().split(", ")
        transaction_number = int(data[0])
        transaction_date = datetime.datetime.strptime(data[1], "%Y-%m-%d").strftime("%m/%d/%Y")
        car_num = data[2]
        description = data[3]
        driver_number = data[4]
        trans_cost = float(data[5])
        hst = float(data[6])
        total = float(data[7])

        # Append transaction data to the list
        transactions.append({
            "Transaction Number": transaction_number,
            "Transaction Date": transaction_date,
            "Car Number": car_num,
            "Description": description,
            "Driver Number": driver_number,
            "Transaction Cost": trans_cost,
            "HST": hst,
            "Total": total
        })

        # Perform calculations for analytics
        if description == "Monthly Stand Fees":
            stand_fees_total += total
        elif description == "Cab Fare":
            cab_fare_total += total

        if car_num == "1":
            car_num_one_total += total
        if car_num == "2":
            car_num_two_total += total
        if car_num == "3":
            car_num_three_total += total
        if car_num == "4":
            car_num_four_total += total
        if car_num == "n/a":
            car_owned_by_driver_total += total

    # Print Driver Financial Listing
    print()
    print("HAB Taxi Services")
    print()
    print(f"Driver Financial Listing Report as of {curr_date.strftime('%Y-%m-%d')}")
    print("-" * 104)
    print(f"Transaction | Transaction |     Description     |  Driver  |  Car   | Transaction |    HST    |    Total")
    print(f"  Number    |    Date     |                     |  Number  | Number |    Cost     |           |         ")
    print("-" * 104)

    # Print the transaction data
    for transaction in transactions:
        print(
            f"   {transaction['Transaction Number']:>3d}        {transaction['Transaction Date']:>10s}    {transaction['Description']:<20s}"
            f"    {transaction['Driver Number']:>4s}      {transaction['Car Number']:>3s}      ${transaction['Transaction Cost']:>7.2f}"
            f"     ${transaction['HST']:>7.2f}    ${transaction['Total']:>7.2f}")

    # Calculate total counter values
    total_transactions = len(transactions)
    total_trans_cost = sum(transaction['Transaction Cost'] for transaction in transactions)
    total_hst = sum(transaction['HST'] for transaction in transactions)
    total_final_total = sum(transaction['Total'] for transaction in transactions)

    # Print total counter
    print("-" * 104)
    print(f"Total Transactions: {total_transactions:>3d}" + (
                " " * 46) + f"${total_trans_cost:>9.2f}   ${total_hst:>9.2f}  ${total_final_total:>9.2f}")

    # Print analytics data
    print("-" * 104)
    print()
    print("Analytics Data:")
    print()
    print(f"    Total Monthly Stand Fees:   ${stand_fees_total:>8.2f}")
    print(f"    Total Cab Fare:             ${cab_fare_total:>8.2f}")
    print(f"    -------------------------------------")
    print(f"    Car Number 1 Revenue:       ${car_num_one_total:8.2f}")
    print(f"    Car Number 2 Revenue:       ${car_num_two_total:8.2f}")
    print(f"    Car Number 3 Revenue:       ${car_num_three_total:8.2f}")
    print(f"    Car Number 4 Revenue:       ${car_num_four_total:8.2f}")
    print(f"    Revenue from Cars")
    print(f"    Owned by Drivers:           ${car_owned_by_driver_total:8.2f}")
    print(f"    -------------------------------------")
    print(f"    Total Revenue:              ${stand_fees_total + cab_fare_total:>8.2f}")
    print()


def our_report():
    # Our Report = Rental Inventory Listing that compares total expenses and total revenue
    # Before Loop -  Print Headings, Initialize Counters & Accumulators, Open File.
    print()
    print("HAB TAXI SERVICES")
    print(f"RENTAL INVENTORY LISTING AS OF {FV.FDateM(curr_date)}")
    print()
    print("CAR  YEAR   MAKE       MODEL      VIN        PURCHASE PRICE    STATUS      TOTAL EXPENSES  TOTAL REVENUE")
    print("                                                                           (before taxes)  (before taxes)")
    print("=========================================================================================================")

    TotCarCtr = 0
    TotExpAcc = 0
    TotRevAcc = 0

    f = open("rentalcars.dat", "r")
    for CarsDataLine in f:

        CarsLine = CarsDataLine.split(",")

        CarNum = CarsLine[0].strip()
        Year = CarsLine[1].strip()
        Make = CarsLine[2].strip()
        Model = CarsLine[3].strip()
        VIN = CarsLine[4].strip()
        PurchasePrice = float(CarsLine[5].strip())
        RentalStat = CarsLine[6].strip()

        TotalExp = 0
        f = open("expenses.dat", "r")
        for ExpenseDataLine in f:
            ExpenseLine = ExpenseDataLine.split(",")
            SubTotal = float(ExpenseLine[4].strip())
            if ExpenseLine[2].strip() == CarNum:
                TotalExp += SubTotal

        TotalRev = 0
        f = open("Revenues.dat", "r")
        for RevenueDataLine in f:
            RevenueLine = RevenueDataLine.split(",")
            TransCost = float(RevenueLine[5].strip())
            if RevenueLine[2].strip() == CarNum:
                TotalRev += TransCost

        # Detailed Line

        print(
            f" {CarNum:<2s}  {Year:<4s}   {Make:<10s} {Model:<10s} {VIN:<8s}       {FV.FDollar2(PurchasePrice):>10s}  "
            f"  {RentalStat:<9s}       {FV.FDollar2(TotalExp):>10s}      {FV.FDollar2(TotalRev):>10s}")

        # Increment Counters & Accumulators

        TotCarCtr += 1
        TotExpAcc += TotalExp
        TotRevAcc += TotalRev

    # Close File

    f.close()
    f.close()
    f.close()

    print("=========================================================================================================")

    print(f"TOTAL RENTAL INVENTORY: {TotCarCtr:<3d}                                                    "
          f"{FV.FDollar2(TotExpAcc):>10s}      {FV.FDollar2(TotRevAcc):>10s} ")
    print()


# MAIN PROGRAM

# This is where stand fees are automatically charged to drivers on the first day
# of each month when the program is turned on.

if curr_date.day == 1:
    revenue = MONTHLY_STAND_FEE
    hst_on_revenue = revenue * HST_RATE
    total_revenue = revenue + hst_on_revenue

    f = open('Employees.dat', 'r')
    driver_num_lst = []
    car_num_rented_lst = []
    for emp_data_line in f:
        emp_line = emp_data_line.split(",")
        driver_num = int(emp_line[1].strip())
        driver_num_lst.append(driver_num)
        car_num_rented = emp_line[15].strip()
        car_num_rented_lst.append(car_num_rented)
    f.close()

    f = open("Revenues.dat", "r")
    rev_driver_num_lst = []
    for rev_data_line in f:
        rev_line = rev_data_line.split(",")
        rev_driver_num = int(rev_line[4].strip())
        rev_driver_num_lst.append(rev_driver_num)
    f.close()

    f = open("Revenues.dat", "a")
    for driver_num in driver_num_lst:
        if driver_num in rev_driver_num_lst:
            continue
        else:
            f.write(f"{NEXT_TRANSACTION_NUM}, ")
            NEXT_TRANSACTION_NUM += 1
            f.write(f"{curr_date.strftime('%Y-%m-%d')}, ")
            for index in range(0, len(car_num_rented_lst)):
                if driver_num == driver_num_lst[index]:
                    f.write(f"{car_num_rented_lst[index]}, ")
            f.write("Monthly Stand Fees, ")
            f.write(f"{driver_num}, ")
            NEXT_DRIVER_NUM += 1
            f.write(f"{MONTHLY_STAND_FEE}, ")
            f.write(f"{hst_on_revenue}, ")
            f.write(f"{total_revenue}\n")
    f.close()

    # Update Defaults.dat file...
    f = open("Defaults.dat", "w")

    f.write(f"{str(NEXT_TRANSACTION_NUM)}\n")
    f.write(f"{str(NEXT_DRIVER_NUM)}\n")
    f.write(f"{str(MONTHLY_STAND_FEE)}\n")
    f.write(f"{str(DAILY_RENTAL_FEE)}\n")
    f.write(f"{str(WEEKLY_RENTAL_FEE)}\n")
    f.write(f"{str(HST_RATE)}\n")

    f.close()

    print()
    print("Stand fees have been automatically charged to drivers and the Defaults.dat file has been updated.")

    # Balance due will now be updated.

while True:
    print()
    print("     HAB Taxi Services")
    print("     Company Services System")
    print()
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Rental Inventory Listing.")
    print("9. Quit Program.")
    print()
    while True:
        try:
            Choice = int(input("   Enter choice (1-9): "))
        except:
            print("Error - choice is not a valid entry.")
        else:
            if Choice < 1 or Choice > 9:
                print("Error - Choice must be between 1 and 9.")
            else:
                break
    if Choice == 1:
        new_employee()
    elif Choice == 2:
        continue  # company_revenues()
    elif Choice == 3:
        continue  # company_expenses()
    elif Choice == 4:
        continue  # car_rentals()
    elif Choice == 5:
        continue  # emp_payment()
    elif Choice == 6:
        continue  # company_profit_listing()
    elif Choice == 7:
        driver_financial_listing()
    elif Choice == 8:
        our_report()
    else:
        break

# Housekeeping
print()
print("Thanks for using HAB Taxi Services Company Services System")
print("Come again soon.")
print()

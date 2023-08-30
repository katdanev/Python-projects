# Written by
# Date written

# The program created for NL Chocolate Company to process salesperson travel claims.

# import libraries
import datetime

# Constants

DAYLY_RATE = 85.00
KM_RATE = 0.17
RENTED_CAR_RATE = 65.00
HST_RATE = 0.15
BONUS1_RATE = 100.00
BONUS2_RATE = 0.04
BONUS3_RATE = 45.00
BONUS4_RATE = 50.00

# function
def FindBonus(TotalDays, CarType, TotalKm, ClaimType, StartDate):

    if TotalDays > 3:
        Bonus1 = BONUS1_RATE  # 100.00
    else:
        Bonus1 = 0

    if CarType == "R":
        Bonus2 = 0

    elif TotalKm > 1000 and CarType == "O":
        Bonus2 = BONUS2_RATE * TotalKm
    else:
        Bonus2 = 0

    if ClaimType == "E":
        Bonus3 = TotalDays * BONUS3_RATE  # 45.00
    else:
        Bonus3 = 0

    # Bonus 4
    if StartDate.month == 12 and 15 <= StartDate.day <= 22:
        Bonus4 = TotalDays * BONUS4_RATE  # 50.00
    else:
        Bonus4 = 0

    Bonus = Bonus1 + Bonus2 + Bonus3 + Bonus4
    Bonus = float(Bonus)

    return Bonus
    # Determine the amount of the bonus


# Inputs

while True:

    while True:
        allowed_num = set("1234567890")
        EmplNumber = input("Enter the employee number: ")
        if EmplNumber == "":
            print("Error - employee number cannot be blank. ")
        elif len(EmplNumber) != 5:
            print("Error - employee number must consist of 5 digits. ")
        elif not EmplNumber.isdigit():
            print("Error - employee number must consist only from digits.")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        FirstName = input("Enter the employee first name: ").title()
        if FirstName == "":
            print("Employee's first name cannot be blank.")
        elif not set(FirstName).issubset(allowed_char):
            print("Error - Employee's first name must consist only from characters.")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        LastName = input("Enter the employee last name: ").title()
        if LastName == "":
            print("Employee's last name cannot be blank.")
        elif not set(LastName).issubset(allowed_char):
            print("Error - Employee's last name must consist only from characters.")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        Location = input("Enter the trip location: ").title()
        if Location == "":
            print("Location cannot be blank.")
        elif not set(Location).issubset(allowed_char):
            print("Error - Location must consist only from characters.")
        else:
            break

    while True:
        try:
            StartDate = input("Enter the trip start date (MM-DD-YYYY): ")
            StartDate = datetime.datetime.strptime(StartDate, "%m-%d-%Y")
        except:
            print("Error - invalid date format. Enter as MM-DD-YYYY. ")
        else:
            break

    while True:
        StartDatePlus7 = StartDate + datetime.timedelta(days=7)
        try:
            EndDate = input("Enter the trip end date (MM-DD-YYYY): ")
            EndDate = datetime.datetime.strptime(EndDate, "%m-%d-%Y")
        except:
            print("Error - invalid date format. Enter as MM-DD-YYYY. ")
        else:
            if EndDate < StartDate:
                print("Error - end date must be biggest than start date")
            elif EndDate > StartDatePlus7:
                print("Error - end date must be no more than 7 days")
            else:
                break

    while True:
        try:
            NumberDays = input("Enter the number of days in the trip: ")
            NumberDays = int(NumberDays)
        except:
            print("Error - invalid km format")
        else:
            if NumberDays == "":
                print("Error - number of days cannot be blank. ")
            elif NumberDays > 7 or NumberDays < 1:
                print("Error - number of days must be between 1 and 7. ")
            else:
                break

    while True:
        allowed_char = set("orOR")
        CarType = input("Did employee use own or rented car (O or R)?: ").upper()
        if CarType == "":
            print("Error - this field cannot be blank. ")
        elif len(CarType) != 1:
            print("Error - car type must consist of 1 letter. ")
        elif not set(CarType).issubset(allowed_char):
            print("Error - car type must be O or R. ")
        else:
            break


    while True:

        if CarType == "O":

            try:
                TotalKm = input("Enter the number of km travelled: ")
                TotalKm = int(TotalKm)
            except:
                print("Error - please enter the valid digits")
            else:
                if TotalKm == "":
                    print("Error - this field cannot be blank. ")
                elif TotalKm > 2000:
                    print("Error - the number of km cannot exceed 2000 km. ")
                else:
                    break
        else:
            break


    while True:
        ClaimType = input("Enter the claim type (S or E): ").upper()
        if ClaimType == "":
            print("Error - this field cannot be blank. ")
        elif ClaimType != "S" and ClaimType != "E":
            print("Error - claim type must be S or E. ")
        else:
            break

    # Calculations

    TotalDays = (EndDate - StartDate).days
    PerDiemAmt = TotalDays * DAYLY_RATE



    if CarType == "O":
        MilAmt = TotalKm * KM_RATE
    else:
        MilAmt = TotalDays * RENTED_CAR_RATE


    if CarType == "R":  #new
        TotalKm = 0

    Bonus = FindBonus(TotalDays, CarType, TotalKm, ClaimType, StartDate)    #function


    ClaimAmt = PerDiemAmt + MilAmt + Bonus
    HST = ClaimAmt * HST_RATE
    ClaimTotal = ClaimAmt + HST

    # Outputs

    print()
    print("                        NL Chocolate Company")

    print("                         TRAVEL CLAIM FORM")
    print("-" * 60)
    print(f"Employee number:                                       {EmplNumber:>5s}")
    print(f"Employee first name:                    {FirstName:>20s}")
    print(f"Employee last name:                     {LastName:>20s}")
    print(f"Trip location:                          {Location:>20s}")
    print()
    StartDateDsp = StartDate.strftime("%m-%d-%Y")
    print(f"Start date:                                       {StartDateDsp:>10s}")
    EndDateDsp = EndDate.strftime("%m-%d-%Y")
    print(f"End date:                                         {EndDateDsp:>10s}")
    print()
    print(f"Number of days:            / {TotalDays:>1d} /")  # is it ok?
    print(f"Car type:                  / {CarType:>1s} /")
    if CarType == "O":
        print(f"Total km travelled:                                     {TotalKm:>4d}")  # d or s?
    print(f"Claim type:                / {ClaimType:>1s} /")
    print()
    PerDiemAmtDsp = "${:,.2f}".format(PerDiemAmt)
    print(f"Per diem amount:                                     {PerDiemAmtDsp:>7s}")
    MilAmtDsp = "${:,.2f}".format(MilAmt)
    print(
        f"Mileage amount:                                      {MilAmtDsp:>7s}")  # print in any case, see the calculations
    BonusDsp = "${:,.2f}".format(Bonus)
    print(f"Bonus:                                               {BonusDsp:>7s}")
    ClaimAmtDsp = "${:,.2f}".format(ClaimAmt)
    print(f"Clam Amount:                                       {ClaimAmtDsp:>9s}")
    print()
    HSTDsp = "${:,.2f}".format(HST)
    print(f"HST:                                                 {HSTDsp:>7s}")
    ClaimTotalDsp = "${:,.2f}".format(ClaimTotal)
    print(f"Claim total:                                       {ClaimTotalDsp:>9s}")
    print("-" * 60)

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

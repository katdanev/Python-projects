
# Description: program for Honest Harry Car Sales to keep track of his sales.

# Written by Kateryna Danevych.

# Date written 07/06/2023

# Import libraries
import datetime


# Constants
HST_RATE = 0.15
TRANSFER_FEE_RATE = 0.01
LUXURY_TAX_RATE = 0.016
FIN_RATE = 39.99

# Main program

while True:
    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-")
        CustFirstName = input("Enter the customer's first name: ").title()
        if CustFirstName =="":
            print("Customer's first name cannot be blank.")
        elif not set (CustFirstName).issubset(allowed_char):
            print("Error - Customer's first name must consist only from characters.")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-")
        CustLastName = input("Enter the customer's last name: ").title()
        if CustLastName =="":
            print("Customer's last name cannot be blank.")
        elif not set (CustLastName).issubset(allowed_char):
            print("Error - Customer's last name must consist only from characters.")
        else:
            break

    while True:
        allowed_num = set("1234567890")
        PhoneNum = input("Enter the customer's phone number (1231235678): ")
        if PhoneNum == "":
            print("Customer's phone number cannot be blank.")
        elif len (PhoneNum) !=10:
            print("Error - the number must consist of 10 digits.")
        elif not PhoneNum.isdigit():
            print ("Error - phone number must consist only from digits.")
        else:
            break

    while True:
        Street = input("Enter the customer's street: ").title()
        if Street == "":
            print("Customer's street cannot be blank.")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        City = input("Enter the city: ").title()
        if City =="":
            print("City cannot be blank.")
        elif not set (City).issubset(allowed_char):
            print("Error - city must consist only from letters.")
        else:
            break

    while True:
        Prov = input("Enter the province (NL, NS, NB, PE): ").upper()  # I used only Atlantic prov
        if Prov == "":
            print("Province cannot be blank.")
        elif len(Prov)!=2:
            print("Error - province must have only 2 characters.")
        elif Prov != "NL" and Prov != "NS" and Prov != "NB" and Prov != "PE":
            print("Error - province is invalid")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ")
        allowed_num = set ("1234567890")
        PostCode = input("Enter the postal code (A1A1A1): ").upper()
        if PostCode == "":
            print("Error - postal code cannot be blank.")
        elif len(PostCode) !=6:
            print("Error - postal code must have only 6 characters.")
        elif not set(PostCode[0]).issubset(allowed_char):
            print("Error - first character in postal code must be a letter. ")
        elif not set(PostCode[2]).issubset(allowed_char):
            print("Error - third character in postal code must be a letter. ")
        elif not set(PostCode[4]).issubset(allowed_char):
            print("Error - fifth character in postal code must be a letter. ")
        elif not set(PostCode[1]).issubset(allowed_num):
            print("Error - second character in postal code must be a number. ")
        elif not set(PostCode[3]).issubset(allowed_num):
            print("Error - fouth character in postal code must be a number. ")
        elif not set(PostCode[5]).issubset(allowed_num):
            print("Error - sixth character in postal code must be a number. ")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-")
        allowed_num = set("1234567890")
        PlateNum = input("Enter the plate number (XXX000): ").upper()
        if PlateNum == "":
            print("Error - plate number cannot be blank.")
        elif len (PlateNum) !=6:
            print("Error - the plate number must consist of 6 characters.")
        elif not set (PlateNum[0:3]).issubset(allowed_char):
            print ("Error - plate number must start with 3 letters.")
        elif not set (PlateNum[3:6]).issubset(allowed_num):
            print ("Error - plate number must end with 3 numbers.")
        elif not set (PlateNum[0]).issubset(allowed_char):  # I think that we don't need this part of the loop below. It contradict each other.
             print("Error - first character must be a letter.")
        elif not set (PlateNum[1]).issubset(allowed_char):
             print("Error - second character must be a letter.")
        elif not set (PlateNum[2]).issubset(allowed_char):
             print("Error - third character must be a letter.")
        elif not set (PlateNum[3]).issubset(allowed_num):  #
             print("Error - fourth character must be a number.")
        elif not set (PlateNum[4]).issubset(allowed_num):
             print("Error - fiths character must be a number.")
        elif not set (PlateNum[5]).issubset(allowed_num):
             print("Error - sixth character must be a number.")
        else:
            break
    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-")
        CarMake = input("Enter the car make: ").capitalize() # I put capitalize, I think it is much better
        if CarMake =="":
            print ("Error - car make cannot be blank.")
        elif not set (CarMake).issubset(allowed_char):
            print("Error - Car make must consist only letters") # but I am not sure, maybe we have a car with numbers?
        else:
            break

    while True:
        alowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-")
        CarModel = input("Enter the car model: ").capitalize()  # I put capitalize, I think it is much better
        if CarModel == "":
            print("Error - car model cannot be blank.")
        elif not set(CarModel).issubset(allowed_char):
            print("Error - Car model must consist only letters")  # but I am not sure, maybe we have a car with numbers?
        else:
            break

    while True:
        allowed_num = set("1234567890")
        Year = input("Enter the year manufactured: ")
        if Year == "":
            print("Error - year cannot be blank.")
        elif not set(Year).issubset(allowed_num):
            print("Error - Year must consist only with numbers")
        elif len (Year) !=4:
            print("Error - the number must consist of 4 digits.")
        else:
            break

    while True:
        SellPrice = input("Enter the selling price: ")
        SellPrice = float(SellPrice)
        if SellPrice > 50000.00:
            print("Error - selling price must not exceed 50000.00")
        else:
            break

    while True:
        AmtTradeIn = input("Enter the amount of the trade in: ")
        AmtTradeIn = float(AmtTradeIn)
        if AmtTradeIn > SellPrice:
            print ("Error - the amount of trade in cannot exceed selling price. ")
        else:
            break

    while True:
        alowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-")
        SalePerName = input("Enter the salespersons name: ").title()
        if SalePerName == "":
            print("Error - car model cannot be blank.")
        elif not set (SalePerName).issubset(allowed_char):
            print("Error - Salespersons name must consist only with letters")
        else:
            break


# Calculations

    PriceAfterTrade = SellPrice - AmtTradeIn

    if SellPrice <= 5000:
        LicenceFee = 75.00
    else:
        LicenceFee = 165.00

    if SellPrice > 20000:
        LuxuryTax = SellPrice * LUXURY_TAX_RATE
    else:
        LuxuryTax = 0

    TransferFee = (SellPrice * TRANSFER_FEE_RATE) + LuxuryTax
    SubTotal = PriceAfterTrade + LicenceFee + TransferFee
    HST = SubTotal * HST_RATE
    TotSalesPrice = SubTotal + HST

    InvDate = datetime.datetime.now()
    InvDateDsp = InvDate.strftime("%B %d, %Y")
    InvDate2Dsp = InvDate.strftime("%d-%b-%y")

    Receipt = CustFirstName[0] + CustLastName[0] + "-" + PlateNum[3:] + "-" + PhoneNum[6:]
    CarDetails = Year + " " + CarMake + " " + CarModel
    CustName = CustFirstName[0] + "." + CustLastName

# Outputs
    print()
    print(f"Honest Harry Car Sales                  Invoice Date: {InvDateDsp}")
    print (f"Used Car Sale and Receipt               Receipt No:     {Receipt}")
    print()

    SellPriceDsp = "${:,.2f}".format(SellPrice)
    print(f"                                      Sale price:        {SellPriceDsp:>9s}")

    AmtTradeInDsp = "${:,.2f}".format(AmtTradeIn)
    print(f"Sold to:                              Trade Allowance:   {AmtTradeInDsp:>9s}")

    print(" "*38 +"-"*29)

    PriceAfterTradeDsp = "${:,.2f}".format(PriceAfterTrade)
    print(f"     {CustName:>29s}    Price after Trade: {PriceAfterTradeDsp:>9s}") #>29s

    LicenceFeeDsp = "${:,.2f}".format(LicenceFee)
    print(f"     {Street:>29s}    Licence Fee:        {LicenceFeeDsp:>9s}")  #>29s

    TransferFeeDsp = "${:,.2f}".format(TransferFee)
    print(f"     {City:>19s},{Prov} {PostCode}    Transfer Fee:       {TransferFeeDsp:>9s}")

    print(" "*38 +"-"*29)

    SubTotalDsp = "${:,.2f}".format(SubTotal)
    print(f"Car Details:                          Subtotal:          {SubTotalDsp:>9s}")

    HSTDsp = "${:,.2f}".format(HST)
    print(f"                                      HST:                {HSTDsp:>9s}")

    print(f"      {CarDetails:>29s} "         "  -----------------------------")
    TotSalesPriceDsp = "${:,.2f}".format(TotSalesPrice)
    print(f"                                      Total sales price: {TotSalesPriceDsp:>9s}")
    print("-"*67)
    print("                Best used cars at the best prices!")

    print()
    print()
    print("                               Financing       Total          Monthly")
    print("     # Years     # Payments       Fee          Price          Payment")
    print("     "+"-"*65)

    for Years in range(1,5):
        Payments = Years * 12
        FinFee = Years * FIN_RATE
        TotPrice = TotSalesPrice + FinFee
        MonPay = TotPrice / Payments

        Payments = int(Payments)
        FinFeeDsp = "${:,.2f}".format(FinFee)
        TotPriceDsp = "${:,.2f}".format(TotPrice)
        MonPayDsp = "${:,.2f}".format(MonPay)
        FirstPayDay = InvDate + datetime.timedelta(days=30)
        FirstPayDayDsp = FirstPayDay.strftime("%d-%b-%y")
        print(f"        {Years:>2d}           {Payments}        {FinFeeDsp:>9s}     {TotPriceDsp:>9s}      {MonPayDsp:>9s}")
    print("     " + "-" * 65)
    print(f"     Invoice date: {InvDate2Dsp}             First payment date: {FirstPayDayDsp} ")
    print()

    while True:
        Continue = input("Do you want to quit (Y/N)? ").upper()
        if Continue == "":
            print("Error - Continue cannot be blank. ")
        elif Continue !="Y" and Continue !="N":
            print("Error - Continue must be Y or N. ")
        else:
            break
    
    if Continue == 'Y':
        break
#Housekeeping
print()
print("                     Have a nice day! See you soon!")
print()


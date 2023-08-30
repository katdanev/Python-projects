# Program created for One Stop Insurance Company
# Written by Kateryna Danevych
# Date written 17/07/23

# Import libraries

# You asked to wrote used libraries:
# import FormatValues as FV, import time from tqdm import tqdm, import datetime

import FormatValues as FV

import time
from tqdm import tqdm
import datetime
InvDate = datetime.datetime.now()

# Open the defaults file and read the values into variables

f = open('OSICDef.dat', 'r')
POLICY_NUM = int(f.readline())
BASIC_RATE = float(f.readline())
DISCOUNT = float(f.readline())
EXTRA_LIAB = float(f.readline())
GLASS_COV = float(f.readline())
LOAN_CAR_COV = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE = float(f.readline())
f.close()

# Main program

while True:
    CustFirst = input("Enter the customer's first name (Type END to quit): ").title()
    if CustFirst == "End":
        break

    CustLast = input("Enter the customer's last name: ").title()
    Address = input("Enter the customer's address: ").title()
    City = input("Enter the customer's city: ").title()

    ProvList = ['NL', 'NB', 'NS', 'PEI']
    while True:
        Prov = input("Enter the province (NL, NB, NS, PEI): ").upper()
        if Prov not in ProvList:
            print("Error - province must be NL, NB, NS or PEI. Please reenter")
        else:
            break
    PostCode = input("Enter the postal code (A1A1A1): ").upper()
    while True:
        try:
            Phone = (int(input("Enter the phone number (7092223344): ")))
        except:
            print("Error - phone number must consist of numbers. Please reenter.")
        else:
            break

    while True:
        try:
            CarNum = (int(input("Enter the number of insured cars: ")))
        except:
            print("Error - number of cars must consist of numbers. Please reenter.")
        else:
            break

    ExtraLiability = input("Do you need Extra liability (Y or N)?: ").upper() #
    GlassCoverage = input("Do you need Glass Coverage (Y or N)?: ").upper() #
    LoanCarCoverage = input("Do you need Loan Car Coverage (Y or N)?: ").upper() #
    PayList = ['Full', 'Monthly']
    while True:
        Pay = input("Full or Monthly pay (Full or Monthly): ").title()
        if Pay not in PayList:
            print("Error - Monthly Pay must be Full or Monthly. Please reenter")
        else:
            break

    # Calculations

    InsPrem = BASIC_RATE * CarNum
    if CarNum > 1:
        InsPrem = BASIC_RATE + (BASIC_RATE - (BASIC_RATE * DISCOUNT)) * (CarNum - 1)

    if ExtraLiability == "Y":
        ExtraLiabCost = EXTRA_LIAB * CarNum
    else:
        ExtraLiabCost = 0

    if GlassCoverage == "Y":
        GlassCovCost = GLASS_COV * CarNum
    else:
        GlassCovCost = 0

    if LoanCarCoverage == "Y":
        LoanCarCovCost = LOAN_CAR_COV * CarNum
    else:
        LoanCarCovCost = 0

    TotalExtraCosts = ExtraLiabCost + GlassCovCost + LoanCarCovCost

    TotInsPremium = InsPrem + TotalExtraCosts
    HST = TotInsPremium * HST_RATE
    TotalCost = TotInsPremium + HST

    if Pay == "Monthly":
        TotalCost = (TotInsPremium + HST + PROC_FEE) / 8

# Payment calculations

    PurDateYear = InvDate.year
    PurDateMonth = InvDate.month
    PurDateDay = InvDate.day

    PayDateYear = InvDate.year
    PayDateMonth = InvDate.month + 1
    PayDateDay = 1

    PayDate = datetime.date(PayDateYear, PayDateMonth, PayDateDay)

    print()
    print("               ONE STOP INSURANCE COMPANY")
    print("                         RECEIPT")
    print()
    InvDateDsp = InvDate.strftime("%Y-%m-%d")
    print(f"Date:  {InvDateDsp:>10s}")
    print("-" * 59)
    print("Client information:               Insurance information:")
    print("-" * 59)
    print(f"Name:    {CustFirst:>20s}     Number of insured cars: {CarNum}")
    print(f"Name:    {CustLast:>20s}     Extra liability:        {ExtraLiability}")
    print(f"Address: {Address:>20s}     Glass coverage:         {GlassCoverage}")
    print(f"       {City:>10s}, {Prov}, {PostCode}     Loaner car:             {LoanCarCoverage}")
    print(f"Phone number:      {Phone}     Type of pay:      {Pay:>7s}")
    print("-"*59)

    InsPremDsp = FV.FDollar2(InsPrem)
    print(f"Insurance premium:                                {InsPremDsp:>9s}")
    TotalExtraCostsDsp = FV.FDollar2(TotalExtraCosts)
    print(f"Total Extra Costs:                                {TotalExtraCostsDsp:>9s}")
    print("-" * 59)
    TotInsPremiumDsp = FV.FDollar2(TotInsPremium)
    print(f"Total insurance premium:                          {TotInsPremiumDsp:>9s}")
    HSTDsp = FV.FDollar2(HST)
    print(f"HST:                                              {HSTDsp:>9s}")
    TotalCostDsp = FV.FDollar2(TotalCost)
    print(f"Total Cost:                                       {TotalCostDsp:>9s}")
    print("-" * 59)
    if Pay == "Monthly":
        print(f"Payment date:                                    {PayDate}")
    print("-" * 59)
    print()

    # Write the data to a text file.

    f = open("Policies.dat", "a")
    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(FV.FDateShort(InvDate)))
    f.write("{}, ".format(CustFirst))
    f.write("{}, ".format(CustLast))
    f.write("{}, ".format(Address))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(PostCode))
    f.write("{}, ".format(str(Phone)))
    f.write("{}, ".format(str(CarNum)))
    f.write("{}, ".format(ExtraLiability))
    f.write("{}, ".format(GlassCoverage))
    f.write("{}, ".format(LoanCarCoverage))
    f.write("{}, ".format(Pay))
    f.write("{}\n ".format(str(TotalCost.__round__(2))))
    f.close()

    POLICY_NUM += 1

    print()
    print()
    print("Saving data - please wait")
    # Processing bar
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)
    print("Policy information processed and saved!")
    time.sleep(1)
    print()


# Write the current values back to the default file.

    f = open('OSICDef.dat', 'w')
    f.write("{}\n".format(str(POLICY_NUM)))
    f.write("{}\n".format(str(BASIC_RATE)))
    f.write("{}\n".format(DISCOUNT))
    f.write("{}\n".format(EXTRA_LIAB))
    f.write("{}\n".format(GLASS_COV))
    f.write("{}\n".format(LOAN_CAR_COV))
    f.write("{}\n".format(HST_RATE))
    f.write("{}\n".format(PROC_FEE))

    f.close()

# в дата файлі після апострофа в назві міста С пишкться з великої

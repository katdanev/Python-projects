# Program written by Kateryna Danevych
# Date written 01/08/2023
# Report for One Stop Insurance Company

# Import required libraries (datetime and FormatValues)

import datetime
import FormatValues as FV

CurDate = datetime.datetime.now()

# Before the loop: Print headings, Initialize summary data, Open the file.
print()
print("ONE STOP INSURANCE COMPANY")
print(f"MONTHLY PAYMENT LISTING AS OF {FV.FDateMedium(CurDate)}")
print()
print("POLICY  CUSTOMER              TOTAL                   TOTAL      MONTHLY")
print("NUMBER  NAME                  PREMIUM        HST      COST       PAYMENT")
print("="*72)

TotPolCtr = 0
TotPremAcc = 0
HSTAcc = 0
TotalCostAcc = 0
MonPayAcc = 0

f = open("Policies.dat", "r")

for PoliciesDataLine in f:

# Inside the loop, Read the record, do any calculations, print the detail line.

    PolLine = PoliciesDataLine.split(",")

# All fields in the list are strings.
# Numbers and dates must be parsed.
# Only grab the values from the list that are required.

    PolNum = PolLine[0].strip()
    CustName = PolLine[2].strip()
    CustLastName = PolLine[3].strip()

    InsPrem = float(PolLine[14].strip())
    Extra1 = PolLine[10].strip()
    Extra2 = PolLine[11].strip()
    Extra3 = PolLine[12].strip()
    Payment = PolLine[13].strip()

    # Exception report
    if Payment == "Monthly":

# Perform any required calculations here.

        if Extra1 == "Y":
            ExtraCost1 = 130
        else:
            ExtraCost1 = 0

        if Extra2 == "Y":
            ExtraCost2 = 86
        else:
            ExtraCost2 = 0

        if Extra3 == "Y":
            ExtraCost3 = 58
        else:
            ExtraCost3 = 0

        ExtraCosts = ExtraCost1 + ExtraCost2 + ExtraCost3
        TotalPremium = InsPrem + ExtraCosts
        HST = TotalPremium * 0.15
        TotalCost = TotalPremium + HST
        MonPayment = (TotalCost + 39.99)/12

    # Print the detail line.
        print(f"{PolNum:>4s}  {CustName:<10s} {CustLastName:<10s}   {FV.FDollar2(TotalPremium):>9s} {FV.FDollar2(HST):>9s}  {FV.FDollar2(TotalCost):>9s}   {FV.FDollar2(MonPayment):>9s}")

# Increment any counters or accumulators.
        TotPolCtr += 1
        TotPremAcc += TotalPremium
        HSTAcc += HST
        TotalCostAcc += TotalCost
        MonPayAcc += MonPayment



# After the loop, close the file, and print the summary data.
f.close()
print("="*72)
print (f"Total policies: {TotPolCtr:>3d}           {FV.FDollar2(TotPremAcc):>9s} {FV.FDollar2(HSTAcc):>9s}  {FV.FDollar2(TotalCostAcc):>9s}     {FV.FDollar2(MonPayAcc)}")
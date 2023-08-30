
# Written by Kateryna Danevych
# Date written 26-05-2023

# Constants

EVEN_SITES_RATE = 80.00
ODD_SITES_RATE = 120.00
EACH_ALT_MEMB_RATE = 5.00
SITE_CLEAN_RATE = 50.00
VIDEO_SURV_RATE = 35.00
MON_DUES_STAND_RATE = 75.00
MON_DUES_EXEC_RATE = 150.00
HST_RATE = 0.15
PROCESSING_FEE = 59.99


# Inputs
SiteNumber = input("Enter the site number: ")
SiteNumber = int(SiteNumber)
MembName = input("Enter the member name: ")
StAdress = input("Enter the street adress: ")
City = input("Enter the city: ")
Prov = input("Enter the province: ").upper()
PostCode = input("Enter the postal code: ").upper()
PhoneNum = input("Enter the phone number: ")
CellNum = input("Enter the cell number: ")
MemType = input("Enter the type of membership (S or E): ").upper()
NumAltMemb = input("Enter the number of alternate members: ")
NumAltMemb = int(NumAltMemb)
WeekClean = input("Weekly site cleaning (Y or N): ").upper()
VideoSurv = input("Video surveillance (Y or N): ").upper()

# Calculations

if SiteNumber % 2 == 0:
    SiteCharges = EVEN_SITES_RATE +(NumAltMemb * EACH_ALT_MEMB_RATE)
else:
    SiteCharges = ODD_SITES_RATE + (NumAltMemb * EACH_ALT_MEMB_RATE)

ExtraCharges = SITE_CLEAN_RATE + VIDEO_SURV_RATE
SubTotal = SiteCharges + ExtraCharges
HST = SubTotal * HST_RATE
TotMonCharges = SubTotal + HST
if MemType == "S":
    MonthlyDues = MON_DUES_STAND_RATE
    MemTypeMessage = "Standart"
else:
    MonthlyDues = MON_DUES_EXEC_RATE
    MemTypeMessage = "Executive"
TotMonFees = TotMonCharges + MonthlyDues
TotYearlyFees = TotMonFees * 12
MonPayment = (TotYearlyFees + PROCESSING_FEE) / 12
CansFee = (SiteCharges * 12) * 0.6

if WeekClean == "Y" and VideoSurv == "Y":
    ExtraCharges = SITE_CLEAN_RATE + VIDEO_SURV_RATE
elif WeekClean == "Y" and VideoSurv == "N":
    ExtraCharges = SITE_CLEAN_RATE + 0
elif WeekClean == "N" and VideoSurv == "Y":
    ExtraCharges = 0 + VIDEO_SURV_RATE
else:
    ExtraCharges = 0

if WeekClean =="Y":
    WeekCleanMessage = "Yes"
else:
    WeekCleanMessage = "No"
if VideoSurv =="Y":
    VideoSurvMessage = "Yes"
else:
    VideoSurvMessage = "No"

# Outputs

print()
print()
print("   St. John's Marina & Yacht Club ")
print("        Yearly Member Receipt")
print("____________________________________")
print()
print("Client Name and Adress: ")
print()
print(f"{MembName:<24s}")
print(f"{City}, {Prov} {PostCode}")
print()
print(f"Phone: {PhoneNum} (H)")
print(f"       {CellNum} (C)")
print()
print(f"Site #: {SiteNumber:<3d} Member type: {MemTypeMessage}")
print()
print(f"Alternate members:                {NumAltMemb:>2d}")
print(f"Weekly site cleaning:            {WeekCleanMessage:>3s}") #new
print(f"Video surveillance:              {VideoSurvMessage:>3s}") #new
print()
SiteChargesDsp = "${:,.2f}".format(SiteCharges)
print(f"Site charges:              {SiteChargesDsp:>9s}")
ExtraChargesDsp = "${:,.2f}".format(ExtraCharges)
print(f"Extra charges:               {ExtraChargesDsp:>7s}")
print("                           ---------")
SubTotalDsp =  "${:,.2f}".format(SubTotal)
print(f"Subtotal:                  {SubTotalDsp:>9s}")
HSTDsp =  "${:,.2f}".format(HST)
print(f"Sales tax (HST):             {HSTDsp:>7s}")
print("                           ---------")
TotMonChargesDsp =  "${:,.2f}".format(TotMonCharges)
print(f"Total monthly charges:     {TotMonChargesDsp:>9s}")
MonthlyDuesDsp = "${:,.2f}".format(MonthlyDues)
print(f"Monthly dues:              {MonthlyDuesDsp:>9s}") # new
print("                           ---------")
TotMonFeesDsp =  "${:,.2f}".format(TotMonFees)
print(f"Total monthly fees:        {TotMonFeesDsp:>9s}")
TotYearlyFeesDsp =  "${:,.2f}".format(TotYearlyFees)
print(f"Total yearly fees:        {TotYearlyFeesDsp:>10s}")
print()
MonPaymentDsp =  "${:,.2f}".format(MonPayment)
print(f"Monthly payment:           {MonPaymentDsp:>9s}")
print("                           ---------")
print("Issued: YYYY-MM-DD")
print("HST Reg No: 549-33-5849-4720-9885")
print()
CansFeeDsp =  "${:,.2f}".format(CansFee)
print(f"Cancellation fee:          {CansFeeDsp:>9s}")







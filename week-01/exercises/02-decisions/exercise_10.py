# USPS
# Below is an abbreviated version of the US Postal Service retail parcel rates:

# Lbs | Zones 1&2 | Zone 3
# =========================
# 1      $7.50      $7.85
# 2       8.25       8.70
# 3       8.70       9.70
# 4       9.20      10.55
# 5      10.20      11.30


# 1. Collect the parcel lbs and zone (1, 2, or 3) from the user.
# 2. Add `if`/`else if`/`else` logic to cover all rates.
# Use whatever strategy you think is best. You can create compound conditions or nest if/else statements.
# If a lbs/zone combo does not exist, print a warning message for the user.

parcel_lbs = int(input("How many pounds is your package?: "))
zone = int(input("Enter postal zone (1, 2, or 3): "))

if parcel_lbs == 1:
    if zone == 1 or zone == 2:
        print("Your total today will be $7.50")
    elif zone == 3:
        print("Your total today will be $7.85")
    else:
        print("Invalid zone.")
elif parcel_lbs == 2:
    if zone == 1 or zone == 2:
        print("Your total today will be $8.25")
    elif zone == 3:
        print("Your total today will be $8.70")
    else:
        print("Invalid zone.")
elif parcel_lbs == 3:
    if zone == 1 or zone == 2:
        print("Your total today will be $8.70")
    elif zone == 3:
        print("Your total today will be $9.70")
    else:
        print("Invalid zone.")
elif parcel_lbs == 4:
    if zone == 1 or zone == 2:
        print("Your total today will be $9.20")
    elif zone == 3:
        print("Your total today will be $10.55")
    else:
        print("Invalid zone.")
else:
    if zone == 1 or zone == 2:
        print("Your total today will be $10.20")
    elif zone == 3:
        print("Your total today will be $11.30")
    else:
        print("Invalid zone.")

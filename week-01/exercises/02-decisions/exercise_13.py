# NEEDLE & HAYSTACK

needle = input("Needle: ")
haystack = input("Haystack: ")

if needle in haystack:
    print("yes")
else:
    print("no")


# 1. Given two string variables: needle and haystack, determine if haystack contains needle.
# Examples
# needle  haystack contains?
#     an      bean      yes
#    een      bean       no
#    ury   Mercury      yes
#    ury     curry       no
#    mer   Mercury       no (case sensitive)
# 2. As a stretch goal, display the location (index) of needle in haystack.

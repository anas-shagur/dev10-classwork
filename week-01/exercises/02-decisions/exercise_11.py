# MANAGER FEATURE REQUESTS
# You have three managers: A, B, and C.
# Occasionally, they ask you to add features to your company software.
# Use if/else statements to enforce the following rules:
# - If all three ask for the feature, print "Feature in progress."
# - If any two of the three ask, print "Adding feature to schedule."
# - If only one of the three ask, print "Going to hold off for a bit."
# - If none of the managers ask, print "Nothing to do..."

manager_a_asked = False
manager_b_asked = False
manager_c_asked = False

# 1. Add decisions statements to cover all scenarios.
# 2. Change manager variables to test all scenarios.


if manager_a_asked:
    if manager_b_asked and manager_c_asked:
        print("Feature in progress.")
    elif manager_b_asked or manager_c_asked:
        print("Adding feature to schedule.")
    else:
        print("Going to hold off for a bit.")
elif manager_b_asked:
    if manager_a_asked and manager_c_asked:
        print("Feature in progress.")
    elif manager_a_asked or manager_c_asked:
        print("Adding feature to schedule.")
    else:
        print("Going to hold off for a bit.")
elif manager_c_asked:
    if manager_b_asked and manager_a_asked:
        print("Feature in progress.")
    elif manager_b_asked or manager_a_asked:
        print("Adding feature to schedule.")
    else:
        print("Going to hold off for a bit.")
else:
    print("Nothing to do...")

# A tuple containing an immutable string and a mutable list
employee_record = ("ID_402", "Active", ["Basic Access"])

print("Initial Tuple:", employee_record)

# Requirement: Modify the tuple item without list conversion 
# We access the list at index 2 and use the .append() method
employee_record[2].append("Admin Privileges")

# We can also modify an existing element within that list
employee_record[2][0] = "Full Access"

print("Modified Tuple:", employee_record)
# Output will reflect the changes within the list while the tuple identity remains.
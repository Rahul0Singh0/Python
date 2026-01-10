age = int(input("Enter your age: "));
has_id = input("Do you have a valid ID? (yes/no): ").lower() == "yes";

if age >= 18 and has_id:
    print("You are eligible to vote.");
else:
    print("You are not eligible to vote.");

is_admin = False

if not is_admin:
    print("Limited access")
else:
    print("Full access")
# Conditionals

total = float(input("Enter your total score: "))

if total >= 90:
    print("You did amazing!")
elif total > 80:
    print("You did good.")
elif (
    total > 70 or total < 80
):  # printing or here allows for the number to be checked twice.
    print("You did mediocre..")
else:
    print("You lowered the class average somehow.")


count = 3
type = "Veggie"

if (type == "Veggie" or type == "Supreme") and (count == 3 or count == 2):
    print("Veggie Pizza.")


# Operators
# == is a comparison between two things, is equal to (A==B).
# != not equal to (A!=B).
# > greater than (A>B).
# >= greater than/equal to (A>=B).
# < less than (A<B).
# <= less than/equal to (A<=B).
# not opposite of opperand value (not a>b).
# and makes both conditions true (A>b and C<D). Has presedence over or.

# Nesting Conditions
if total > 70:
    if (
        total > 90
    ):  # checks if the total is greater than 90, prints well done, if not, prints below
        if total > 98:  # checks here again
            print("Really good job!")
        else:
            print("Simple good job")
    else:
        print("Satisfactory")
else:
    print("Work hard")

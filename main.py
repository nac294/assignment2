##################################################################################################
# Define a function to calculate BMI
def get_bmi(height, weight) -> float:

    # Apply the metric conversions
    weight *= 0.45
    height *= 0.025

    height = height ** 2  # pow(weight, 2)

    # Print the BMI or catch division by 0
    try:
        res = weight / height
        res = round(res, 1)
        print("BMI: ", res)

    except ZeroDivisionError:
        print("Error attempted division by 0")
        res = 0

    return res


##################################################################################################
# Define a function to print the correct output
def handle_output(bmi) -> str:

    # No one can have a bmi < 0
    # Return a value that will make the code loop again
    if bmi <= 0:
        return "Invalid BMI"

    # Otherwise, print the user's weight category and break the loop
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal weight"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


##################################################################################################
# Define a function to handle the user's input
def handle_input() -> None:

    while True:

        # Get the user's height/weight
        height = input("Enter your height in feet\n>> ")

        # Convert the user's input to inches
        tempList = height.split(".")
        try:
            feet = float(tempList[0])
            inches = float(tempList[1])
        except IndexError:
            print("Error please input height in this way: Ft.In\n")
            continue

        feet *= 12
        height = feet + inches

        weight = float(input("\nEnter your weight in pounds\n>> "))
        print("\n")

        # Calculate the BMI and print the result
        print(handle_output(get_bmi(height, weight)))
        break

    return


if __name__ == "__main__":

    userChoice = None

    while userChoice != "Y" and userChoice != "y":
        handle_input()
        userChoice = input("\nWould you like to exit the program? (Y/y): ")
        print("\n")

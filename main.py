from flask import Flask, render_template, url_for, redirect, request

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
def handle_output(bmi) -> tuple:

    # No one can have a bmi < 0
    # Return a value that will make the code loop again
    if bmi <= 0:
        return bmi, "Invalid input"

    # Otherwise, print the user's weight category and break the loop
    if bmi < 18.5:
        return bmi, "Underweight"
    elif bmi <= 24.9:
        return bmi, "Normal weight"
    elif bmi <= 29.9:
        return bmi, "Overweight"
    else:
        return bmi, "Obese"


##################################################################################################
# Define a function to handle the user's input
def handle_input(feet, inches, weight) -> tuple:

    # Perform metric conversions
    feet *= 12
    height = feet + inches

    # Calculate the BMI and print the result
    return handle_output(get_bmi(height, weight))


##################################################################################################
# Define the inner workings of the app
BMI_app = Flask(__name__)

@BMI_app.route('/home', methods=['POST', 'GET'])
def home():

    msg = None
    bmi = None
    if request.method == "POST":
        feet = float(request.form.get("ft", False))
        inches = float(request.form.get("in", False))
        weight = float(request.form.get("wt", False))

        print(feet, inches, weight)
        bmi, msg = handle_input(feet, inches, weight)
        print(bmi, msg)

        # If the result was invalid, we want to print the error, not the BMI value
        if msg == "Invalid input":
            return render_template("home.html", error=msg)

    return render_template("home.html", output=msg, BMI=bmi)

@BMI_app.route('/')
def init():
    return redirect(url_for("home"))


if __name__ == '__main__':
    BMI_app.run(debug=True)
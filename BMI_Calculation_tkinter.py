from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(300,300)
window.config(padx=30, pady=30)

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()
    gender = gender_var.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi, gender)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")

def write_result(bmi, gender):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "

    if gender == "male":
        if bmi <= 18.5:
            result_string += "severely thin!"
        elif 18.5 < bmi <= 20:
            result_string += "moderately thin!"
        elif 20 < bmi <= 25:
            result_string += "normal weight"
        elif 25 < bmi <= 30:
            result_string += "overweight"
        elif 30 < bmi <= 35:
            result_string += "obese class 1"
        elif 35 < bmi <= 40:
            result_string += "obese class 2"
        else:
            result_string += "obese class 3"
    else:
        if bmi <= 17.5:
            result_string += "severely thin!"
        elif 17.5 < bmi <= 19:
            result_string += "moderately thin!"
        elif 19 < bmi <= 24:
            result_string += "normal weight"
        elif 24 < bmi <= 29:
            result_string += "overweight"
        elif 29 < bmi <= 34:
            result_string += "obese class 1"
        elif 34 < bmi <= 39:
            result_string += "obese class 2"
        else:
            result_string += "obese class 3"

    return result_string


# Gender Selection
gender_label = Label(text="Select Gender")
gender_label.pack()

gender_var = StringVar(value="male")
male_radio = Radiobutton(text="Male", variable=gender_var, value="male")
female_radio = Radiobutton(text="Female", variable=gender_var, value="female")
male_radio.pack()
female_radio.pack()

# Weight
weight_input_label = Label(text="Enter Your Weight (kg)")
weight_input_label.pack()

weight_input = Entry(width=10)
weight_input.pack()

# Height
height_input_label = Label(text="Enter Your Height (cm)")
height_input_label.pack()

height_input = Entry(width=10)
height_input.pack()

# Calculate Button
calculate_button = Button(text="Calculate", command=calculate_bmi)
calculate_button.pack(pady=10)

# Result
result_label = Label()
result_label.pack()

window.mainloop()

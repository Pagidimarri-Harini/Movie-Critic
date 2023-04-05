import pandas as pd
import tkinter as tk
import numpy as np
from tkinter import *
import joblib
from tkinter import ttk, filedialog
from xgboost import XGBRegressor
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfile
from sklearn.model_selection import train_test_split
import os



# Create a tkinter window
root = tk.Tk()
root.geometry('1000x600')
root.title('Movie Critic')
root.configure(bg="pink")


image_0 = Image.open(r"C:\Users\DELL\Desktop\vs code\Python\ML_final.jpeg")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
image = image_0.resize((width, height))

bg_img = ImageTk.PhotoImage(image_0) 
bg_lbl = Label(root,image = bg_img)
bg_lbl.place(x = 0, y = 0, relwidth=1, relheight=1)
# bg_lbl.pack(fill="both", expand = True)
my_text = Entry(root, width=30, justify=CENTER, bg = 'pink', font=('Times', 60,'bold'))
my_text.insert(0, "MOVIE CRITIC")
my_text.pack(padx=50, pady=50)

# Create input labels and entry boxes
def open2():
    root1 = Toplevel()
    root1.geometry("1200x600")
    root1.title("Input Page")
    root1.configure(background = "pink")
    # canvas = Canvas(root1, width=500, height=500)
    # canvas.pack()
    # bg_image = PhotoImage(file="ML_project_img.jpeg")
    # canvas.create_image(0, 0, image=bg_image, anchor="nw")

    padx = 10
    pady = 5

    budget_label = tk.Label(root1, text='Budget in 1 million:', bg = "pink")
    budget_label.pack()
    budget_entry = tk.Entry(root1)
    budget_entry.pack()

    has_a_tagline_label = tk.Label(root1, text='Does the movie has tagline?', bg = "pink")
    has_a_tagline_label.pack()
    has_a_tagline_entry = tk.Entry(root1)
    has_a_tagline_entry.pack()

    production_country_United_States_of_America_label = tk.Label(root1, text='is the production country United States of America?:', bg = "pink")
    production_country_United_States_of_America_label.pack()
    production_country_United_States_of_America_entry = tk.Entry(root1)
    production_country_United_States_of_America_entry.pack()

    num_cast_label = tk.Label(root1, text='Number of cast members:', bg = "pink")
    num_cast_label.pack()
    num_cast_entry = tk.Entry(root1)
    num_cast_entry.pack()

    genders_2_cast_label = tk.Label(root1, text='Number of male cast members:', bg = "pink")
    genders_2_cast_label.pack()
    genders_2_cast_entry = tk.Entry(root1)
    genders_2_cast_entry.pack()

    num_crew_label = tk.Label(root1, text='Number of crew members:', bg = "pink")
    num_crew_label.pack()
    num_crew_entry = tk.Entry(root1)
    num_crew_entry.pack()

    genders_1_crew_label = tk.Label(root1, text='No of female crew members', bg = "pink")
    genders_1_crew_label.pack()
    genders_1_crew_entry = tk.Entry(root1)
    genders_1_crew_entry.pack()

    genders_2_crew_label = tk.Label(root1, text='No of male crew members:', bg = "pink")
    genders_2_crew_label.pack()
    genders_2_crew_entry = tk.Entry(root1)
    genders_2_crew_entry.pack()

    departments_Sound_label = tk.Label(root1, text='No.of members in sound department:', bg = "pink")
    departments_Sound_label.pack()
    departments_Sound_entry = tk.Entry(root1)
    departments_Sound_entry.pack()

    departments_Art_label = tk.Label(root1, text='No.of members in art department:', bg = "pink")
    departments_Art_label.pack()
    departments_Art_entry = tk.Entry(root1)
    departments_Art_entry.pack()

    departments_Editing_label = tk.Label(root1, text='No.of members in editing department:', bg = "pink")
    departments_Editing_label.pack()
    departments_Editing_entry = tk.Entry(root1)
    departments_Editing_entry.pack()

    bud_year_label = tk.Label(root1, text='Enter the ratio of budget and release year:', bg = "pink")
    bud_year_label.pack()
    bud_year_entry = tk.Entry(root1)
    bud_year_entry.pack()

# Create a function to predict using a trained model
    def out_predict():
        features=[float(budget_entry.get()), int(has_a_tagline_entry.get()), int(production_country_United_States_of_America_entry.get()), int(num_cast_entry.get()), int(genders_2_cast_entry.get()), int(num_crew_entry.get()),int(genders_1_crew_entry.get()), int(genders_2_crew_entry.get()), int(departments_Sound_entry.get()),int(departments_Art_entry.get()), int(departments_Editing_entry.get()), float(bud_year_entry.get())]
        #X = pd.DataFrame(features)
        X = np.array(features).reshape(1, -1)
        train = pd.read_csv("train_preprocess.csv")
        y_val = train['revenue']
        X_val = train.drop(['revenue'], axis = 1)
        # model = joblib.load("C:\\Users\\DELL\\Downloads\\xgb_f.joblib")
        model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
        model.fit(X_val, y_val)
        #model.fit(X, [0, 1])
        prediction = model.predict(X)
        return prediction[0]
        #model.fit(X, ['Not Transported', 'Transported'])
        #return model.predict(X)'''

    # Create a function to update the output label
    def update_output():
        prediction = out_predict()
        prediction = np.expm1(prediction)
        output_label.config(text=f"Predicted revenue: {prediction:,.3f}")

    # Create a button to trigger the prediction function
    predict_button = tk.Button(root1, text='Predict', command=update_output, bg = "light blue")
    predict_button.pack()

    predict_button.place(x = 570, y = 500)
    output_label = tk.Label(root1, text='Prediction: ', bg = "pink")
    output_label.pack()
    output_label.place(x = 570, y = 540)


# print the coordinates
    

    # Create an output label to display the predicted value


btnOpen=Button(root,text="Input Page",height = 3, width = 20,bg = 'pink', command=open2)
btnOpen.configure(font=("Arial", 13))
#
btnOpen.pack(side='bottom')
root.mainloop()
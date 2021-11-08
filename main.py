import tkinter


def calculate():
    miles = int(entry.get())
    kms = round(miles * 1.60934, 2)
    label_km_value.config(text=f"{kms}")


# New window
window = tkinter.Tk()
window.title("Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

# Entry
entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

# Labels
label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_km_value = tkinter.Label(text="")
label_km_value.grid(column=1, row=1)

label_km = tkinter.Label(text="km")
label_km.grid(column=2, row=1)

# Button
button = tkinter.Button(text="Calculate",  command=calculate)
button.grid(column=1, row=2)

window.mainloop()

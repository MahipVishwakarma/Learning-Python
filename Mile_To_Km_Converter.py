from tkinter import *

def convert():
    result = float(miles_value.get()) * 1.61
    km_result.config(text=result)


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)


miles_value = Entry(width=5)
miles_value.grid(column=1, row=0)


miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)


equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)


km_result = Label(text="0")
km_result.grid(column=1, row=1)


km_label = Label(text="kilometers")
km_label.grid(column=2, row=1)


calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)




window.mainloop()
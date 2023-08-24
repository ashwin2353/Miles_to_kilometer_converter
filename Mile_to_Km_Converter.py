import tkinter

window = tkinter.Tk()
window.title('Miles to Kilometer Converter')
window.minsize(width=350, height=200)
window.config(pady=50, padx=50)
window.grid()

# Label
my_label = tkinter.Label(text='is equal to', font=('Arial', 10, 'bold'))
my_label.grid(column=0, row=1)
my_label.config(pady=10,padx=10)

my_label_1 = tkinter.Label(text='Miles', font=('Arial', 10, 'bold'))
my_label_1.grid(column=2, row=0)
my_label_1.config(pady=10,padx=10)

my_label_2 = tkinter.Label(text='Km', font=('Arial', 10, 'bold'))
my_label_2.grid(column=2, row=1)
my_label_2.config(pady=10,padx=10)

my_label_3 = tkinter.Label(text='0', font=('Arial', 10, 'bold'))
my_label_3.grid(column=1, row=1)
my_label_3.config(pady=10,padx=10)

# Button
def miles_to_km():
    value = round(float(input.get()) * 1.609344,2)
    my_label_3.config(text=value)



button = tkinter.Button(text='Calculate', command = miles_to_km)
button.grid(column=1, row=2)
button.config(pady=10,padx=10)

# Entry
input = tkinter.Entry(width=17)
input.grid(column=1, row=0)
print(input.get())






window.mainloop()
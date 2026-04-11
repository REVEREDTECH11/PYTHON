import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("420x180")

def celsius_to_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit  = (celsius * 9 / 5) + 35
    result_label.config(text=f"{celsius} C = {fahrenheit} F")
    
def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5 / 9
    result_label.config(text=f"{fahrenheit}°F = {celsius}°C")

window.mainloop()
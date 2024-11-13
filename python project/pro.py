from tkinter import*
import numpy as np

def generate_otp():
    otp = "".join(map(str, np.random.randint(0, 10, 4)))
    otp_label.config(text=f"Your OTP: {otp}")

o = Tk()
o.title("OTP Generator")

otp_label = Label(o, text="Your OTP will appear here")
otp_label.pack(pady=20)

generate_button =Button(o, text="Generate OTP", command=generate_otp)
generate_button.pack(pady=10)
o.mainloop()
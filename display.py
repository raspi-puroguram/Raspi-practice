from tkinter import *
from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep

human_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(human_pin, GPIO.IN)

root = Tk()
root.geometry("720x480")
root.title("Human Display")

c = Canvas(root, bg="#FFFFFF" , width=500, height=480)
c.pack(expand=True, fill='x', padx=5, side='left')

ch = c.create_text(500, 80, font=('', 60, 'bold'), fill='red')
cd = c.create_text(500, 180, font=('', 40, 'bold'), fill='black')
ct = c.create_text(500, 280, font=('', 80), fill='black')
cf = c.create_text(500, 400, font=('', 40), fill='blue')

root.attributes("-zoomed", "1")

root.attributes("-topmost", False)

def main():
    hpin= GPIO.input(human_pin)
    if hpin == 1:
        h='Comming Human!' #'Human Detected'
    else:
        h= 'Not Human' #'No Human'
    print(h)
    
    now = datetime.now()
    d =  '{0:0>4d}nen{1:0>2d}tuki{2:0>2d}niti ({3}) '.format(now.year, now.month,now.day, now.strftime('%a'))
    
    t = '{0:0>2d}:{1:0>2d}:{2:0>2d}' .format(now.hour, now.minute, now.second)
    
    c.itemconfigure(ch, text='Human Display')
    c.itemconfigure(cd, text=d)
    c.itemconfigure(ct, text=t)
    c.itemconfigure(cf, text=h)
    c.update()
    root.after(1000, main)
    
root.after(1000, main)
root.mainloop()
GPIO.cleanup()
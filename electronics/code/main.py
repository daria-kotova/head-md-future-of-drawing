from PIL import Image, ImageTk
from tkinter import Tk, Frame, Label, Canvas
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_outline_state = True
last_shading_state = True

reader = SimpleMFRC522()

A4_WIDTH = 595
A4_HEIGHT = 842


root = Tk()
root.configure(background='black')
root.attributes('-fullscreen', True)
root.geometry(f"{A4_WIDTH}x{A4_HEIGHT}")
root.title("Image Projector")

canvas = Canvas(root, width=500, height=100, bd=0, bg='black', highlightthickness=0)
canvas.pack()

blank_image_file = "/home/pi/pi-rfid/images/default.jpg"


#Dictionary for each animal
bear = {
    "outline": "/home/pi/pi-rfid/images/outlines/outline-bear.jpg",
    "shading": "/home/pi/pi-rfid/images/shading/shading-bear.jpg"
}

frog = {
    "outline": "/home/pi/pi-rfid/images/outlines/outline-frog.jpg",
    "shading": "/home/pi/pi-rfid/images/shading/shading-frog.jpg"
}

plane = {
    "outline": "/home/pi/pi-rfid/images/outlines/outline-plane.jpg",
    "shading": "/home/pi/pi-rfid/images/shading/shading-plane.jpg"
}

previous_tag= ""
state = ""
button_state = ""

def read_nfc():
    try:
        tag_id, tag_text = reader.read_no_block()
        if tag_text is not None:
            print(tag_text)
            #previous_tag = tag_text
            return tag_text.strip()
        
    except:
        print("Error reading NFC tag")
        pass

def check_switch():
    global last_outline_state
    global last_shading_state
	
    input_outline_state = GPIO.input(19)
	
    if input_outline_state == False and last_outline_state == True:
        print('Outline Button Pressed')
        last_outline_state = False
        return("o_on")

    if input_outline_state == True and last_outline_state == False:
        print('Outline Button Released')
        last_outline_state = True
        return("o_off")
		
    input_shading_state = GPIO.input(13)
	
    if input_shading_state == False and last_shading_state == True:
        print('Shading Button Pressed')
        last_shading_state = False
        return("s_on")
		
    if input_shading_state == True and last_shading_state == False:
        print('Shading Button Released')
        last_shading_state = True
        return("s_off")


def display_image(image_file):
    image = Image.open(image_file)
    image = image.resize((A4_WIDTH, A4_HEIGHT), resample=Image.BICUBIC)
    tk_image = ImageTk.PhotoImage(image)
    label.config(image=tk_image)
    label.image = tk_image

def update_image():
    try:
        global state
        global previous_tag
        global button_state

        tag = read_nfc()

        button = check_switch()
        if button != None:
            button_state = button


        if tag is not None:
            if tag != previous_tag:

                if tag == "bear":
                    state = "bear"
                    button_state = "o_on"

                elif tag == "frog":
                    state = "frog"
                    button_state = "o_on"

                elif tag == "plane":
                    state = "plane"
                    button_state = "o_on"               
                
                previous_tag = tag

        if state == "bear":
            if button_state == "s_off":
                image_file = bear["shading"]
            else:
                image_file = bear["outline"]

        if state == "frog":
            if button_state == "s_off":
                image_file = frog["shading"]
            else:
                image_file = frog["outline"]

        if state == "plane":
            if button_state == "s_off":
                image_file = plane["shading"]
            else:
                image_file = plane["outline"]

        display_image(image_file)

    except:
        pass
    
    try:
        root.after(10, update_image)
    except KeyboardInterrupt:
        GPIO.cleanup() 
        exit()



label = Label(root)
label.pack()

display_image(blank_image_file)
root.after(100, update_image)

root.mainloop()

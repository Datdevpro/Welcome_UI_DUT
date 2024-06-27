import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import math 
from datetime import datetime
import time 

# name: tên, rank: học hàm, title: chức vụ

def UI_display():
    #set up window screen
    root = tk.Tk()
    global width, height
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root['background']='#CCFFFF'
    root.title("Welcome")
    root.resizable(False,False) # cho phép resize cửa sổ hay không

    ## set up function needed
    #function resize image
    def resize_image(image, new_width, new_height):
        resized_image = image.resize((new_width, new_height))
        return resized_image

    # function resize and open image
    def open_resize(image):
        #global width, height
        open_img = Image.open(image)
        resize_img = resize_image(open_img, width, height)
        main_img = ImageTk.PhotoImage(resize_img)
        return main_img

    # function auto update background via seasons
    def auto_update_background():
        now = datetime.now()
        day = now.day
        month = now.month

        if 3 <= month <= 5:
            background_image = spring_image
        elif 6 <= month <= 8:
            background_image = summer_image
        elif 9 <= month <= 11:
            background_image = autumn_image
        else:
            background_image = winter_image

        bg_label.config(image=background_image)
        bg_label.image = background_image

        root.after(3600000*24, auto_update_background)

    # image background    
    spring_image = open_resize("muaxuan.jpg")
    winter_image = open_resize("muadong.jpg")
    summer_image = open_resize("muahe.jpg")
    autumn_image = open_resize("muathu.jpg")
    default_bg = "muaxuan.jpg"
    bg_img = open_resize(default_bg)
    bg_label = Label(root, image = bg_img)
    bg_label.place(x=0, y=0)
    auto_update_background()


    # clock animation
    global WIDTH, HEIGHT, clock_frame
    WIDTH = 300
    HEIGHT = 300
    clock_frame = Frame(root,bg='white')
    clock_frame.place(relx=0.972, rely=0.02,  anchor="ne")
    canvas = tk.Canvas(clock_frame, width=WIDTH, height=HEIGHT,bg='white', highlightthickness=0)
    canvas.pack()
    def update_clock():
        canvas.delete("all")
        now = time.localtime()
        hour = now.tm_hour % 12
        minute = now.tm_min
        second = now.tm_sec
    
        # Draw clock face
        canvas.create_oval(2, 2, WIDTH-8, HEIGHT-8, outline="green", width=5)
        # Draw hour numbers
        for i in range(12):
            angle = i * math.pi/6 - math.pi/2
            x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(angle)
            y = HEIGHT/2 + 0.7 * WIDTH/2 * math.sin(angle)
            if i == 0:
                canvas.create_text(x, y, text=str(i+12), font=("Helvetica", 13))
            else:
                canvas.create_text(x, y, text=str(i), font=("Helvetica", 13))
    
        # Draw minute lines
        for i in range(60):
            angle = i * math.pi/30 - math.pi/2
            x1 = WIDTH/2 + 0.8 * WIDTH/2 * math.cos(angle)
            y1 = HEIGHT/2 + 0.8 * HEIGHT/2 * math.sin(angle)
            x2 = WIDTH/2 + 0.9 * WIDTH/2 * math.cos(angle)
            y2 = HEIGHT/2 + 0.9 * HEIGHT/2 * math.sin(angle)
            if i % 5 == 0:
                canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
            else:
                canvas.create_line(x1, y1, x2, y2, fill="black", width=1)
    
        # Draw hour hand
        hour_angle = (hour + minute/60) * math.pi/6 - math.pi/2
        hour_x = WIDTH/2 + 0.5 * WIDTH/2 * math.cos(hour_angle)
        hour_y = HEIGHT/2 + 0.5 * HEIGHT/2 * math.sin(hour_angle)
        canvas.create_line(WIDTH/2, HEIGHT/2, hour_x, hour_y, fill="black", width=6)
    
        # Draw minute hand
        minute_angle = (minute + second/60) * math.pi/30 - math.pi/2
        minute_x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(minute_angle)
        minute_y = HEIGHT/2 + 0.7 * HEIGHT/2 * math.sin(minute_angle)
        canvas.create_line(WIDTH/2, HEIGHT/2, minute_x, minute_y, fill="black", width=4)
    
        # Draw second hand  
        second_angle = second * math.pi/30 - math.pi/2
        second_x = WIDTH/2 + 0.6 * WIDTH/2 * math.cos(second_angle)
        second_y = HEIGHT/2 + 0.6 * WIDTH/2 * math.sin(second_angle)
        canvas.create_line(WIDTH/2, HEIGHT/2, second_x, second_y, fill="red", width=2)
    
        canvas.after(1000, update_clock)
    update_clock()

    # date time func ( định dạng digital )
    def date_time():
        now = datetime.now()
        date_string = now.strftime("%A, %d %B %Y")
        date_label.config(text=date_string)
        date_label.after(1000, date_time)
    date_label = Label(clock_frame, font=('Helvetica', 15), bg="white")
    date_label.pack(pady = 10)
    date_time()


    # frame logo
    img_frame = tk.Frame(root, bg='white')

    img_frame.place(relx=0.5, rely=0, anchor='n')
    image2 = Image.open("UDN.png")
    resize_img2 = resize_image(image2, 200, 200)
    tk_img2 = ImageTk.PhotoImage(resize_img2)
    image_label2 = Label(img_frame, image=tk_img2)
    image_label2.pack(side='left', padx=40, pady=25)
    image = Image.open("DUT.jpg")
    resize_img = resize_image(image, 200, 200)
    tk_img = ImageTk.PhotoImage(resize_img)
    image_label = Label(img_frame, image=tk_img)
    image_label.pack(side='left', padx=40, pady=25) 


    #frame text welcome
    text_frame = Frame(root, bg='white')
    text_frame.place(relx=0.5, rely=0.61, anchor='center')
    sb_label = tk.Label(text_frame, text = "Welcome to Smart Building", font=("Pinyon Script", 50, 'bold italic'), fg = '#0b5394', bg='white')
    sb_label.pack()

    welcome_text = Label(text_frame, text="Kính Chào", font=("Montserrat", 50, 'bold'), fg = '#9db521', bg='white', padx=150)
    welcome_text.pack(pady=20)

    rank = "PGS "
    name = "Phạm Văn Tuấn"
    title = "Trưởng phòng "
    position = "Phòng khảo thí và chất lượng đảm bảo giáo dục"
    name_text = Label(text_frame, text=rank+name, font=("Arial", 40, 'bold'), fg = '#0b5394', bg='white', padx=60)
    name_text.pack(pady=20)

    #position = "Trưởng phòng"
    tilte_text = Label(text_frame, text=title + position, font=("Arial", 40), fg = '#0b5394', bg='white', padx=50, wraplength=1111)
    tilte_text.pack(pady=20)

    #position_text = Label(text_frame, text="Phòng khảo thí CLĐTGD", font=("Arial", 40), fg = '#0b5394', bg='white', padx=50, wraplength=1100)
    #position_text.pack(pady=20)





    # hàm update name
    # def update_name():
    #     global current_index
    #     if current_index < len(name_list):
    #         name_text.config(text=name_list[current_index])
    #         tilte_text.config(text=tilte[name_list[current_index]])
    #         current_index += 1

    #     if current_index > len(name_list):
    #         name_text.after_cancel()  # Hủy lịch cập nhật
    #     name_text.after(1500, update_name)


    # name_list = ["Alice", "Bob", "Charlie", "David", "Emma"]
    # tilte = {"Alice":"chef", "Bob":"student", "Charlie":"police", "David":"teacher", "Emma":"cast"}
    # current_index = 0
    # update_name()


    root.mainloop()

UI_display()

# đây là phiên bản chỉnh sửa  1
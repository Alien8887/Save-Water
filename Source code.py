import tkinter as tk
import random
import turtle
import keyboard
from keyboard import *
import time
from turtle import *
from tkinter import *
import pygame
import tkinter.font as tkFont
from datetime import datetime
import tkinter.messagebox as mb
import sys
speed = 0
score = 0


moode = 1

def exit_game():
    awnser = mb.askyesno("ایا میخواهید خارج شوید؟", "خروج")
    if awnser:
        sys.exit()
menu = Tk()
var = IntVar()
def first_level():
    global score, speed
    speed = 2
    score = 10

def second_level():
    global score, speed
    speed = 3.5
    score = 20

def third_level():
    global score, speed
    speed = 5
    score = 30

def fake_start():
    global speed, main_username, username_entry
    if speed == 0:
        mb.showwarning("یکی از سطح ها را انتخاب کنید", "شما هیچ سطحی را انتخاب نکرده اید")
    else:
        with open("user names.txt", "a", encoding='utf-8') as just_write_the_file:
            with open("user names.txt", "r", encoding='utf-8') as username:
                        lst_usernames = username.read().split("/")
                        try:
                            for i in lst_usernames:
                                if username_entry.get() == i.lower():
                                    main_username = username_entry.get()
                                    break
                            if not "main_username" in locals():
                                with open("user names.txt", "a", encoding='utf-8') as username:
                                    username.write(f"{username_entry.get()}/")
                                    main_username = username_entry.get()
                        except FileNotFoundError:
                            print("error")
        menu.destroy()
def about_us():
    mb.showinfo("درباره ما", "سازنده : علی قاسمی"
                                                    "\nمدرسه آزیتا افشار نژاد"
                                                    "\nپایه هشتم"
                                                    "\nشماره تماس : 09945388491"
                                                    "\nتیر 1402")
def game_guide():
    mb.showinfo("راهنمای بازی", "\nبا استفاده از کلید های"
                                                       "\n7 8 9"
                                                       "\n4 5 6"
                                                       "\n1 2 3"
                                                       "\nدر نام پد خود یا از کلید های"
                                                       "\nq w e"
                                                       "\na s d"
                                                       "\nz x c"
                                                       "\nدر کیبورد خود اقدام به متوقف کردن قطره های آب کنید"
                                                        "\nترتیب شیر ها به ترتیب کلید های رو کیبوردتان است"
                                "\nاین بازی برای تقویت دقت تمرکز سرعت و هماهنگی بین دست و چشم طراحی شده است"
                                "\nاگر برای اولین بار این بازی را تجربه میکنید شاید نتوانید بدون نگاه کردن به کیبورد دکمه مورد نظر شیر را بزنید اما با تمرین و تلاش میتوانید این کار را انجام دهید پس ناامید نشوید")
def records():
    try:

        with open(f"{main_username}'s score.txt", "r", encoding="utf-8") as record_file:
            myrecords = record_file.read()
            mb.showinfo("امتیاز های قبلی شما", myrecords)

    except FileNotFoundError:
        mb.showwarning("امتیاز های قبلی شما", "برای شما امتیازی ثبت نشده است")
def chose_mode():
    global text_font
    open_setting_window = Tk()
    text_font = tkFont.Font(family="Tahoma", size=15)
    Label(open_setting_window, text="یکی از حالت های زیر را انتخاب کنید", font=text_font).pack()

    def chose_bomb():
        global moode
        mb.showinfo("حالت بمبی", "حالت بمبی با موفقیت فعال شد")
        moode = 2

    def chose_usuall():
        global moode
        mb.showinfo("حالت عادی", "حالت عادی با موفقیت فعال شد")
        moode = 1
    Button(open_setting_window, text="بمبی", command=chose_bomb, font=text_font).pack(side="top", pady=4, fill="x")
    Button(open_setting_window, text="عادی", command=chose_usuall, font=text_font).pack(side="top", pady=4, fill="x")
    open_setting_window.mainloop()

def set_bomb_position():
    bomb1.hideturtle()
    bomb2.hideturtle()
    bomb3.hideturtle()
    bomb4.hideturtle()
    bomb5.hideturtle()
    bomb6.hideturtle()
    bomb7.hideturtle()
    bomb8.hideturtle()
    bomb9.hideturtle()
    bomb1.goto(-370, 180)
    bomb2.goto(-10, 180)
    bomb3.goto(330, 180)
    bomb4.goto(-370, 30)
    bomb5.goto(-10, 30)
    bomb6.goto(330, 30)
    bomb7.goto(-370, -120)
    bomb8.goto(-10, -120)
    bomb9.goto(330, -120)
def set_position(): #تعین موقعیت ابجکت ها
    no1.hideturtle()
    no2.hideturtle()
    no3.hideturtle()
    no4.hideturtle()
    no5.hideturtle()
    no6.hideturtle()
    no7.hideturtle()
    no8.hideturtle()
    no9.hideturtle()
    no1.goto(-370, 180)
    no2.goto(-10, 180)
    no3.goto(330, 180)
    no4.goto(-370, 30)
    no5.goto(-10, 30)
    no6.goto(330, 30)
    no7.goto(-370, -120)
    no8.goto(-10, -120)
    no9.goto(330, -120)
title_font = tkFont.Font(family="B Nazanin", size=25)
text_font = tkFont.Font(family="Tahoma", size=15)
my_logo = PhotoImage(file="image/logo.png")
logo = Label(menu, image=my_logo).pack(side="top", pady=4, fill="x")
welcome = Label(menu, text="نام کاربری خود را وارد کنید", font=text_font).pack(side="top", pady=4)
username_entry = tk.Entry(menu)
username_entry.pack()
lbl_chose = Label(menu, text="سطح خود را انتخاب کنید", font=text_font).pack(side="top", pady=4)
r1 = Radiobutton(menu, text="اسان", command=first_level, font=text_font, value=1, variable=var)
r1.pack()
r2 = Radiobutton(menu, text="متوسط", command=second_level, font=text_font, value=2, variable=var)
r2.pack()
r3 = Radiobutton(menu, text="سخت", command=third_level, font=text_font, value=3, variable=var)
r3.pack()
Button(text="شروع", command=fake_start, font=text_font).pack(side="top", pady=4, fill="x")
Button(text="راهنمای بازی", command=game_guide, font=text_font).pack(side="top", pady=4, fill="x")
Button(text="انتخاب حالت", command=chose_mode, font=text_font).pack(side="top", pady=4, fill="x")
Button(text="درباره ما", command=about_us, font=text_font).pack(side="top", pady=4, fill="x")
Button(text="خروج", command=exit_game, font=text_font).pack(side="top", pady=0, fill="both")
menu.mainloop()
if "main_username" in locals():
    pass
else:exit()
turtle.bgcolor("orange") #بک گراند بازی
turtle.title("نجات آب")
turtle.screensize(400, 300)
turtle.setup(1.0, 1.0)
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-375, 290)
turtle.addshape("image/water.gif")
turtle.addshape("image/Faucet.gif")
turtle.addshape("image/bowl.gif")
turtle.addshape("image/bomb.gif")
base = turtle.Turtle() #ساختن ابجکت های بازی
base.penup()
base.goto(-600, -350)
base.pendown()
base.speed(0.5)
base.width(3)
base.forward(1200)
base.hideturtle()
base1 = turtle.Turtle()
base2 = turtle.Turtle()
base3 = turtle.Turtle()
base11 = turtle.Turtle()
base21 = turtle.Turtle()
base31 = turtle.Turtle()
base12 = turtle.Turtle()
base22 = turtle.Turtle()
base32 = turtle.Turtle()
base13 = turtle.Turtle()
base23 = turtle.Turtle()
base33 = turtle.Turtle()
base14 = turtle.Turtle()
base24 = turtle.Turtle()
base34 = turtle.Turtle()
base15 = turtle.Turtle()
base25 = turtle.Turtle()
base35 = turtle.Turtle()
base16 = turtle.Turtle()
base26 = turtle.Turtle()
base36 = turtle.Turtle()
base1.penup()
base2.penup()
base3.penup()
base11.penup()
base21.penup()
base31.penup()
base12.penup()
base22.penup()
base32.penup()
base13.penup()
base23.penup()
base33.penup()
base14.penup()
base24.penup()
base34.penup()
base15.penup()
base25.penup()
base35.penup()
base16.penup()
base26.penup()
base36.penup()
base1.speed(0.1)
base2.speed(0.1)
base3.speed(0.1)
base11.speed(0.1)
base21.speed(0.1)
base31.speed(0.1)
base12.speed(0.1)
base22.speed(0.1)
base32.speed(0.1)
base13.speed(0.1)
base23.speed(0.1)
base33.speed(0.1)
base14.speed(0.1)
base24.speed(0.1)
base34.speed(0.1)
base15.speed(0.1)
base25.speed(0.1)
base35.speed(0.1)
base16.speed(0.1)
base26.speed(0.1)
base36.speed(0.1)
base1.hideturtle()
base2.hideturtle()
base3.hideturtle()
base11.hideturtle()
base21.hideturtle()
base31.hideturtle()
base12.shape("image/bowl.gif")
base22.shape("image/bowl.gif")
base32.shape("image/bowl.gif")
base13.hideturtle()
base23.hideturtle()
base33.hideturtle()
base14.hideturtle()
base24.hideturtle()
base34.hideturtle()
base15.hideturtle()
base25.hideturtle()
base35.hideturtle()
base16.hideturtle()
base26.hideturtle()
base36.hideturtle()
base1.goto(-370, -348)
base2.goto(-10, -348)
base3.goto(330, -348)
base11.goto(-370, -349)
base21.goto(-10, -349)
base31.goto(330, -349)
base12.goto(-370, -350)
base22.goto(-10, -350)
base32.goto(330, -350)
base13.goto(-370, -351)
base23.goto(-10, -351)
base33.goto(330, -351)
base14.goto(-370, -352)
base24.goto(-10, -352)
base34.goto(330, -352)
base15.goto(-370, -353)
base25.goto(-10, -353)
base35.goto(330, -353)
base16.goto(-370, -354)
base26.goto(-10, -354)
base36.goto(330, -354)
no1 = turtle.Turtle()
no1.shape("image/water.gif")
no2 = turtle.Turtle()
no2.shape("image/water.gif")
no3 = turtle.Turtle()
no3.shape("image/water.gif")
no4 = turtle.Turtle()
no4.shape("image/water.gif")
no5 = turtle.Turtle()
no5.shape("image/water.gif")
no6 = turtle.Turtle()
no6.shape("image/water.gif")
no7 = turtle.Turtle()
no7.shape("image/water.gif")
no8 = turtle.Turtle()
no8.shape("image/water.gif")
no9 = turtle.Turtle()
no9.shape("image/water.gif")
if moode == 2:
    bomb1 = turtle.Turtle()
    bomb2 = turtle.Turtle()
    bomb3 = turtle.Turtle()
    bomb4 = turtle.Turtle()
    bomb5 = turtle.Turtle()
    bomb6 = turtle.Turtle()
    bomb7 = turtle.Turtle()
    bomb8 = turtle.Turtle()
    bomb9 = turtle.Turtle()
    bomb9.speed(0.5)
    bomb8.speed(0.5)
    bomb7.speed(0.5)
    bomb6.speed(0.5)
    bomb5.speed(0.5)
    bomb4.speed(0.5)
    bomb3.speed(0.5)
    bomb2.speed(0.5)
    bomb1.speed(0.5)
    bomb1.shape("image/bomb.gif")
    bomb2.shape("image/bomb.gif")
    bomb3.shape("image/bomb.gif")
    bomb4.shape("image/bomb.gif")
    bomb5.shape("image/bomb.gif")
    bomb6.shape("image/bomb.gif")
    bomb7.shape("image/bomb.gif")
    bomb8.shape("image/bomb.gif")
    bomb9.shape("image/bomb.gif")
    bomb1.penup()
    bomb2.penup()
    bomb3.penup()
    bomb4.penup()
    bomb5.penup()
    bomb6.penup()
    bomb7.penup()
    bomb8.penup()
    bomb9.penup()
    bomb1.right(90)
    bomb2.right(90)
    bomb3.right(90)
    bomb4.right(90)
    bomb5.right(90)
    bomb6.right(90)
    bomb7.right(90)
    bomb8.right(90)
    bomb9.right(90)
    set_bomb_position()
no1.speed(0.5)
no2.speed(0.5)
no3.speed(0.5)
no4.speed(0.5)
no5.speed(0.5)
no6.speed(0.5)
no7.speed(0.5)
no8.speed(0.5)
no9.speed(0.5)
no1.penup()
no2.penup()
no3.penup()
no4.penup()
no5.penup()
no6.penup()
no7.penup()
no8.penup()
no9.penup()
no1.right(90)
no2.right(90)
no3.right(90)
no4.right(90)
no5.right(90)
no6.right(90)
no7.right(90)
no8.right(90)
no9.right(90)
set_position()
pic7 = Turtle()
pic7.shape("image/Faucet.gif")
pic7.penup()
pic7.goto(-350, 200)
pic7.speed(0)
pic8 = Turtle()
pic8.shape("image/Faucet.gif")
pic8.penup()
pic8.goto(10, 200)
pic8.speed(0)
pic9 = Turtle()
pic9.shape("image/Faucet.gif")
pic9.penup()
pic9.goto(350, 200)
pic9.speed(0)
pic4 = Turtle()
pic4.shape("image/Faucet.gif")
pic4.penup()
pic4.goto(-350, 50)
pic4.speed(0)
pic5 = Turtle()
pic5.shape("image/Faucet.gif")
pic5.penup()
pic5.goto(10, 50)
pic5.speed(0)
pic6 = Turtle()
pic6.shape("image/Faucet.gif")
pic6.penup()
pic6.goto(350, 50)
pic6.speed(0)
pic1 = Turtle()
pic1.shape("image/Faucet.gif")
pic1.penup()
pic1.goto(-350, -100)
pic1.speed(0)
pic2 = Turtle()
pic2.shape("image/Faucet.gif")
pic2.penup()
pic2.goto(10, -100)
pic2.speed(0)
pic3 = Turtle()
pic3.shape("image/Faucet.gif")
pic3.penup()
pic3.goto(350, -100)
pic3.speed(0)
no1.width(15)
no2.width(15)
no3.width(15)
no4.width(15)
no5.width(15)
no6.width(15)
no7.width(15)
no8.width(15)
no9.width(15)
def fake_start():
    global speed, main_username
    if speed == 0:
        mb.showwarning("یکی از سطح ها را انتخاب کنید", "شما هیچ سطحی را انتخاب نکرده اید")
    else:
        menu.destroy()
        main_username = username_entry.get()
def q7(): #تابع های خوردن یک کلید
    return keyboard.is_pressed("7") or keyboard.is_pressed("q")
def w8():
    return keyboard.is_pressed("8") or keyboard.is_pressed("w")
def e9():
    return keyboard.is_pressed("9") or keyboard.is_pressed("e")
def a4():
    return keyboard.is_pressed("4") or keyboard.is_pressed("a")
def s5():
    return keyboard.is_pressed("5") or keyboard.is_pressed("s")
def d6():
    return keyboard.is_pressed("6") or keyboard.is_pressed("d")
def z1():
    return keyboard.is_pressed("1") or keyboard.is_pressed("z")
def x2():
    return keyboard.is_pressed("2") or keyboard.is_pressed("x")
def c3():
    return keyboard.is_pressed("3") or keyboard.is_pressed("c")

def bomb_lose(finall_score):
    global avg_reflex, right_accuracy, wrong_accuracy, text_font
    pygame.init()
    lose_sound = pygame.mixer.music.load("audio/lose.mp3")
    pygame.mixer.music.play()
    lose_message = tk.Tk()
    title_font = tkFont.Font(family="B Nazanin", size=25)
    text_font = tkFont.Font(family="Tahoma", size=15)

    lbl_lose_message = Label(lose_message, text="شما باختید\n"
                                                 f"امتیاز نهایی شما = {finall_score}", font=text_font).pack(side="top", pady=4, fill="x")
    sum_accuracy = right_accuracy + wrong_accuracy
    if sum_accuracy != 0:
        x = 100 - (wrong_accuracy * (100/sum_accuracy))
    else: x = 0
    if len(avg_reflex) == 0:
        lbl_show_time = Label(lose_message, text="شما عکس العملی نشان ندادید", font=text_font).pack(side="top", pady=4, fill="x")
    else: lbl_show_time = Label(lose_message, text=f" میانگین عکس العمل شما به ثانیه= {sum(avg_reflex)/ len(avg_reflex)}", font=text_font).pack(side="top", pady=4, fill="x")

    lbl_accuracy = Label(lose_message, text=f"دقت شما = %{x}", font=text_font).pack(side="top", pady=4, fill="x")

    def replay2(): #تابع شروع مجدد
        global finall_score, avg_reflex, wrong_accuracy, right_accuracy
        wrong_accuracy = 0
        right_accuracy = 0
        finall_score = 0
        avg_reflex = []
        finall_time = 0
        bool = True
        score_writer.clear()
        lose_message.destroy()
        set_position()
        set_bomb_position()
        time.sleep(0.5)
        timer()
        bomb_replay(True)

    def replay3(): #تابع شروع مجدد برای منوی فراخوان شده
        global finall_score, avg_reflex, wrong_accuracy, right_accuracy
        wrong_accuracy = 0
        right_accuracy = 0
        finall_score = 0
        avg_reflex = []
        finall_time = 0
        bool = True
        score_writer.clear()
        set_position()
        set_bomb_position()
        time.sleep(0.5)
        timer()
        bomb_replay(True)
    user_score = open(f"{main_username}'s score.txt", "a", encoding="utf-8")
    user_score.write(f"امتیاز شما ={finall_score}\n")
    if len(avg_reflex) != False:
        user_score.write(f"میانگین عکس العمل شما به ثانیه ={sum(avg_reflex) / len(avg_reflex)}\n")

    else:
        user_score.write("عکس العملی برای شما ثبت نشده است\n")
    user_score.write(f"دقت شما = %{x}\n")
    user_score.write("---------------------------------------------\n")
    user_score.close()
    with open(f"high {main_username}'s score.txt", "a", encoding='utf-8') as scores:
        scores.write(f"{finall_score}/")
    with open(f"high {main_username}'s score.txt", "r", encoding='utf-8') as scores:
        lst_scores = scores.read().split("/")
        lst_scores.remove("")
        new_lst_scores = []
        for i in lst_scores:
            i = float(i)
            new_lst_scores.append(int(i))
        num_max = max(new_lst_scores)
        lbl_scores = Label(lose_message, text=f"بالا ترین امتیاز شما = {num_max}", font=text_font).pack(side="top", pady=4, fill="x")

    def open_menu():
        global text_font, var
        lose_message.destroy()
        menu = Tk()
        title_font = tkFont.Font(family="B Nazanin", size=25)
        text_font = tkFont.Font(family="Tahoma", size=15)
        global score, speed
        speed = 0
        score = 0

        def fake_start():
            global speed
            if speed == 0:
                mb.showwarning("یکی از سطح ها را انتخاب کنید", "شما هیچ سطحی را انتخاب نکرده اید")
            else:
                menu.destroy()
                replay3()
        lbl_chose = Label(menu, text="سطح خود را انتخاب کنید", font=text_font).pack()
        r1 = Radiobutton(menu, text="اسان", command=first_level, font=text_font, value=1, variable=var)
        r1.pack(side="top", pady=4, fill="x")
        r2 = Radiobutton(menu, text="متوسط", command=second_level, font=text_font, value=2, variable=var)
        r2.pack(side="top", pady=4, fill="x")
        r3 = Radiobutton(menu, text="سخت", command=third_level, font=text_font, value=3, variable=var)
        r3.pack(side="top", pady=4, fill="x")
        btn_start = Button(menu, text="شروع", command=fake_start, font=text_font).pack(side="top", pady=4, fill="x")
        btn_game_guide = Button(menu, text="راهنمای بازی", command=game_guide, font=text_font).pack(side="top", pady=4, fill="x")
        btn_records = Button(menu, text="امتیاز های قبلی شما", command=records, font=text_font).pack(side="top", pady=4, fill="x")
        btn_about_us = Button(menu, text="درباره ما", command=about_us, font=text_font).pack(side="top", pady=4, fill="x")
        btn_exit = Button(menu, text="خروج", command=exit_game, font=text_font).pack(side="top", pady=4, fill="x")
        menu.mainloop()
    bool = False
    lbl_y_n = Label(lose_message, text="ایا میخواهید دوباره بازی کنید؟", font=text_font).pack(side="top", pady=4, fill="x")
    btn_again = Button(lose_message, text="بله", command=replay2, font=text_font).pack(side="top", pady=4, fill="x")
    btn_exit = Button(lose_message, text="خیر", command=exit_game, font=text_font).pack(side="top", pady=4, fill="x")
    btn_menu = Button(lose_message, text="صفحه اصلی", command=open_menu, font=text_font).pack(side="top", pady=4, fill="x")
    lose_message.mainloop()
def lose(finall_score):#تابع باختن
    global avg_reflex, right_accuracy, wrong_accuracy, text_font
    pygame.init()
    lose_sound = pygame.mixer.music.load("audio/lose.mp3")
    pygame.mixer.music.play()
    lose_message = tk.Tk()
    title_font = tkFont.Font(family="B Nazanin", size=25)
    text_font = tkFont.Font(family="Tahoma", size=15)

    lbl_lose_message = Label(lose_message, text="شما باختید\n"
                                                 f"امتیاز نهایی شما = {finall_score}", font=text_font).pack(side="top", pady=4, fill="x")
    sum_accuracy = right_accuracy + wrong_accuracy
    if sum_accuracy != 0:
        x = 100 - (wrong_accuracy * (100/sum_accuracy))
    else: x = 0
    if len(avg_reflex) == 0:
        lbl_show_time = Label(lose_message, text="شما عکس العملی نشان ندادید", font=text_font).pack(side="top", pady=4, fill="x")
    else: lbl_show_time = Label(lose_message, text=f" میانگین عکس العمل شما به ثانیه= {sum(avg_reflex)/ len(avg_reflex)}", font=text_font).pack(side="top", pady=4, fill="x")

    lbl_accuracy = Label(lose_message, text=f"دقت شما = %{x}", font=text_font).pack(side="top", pady=4, fill="x")

    def replay2(): #تابع شروع مجدد
        global finall_score, avg_reflex, wrong_accuracy, right_accuracy
        wrong_accuracy = 0
        right_accuracy = 0
        finall_score = 0
        avg_reflex = []
        finall_time = 0
        bool = True
        score_writer.clear()
        lose_message.destroy()
        set_position()
        time.sleep(0.5)
        timer()
        replay(True)

    def replay3(): #تابع شروع مجدد برای منوی فراخوان شده
        global finall_score, avg_reflex, wrong_accuracy, right_accuracy
        wrong_accuracy = 0
        right_accuracy = 0
        finall_score = 0
        avg_reflex = []
        finall_time = 0
        bool = True
        score_writer.clear()
        set_position()
        time.sleep(0.5)
        timer()
        replay(True)
    user_score = open(f"{main_username}'s score.txt", "a", encoding="utf-8")
    user_score.write(f"امتیاز شما ={finall_score}\n")
    if len(avg_reflex) != False:
        user_score.write(f"میانگین عکس العمل شما به ثانیه ={sum(avg_reflex) / len(avg_reflex)}\n")

    else:
        user_score.write("عکس العملی برای شما ثبت نشده است\n")
    user_score.write(f"دقت شما = %{x}\n")
    user_score.write("---------------------------------------------\n")
    user_score.close()
    with open(f"high {main_username}'s score.txt", "a", encoding='utf-8') as scores:
        scores.write(f"{finall_score}/")
    with open(f"high {main_username}'s score.txt", "r", encoding='utf-8') as scores:
        lst_scores = scores.read().split("/")
        lst_scores.remove("")
        new_lst_scores = []
        for i in lst_scores:
            i = float(i)
            new_lst_scores.append(int(i))
        num_max = max(new_lst_scores)
        lbl_scores = Label(lose_message, text=f"بالا ترین امتیاز شما = {num_max}", font=text_font).pack(side="top", pady=4, fill="x")

    def open_menu():
        global text_font, var
        lose_message.destroy()
        menu = Tk()
        title_font = tkFont.Font(family="B Nazanin", size=25)
        text_font = tkFont.Font(family="Tahoma", size=15)
        global score, speed
        speed = 0
        score = 0

        def fake_start():
            global speed
            if speed == 0:
                mb.showwarning("یکی از سطح ها را انتخاب کنید", "شما هیچ سطحی را انتخاب نکرده اید")
            else:
                menu.destroy()
                replay3()
        lbl_chose = Label(menu, text="سطح خود را انتخاب کنید", font=text_font).pack()
        r1 = Radiobutton(menu, text="اسان", command=first_level, font=text_font, value=1, variable=var)
        r1.pack()
        r2 = Radiobutton(menu, text="متوسط", command=second_level, font=text_font, value=2, variable=var)
        r2.pack()
        r3 = Radiobutton(menu, text="سخت", command=third_level, font=text_font, value=3, variable=var)
        r3.pack()
        btn_start = Button(menu, text="شروع", command=fake_start, font=text_font).pack(side="top", pady=4, fill="x")
        btn_game_guide = Button(menu, text="راهنمای بازی", command=game_guide, font=text_font).pack(side="top", pady=4, fill="x")
        btn_records = Button(menu, text="امتیاز های قبلی شما", command=records, font=text_font).pack(side="top", pady=4, fill="x")
        btn_about_us = Button(menu, text="درباره ما", command=about_us, font=text_font).pack(side="top", pady=4, fill="x")
        btn_exit = Button(menu, text="خروج", command=exit_game, font=text_font).pack(side="top", pady=4, fill="x")
        menu.mainloop()

    bool = False
    lbl_y_n = Label(lose_message, text="ایا میخواهید دوباره بازی کنید؟", font=text_font).pack(side="top", pady=4, fill="x")
    btn_again = Button(lose_message, text="بله", command=replay2, font=text_font).pack(side="top", pady=4, fill="x")
    btn_exit = Button(lose_message, text="خیر", command=exit_game, font=text_font).pack(side="top", pady=4, fill="x")
    btn_menu = Button(lose_message, text="صفحه اصلی", command=open_menu, font=text_font).pack(side="top", pady=4, fill="x")
    lose_message.mainloop()
def win(): #تابع بردن
    pygame.init()
    win_sound = pygame.mixer.music.load("audio/win.mp3")
    pygame.mixer.music.play()
    global score, finall_score, right_accuracy, start_time, stop_time, row
    right_accuracy += 1
    set_position()
    time.sleep(0.2)
    stop_timer()
    if r == 1:
        distance = no1.distance(-370, -350)
    elif r == 4:
        distance = no4.distance(-370, -350)
    elif r == 7:
        distance = no7.distance(-370, -350)
    elif r == 2:
        distance = no2.distance(-10, -350)
    elif r  == 5:
        distance = no5.distance(-10, -350)
    elif r == 8:
        distance = no8.distance(-10, -350)
    elif r  == 3:
        distance = no3.distance(330, -350)
    elif r == 6:
        distance = no6.distance(330, -350)
    elif r == 9:
        distance = no9.distance(330, -350)
    reflex = round(stop_time - start_time, 3)
    finall_score += (score + round(distance)//10 - round(reflex, 1)*10)*row
    avg_reflex.append(reflex)
    print(avg_reflex[-1])
    replay(True)
def bomb_win(): #تابع بردن
    pygame.init()
    win_sound = pygame.mixer.music.load("audio/win.mp3")
    pygame.mixer.music.play()
    global score, finall_score, right_accuracy, start_time, stop_time, row
    right_accuracy += 1
    set_position()
    time.sleep(0.2)
    stop_timer()
    if r == 1:
        distance = no1.distance(-370, -350)
    elif r == 4:
        distance = no4.distance(-370, -350)
    elif r == 7:
        distance = no7.distance(-370, -350)
    elif r == 2:
        distance = no2.distance(-10, -350)
    elif r  == 5:
        distance = no5.distance(-10, -350)
    elif r == 8:
        distance = no8.distance(-10, -350)
    elif r  == 3:
        distance = no3.distance(330, -350)
    elif r == 6:
        distance = no6.distance(330, -350)
    elif r == 9:
        distance = no9.distance(330, -350)
    reflex = round(stop_time - start_time, 3)
    finall_score += (score + round(distance)//10 - round(reflex, 1)*10)*row
    avg_reflex.append(reflex)
    print(avg_reflex[-1])
    bomb_replay(True)

def timer():
    for i in range(3): #تابع ساختن تایمر شروع بازی
        num_timer = turtle.Turtle()
        num_timer.hideturtle()
        num_timer.penup()
        num_timer.goto(10, 50)
        num_timer.write(i+1, align="center", font=("Arial", 100, "normal"))
        pygame.init()
        timer = pygame.mixer.music.load("audio/timer.mp3")
        pygame.mixer.music.play()
        time.sleep(1)
        num_timer.clear()
    pygame.init()
    timer = pygame.mixer.music.load("audio/ding.mp3")
    pygame.mixer.music.play()

timer()
wrong_accuracy = 0
right_accuracy = 0
finall_score = 0
avg_reflex = []
un_change_first_level_bool = True
un_change_second_level_bool = True
test_number = 0
def bomb_sound():
    pygame.init()
    bombs_sound = pygame.mixer.music.load("audio/bomb.mp3")
    pygame.mixer.music.play()

def p_t(): #تابع مجازات کردن
    pygame.init()
    pt_sound = pygame.mixer.music.load("audio/pt.mp3")
    pygame.mixer.music.play()
    global finall_score, score, wrong_accuracy
    wrong_accuracy += 1
    stop_timer()
    reflex = round(stop_time - start_time, 3)
    finall_score += (- (score)*3 - round(reflex)*10)*row
    score_writer.clear()
    score_writer.write(f"امتیاز = {finall_score}", font=("Arial", 20, "normal"))
    time.sleep(0.2)
def bomb_p_t(): #تابع مجازات کردن
    bomb_sound()
    global finall_score, score, wrong_accuracy
    wrong_accuracy += 1
    stop_timer()
    reflex = round(stop_time - start_time, 3)
    finall_score += (- (score)*3 - round(reflex)*10)*row
    score_writer.clear()
    score_writer.write(f"امتیاز = {finall_score}", font=("Arial", 20, "normal"))
    time.sleep(0.2)

def start_timer():
    global start_time
    start_time = datetime.now().timestamp()
    return start_time

def stop_timer():
    global stop_time
    stop_time = datetime.now().timestamp()
    return stop_time

def bomb_replay(bool):#حلقه اصلی بازی
    global finall_score, score, stop_time, start_time, row, r, avg_reflex, right_accuracy, wrong_accuracy, speed, test_number, text_font, text_font
    if speed == 2 and finall_score > 1000 and un_change_first_level_bool:
        change_level = Tk()
        title_font = tkFont.Font(family="B Nazanin", size=25)
        text_font = tkFont.Font(family="Tahoma", size=15)
        def change_first_level():
            global speed, score
            speed = 3.5
            score = 20
            change_level.destroy()
            timer()
            bomb_replay(True)
        def un_change_first_level():
            global un_change_first_level_bool
            un_change_first_level_bool = False
            change_level.destroy()
            timer()
            bomb_replay(True)
        Label(change_level, text="تبریک!\n"
                                    "شما توانستید مرحله اول را به خوبی رد کنید", font=text_font).pack()
        sum_accuracy = right_accuracy + wrong_accuracy
        if sum_accuracy != 0:
            x = 100 - (wrong_accuracy * (100 / sum_accuracy))
        else:
            x = 0
        if len(avg_reflex) == 0:
            lbl_show_time = Label(change_level, text="شما عکس العملی نشان ندادید", font=text_font).pack()
        else:
            lbl_show_time = Label(change_level,
                                    text=f" میانگین عکس العمل شما به ثانیه= {sum(avg_reflex) / len(avg_reflex)}",
                                    font=text_font).pack()

            lbl_accuracy = Label(change_level, text=f"دقت شما = %{x}", font=text_font).pack()
            Message(change_level, text="شما میتوانید برای بهتر کردن عکس العمل خود به مرحله بعد بروید"
                                       "اما اگر فکر میکنید نیاز به تمرین بیشتر دارید میتوانید در همین مرحله بمانبد", font=text_font).pack()
            Button(change_level, text="بله", command=change_first_level, font=text_font).pack(fill="x")
            Button(change_level, text="خیر", command=un_change_first_level, font=text_font).pack(fill="x")
            change_level.mainloop()
    elif speed == 3.5 and finall_score > 2000 and un_change_second_level_bool:
        def change_second_level():
            global speed, score
            speed = 5
            score = 30
            change_level.destroy()
            timer()
            bomb_replay(True)
        def un_change_second_level():
            global un_change_second_level_bool
            un_change_second_level_bool = False
            change_level.destroy()
            timer()
            bomb_replay(True)
        change_level = Tk()
        title_font = tkFont.Font(family="B Nazanin", size=25)
        text_font = tkFont.Font(family="Tahoma", size=15)
        Label(change_level, text="تبریک!\n"
                                    "شما توانستید مرحله دوم را به خوبی رد کنید", font=text_font).pack()
        sum_accuracy = right_accuracy + wrong_accuracy
        if sum_accuracy != 0:
            x = 100 - (wrong_accuracy * (100 / sum_accuracy))
        else:
            x = 0
        if len(avg_reflex) == 0:
            lbl_show_time = Label(change_level, text="شما عکس العملی نشان ندادید", font=text_font).pack()
        else:
            lbl_show_time = Label(change_level,
                                    text=f" میانگین عکس العمل شما به ثانیه= {sum(avg_reflex) / len(avg_reflex)}",
                                    font=text_font).pack()

            lbl_accuracy = Label(change_level, text=f"دقت شما = %{x}", font=text_font).pack()
            Message(change_level, text="شما میتوانید برای بهتر کردن عکس العمل خود به مرحله بعد بروید"
                                     "اما اگر فکر میکنید نیاز به تمرین بیشتر دارید میتوانید در همین مرحله بمانبد", font=text_font).pack()
            Button(change_level, text="بله", command=change_second_level, font=text_font).pack(fill="x")
            Button(change_level, text="خیر", command=un_change_second_level, font=text_font).pack(fill="x")
            change_level.mainloop()
    r = random.randint(1, 9)
    start_timer()
    score_writer.clear()
    score_writer.write(f"امتیاز = {finall_score}", font=("Arial", 20, "normal"))
    if speed == 5 and finall_score > 3000:
        test_number += 1
    if 5 == test_number:
        speed += 0.5
    elif 10 == test_number:
        speed += 0.5
    bomb = random.randint(1, 4)
    if bomb == 3:
        if r == 1:
            row = 1
            bomb1.showturtle()
            while bool:
                bomb1.forward(speed)
                if bomb1.pos() == base1.pos() or bomb1.pos() == base11.pos() or bomb1.pos() == base12.pos() or bomb1.pos() == base13.pos() or bomb1.pos() == base14.pos():
                    set_bomb_position()
                    bomb_replay(True)
                    break
                if q7():
                    bomb_p_t()
                    set_bomb_position()
                    bomb_replay(True)
                    break

        elif r == 2:
            row = 1
            bomb2.showturtle()
            while bool:
                bomb2.forward(speed)
                if bomb2.pos() == base2.pos() or bomb2.pos() == base21.pos() or bomb2.pos() == base22.pos() or bomb2.pos() == base23.pos() or bomb2.pos() == base24.pos():
                    set_bomb_position()
                    bomb_replay(True)
                    break
                if w8():
                    bomb_p_t()
                    set_bomb_position()
                    bomb_replay(True)
                    break

        elif r == 3:
            row = 1
            bomb3.showturtle()
            while bool:
                bomb3.forward(speed)
                if bomb3.pos() == base3.pos() or bomb3.pos() == base31.pos() or bomb3.pos() == base32.pos() or bomb3.pos() == base33.pos() or bomb3.pos() == base34.pos():
                    set_bomb_position()
                    bomb_replay(True)
                    break
                if e9():
                    bomb_p_t()
                    set_bomb_position()
                    bomb_replay(True)
                    break

        elif r == 4:
            row = 1.5
            bomb4.showturtle()
            while bool:
                bomb4.forward(speed)
                if bomb4.pos() == base1.pos() or bomb4.pos() == base11.pos() or bomb4.pos() == base12.pos() or bomb4.pos() == base13.pos() or bomb4.pos() == base14.pos():
                    set_bomb_position()
                    bomb_replay(True)
                    break
                if a4():
                    bomb_p_t()
                    set_bomb_position()
                    bomb_replay(True)
                    break

        elif r == 5:
            row = 1.5
            bomb5.showturtle()
            while bool:
                bomb5.forward(speed)
                if bomb5.pos() == base2.pos() or bomb5.pos() == base21.pos() or bomb5.pos() == base22.pos() or bomb5.pos() == base23.pos() or bomb5.pos() == base24.pos():
                    set_bomb_position()
                    bomb_replay(True)
                    break
                if s5():
                    bomb_p_t()
                    set_bomb_position()
                    bomb_replay(True)
                    break

        elif r == 6:
            row = 1.5
            bomb6.showturtle()
            while bool:
                bomb6.forward(speed)
                if bomb6.pos() == base3.pos() or bomb6.pos() == base31.pos() or bomb6.pos() == base32.pos() or bomb6.pos() == base33.pos() or bomb6.pos() == base34.pos():
                    set_bomb_position()
                    bomb_replay(True)
                    break
                if d6():
                    bomb_p_t()
                    set_bomb_position()
                    bomb_replay(True)
                    break

        elif r == 7:
            row = 2
            bomb7.showturtle()
            while bool:
                bomb7.forward(speed)
                if bomb7.pos() == base1.pos() or bomb7.pos() == base11.pos() or bomb7.pos() == base12.pos() or bomb7.pos() == base13.pos() or bomb7.pos() == base14.pos():
                    set_bomb_position()
                    bomb_replay(True)
                    break
                if z1():
                    bomb_p_t()
                    set_bomb_position()
                    bomb_replay(True)
                    break

        elif r == 8:
            row = 2
            bomb8.showturtle()
            while bool:
                bomb8.forward(speed)
                if bomb8.pos() == base2.pos() or bomb8.pos() == base21.pos() or bomb8.pos() == base22.pos() or bomb8.pos() == base23.pos() or bomb8.pos() == base24.pos():
                    set_bomb_position()
                    bomb_replay(True)
                    break
                if x2():
                    bomb_p_t()
                    set_bomb_position()
                    bomb_replay(True)
                    break

        elif r == 9:
            bomb9.showturtle()
            row = 2
            while bool:
                bomb9.forward(speed)
                if bomb9.pos() == base3.pos() or bomb9.pos() == base31.pos() or bomb9.pos() == base32.pos() or bomb9.pos() == base33.pos() or bomb9.pos() == base34.pos():
                    set_bomb_position()
                    bomb_replay(True)
                    break
                if c3():
                    bomb_p_t()
                    set_bomb_position()
                    bomb_replay(True)
                    break
    ##########################
    else:
        if r == 1:
            row = 1
            no1.showturtle()
            while bool:
                no1.forward(speed)
                if no1.pos() == base1.pos() or no1.pos() == base11.pos() or no1.pos() == base12.pos() or no1.pos() == base13.pos() or no1.pos() == base14.pos():
                    bomb_lose(finall_score)  # چک کردن باخت
                    break
                if q7():  # چک کردن برد
                    bomb_win()
                    break
                if w8() or e9() or a4() or s5() or d6() or z1() or x2() or c3():
                    p_t()  # چک کردن اشتباه

        elif r == 2:
            row = 1
            no2.showturtle()
            while bool:
                no2.forward(speed)
                if no2.pos() == base2.pos() or no2.pos() == base21.pos() or no2.pos() == base22.pos() or no2.pos() == base23.pos() or no2.pos() == base24.pos():
                    bomb_lose(finall_score)
                    break
                if w8():
                    bomb_win()
                    break
                if q7() or e9() or a4() or s5() or d6() or z1() or x2() or c3():
                    p_t()

        elif r == 3:
            row = 1
            no3.showturtle()
            while bool:
                no3.forward(speed)
                if no3.pos() == base3.pos() or no3.pos() == base31.pos() or no3.pos() == base32.pos() or no3.pos() == base33.pos() or no3.pos() == base34.pos():
                    bomb_lose(finall_score)
                    break
                if e9():
                    bomb_win()
                    break
                if q7() or w8() or a4() or s5() or d6() or z1() or x2() or c3():
                    p_t()

        elif r == 4:
            row = 1.5
            no4.showturtle()
            while bool:
                no4.forward(speed)
                if no4.pos() == base1.pos() or no4.pos() == base11.pos() or no4.pos() == base12.pos() or no4.pos() == base13.pos() or no4.pos() == base14.pos():
                    bomb_lose(finall_score)
                    break
                if a4():
                    bomb_win()
                    break
                if q7() or w8() or e9() or s5() or d6() or z1() or x2() or c3():
                    p_t()

        elif r == 5:
            row = 1.5
            no5.showturtle()
            while bool:
                no5.forward(speed)
                if no5.pos() == base2.pos() or no5.pos() == base21.pos() or no5.pos() == base22.pos() or no5.pos() == base23.pos() or no5.pos() == base24.pos():
                    bomb_lose(finall_score)
                    break
                if s5():
                    bomb_win()
                    break
                if q7() or w8() or e9() or a4() or d6() or z1() or x2() or c3():
                    p_t()

        elif r == 6:
            row = 1.5
            no6.showturtle()
            while bool:
                no6.forward(speed)
                if no6.pos() == base3.pos() or no6.pos() == base31.pos() or no6.pos() == base32.pos() or no6.pos() == base33.pos() or no6.pos() == base34.pos():
                    bomb_lose(finall_score)
                    break
                if d6():
                    bomb_win()
                    break
                if q7() or w8() or e9() or s5() or a4() or z1() or x2() or c3():
                    p_t()

        elif r == 7:
            row = 2
            no7.showturtle()
            while bool:
                no7.forward(speed)
                if no7.pos() == base1.pos() or no7.pos() == base11.pos() or no7.pos() == base12.pos() or no7.pos() == base13.pos() or no7.pos() == base14.pos():
                    bomb_lose(finall_score)
                    break
                if z1():
                    bomb_win()
                    break
                if q7() or w8() or e9() or s5() or a4() or d6() or x2() or c3():
                    p_t()

        elif r == 8:
            row = 2
            no8.showturtle()
            while bool:
                no8.forward(speed)
                if no8.pos() == base2.pos() or no8.pos() == base21.pos() or no8.pos() == base22.pos() or no8.pos() == base23.pos() or no8.pos() == base24.pos():
                    bomb_lose(finall_score)
                    break
                if x2():
                    bomb_win()
                    break
                if q7() or w8() or e9() or s5() or a4() or d6() or z1() or c3():
                    p_t()

        elif r == 9:
            row = 2
            no9.showturtle()
            while bool:
                no9.forward(speed)
                if no9.pos() == base3.pos() or no9.pos() == base31.pos() or no9.pos() == base32.pos() or no9.pos() == base33.pos() or no9.pos() == base34.pos():
                    bomb_lose(finall_score)
                    break
                if c3():
                    bomb_win()
                    break
                if q7() or w8() or e9() or s5() or a4() or d6() or x2() or z1():
                    p_t()
def replay(bool):#حلقه اصلی بازی
    global finall_score, score, stop_time, start_time, row, r, avg_reflex, right_accuracy, wrong_accuracy, speed, test_number, text_font
    if speed == 2 and finall_score > 1000 and un_change_first_level_bool:
        change_level = Tk()
        title_font = tkFont.Font(family="B Nazanin", size=25)
        text_font = tkFont.Font(family="Tahoma", size=15)
        def change_first_level():
            global speed, score
            speed = 3
            score = 20
            change_level.destroy()
            timer()
            replay(True)
        def un_change_first_level():
            global un_change_first_level_bool
            change_level.destroy()
            un_change_first_level_bool = False
            timer()
            replay(True)
        Label(change_level, text="تبریک!\n"
                                    "شما توانستید مرحله اول را به خوبی رد کنید", font=text_font).pack()
        sum_accuracy = right_accuracy + wrong_accuracy
        if sum_accuracy != 0:
            x = 100 - (wrong_accuracy * (100 / sum_accuracy))
        else:
            x = 0
        if len(avg_reflex) == 0:
            lbl_show_time = Label(change_level, text="شما عکس العملی نشان ندادید", font=text_font).pack()
        else:
            lbl_show_time = Label(change_level,
                                    text=f" میانگین عکس العمل شما به ثانیه= {sum(avg_reflex) / len(avg_reflex)}",
                                    font=text_font).pack()

            lbl_accuracy = Label(change_level, text=f"دقت شما = %{x}", font=text_font).pack()
            Message(change_level, text="شما میتوانید برای بهتر کردن عکس العمل خود به مرحله بعد بروید"
                                     "اما اگر فکر میکنید نیاز به تمرین بیشتر دارید میتوانید در همین مرحله بمانبد", font=text_font).pack()
            Button(change_level, text="بله", command=change_first_level, font=text_font).pack(fill="x")
            Button(change_level, text="خیر", command=un_change_first_level, font=text_font).pack(fill="x")
            change_level.mainloop()
    elif speed == 3 and finall_score > 2000 and un_change_second_level_bool:
        def change_second_level():
            global speed, score
            speed = 4
            score = 30
            change_level.destroy()
            timer()
            replay(True)
        def un_change_second_level():
            global un_change_second_level_bool
            change_level.destroy()
            un_change_second_level_bool = False
            timer()
            replay(True)
        change_level = Tk()
        title_font = tkFont.Font(family="B Nazanin", size=25)
        text_font = tkFont.Font(family="Tahoma", size=15)
        Label(change_level, text="تبریک!\n"
                                    "شما توانستید مرحله دوم را به خوبی رد کنید", font=text_font).pack()
        sum_accuracy = right_accuracy + wrong_accuracy
        if sum_accuracy != 0:
            x = 100 - (wrong_accuracy * (100 / sum_accuracy))
        else:
            x = 0
        if len(avg_reflex) == 0:
            lbl_show_time = Label(change_level, text="شما عکس العملی نشان ندادید", font=text_font).pack()
        else:
            lbl_show_time = Label(change_level,
                                    text=f" میانگین عکس العمل شما به ثانیه= {sum(avg_reflex) / len(avg_reflex)}",
                                    font=text_font).pack()

            lbl_accuracy = Label(change_level, text=f"دقت شما = %{x}", font=text_font).pack()
            Message(change_level, text="شما میتوانید برای بهتر کردن عکس العمل خود به مرحله بعد بروید "
                                     "اما اگر فکر میکنید نیاز به تمرین بیشتر دارید میتوانید در همین مرحله بمانبد", font=text_font).pack()
            Button(change_level, text="بله", command=change_second_level, font=text_font).pack(fill="x")
            Button(change_level, text="خیر", command=un_change_second_level, font=text_font).pack(fill="x")
            change_level.mainloop()
    r = random.randint(1, 9)
    start_timer()
    score_writer.clear()
    score_writer.write(f"امتیاز = {finall_score}", font=("Arial", 20, "normal"))
    if speed == 5:
        test_number += 1
    if 5 == test_number:
        speed += 0.5
    elif 10 == test_number:
        speed += 0.5
    if r == 1:
        row = 1
        no1.showturtle()
        while bool:
            no1.forward(speed)
            if no1.pos() == base1.pos() or no1.pos() == base11.pos() or no1.pos() == base12.pos() or no1.pos() == base13.pos() or no1.pos() == base14.pos():
                lose(finall_score)#چک کردن باخت
                break
            if q7(): #چک کردن برد
                win()
                break
            if w8() or e9() or a4() or s5() or d6() or z1() or x2() or c3():
                p_t() #چک کردن اشتباه

    elif r == 2:
        row = 1
        no2.showturtle()
        while bool:
            no2.forward(speed)
            if no2.pos() == base2.pos() or no2.pos() == base21.pos() or no2.pos() == base22.pos() or no2.pos() == base23.pos() or no2.pos() == base24.pos():
                lose(finall_score)
                break
            if w8():
                win()
                break
            if q7() or e9() or a4() or s5() or d6() or z1() or x2() or c3():
                p_t()

    elif r == 3:
        row = 1
        no3.showturtle()
        while bool:
            no3.forward(speed)
            if no3.pos() == base3.pos() or no3.pos() == base31.pos() or no3.pos() == base32.pos() or no3.pos() == base33.pos() or no3.pos() == base34.pos():
                lose(finall_score)
                break
            if e9():
                win()
                break
            if q7() or w8() or a4() or s5() or d6() or z1() or x2() or c3():
                p_t()

    elif r == 4:
        row = 1.5
        no4.showturtle()
        while bool:
            no4.forward(speed)
            if no4.pos() == base1.pos() or no4.pos() == base11.pos() or no4.pos() == base12.pos() or no4.pos() == base13.pos() or no4.pos() == base14.pos():
                lose(finall_score)
                break
            if a4():
                win()
                break
            if q7() or w8() or e9() or s5() or d6() or z1() or x2() or c3():
                p_t()

    elif r == 5:
        row = 1.5
        no5.showturtle()
        while bool:
            no5.forward(speed)
            if no5.pos() == base2.pos() or no5.pos() == base21.pos() or no5.pos() == base22.pos() or no5.pos() == base23.pos() or no5.pos() == base24.pos():
                lose(finall_score)
                break
            if s5():
                win()
                break
            if q7() or w8() or e9() or a4() or d6() or z1() or x2() or c3():
                p_t()

    elif r == 6:
        row = 1.5
        no6.showturtle()
        while bool:
            no6.forward(speed)
            if no6.pos() == base3.pos() or no6.pos() == base31.pos() or no6.pos() == base32.pos() or no6.pos() == base33.pos() or no6.pos() == base34.pos():
                lose(finall_score)
                break
            if d6():
                win()
                break
            if q7() or w8() or e9() or s5() or a4() or z1() or x2() or c3():
                p_t()

    elif r == 7:
        row = 2
        no7.showturtle()
        while bool:
            no7.forward(speed)
            if no7.pos() == base1.pos() or no7.pos() == base11.pos() or no7.pos() == base12.pos() or no7.pos() == base13.pos() or no7.pos() == base14.pos():
                lose(finall_score)
                break
            if z1():
                win()
                break
            if q7() or w8() or e9() or s5() or a4() or d6() or x2() or c3():
                p_t()

    elif r == 8:
        row = 2
        no8.showturtle()
        while bool:
            no8.forward(speed)
            if no8.pos() == base2.pos() or no8.pos() == base21.pos() or no8.pos() == base22.pos() or no8.pos() == base23.pos() or no8.pos() == base24.pos():
                lose(finall_score)
                break
            if x2():
                win()
                break
            if q7() or w8() or e9() or s5() or a4() or d6() or z1() or c3():
                p_t()

    elif r == 9:
        row = 2
        no9.showturtle()
        while bool:
            no9.forward(speed)
            if no9.pos() == base3.pos() or no9.pos() == base31.pos() or no9.pos() == base32.pos() or no9.pos() == base33.pos() or no9.pos() == base34.pos():
                lose(finall_score)
                break
            if c3():
                win()
                break
            if q7() or w8() or e9() or s5() or a4() or d6() or x2() or z1():
                p_t()
if moode == 1:
    replay(True)
elif moode == 2:
    bomb_replay(True)

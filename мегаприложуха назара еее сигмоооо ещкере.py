from time import *
print('выберите 1 из категорий ниже')
print('игры(1)')
print('приложения(2)')
first_vibor=int(input('напишите номер категории - '))
print()
if first_vibor== 1:
	print('хорошо, теперь выбирите саму игру')
	print()
	print('рисовалка(1)')
	print('угадай число(2)')
	print('тренажер клавиатуры(3)')
	sec_vibor=int(input())
	if sec_vibor==1:
		import tkinter
		wind = tkinter.Tk()
		canvas = tkinter.Canvas(wind, width=750, height=500, bg='white')
		canvas.pack()
		lastX, lastY = 0,0
		colour = 'black'

		lbl = tkinter.Label(wind, text = "by w0rldk1ll")
		lbl.pack()
		lbl = tkinter.Label(wind, text = "version 1.1")
		lbl.pack()

		def store_position(event):
			global lastX, lastY
			lastX = event.x
			lastY = event.y
		def on_click(event):
			store_position(event)
		def on_drag(event):
			canvas.create_line(lastX, lastY, event.x, event.y, fill = colour, width = 7)
			store_position(event)
			
		canvas.bind("<Button-1>", on_click)
		canvas.bind("<B1-Motion>", on_drag)

		red_id = canvas.create_rectangle(10, 10, 30, 30, fill = "red")
		blue_id = canvas.create_rectangle(10, 35, 30, 55, fill = "blue")
		green_id = canvas.create_rectangle(10, 60, 30, 80, fill = "green")
		black_id = canvas.create_rectangle(10, 85, 30, 105, fill = "black")
		white_id = canvas.create_rectangle(10, 110, 30, 130, fill = "white")
		yellow_id = canvas.create_rectangle(10, 135, 30, 155, fill = "yellow")
		cyan_id = canvas.create_rectangle(10, 160, 30, 180, fill = "cyan")
		purple_id = canvas.create_rectangle(10, 185, 30, 205, fill = "purple")
		orange_id = canvas.create_rectangle(10, 210, 30, 230, fill = "orange")
		pink_id = canvas.create_rectangle(10, 235, 30, 255, fill = "pink")
		grey_id = canvas.create_rectangle(10, 260, 30, 280, fill = "grey")
		dsb_id = canvas.create_rectangle(10, 285, 30, 305, fill = "deepskyblue")
		choco_id = canvas.create_rectangle(10, 310, 30, 330, fill = "chocolate")
		dsg_id = canvas.create_rectangle(10, 335, 30, 355, fill = "darkslategray")
		slateblue_id = canvas.create_rectangle(10, 360, 30, 380, fill = "slateblue")
		teal_id = canvas.create_rectangle(10, 385, 30, 405, fill = "teal")
		forest_id = canvas.create_rectangle(10, 410, 30, 430, fill = "forestgreen")
		lc_id = canvas.create_rectangle(10, 435, 30, 455, fill = "lemonchiffon")
		fb_id = canvas.create_rectangle(10, 460, 30, 480, fill = "firebrick")


		def set_colour_red(event):
			global colour
			colour="red"

		def set_colour_blue(event):
			global colour
			colour="blue"

		def set_colour_green(event):
			global colour
			colour="green"

		def set_colour_black(event):
			global colour
			colour="black"

		def set_colour_white(event):
			global colour
			colour="white"

		def set_colour_yellow(event):
			global colour
			colour="yellow"

		def set_colour_cyan(event):
			global colour
			colour="cyan"

		def set_colour_purple(event):
			global colour
			colour="purple"

		def set_colour_orange(event):
			global colour
			colour="orange"

		def set_colour_pink(event):
			global colour
			colour="pink"

		def set_colour_grey(event):
			global colour
			colour="grey"

		def set_colour_dsb(event):
			global colour
			colour="deepskyblue"

		def set_colour_choco(event):
			global colour
			colour="chocolate"

		def set_colour_dsg(event):
			global colour
			colour="darkslategray"

		def set_colour_teal(event):
			global colour
			colour="teal"

		def set_colour_forest(event):
			global colour
			colour="forestgreen"

		def set_colour_sb(event):
			global colour
			colour="slateblue"

		def set_colour_lc(event):
			global colour
			colour="lemonchiffon"

		def set_colour_fb(event):
			global colour
			colour="firebrick"

		canvas.tag_bind(red_id, "<Button-1>", set_colour_red)
		canvas.tag_bind(blue_id, "<Button-1>", set_colour_blue)
		canvas.tag_bind(green_id, "<Button-1>", set_colour_green)
		canvas.tag_bind(black_id, "<Button-1>", set_colour_black)
		canvas.tag_bind(white_id, "<Button-1>", set_colour_white)
		canvas.tag_bind(yellow_id, "<Button-1>", set_colour_yellow)
		canvas.tag_bind(cyan_id, "<Button-1>", set_colour_cyan)
		canvas.tag_bind(purple_id, "<Button-1>", set_colour_purple)
		canvas.tag_bind(orange_id, "<Button-1>", set_colour_orange)
		canvas.tag_bind(pink_id, "<Button-1>", set_colour_pink)
		canvas.tag_bind(grey_id, "<Button-1>", set_colour_grey)
		canvas.tag_bind(dsb_id, "<Button-1>", set_colour_dsb)
		canvas.tag_bind(choco_id, "<Button-1>", set_colour_choco)
		canvas.tag_bind(dsg_id, "<Button-1>", set_colour_dsg)
		canvas.tag_bind(teal_id, "<Button-1>", set_colour_teal)
		canvas.tag_bind(forest_id, "<Button-1>", set_colour_forest)
		canvas.tag_bind(slateblue_id, "<Button-1>", set_colour_sb)
		canvas.tag_bind(lc_id, "<Button-1>", set_colour_lc)
		canvas.tag_bind(fb_id, "<Button-1>", set_colour_fb)

		wind.mainloop()
	elif sec_vibor==2:
		import random
		n = random.randint(1,10)
		print('Welcome to the game "guess the number!')
		input('if you are ready press enter')
		f = int(input('enter a number from 1 to 10: '))
		while n != f:
			if n < f:
				print('number is less')
			else:
				print('number is greater')
			f = int(input('please try again: '))
		print('you win')
		input('press enter to exit')
	elif sec_vibor==3:
		import sys
		import random
		from random import *
		input('press enter')
		print('input et to exit')
		bl = 0
		list = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
		while True:
			ok = choice(list)
			print(f'score - {bl}')
			print()
			print(ok)
			ol = input()
			if ol == ok:
				print('+1')
				bl += 1
			if ol != ok and ol != "et":
				print('-1')
				bl -= 1
			if ol == "et":
				sys.exit()

if first_vibor==2:
	print('отлично, теперь выберите какое именно приложение вы хотите открыть')
	print('браузер(1)')
	print('калькулятор(2)')
	
	eshe_vibor=int(input())
	if eshe_vibor==1:
		from tkinter import *
		from webbrowser import *

		def yt():
			yts = ent.get()
			open(f'https://www.youtube.com/results?search_query={yts}')

		def gl():
			gls = enta.get()
			open(f'https://www.google.ru/search?q={gls}')

		def wp():
			wps = entb.get()
			open(f'https://ru.wikipedia.org/wiki/{wps}')

		w = Tk()
		w.geometry('500x500')
		w.config(bg='darkgreen')
		lbl = Label(w,text="enter a request (youtube)",bg='darkgreen')
		ent = Entry(w, bg='green')
		btn = Button(w,text="start",bg='green', command=yt)
		lbl.pack()
		ent.pack()
		btn.pack()
		lbla = Label(w,text="enter a request (google)",bg='darkgreen')
		enta = Entry(w, bg='green')
		btna = Button(w,text="start",bg='green', command=gl)
		lbla.pack()
		enta.pack()
		btna.pack()
		lblb = Label(w,text="enter a request (wikipedia)",bg='darkgreen')
		entb = Entry(w, bg='green')
		btnb = Button(w,text="start",bg='green', command=wp)
		lblb.pack()
		entb.pack()
		btnb.pack()
		mainloop()
	
	if eshe_vibor==2:
		print(eval(input('>>>')))
		

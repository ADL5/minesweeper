from sys import exit
from tkinter import *
from tkinter.messagebox import showerror
from tkinter import ttk
from random import randint
from PIL import Image, ImageTk
from time import sleep
import os
import threading
from json import load, dump

data = {"record_8*8": 10000, 'record_16*16': 10000, "record_16*30": 10000,"recursion_akkord": False}

if not (os.path.exists('data_minesweeper.json')):
	with open('data_minesweeper.json', 'w') as file:
		dump(data, file)
else:
	with open('data_minesweeper.json', 'r') as file:
		data = load(file)

if os.path.exists('pictures'):
	os.chdir('pictures')
else:
	showerror('FileError', 'Required files were not found.')
	exit()

n = 8 #sizes field 8 8   16 16   16 30
m = 8

k = int()
flag_x = int()
wid = int()
hei = int()
wid_plus = int()
rel_hei_coils = int()
flag_relx = int()
flag_rely = int()
btn_pady = int()
timer_relx = int()
size = int()
width = int()
width_pic = int()
rel_wid = int()
hei_plus = int()
rel_y = int()
def th_16():
	global k,flag_x,wid,hei,wid_plus,rel_hei_coils,flag_relx,flag_rely,btn_pady,timer_relx,size,width,width_pic,rel_wid,hei_plus,rel_y
	k = 99
	flag_x = 30
	wid = 1000
	hei = 650
	wid_plus = 300
	rel_hei_coils = 0.8
	flag_relx = 0.15
	flag_rely = 0.18
	btn_pady = 30
	timer_relx = 0.85
	size = 35
	width = 63
	width_pic = 63
	rel_wid = 1
	hei_plus = 50
	rel_y = 125 / hei
def six_16():
	global k, flag_x, wid, hei, wid_plus, rel_hei_coils, flag_relx, flag_rely, btn_pady, timer_relx, size, width, width_pic,rel_wid,hei_plus,rel_y
	k = 40
	flag_x = 36
	wid = 600
	hei = 675
	wid_plus = 800
	rel_hei_coils = 1
	flag_relx = 0.15
	flag_rely = 0.18
	btn_pady = 30
	timer_relx = 0.85
	size = 35
	width = 63
	width_pic = 63
	rel_wid = 1
	hei_plus = 50
	rel_y = 125 / hei
def eight_8():
	global k, flag_x, wid, hei, wid_plus, rel_hei_coils, flag_relx, flag_rely, btn_pady, timer_relx, size, width, width_pic,rel_wid,hei_plus,rel_y
	k = 10
	flag_x = 63
	wid = 500
	hei = 625
	wid_plus = 800
	rel_hei_coils = wid / hei
	flag_relx = 0.149
	flag_rely = 0.28
	btn_pady = 30
	timer_relx = 0.851
	size = 35
	width = 63
	width_pic = 63
	size_records = 20

sizes_of_fields_func = {"8x8": eight_8,"16x16": six_16,"16x30":th_16}
if m == 30:
	th_16()
elif n == m == 16:
	six_16()
else:
	eight_8()
	
rel_wid = 1
hei_plus = 50
rel_y = 125 / hei
end_flag = False
timer_flag = True
win_flag = False

root = Tk()
root.title('minesweeper')
root.geometry(f'{wid}x{hei}+{wid_plus}+{hei_plus}')
root['bg'] = 'black'
root.resizable(False,False)
sizes = ['8x8','16x16','16x30']

sizes = ['8x8','16x16','16x30']
default_size = StringVar(value=sizes[0])
enabled = IntVar(value=data["recursion_akkord"])

def bombs():
	global field_game
	for i in range(k):
		x = randint(0, n - 1)
		y = randint(0, m - 1)
		while field_game[x][y] == -1:
			x = randint(0, n - 1)
			y = randint(0, m - 1)
		field_game[x][y] = -1
	return

def nums_for_bombs():
	global field_game
	for i in range(n):
		for j in range(m):
			if field_game[i][j] == -1:
				for i2 in range(i - 1, i + 2):
					for j2 in range(j - 1, j + 2):
						if 0 <= i2 < n and 0 <= j2 < m and field_game[i2][j2] != -1:
							field_game[i2][j2] += 1
	return

def new_game(count=True):
	global field_game, field_player, count_steps, flag_counter, end_flag,win_flag,timer_flag
	timer_flag = False
	end_flag = False
	win_flag = False
	btn_smile['image'] = pic_good_smile
	flag_counter = k
	label_flags['text'] = flag_counter
	field_game = [[0] * m for _ in range(n)]
	field_player = [[-2] * m for i in range(n)]
	if count:
		count_steps = 0
	else:
		count_steps = 1
	bombs()
	nums_for_bombs()
	label_timer['text'] = 0
	for i in range(n):
		for j in range(m):
			field_btns[i][j]['image'] = pic_default
		
def thread_timer():
	global timer_flag
	count_timer = 0
	timer_flag = True
	while timer_flag:
		if abs(count_timer-int(count_timer)) <= 0.1:
			label_timer['text'] = int(count_timer)
		sleep(0.1)
		count_timer += + 0.1
	if win_flag:
		count_timer = int(count_timer)
		if count_timer < data["record_8*8"] and m == 8:
			data["record_8*8"] = count_timer
		elif count_timer < data["record_16*16"] and m == 16:
			data["record_16*16"] = count_timer
		elif count_timer < data["record_16*30"] and m == 30:
			data["record_16*30"] = count_timer
		with open('data_minesweeper.json','w') as file:
			dump(data,file)
			
def open_smile_frame(event):

	def save_flag_recursion():
		global data
		data["recursion_akkord"] = enabled.get()
		with open('data_minesweeper.json', 'w') as file:
	 		dump(data,file)

	def swap_field_size():
		sizes_of_fields_func[default_size.get()]()
		root.resizable(True,True)
		root.geometry(f'{wid}x{hei}+{wid_plus}+{hei_plus}')
		root.resizable(False,False)
		frame_main.place_configure(relwidth=rel_wid, relheight=rel_hei_coils, rely=rel_y)

		pic_default = picdefault.resize((flag_x, flag_y), Image.LANCZOS)
		pic_default = ImageTk.PhotoImage(pic_default)
		



	def forget_smile_face():
		new_game()
		frame_smile.place_forget()

	with open('data_minesweeper.json', 'r') as file:
	 	data = load(file)
	record8 = data["record_8*8"]
	record16 = data["record_16*16"]
	record30 = data["record_16*30"]
	if data["record_8*8"] == 10000:
		record8 = None
	if data["record_16*16"] == 10000:
		record16 = None
	if data["record_16*30"] == 10000:
		record30 = None

	frame_smile = Frame(root, bg='gray60')
	btn_smile_face = Button(frame_smile, image=pic_good_smile, border=0, activebackground='gray60', background='gray60',width=width, height=width, command=forget_smile_face)
	btn_smile_face.pack(pady=btn_pady)
	combobox_sizes_game = ttk.Combobox(frame_smile, values=sizes, textvariable=default_size, background='gray10',state="readonly")
	combobox_sizes_game.pack()
	btn_play = Button(frame_smile,text="PLAY",font=('unispace',10),width=20,height=1,background='gray80',activebackground='gray70',border=1,command=swap_field_size)
	btn_play.pack(pady=5)
	label_record_88 = Label(frame_smile,text=f'record 8x8: {record8} sec',background='gray60',font=("unispace",15),width=20,height=2)
	label_record_88.pack()
	label_record_1616 = Label(frame_smile, text=f'record 16x16: {record16} sec', background='gray60',font=("unispace", 15), width=30, height=2)
	label_record_1616.pack()
	label_record_1630 = Label(frame_smile, text=f'record 16x30: {record30} sec', background='gray60',font=("unispace", 15), width=30, height=2)
	label_record_1630.pack()
	checkbtn_recursion = Checkbutton(frame_smile,text='recursion akkord',font=("unispace", 15),width=30, command=save_flag_recursion,height=2,bg='gray60',activebackground='gray60',variable=enabled)
	checkbtn_recursion.pack()
	frame_smile.place(relwidth=1, relheight=1)

flag_counter = k
flag_y = flag_x
count_steps = 0

pic_good_smile = Image.open('good_smile.png')
pic_good_smile = pic_good_smile.resize((width_pic, width_pic), Image.LANCZOS)
pic_good_smile = ImageTk.PhotoImage(pic_good_smile)

pic_cry_smile = Image.open('cry_smile.png')
pic_cry_smile = pic_cry_smile.resize((width_pic, width_pic), Image.LANCZOS)
pic_cry_smile = ImageTk.PhotoImage(pic_cry_smile)

win_smile = Image.open('win_smile.png')
win_smile = win_smile.resize((flag_x, flag_y), Image.LANCZOS)
win_smile = ImageTk.PhotoImage(win_smile)

frame_side = Frame(root, bg='gray60')
label_flags = Label(frame_side, text=flag_counter, font=('unispace', size), background='gray60')
label_flags.place(relx=flag_relx, rely=flag_rely)

btn_smile = Button(frame_side, image=pic_good_smile, border=0, command=new_game, activebackground='gray60',background='gray60', width=width, height=width)
btn_smile.bind("<Button-3>", open_smile_frame)
btn_smile.pack(pady=btn_pady)

label_timer = Label(frame_side, text=0, background='gray60', font=('unispace', size))
label_timer.place(relx=timer_relx, rely=flag_rely, anchor='ne')
frame_side.place(relwidth=1, relheight=0.2)

pic_flag = Image.open('cell_flag.png')
pic_flag = pic_flag.resize((flag_x, flag_y), Image.LANCZOS)
pic_flag = ImageTk.PhotoImage(pic_flag)

picdefault = Image.open('cell.png')
pic_default = picdefault.resize((flag_x, flag_y), Image.LANCZOS)
pic_default = ImageTk.PhotoImage(pic_default)

pic_bomb = Image.open('cell_bomb.png')
pic_bomb = pic_bomb.resize((flag_x, flag_y), Image.LANCZOS)
pic_bomb = ImageTk.PhotoImage(pic_bomb)

pic_boom_bomb = Image.open('boom_bomb.png')
pic_boom_bomb = pic_boom_bomb.resize((flag_x, flag_y), Image.LANCZOS)
pic_boom_bomb = ImageTk.PhotoImage(pic_boom_bomb)

pic_boom_flag = Image.open('boom_flag.png')
pic_boom_flag = pic_boom_flag.resize((flag_x, flag_y), Image.LANCZOS)
pic_boom_flag = ImageTk.PhotoImage(pic_boom_flag)

pic_0 = Image.open('cell_0.png')
pic_0 = pic_0.resize((flag_x, flag_y), Image.LANCZOS)
pic_0 = ImageTk.PhotoImage(pic_0)

pic_1 = Image.open('cell_1.png')
pic_1 = pic_1.resize((flag_x, flag_y), Image.LANCZOS)
pic_1 = ImageTk.PhotoImage(pic_1)

pic_2 = Image.open('cell_2.png')
pic_2 = pic_2.resize((flag_x, flag_y), Image.LANCZOS)
pic_2 = ImageTk.PhotoImage(pic_2)

pic_3 = Image.open('cell_3.png')
pic_3 = pic_3.resize((flag_x, flag_y), Image.LANCZOS)
pic_3 = ImageTk.PhotoImage(pic_3)

pic_4 = Image.open('cell_4.png')
pic_4 = pic_4.resize((flag_x, flag_y), Image.LANCZOS)
pic_4 = ImageTk.PhotoImage(pic_4)

pic_5 = Image.open('cell_5.png')
pic_5 = pic_5.resize((flag_x, flag_y), Image.LANCZOS)
pic_5 = ImageTk.PhotoImage(pic_5)

pic_6 = Image.open('cell_6.png')
pic_6 = pic_6.resize((flag_x, flag_y), Image.LANCZOS)
pic_6 = ImageTk.PhotoImage(pic_6)

pic_7 = Image.open('cell_7.png')
pic_7 = pic_7.resize((flag_x, flag_y), Image.LANCZOS)
pic_7 = ImageTk.PhotoImage(pic_7)

pic_8 = Image.open('cell_8.png')
pic_8 = pic_8.resize((flag_x, flag_y), Image.LANCZOS)
pic_8 = ImageTk.PhotoImage(pic_8)

list_picks = [pic_0, pic_1, pic_2, pic_3, pic_4, pic_5, pic_6, pic_7, pic_8]

field_game = [[0] * m for _ in range(n)]  # field of game -1 = bomb 0-8 = cell
field_player = [[-2] * m for i in range(n)]  # -2 = closed; -1 = flag; 0-8 = cell;
field_btns = [[0] * m for i in range(n)]  # list of buttons
os.chdir('..')

def win():
	count_closed = 0
	for i in range(n):
		for j in range(m):
			if field_player[i][j] <= -1:
				count_closed += 1
	if count_closed == k:
		show_field(-1, -1, win=True)


def akkord(x, y):
	recursion = enabled.get()
	count_flag = 0
	for x2 in range(x - 1, x + 2):
		for y2 in range(y - 1, y + 2):
			if 0 <= x2 < n and 0 <= y2 < m:
				if field_player[x2][y2] == -1:
					count_flag += 1
	if count_flag != field_player[x][y]:
		return
	for x2 in range(x - 1, x + 2):
		for y2 in range(y - 1, y + 2):
			if 0 <= x2 < n and 0 <= y2 < m and not (field_player[x2][y2] > -1):
				if field_game[x2][y2] == -1 and field_player[x2][y2] != -1:
					show_field(x2, y2)
					return
				dfs(x2, y2)
				if recursion:
					akkord(x2, y2)

def dfs(x, y):
	if x < 0 or x >= n or y < 0 or y >= m or field_player[x][y] > -2:
		return
	if field_player[x][y] != -1:
		field_player[x][y] = field_game[x][y]
	field_btns[x][y]['image'] = list_picks[field_game[x][y]]
	if field_game[x][y] > 0:
		return
	for x2 in range(x - 1, x + 2):
		for y2 in range(y - 1, y + 2):
			if x2 != x or y2 != y:
				dfs(x2, y2)


def show_field(x, y, win=False):
	global field_btns, btn_smile, end_flag, flag_counter,win_flag,timer_flag
	timer_flag = False
	end_flag = True
	if win:
		btn_smile['image'] = win_smile
		for i in range(n):
			for j in range(n):
				if field_game[i][j] == -1 and field_player[i][j] != -1:
					field_btns[i][j]['image'] = pic_flag
		win_flag = True
		return
	for i in range(n):
		for j in range(m):
			if field_game[i][j] >= 0:
				field_btns[i][j]['image'] = list_picks[field_game[i][j]]
			if field_game[i][j] != -1 and field_player[i][j] == -1:
				field_btns[i][j]['image'] = pic_boom_flag
			elif field_game[i][j] == -1 and field_player[i][j] == -1:
				field_btns[i][j]['image'] = pic_flag
			elif field_game[i][j] == -1 and field_player[i][j] != -1:
				field_btns[i][j]['image'] = pic_bomb
	btn_smile['image'] = pic_cry_smile
	field_btns[x][y]['image'] = pic_boom_bomb


def action(event):
	global count_steps, flag_counter, field_game,end_flag
	num_btn = event.widget.cget('text').split('_')
	index_i = int(num_btn[0])
	index_j = int(num_btn[1])
	if end_flag:
		return
	if event.num == 3:
		if field_player[index_i][index_j] >= 0:
			return
		if field_player[index_i][index_j] != -1:
			field_btns[index_i][index_j]['image'] = pic_flag
			field_player[index_i][index_j] = -1
			flag_counter -= 1
			label_flags['text'] = flag_counter
			return
		elif field_player[index_i][index_j] == -1:
			field_btns[index_i][index_j]['image'] = pic_default
			field_player[index_i][index_j] = -2
			flag_counter += 1
			label_flags['text'] = flag_counter
			return
	elif event.num == 1:
		count_steps += 1
		if count_steps == 1:
			while field_game[index_i][index_j] != 0:
				field_game = [[0] * m for _ in range(n)]
				bombs()
				nums_for_bombs()
			thread = threading.Thread(target=thread_timer)
			thread.start()
			dfs(index_i, index_j)
		elif field_game[index_i][index_j] == -1:
			show_field(index_i, index_j)
		elif field_game[index_i][index_j] == field_player[index_i][index_j] > 0:
			akkord(index_i, index_j)
		else:
			dfs(index_i, index_j)
		win()

def buttonpress(event):
	global field_btns, pic_default
	num_btn = event.widget.cget('text').split('_')
	index_i = int(num_btn[0])
	index_j = int(num_btn[1])
	if field_player[index_i][index_j] < 0:
		return
	for i2 in range(index_i-1,index_i+2):
		for j2 in range(index_j-1,index_j+2):
			if 0<=i2<=n and 0<=j2<=m and field_player[i2][j2] == -2:
				field_btns[i2][j2]['image'] = pic_0

def buttonrelease(event):
	global field_btns
	num_btn = event.widget.cget('text').split('_')
	index_i = int(num_btn[0])
	index_j = int(num_btn[1])
	if field_player[index_i][index_j] < 0:
		return
	for i2 in range(index_i-1,index_i+2):
		for j2 in range(index_j-1,index_j+2):
			if 0<=i2<n and 0<=j2<m and field_player[i2][j2] == -2:
				field_btns[i2][j2]['image'] = pic_default
				
frame_main = Frame(root, bg='black')
for i in range(n):
	frame_main.columnconfigure(index=i, weight=1)
	for j in range(m):
		frame_main.rowconfigure(index=j, weight=1)
		field_btns[i][j] = Label(frame_main, text=f'{i}_{j}', image=pic_default, background='gray60')
		field_btns[i][j].bind('<Button-1>', action)
		field_btns[i][j].bind('<Button-3>', action)
		field_btns[i][j].bind('<ButtonPress-2>', buttonpress)
		field_btns[i][j].bind('<ButtonRelease-2>', buttonrelease)
		field_btns[i][j].grid(row=i, column=j, sticky='nsew')
bombs()
nums_for_bombs()
frame_main.place(relwidth=rel_wid, relheight=rel_hei_coils, rely=rel_y)

root.mainloop()

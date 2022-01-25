"""
Этот модуль содержит графический интерфейс
- Имя
- Номер телефона
- Почта
- Адрес
- День рождения
"""

import tkinter as tk
import contact_book_module as cb


list_info = [0 for i in range(5)]


def lift_frame(frame_name):
	frame_name.lift()


def disp_info_name(evt):
	index = lbx.curselection()
	seltext = lbx.get(index)
	call_edit(seltext)
	info = cb.search(seltext)
	output1.delete(1.0, tk.END)
	output1.insert(tk.END, info)


def call_add(list_info):
	cb.add_contact(list_info)


def call_edit(seltext):
	global list_info
	info = cb.search_name(seltext)
	list_info = info.get_info()
	name = tk.Entry(f3, width=20, bg="white", highlightbackground='white')
	name.insert(0, list_info[0])
	name.place(relx=0.30, rely=0.25, relwidth=0.4, relheight=0.05)
	phone = tk.Entry(f3, width=20, bg="white", highlightbackground='white')
	phone.insert(0, list_info[1])
	phone.place(relx=0.30, rely=0.30, relwidth=0.4, relheight=0.05)
	email = tk.Entry(f3, width=20, bg="white", highlightbackground='white')
	email.insert(0, list_info[2])
	email.place(relx=0.30, rely=0.35, relwidth=0.4, relheight=0.05)
	addy = tk.Entry(f3, width=20, bg="white", highlightbackground='white')
	addy.insert(0, list_info[3])
	addy.place(relx=0.30, rely=0.40, relwidth=0.4, relheight=0.05)
	bd = tk.Entry(f3, width=20, bg="white", highlightbackground='white')
	bd.insert(0, list_info[4])
	bd.place(relx=0.30, rely=0.45, relwidth=0.4, relheight=0.05)
	b6 = tk.Button(f3, text="Редактировать", highlightbackground='grey',
	command=lambda: cb.edit(list_info[0], [name.get(), phone.get(), email.get(),
	addy.get(), bd.get()]))
	b6.place(relx=0.42, rely=0.60, relwidth=0.15, relheight=0.05)


def name_search(sv):
	try:
		lbx.delete(0, tk.END)
	except:
		pass
	name = sv.get()
	names = cb.get_names(name)
	for n, name in enumerate(names):
		lbx.insert(n, name)


def initial_listbox():
	try:
		lbx.delete(0, tk.END)
	except:
		pass
	name = ' '
	names = cb.get_names(name)
	for n, name in enumerate(names):
		lbx.insert(n, name)


def call_add(list_info):
	cb.add_contact(list_info)
	initial_listbox()


root = tk.Tk()
root.title("Контакты")
root.geometry("800x600")

canvas = tk.Canvas(root, height=600, width=600)
canvas.place(relwidth=1, relheight=1)
# фон задний левый блок контакты #339fa1 бирюзовый
f1 = tk.Frame(canvas, bg="#339fa1", bd=5)
f1.place(relwidth=0.25, relheight=1)

sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: name_search(sv))

textentry1 = tk.Entry(f1, width=50, bg="white", textvariable=sv,
highlightbackground="white")

textentry1.insert(0, "Поиск")
textentry1.place(relx=0.039, rely=0.04, relwidth=0.925, relheight=0.035)
textentry1.pack()

# передний фон имена #1d6769 Темно-бирюзовый
lbx = tk.Listbox(f1, background="#1d6769", fg="white",
selectbackground='#339fa1', selectmode=tk.SINGLE)

lbx.place(relx=0.1, rely=0.2, relwidth=0.9, relheight=0.45)
lbx.config(borderwidth=0)
initial_listbox()
lbx.bind('<<ListboxSelect>>', disp_info_name)

sbr = tk.Scrollbar(lbx)
sbr.pack(side="right", fill="y")

sbr.config(command=lbx.yview)
lbx.config(yscrollcommand=sbr.set)

# бг второй фрейм
f2 = tk.Frame(canvas, bg="#339fa1", bd=5)
f2.place(relx=0.25, relwidth=0.75, relheight=1)

# фон внутренний фрейм
output1 = tk.Text(f2, background="#1d6769", fg="white")
output1.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.45)

# верхняя кнопка
b1 = tk.Button(f2, text="Новый контакт", font=("Futura PT Bold", "10"),
fg='#1d6769', command=lambda: lift_frame(f4))
b1.place(relx=0.3, rely=0.7, relwidth=0.455, relheight=0.045)

# нижняя кнопка
b2 = tk.Button(f2, text="Редактировать", font=("Futura PT Bold", "10"),
command=lambda: lift_frame(f3))

b2.place(relx=0.3, rely=0.75, relwidth=0.455, relheight=0.045)

b1.config(highlightbackground="grey", bg='#1d6769', fg="white")
b2.config(highlightbackground="grey", bg='#1d6769', fg="white")

f3 = tk.Frame(canvas, bg="#1d6769", bd=5)
f3.place(relx=0.25, relwidth=0.75, relheight=1)

b4 = tk.Button(f3, text="Назад", font=("Futura PT Bold", "12"),
command=lambda: lift_frame(f2))

b4.place(relx=0.85, rely=1.928, relwidth=0.0955, relheight=0.045)
b4.config(highlightbackground="grey", bg='#1d6769', fg='black')

f4 = tk.Frame(canvas, bg="#1d6769", bd=5)
f4.place(relx=0.25, relwidth=0.75, relheight=1)

b4 = tk.Button(f4, text="Назад", font=("Futura PT Bold", "12"),
command=lambda: lift_frame(f2))

b4.place(relx=0.85, rely=0.928, relwidth=0.0955, relheight=0.045)

b4.config(highlightbackground="#1d6769", bg='#1d6769', fg='black')

#поле с инфой
name = tk.Entry(f4, width=20, bg="white", highlightbackground='white')
name.insert(0, " Имя Фамилия")
name.place(relx=0.30, rely=0.25, relwidth=0.4, relheight=0.05)
phone = tk.Entry(f4, width=20, bg="white", highlightbackground='white')
phone.insert(0, " Телефон")
phone.place(relx=0.30, rely=0.30, relwidth=0.4, relheight=0.05)
email = tk.Entry(f4, width=20, bg="white", highlightbackground='white')
email.insert(0, " Email")
email.place(relx=0.30, rely=0.35, relwidth=0.4, relheight=0.05)
addy = tk.Entry(f4, width=20, bg="white", highlightbackground='white')
addy.insert(0, " Адрес")
addy.place(relx=0.30, rely=0.40, relwidth=0.4, relheight=0.05)
bd = tk.Entry(f4, width=20, bg="white", highlightbackground='white')
bd.insert(0, " ДДММГГ")
bd.place(relx=0.30, rely=0.45, relwidth=0.4, relheight=0.05)

b5 = tk.Button(
	f4,
	text="Добавить",
	highlightbackground='white',
	command=lambda: call_add(
		[name.get(), phone.get(), email.get(), addy.get(), bd.get()]
	),
)
b5.place(relx=0.42, rely=0.60, relwidth=0.15, relheight=0.05)

f2.lift()


if __name__ == "__main__":
	root.mainloop()

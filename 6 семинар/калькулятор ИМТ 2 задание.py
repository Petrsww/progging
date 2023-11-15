from tkinter import *
from tkinter import ttk

# Задаем функцию пересчета. обратите внимание, что к feet и meters мы обращаемся как к глобальным переменным, в общем случае так делать нехорошо
# *args означает, что функция может принимать любое количество переменных. здесь они не используется, поэтому для общности написали так

def calculate(*args):
    try:
        value1 = float(w.get())
        value2 = float(h.get())/100
        a=float(value1/value2**2)
        meters.set(a)
        if a<16:
            d.set('Выраженный дефицит массы тела')                   
        elif a<=18/5 and a>=16:
            d.set('Недостаточная масса тела')      
        elif a>18.5 and a<25:
            d.set('Норма')
        elif a>=25 and a<=30:
            d.set('Избыточная масса тела')
        elif a>30 and a<35:
            d.set('Ожирение 1 степени')
        elif a>=35 and a<=40:
            d.set('Ожирение 2 степени')
        elif a>=40:
            d.set('Ожирение 3 степени')
    except ValueError:
        pass

# Создадим основное окно приложения
root = Tk()
root.title("ИМТ")

'''
Зададим виджет Frame с названием mainframe, который будет содержать элементы нашего интерфейса.
После того, как мы создали его, grid() помещает его в окно приложения. 
columnconfigure/rowconfigure говорит что mainframe должен также расширяться
и занимать все свободное место при изменении размеров окна
'''
mainframe = ttk.Frame(root, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

'''
Первый виджет Entry должен принимать количество футов.

Когда мы создаем виджет, нам нужно указать его родителя.
Это виджет, внутри которого будет размещен новый виджет.
Наша запись и другие виджеты, которые мы вскоре создадим, считаются дочерними элементами mainframe.
Родительский элемент передается в качестве первого параметра при создании экземпляра объекта виджета.

Также мы задали, что наше окно ввода должно иметь ширину под 7 символов.

Также мы создали глобальную переменную feet как textvariable для Entry. 
Когда ввод поменяется, Tkinter автоматически обновит feet. 
Для задания feet используется конструктор по умолчанию для таких переменных -- StringVar()

When widgets are created, they don't automatically appear on the screen; 
Tkinter должен знать куда вы хотите поместить виджеты относительно друг друга. 
За это отвечает функция grid. Она помещает содержимое в column (1, 2, or 3) и row (also 1, 2, or 3) окна.
sticky отвечает за то, по какой стороне будет выравнивание. W (west) означает запад, то есть левую сторону ячейки
W,E (west-east) означает и левую и правую сторону одновременно, то есть выравнивание посередине.
В Python определены константы для направлений компаса, поэтому вы можете писать просто W или (W, E).
'''
w = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=w)
feet_entry.grid(column=1, row=2, sticky=(W))

h = StringVar()
fee_entry = ttk.Entry(mainframe, width=7, textvariable=h)
fee_entry.grid(column=2, row=2, sticky=(E))


'''
Дальше создаем окно вывода.
'''
d = StringVar()
ttk.Label(mainframe, textvariable=d).grid(column=3, row=3, sticky=(E))
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=3, sticky=(W,E))

'''
По нажатии на кнопку будем выполнять функцию calculate. Поскольку в ней уже прописаны операции напрямую с feet и meters,
то нам не нужно задавать какие-либо аргументы, функция автоматически положит нужное значение в meters и значение в 
определенном выше Label обновится.
'''
ttk.Button(mainframe, text="посчитать имт", command=calculate).grid(column=3, row=2, sticky=W)
#косметические подписи, обратите внимание на расположение
ttk.Label(mainframe, text="Вес").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Рост").grid(column=2, row=1, sticky=E)
ttk.Label(mainframe, text="ИМТ").grid(column=1, row=3, sticky=W)

# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# сразу помещает курсор ввода в поле feet_entry
feet_entry.focus()
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось calculate
root.bind("<Return>", calculate)

# циклим наше окно
root.mainloop()

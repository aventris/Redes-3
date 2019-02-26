import os, errno
import shutil
import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()



def obtenerDatos():

    datos = entry1.get()
    datos = datos+" "+comboVersion.get()
    datos = datos+" "+entry3.get()
    datos = datos+" "+entry4.get()+"\n"

    try:
        os.makedirs(entry1.get())
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    print(datos)
    f = open("agentes.txt","a")
    f.write(datos)
    ventana.destroy()

def borrar():
    dato = "192.168.0.1"
    with open("agentes.txt", "r") as input:
        with open("aux.txt", "w") as output:
            for line in input:
                if dato not in line:
                    output.write(line)
    os.remove("agentes.txt")
    os.rename("aux.txt","agentes.txt")
    shutil.rmtree(dato, ignore_errors=True)

ventana.title("Agregar agente")

ventana.geometry("500x400")
rows = 0
while rows < 10:
    ventana.rowconfigure(rows, weight=1)
    rows+=1

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(4, weight=1)
label1 = tk.Label(text = "Host name")
label1.grid(column=1,row=0)

label2 = tk.Label(text = "Version")
label2.grid(column=1,row=1)

label3 = tk.Label(text = "Puerto")
label3.grid(column=1,row=2)

label4 = tk.Label(text = "Comunidad")
label4.grid(column=1,row=3)

entry1 = tk.Entry()
entry1.grid(column=2,row=0)

comboVersion = ttk.Combobox(ventana,values=["SNMPv1","SNMPv2"])
comboVersion.grid(column=2,row=1)
comboVersion.current(0)

entry3 = tk.Entry()
entry3.insert(0,'161')
entry3.config(state='readonly')
entry3.grid(column=2,row=2)

entry4 = tk.Entry()
entry4.grid(column=2,row=3)

button1 = tk.Button(ventana,text = "Agregar",command=obtenerDatos)
button1.grid(column=1, row=6)

button2 = tk.Button(ventana,text = "Cancelar",command=ventana.destroy)
button2.grid(column=3, row=6)

button3 = tk.Button(ventana,text = "Cancelar",command=borrar)
button3.grid(column=3, row=8)
ventana.mainloop()

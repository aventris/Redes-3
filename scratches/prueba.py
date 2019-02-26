import os, errno, subprocess
import shutil
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *


def main():
    root = tk.Tk()
    app = Root(root)
class Root:

    def __init__(self, master):
        self.master = master
        self.master.title("Prueba")
        self.master.geometry("700x400")
        self.frame = Frame(self.master)
        #self.frame.grid()
        self.frame.grid()

        self.label1 = Label(self.frame,text="Agentes:")
        self.label1.grid(column=0,row=0)

        self.list1 = Treeview(self.frame, selectmode='browse')
        self.list1['columns'] = ('Host', 'Version', 'Puerto', 'Comunidad', 'Estatus')
        self.list1.heading("#0", text='ID', anchor='w')
        self.list1.column("#0", width='50', anchor='w')
        self.list1.heading('Host', text='Host')
        self.list1.column('Host', width='120', anchor='center')
        self.list1.heading('Comunidad', text='Comunidad')
        self.list1.column('Comunidad', width='150', anchor='center')
        self.list1.heading('Puerto', text='Puerto')
        self.list1.column('Puerto', width='80', anchor='center')
        self.list1.heading('Estatus', text='Estatus')
        self.list1.column('Estatus', width='80', anchor='center')
        self.list1.heading('Version', text='Version')
        self.list1.column('Version', width='80', anchor='center')
        self.treeview = self.list1
        self.treeview.grid(column=1,columnspan=3)

        self.actualizar()

        self.button5 = Button(self.frame, text="Actualizar", command=self.actualizar)
        self.button5.grid(column=3, row=0)

        self.button1 = Button(self.frame, text="Agregar", command = self.new_window)
        self.button1.grid(column=0,row=8)

        self.button2 = Button(self.frame, text="Eliminar", command=self.new_window2)
        self.button2.grid(column=1,row=8)

        self.button3 = Button(self.frame, text="Grafcas", command=self.new_window2)
        self.button3.grid(column=2, row=8)

        self.button4 = Button(self.frame, text="Detalles", command=self.new_window4)
        self.button4.grid(column=3, row=8)

        self.master.mainloop()
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = agregarAgente(self.newWindow)
        self.master.wait_window(self.app.master)
        self.actualizar()

    def new_window2(self):
        self.newWindow = Toplevel(self.master)
        self.app = eliminarAgente(self.newWindow)
        self.master.wait_window(self.app.master)
        self.actualizar()

    def new_window3(self):
        self.newWindow = Toplevel(self.master)
        self.app = eliminarAgente(self.newWindow)

    def new_window4(self):
        self.newWindow = Toplevel(self.master)
        self.app = infoAgente(self.newWindow)

    def actualizar(self):
        self.treeview.delete(*self.treeview.get_children())
        i = 1
        with open("agentes.txt", "r") as input:
            for line in input:
                aux = line.split()
                estatus = "0"
                self.treeview.insert('', 'end', text=i, values=(aux[0], aux[1], aux[2], aux[3], estatus))
                i += 1

class agregarAgente:
    def __init__(self, master):

        def obtenerDatos():
            datos = self.entry1.get()
            datos = datos + " " + self.comboVersion.get()
            datos = datos + " " + self.entry3.get()
            datos = datos + " " + self.entry4.get() + "\n"

            try:
                os.makedirs(self.entry1.get())
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            print(datos)
            f = open("agentes.txt", "a")
            f.write(datos)
            self.master.destroy()

        self.master = master
        self.master.title("Agregar agente")
        self.master.geometry("500x400")
        self.frame = Frame(self.master)
        self.frame.grid()

        rows = 0
        while rows < 10:
            self.master.rowconfigure(rows, weight=1)
            rows += 1

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(4, weight=1)

        self.label1 = tk.Label(self.master, text="Host name")
        self.label1.grid(column=1, row=0)

        self.label2 = tk.Label(self.master, text="Version")
        self.label2.grid(column=1, row=1)

        self.label3 = tk.Label(self.master, text="Puerto")
        self.label3.grid(column=1, row=2)

        self.label4 = tk.Label(self.master, text="Comunidad")
        self.label4.grid(column=1, row=3)

        self.entry1 = tk.Entry(self.master)
        self.entry1.grid(column=2, row=0)

        self.comboVersion = ttk.Combobox(self.master, values=["SNMPv1", "SNMPv2"])
        self.comboVersion.grid(column=2, row=1)
        self.comboVersion.current(0)

        self.entry3 = tk.Entry(self.master)
        self.entry3.insert(0,'161')
        self.entry3.grid(column=2, row=2)

        self.entry4 = tk.Entry(self.master)
        self.entry4.grid(column=2, row=3)

        self.button1 = tk.Button(self.master, text="Agregar", command=obtenerDatos)
        self.button1.grid(column=1, row=6)

        self.button2 = tk.Button(self.master, text="Cancelar", command=self.master.destroy)
        self.button2.grid(column=3, row=6)

class eliminarAgente:
    def __init__(self, master):
        def borrar():
            aux = self.list1.focus()

            dato = int((self.list1.item(aux))['text'])-1
            folder = (self.list1.item(aux))['values'][0]

            with open("agentes.txt", "r") as input:
                with open("aux.txt", "w") as output:
                    for i,line in enumerate(input):
                        if dato != i:
                            print("funciona")
                            output.write(line)
            os.remove("agentes.txt")
            os.rename("aux.txt", "agentes.txt")
            shutil.rmtree(folder, ignore_errors=True)
            self.master.destroy();


        self.master = master
        self.master.title("Agregar agente")
        self.master.geometry("800x400")
        self.frame = Frame(self.master)
        self.frame.grid(column=0,row=0)


        rows = 0
        while rows < 10:
            self.master.rowconfigure(rows, weight=1)
            rows += 1

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(4, weight=1)

        self.list1 = Treeview(self.master, selectmode ='browse')
        self.list1['columns']=('Host','Comunidad','Puerto','Version')
        self.list1.heading("#0", text='ID',anchor='w')
        self.list1.column("#0",width=50,anchor='w')

        self.list1.heading('Host', text='Host')
        self.list1.column('Host', width='100')
        self.list1.heading('Comunidad', text='Comunidad')
        self.list1.column('Comunidad', width='200')
        self.list1.heading('Puerto', text='Puerto')
        self.list1.column('Puerto', width='100')
        self.list1.heading('Version', text='Version')
        self.list1.column('Version', width='100')
        self.list1.grid(sticky = (N,S,W,E))
        self.treeview = self.list1
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        i=1
        with open("agentes.txt", "r") as input:
            for line in input:
                aux = line.split()
                self.treeview.insert('', 'end', text=i, values=(aux[0],aux[1], aux[2], aux[3]))
                i+=1

        self.button1=Button(self.master,text="ELiminar", command=borrar)
        self.button1.grid()

        self.button2=Button(self.master, text="Cancelar", command=self.master.destroy)
        self.button2.grid()

        #=======================================================================
class infoAgente:
    def __init__(self,master):
        def getstate():
            ip=str(self.input1.get())
            comunidad = str(self.input2.get())
            print(comunidad)
            print(ip)
            Nombre_dispositivo = []
            Informacion_contacto = []
            Ubicacion = []
            Informacion_dispositivo = []
            Numero_interfaces = []

            Nombre_dispositivo = subprocess.getoutput(
                'snmpget -v2c -c ' + comunidad + ' ' + ip + ' ' + '1.3.6.1.2.1.1.5.0')

            print(Nombre_dispositivo.split(":")[1])

            Informacion_contacto = subprocess.getoutput(
                'snmpget -v2c -c ' + comunidad + ' ' + ip + ' ' + '1.3.6.1.2.1.1.4.0')
            print(Informacion_contacto.split())

            Ubicacion = subprocess.getoutput('snmpget -v2c -c ' + comunidad + ' ' + ip + ' ' + '1.3.6.1.2.1.1.6.0')
            print(Ubicacion.split(":")[1])

            Informacion_dispositivo = subprocess.getoutput(
                'snmpget -v2c -c ' + comunidad + ' ' + ip + ' ' + '1.3.6.1.2.1.1.1.0')
            print(Informacion_dispositivo.split(":")[3])

            Numero_interfaces = subprocess.getoutput(
                'snmpget -v2c -c ' + comunidad + ' ' + ip + ' ' + '1.3.6.1.2.1.2.1.0')
            print(Numero_interfaces.split(":")[1])

            Tiepo_activo = subprocess.getoutput(
                'snmpget -v2c -c ' + comunidad + ' ' + ip + ' ' + '1.3.6.1.2.1.2.2.1.9.1')
            print(Tiepo_activo.split("ks:")[1])

        self.master = master
        self.master.title("Agregar agente")
        self.master.geometry("800x400")
        self.frame = Frame(self.master)
        self.frame.grid()

        self.input1 = Entry(self.frame)
        self.input1.grid(column=3,row=0)
        self.input2 = Entry(self.frame)
        self.input2.grid(column=1,row=0)

        self.label1 = Label(self.frame,text="Host: ")
        self.label1.grid(column=1,row=1)

        self.label2 = Label(self.frame,text="Puerto: ")
        self.label2.grid(column=2, row=2)

        self.label3 = Label(self.frame,text="Version: ")
        self.label3.grid(column=1, row=3)

        self.label4 = Label(self.frame,text="Grupo: ")
        self.label4.grid(column=1, row=4)

        self.label5 = Label(self.frame,text="Contacto: ")
        self.label5.grid(column=1, row=5)

        self.label6 = Label(self.frame,text="Tiempo en linea: ")
        self.label6.grid(column=1, row=6)

        self.label7 = Label(self.frame,text="Dispositivo: ")
        self.label7.grid(column=1, row=7)

        self.button1 = Button(self.frame, command=getstate)
        self.button1.grid(column=2,row=0)
if __name__ == "__main__":
    main()
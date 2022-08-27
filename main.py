#https://es.stackoverflow.com/questions/280768/c%C3%B3mo-cambiar-din%C3%A1micamente-el-contenido-de-un-listbox-en-base-a-la-opci%C3%B3n-elegi
#Message box, entry(con nota del alumno) y label indicandole al profesor
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ConsultaAlumnos():
    #Ejemplos de nombres para los alumnos 
    lista = {
        0: {"nombre" : "Luciano González", "turno" : "tarde"},
        1: {"nombre" : "Juan Jose", "turno" : "manana"},
        2: {"nombre" : "Ana Sofía Granado", "turno" : "manana"},
        3: {"nombre" : "Cristóbal Leon", "turno" : "manana"},
        4: {"nombre" : "Antonia Leon", "turno" : "manana"},
        5: {"nombre" : "Maximiliano Crespo", "turno" : "manana"},
        6: {"nombre" : "Magdalena Garrido", "turno" : "manana"},
        7: {"nombre" : "Paz Gómez", "turno" : "tarde"},
        8: {"nombre" : "María Paula Jasso", "turno" : "tarde"},
        9: {"nombre" : "Fernando Domínquez", "turno" : "tarde"},
        10: {"nombre" : "Anthony Soto", "turno" : "tarde"},
        11: {"nombre" : "Natalia Alonso", "turno" : "tarde"},
        12: {"nombre" : "Michelle Ramirez", "turno" : "tarde"},
        13: {"nombre" : "Alex Granado", "turno" : "tarde"},
        14: {"nombre" : "Samantha Delgado", "turno" : "tarde"},
    }
    

    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Panel de pestañas en Tcl/Tk")
        
        
        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self.ventana1)
        self.frameGuargarDatos = tk.Frame(self.notebook)
        self.frameGuargarDatos.config(bg="#8CD0F7")
        self.frameCargarDatos = tk.Frame(self.notebook)
        self.frameCargarDatos.config(bg="#8CD0F7")
        self.MasterGuardarDatos(self.frameGuargarDatos)
        self.MasterCargarDatos (self.frameCargarDatos)
        
        # Añadirlas al panel con su respectivo texto.
        self.notebook.add(self.frameGuargarDatos, text="Web", padding=20)

        self.notebook.add(self.frameCargarDatos, text="Foro", padding=20)
        
        self.notebook.pack(padx=10, pady=10)
        
        self.ventana1.mainloop()
    
    def MasterGuardarDatos(self, masterGuarda):
        
        # self.ventana1=tk.Tk()
        # self.ventana1.config(bg="#8CD0F7")
        # self.ventana1.title("Colegio Atid")
        # self.ventana1.resizable(0,0)
        self.titulo=tk.Label(masterGuarda,text="Información General")
        self.titulo.config(bg="#8CD0F7", font=("Arial", 20))
        self.titulo.grid(row=0, column=3,columnspan=6,pady=10)
        self.notAlumno=tk.Entry(masterGuarda)
        self.notAlumno.grid(row=4, column=9,columnspan=4,padx=10,pady=10)
        self.label2=tk.Label(masterGuarda,text="Nota del alumno:")
        self.label2.grid(row=4, column=8,pady=10)
        self.label2.config(bg="#8CD0F7")
        #<-----------------------------Boton para filtrar entre las opciones de la listbox-------------------------------------------->
        self.boton_filtrar=tk.Button(masterGuarda, text="Filtrar",command=self.filtro, cursor="hand2",activebackground="#8CD0F7")
        self.boton_filtrar.grid(row=1,column=10,columnspan=4)
        #<------------------------------Botones de filtro mañana, tarde y todos--------------------------------------------------------> 
        self.check1_value = tk.BooleanVar()
        self.check1=tk.Checkbutton(masterGuarda,text="Mañana", variable=self.check1_value)
        self.check1.grid(column=6, row=1)
        self.check1.config(bg="#8CD0F7", activebackground="#8CD0F7")
        self.check2_value = tk.BooleanVar()
        self.check2=tk.Checkbutton(masterGuarda,text="Tarde", variable=self.check2_value)
        self.check2.grid(column=7, row=1)
        self.check2.config(bg="#8CD0F7", activebackground="#8CD0F7")
        self.check3_value = tk.BooleanVar()
        self.check3=tk.Checkbutton(masterGuarda,text="Todos", variable=self.check3_value)
        self.check3.grid(column=8, row=1)
        self.check3.config(bg="#8CD0F7", activebackground="#8CD0F7")
        #<---------------------------------------------------------------------------------------------------------------------------------->
        self.scroll1 = tk.Scrollbar(masterGuarda, orient=tk.VERTICAL)
        self.listbox1=tk.Listbox(masterGuarda, selectmode=tk.SINGLE, yscrollcommand=self.scroll1.set,bg="#ADD7EF",exportselection=False)
        self.listbox1.grid(column=0,row=1,padx="10",pady="10")
        self.scroll1.configure(command=self.listbox1.yview)        
        self.scroll1.grid(column=1, row=1, sticky='NS')     
        self.listbox1.grid(column=0,row=1)
        self.label1=ttk.Label(masterGuarda, text="Seleccione la asignatura:")
        self.label1.grid(column=0, row=4)
        self.label1.config(background="#8CD0F7")
        self.opcionMateria=tk.StringVar()
        asignatura=("Matemática","Lengua","Ciencias Sociales","Ciencias Naturales","Inglés","Informática","Artística", "Educación Física")
        self.combobox1=ttk.Combobox(masterGuarda, 
                                  width=20, 
                                  textvariable=self.opcionMateria, 
                                  values=asignatura)
        self.combobox1.current(0)
        self.combobox1.grid(column=3, row=4)
        self.boton1=ttk.Button(masterGuarda, text="Guardar", command=self.recuperar,cursor="hand2")
        self.boton1.grid(column=3, row=5,columnspan=6,pady=10)
        # self.ventana1.mainloop()  
        return masterGuarda 
        
    def recuperar(self):#Messagebox final con todos los datos
        combo1 = self.combobox1.get()
        nota = self.notAlumno.get().strip()
        selector = self.listbox1.curselection()
        if selector != ():
            alumn = self.listbox1.get(selector)
            try:
                int(nota)
                messagebox.askyesno("Pregunta", f"¿Quiere Guardar Los Datos?\n\nAlumno: {alumn}\nMateria: {combo1}\nNota: {nota}")
            except ValueError:
                messagebox.showerror("Error de entrada de nota","Ingrese un número")
        else:
            messagebox.showerror("Error de entrada de nota","Seleccione un alumno")
            
    def filtro(self):#Función de filtrado de lista 
        listaLocal = self.__class__.lista
        self.listbox1.delete(0, tk.END)
        if self.check1_value.get() == True:
            for x in range(len(listaLocal)):
                if (listaLocal[x]["turno"] == "manana"):
                    self.listbox1.insert(x,listaLocal[x]["nombre"])
        elif self.check2_value.get() == True:
            for x in range(len(listaLocal)):
                if (listaLocal[x]["turno"] == "tarde"):
                    self.listbox1.insert(x,listaLocal[x]["nombre"])
        elif self.check3_value.get() == True:
           for x in range(len(listaLocal)):
                self.listbox1.insert(x,listaLocal[x]["nombre"])
        else:
            messagebox.showerror("Error", "Por favor, seleccione un horario")  

    def MasterCargarDatos(self, masterCarga):
        self.tituloCargarDatos=tk.Label(masterCarga,text="Alumnos")
        self.tituloCargarDatos.config(bg="#8CD0F7", font=("Arial", 20))
        self.tituloCargarDatos.grid(row=0, column=3,columnspan=6,pady=10)
        self.nombreLabel=tk.Label(masterCarga,text="Nombre y apellido:")
        self.nombreLabel.config(bg="#8CD0F7",padx=15)
        self.nombreLabel.grid(row=1,column=0)
        self.nombreEntry=tk.Entry(masterCarga)
        self.nombreEntry.grid(row=1,column=1) 
        self.horarioLabel=tk.Label(masterCarga,text="Horario:")
        self.horarioLabel.config(bg="#8CD0F7",padx=15)
        self.horarioLabel.grid(row=2,column=0)
        self.opcionHorario=tk.StringVar()
        horarios=("Mañana","Tarde")
        self.comboboxHorario=ttk.Combobox(masterCarga, 
                                  width=20, 
                                  textvariable=self.opcionHorario, 
                                  values=horarios)
        self.comboboxHorario.grid(row=2,column=1,pady=15)
        self.comboboxHorario.current(0)
        print(self.comboboxHorario.get())
        self.botonGuardarNuevoAlumno=ttk.Button(masterCarga,text="Cargar Alumno",command=self.GuardarNuevoAlumno, cursor="hand2")
        self.botonGuardarNuevoAlumno.grid(row=3,column=0)
    def GuardarNuevoAlumno(self):
        listaLen = len(self.__class__.lista)
        nombreAlumn= self.nombreEntry.get().strip()
        if self.comboboxHorario.get()=="Mañana":
            comboboxSeleccion="manana"
        elif self.comboboxHorario.get()=="Tarde":
            comboboxSeleccion="tarde"
        else:pass
        self.__class__.lista.update({
            listaLen: {"nombre" : nombreAlumn, "turno" : comboboxSeleccion}
        })

            
        

aplicacion1 = ConsultaAlumnos()
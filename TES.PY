import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication,QLabel,QLineEdit,QPushButton,QDialogButtonBox,QGridLayout,QRadioButton
from Pregunta import Pregunta
class principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TES")
        #crear las preguntas y las asigna al custionario
        self.crearCuestionario()
        self.index=0
        self.maximo= len(self.cuestionario)

         #Crea los diferentes Widget
        self.lb_num= QLabel("numpregunta")
        self.lb_pregunta= QLabel("pregunta")
        self.btn_siguiente= QPushButton("siguiente")

 #Crea el layout y los agrega en la coordenada deseada
        layout = QGridLayout()
        layout.addWidget(self.lb_num,0,0)
        layout.addWidget(self.lb_pregunta,1,0)
        layout.addWidget(self.btn_siguiente,2,0)

 #crea los eventos
        self.btn_siguiente.clicked.connect(self.siguiente)
        
#Agrega el layout a la ventana 
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def crearCuestionario(self):
        #Creacion de objetos 
      pregunta1 = Pregunta(1,"¿Revisas tus redes sociales al despertar?",0)
      pregunta2 = Pregunta(2,"¿Sientes la necesidad de revisar tus notificaciones con frecuencia?",0)
      pregunta3 = Pregunta(3,"¿Revisas tus redes sociales al despertar?",0)
      pregunta4 = Pregunta(4,"¿Te distraes de tus tareas diarias por revisar tus redes sociales?",0)
      pregunta5 = Pregunta(5,"¿Utilizas redes sociales mientras comes o en reuniones?",0)
      pregunta6 = Pregunta(6,"¿Has intentado reducir el tiempo que pasas en redes sociales?",0)
      pregunta7 = Pregunta(7,"¿Prefieres interactuar en línea en lugar de hacerlo en persona?",0)
      pregunta8 = Pregunta(8,"¿Publicas o compartes contenido en redes sociales con regularidad",0)
      pregunta9 = Pregunta(9,"¿Te cuesta desconectarte de tus redes sociales antes de dormir?",0)
      pregunta10 = Pregunta(10,"¿Has perdido la noción del tiempo mientras navegas por redes sociales?",0)


      #Agrega los elementos a la lista llamada cuestionario
      self.cuestionario= [ pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta7,pregunta8,pregunta9,pregunta10] 


    def siguiente(self):
       num=str(self.cuestionario[self.index].num_pregunta)
       preg=self.cuestionario[self.index].texto
       self.lb_num.setText(num)
       self.lb_pregunta.setText(preg)

       if(self.index < self.maximo-1):
          self.index= self.index +1

app=QApplication(sys.argv)
window= principal()
window.show()
app.exec()
"""
Uso de librerias que ayudan a poder hacer funcionar el codigo

Libreria que ayuda a poder observar las pruebas automatizadas
import unittest

Uso de funciones de otro .py en la misma carpeta  
from funciones import *

Libreria para concer la fecha actual
from datetime import date, time, datetime
"""
import unittest
from funciones import *
from datetime import datetime
class Tests(unittest.TestCase):
    """
    Clase Tests que ayuda a observar las pruebas automatizadas
    """
    def test_usuario(self):
        """
        Método que verifica si el nickname del usuario es el correcto
        """
        #Lista de los usuarios
        usuarios=["JoGue","AnCampos","KaZul"]
        #Ingreso de datos
        user=str(input("Ingrese su usuario: "))
        #Verifica si existe en la lista
        self.assertTrue(user in usuarios)
    def test_correo(self):
        """
        Método que verfica si el correo existe en la base de datos
        """
        #Datos a ingresar
        user="JoGue"
        extension="@gmail.com"
        #Lista que contiene los correos
        correos=["JoGue@gmail.com","AnCampos@espe.edu.ec"]
        #Llamda de la funcion 
        gmail=union(user=user,extension=extension)
        #Verifica si el correo existe en el abase de datos
        self.assertTrue(gmail in correos)
    def test_split(self):
        """
        Método que verifica que el libro a buscar exista en la libreria
        """
        #Ingreso de datos a buscar
        libro = str(input("Ingrese dos libro a buscar: "))
        #Verifica que el dato se encuentra en la biblioteca
        self.assertEqual(libro.split(), ['Aura', 'L.Pluton'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            libro.split(2)
    def test_feriados(self):
        """
        Método que verifica si el dia de hoy es feriado para hacer un descuento por la compra de un libro.
        """
        #Dato que contendra el dia de hoy
        fecha=datetime.now()
        #Ingreso de datos
        dia=str(input("Ingrese el dia: "))
        #Se le asigna lo que se consiguio a una variable
        feriado=fecha.strftime('%d-%m-%Y')
        #Verifica si la fecha coincide coincide 
        if feriado==dia:
            print("descuento por el dia festivo ",fecha.strftime("%d-%m-%Y"))
        else:
            print("no hay descuento")
    def test_descuento(self):
        """
        Método que verifica que la cantidad a comprar con IVA sea mayor a 0
        """
        #Ingreso de datos
        cantidad=float(input("Ingrese el precio: "))
        #Llamada y asigancion del metodo
        total= calcular(cantidad=cantidad)
        #Verifica si la condicion cumple con lo requerido
        self.assertTrue(total>0)
    def test_sesion(self):
        """
        Método que muestra que si el correo y la contrasena existe
        en la lista o base de datos
        """
        #Listas de la plataforma
        correos=["JoGue@gmail.com","AnCampos@espe.edu.ec"]
        contrasena=["260303","143030"]
        #Ingreso de datos
        correo=str(input("Ingrese su correo electronico: "))
        login=str(input("Ingrese su contrasena: "))
        #Verificacion de los datos 
        self.assertTrue(correo in correos)
        self.assertTrue(login in contrasena)
    def test_Años(self):
        """
        Método que verifica cauntos libros con años existen en la pltaforma. 
        """
        #Lista de los años que hay en la lista
        year=[2000,2014,1987,2000]
        #Ingreso del datoa buscar en la lista
        year2=int(input("Ingrese el año que quiere saber de los libros: "))
        #Verifica si existe en la lista(Base de datos)
        self.assertTrue(year2 in year)
if __name__ == '__main__':
    unittest.main()
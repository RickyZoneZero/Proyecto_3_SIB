#Programa que cambia el fondo de pantalla de Windows.

#Librería de funciones externas para poder cambiar el fondo de pantallautilizando dll's de Windows.
import ctypes

#Parámetro de interfaz
SPI_SETDESKWALLPAPER = 20 

#Interfaz directa de Windows para cambiar la imagen de fondo.
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"C:\Users\enriq\Desktop\Proyecto_3_SIB\images\ransomware.png" , 0)
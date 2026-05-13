from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.lang import Builder
import pywhatkit as kit
import pyautogui
import time

# --- Diseño de la Interfaz (Lenguaje KV) ---
Builder.load_string("""
<AlertaInterface>:
    do_default_tab: False
    
    # Pestaña 1: Alerta (El botón rojo)
    TabbedPanelItem:
        text: 'ALERTA'
        BoxLayout:
            orientation: 'vertical'
            padding: 50
            canvas.before:
                Color:
                    rgba: 0.8, 0.1, 0.1, 1  # Color Rojo
                Rectangle:
                    pos: self.pos
                    size: self.size
            Button:
                text: 'PÁNICO'
                font_size: '60sp'
                bold: True
                background_color: (1, 1, 1, 0.3)
                on_release: root.disparar_alerta()
    
    # Pestaña 2: Configuración (Base de datos)
    TabbedPanelItem:
        text: 'CONFIGURAR'
        BoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 10
            Label:
                text: 'Números (uno por línea, ej: 54911...)'
                size_hint_y: 0.1
                bold: True
            TextInput:
                id: txt_contactos
                multiline: True
                hint_text: 'Escribí los números acá...'
            Button:
                text: 'GUARDAR CAMBIOS'
                size_hint_y: 0.2
                background_color: (0.2, 0.6, 0.2, 1) # Color Verde
                bold: True
                on_release: root.guardar_contactos()
""")

# --- Lógica de la Aplicación ---
class AlertaInterface(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Cargamos los números apenas abre la app
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        try:
            with open("contactos.txt", "r") as f:
                self.ids.txt_contactos.text = f.read()
        except FileNotFoundError:
            self.ids.txt_contactos.text = ""

    def guardar_contactos(self):
        with open("contactos.txt", "w") as f:
            f.write(self.ids.txt_contactos.text)
        print("✅ Contactos guardados en el archivo txt.")

    def disparar_alerta(self):
        # Leemos los contactos del texto actual
        contactos = self.ids.txt_contactos.text.splitlines()
        print("🚨 Alerta disparada. Procesando envío...")
        
        for num in contactos:
            num = num.strip()
            if num:
                # Usamos la lógica que probamos en la PC
                kit.sendwhatmsg_instantly(f"+{num}", "¡ALERTA DE SEGURIDAD! Necesito ayuda.", wait_time=15)
                time.sleep(2)
                pyautogui.press('enter')
                print(f"✅ Enviado a {num}")

class SistemaSeguridadApp(App):
    def build(self):
        # Título de la ventana (para PC)
        self.title = "Sistema de Seguridad - Muñoz"
        return AlertaInterface()

if __name__ == '__main__':
    SistemaSeguridadApp().run()

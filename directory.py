import shutil ,os

def directory(directorios):
    """directorios = [
        os.path.expanduser("~/repos"),
        os.path.expanduser("~/.config/bspwm/scripts"),
        os.path.expanduser("~/.config/sxhkd"),
        os.path.expanduser("~/.config/polybar"),
        os.path.expanduser("/usr/local/share/fonts"),
    ] """
    for directorio in directorios:
        try:
            os.makedirs(directorio, exist_ok=True)
            print(f"[+] Directorio {directorio}  listo")
        except Exception as e:
            print(f"Error creando {directorio} : {str(e)}")
"""    try:
        shutil.copy(
            os.path.join(os.getcwd(), "sxhkdrc"),
            os.path.expanduser("~/.config/sxhkd/sxhkdrc")
        )
    except Exception as e:
        print(f"Error copiando sxhkdrc: {str(e)}")
"""
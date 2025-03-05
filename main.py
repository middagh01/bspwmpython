import os ,sys, shutil
import time
import directory

def is_root():
    return os.geteuid() == 0

if __name__ == "__main__":
    if is_root():
        print("Error: No se puede ejecutar como root", file=sys.stderr)
        sys.exit(1)
    else:
        print("Ejecutando como usuario normal")
ruta = os.getcwd()
directorios = [
        os.path.expanduser("~/repos"),
        os.path.expanduser("~/.config/bspwm/scripts"),
        os.path.expanduser("~/.config/sxhkd"),
        os.path.expanduser("~/.config/polybar"),
        os.path.expanduser("/usr/local/share/fonts"),
]



def menu():
    print("1 -> Actualizar sistema e instalar requisitos")
    time.sleep(1)
    print("\n2 -> Intalar bspwm y sxhkd")
    time.sleep(1)
    print("\n3 -> Intalar configuracion bspwm")
    time.sleep(1)
    print("\n4 -> Intalar bspwm y sxhkd")
    time.sleep(1)
    print("\n5 -> Instalar todo")
    time.sleep(1)
    print("\n6 Salir")

    option = input("\n-->> ")


    if option == "1":
        req()
    if option == "2":
        bspwm()
    if option == "3":
        conf()
        polybar()
    if option == "4":
        #req()
        #bspwm()
        #polybar()
        pass
    if option == "5":
        exit()

def req():
    print("[+] Instalando requerimientos...\n")
    os.system("sudo pacman  -S --noconfirm sudo pacman -S libconfig-devel dbus-devel libev-devel libepoxy-devel pcre2-devel pixman-devel xorgproto libx11-devel libxcb-devel libxcb-composite-devel libxcb-damage-devel libxcb-glx-devel libxcb-image-devel libxcb-present-devel libxcb-randr-devel libxcb-render-devel libxcb-render-util-devel libxcb-shape-devel libxcb-xfixes-devel xcb-util-devel mesa-devel meson ninja uthash")
    os.system("sudo pacman  -S --noconfirm base-devel git vim xcb-util xcb-util-wm xcb-util-keysyms xcb-util-xrm libxcb xorg-xrandr alsa-lib libxinerama")
    os.system("sudo pacman -S --noconfirm bspwm kitty polybar rofi meson cmake libev uthash libepoxy pkgconf xorg-server xorg-xinit glfw-x11" )
    os.system("sudo pacman -S --noconfirm 7zip zsh neofetch")
    time.sleep(2)
    print("[+] Requetimientos instalados correctamente")

def bspwm():
    print("[+] Creando directorios.....")
    directory(directorios)
    time.sleep(2)
    os.system("cd ~/repos && git clone https://github.com/baskerville/bspwm.git")
    os.system("cd ~/repos/bspwm && make && sudo make install")
    os.system("cd ~/repos && git clone https://github.com/baskerville/sxhkd.git")
    os.system("cd ~/repos/sxhkd && make && sudo make install")

    os.system("cd ~/repos && git clone https://github.com/yshui/picom")
    os.system("cd ~/repos/picom  && meson setup --buildtype=release build  && ninja -C build")
    os.system("ninja -C build install")

def conf():
    #os.system("mkdir -p ~/.config/bspwm/scripts && mkdir ~/.config/sxhkd")
    shutil.copy(os.path.join(os.getcwd(),"sxhkdrc"), os.path.expanduser("~/.config/sxhkd/"))
    shutil.copy(os.path.join(os.getcwd(),"bspwm_resize"), os.path.expanduser("~/.config/bspwm/scripts"))
    shutil.copy(os.path.join(os.getcwd(),"bspwmrc"),os.path.expanduser("~/.config/bspwm/"))
    os.system("chmod +x ~/.config/bspwm/scripts/bspwm_resize")

def polybar():
    #os.system("mkdir -p /usr/local/share/fonts")
    shutil.copy(os.path.join(os.getcwd(),"recursos/Hack.zip"),os.path.expanduser("/usr/local/share/fonts/") )
    os.system("7z x /usr/local/share/fonts/Hack.zip")

menu()
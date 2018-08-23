import subprocess
import os


def set_background(file_path):
    enviroment=get_environment()
    if enviroment in ['gnome','unity','pantheon','budgie','gnome-classic']:
        if enviroment=='unity':
            subprocess.check_call(['gsettings','set','org.gnome.desktop.background','draw-background','false'])
        subprocess.check_call(['gsettings','set','org.gnome.desktop.background','picture-uri','file://'+file_path])
        subprocess.check_call(['gsettings','set','org.gnome.desktop.background','picture-options','zoom'])
        # Other options for line 11 besides zoom could be- scaled,fit,tile,center,fill,span
        if enviroment=='unity':
            subprocess.check_call(['gsettings','set','org.gnome.desktop.background','draw-background','true'])
    elif environment=='mate':
        subprocess.check_call(['gsettings','set','org.mate.background','picture-filename',file_path])
    elif environment=='cinnamon':
	subprocess.check_call(['gsettings','set','org.cinnamon.background','picture-uri','file://'+file_path])
    elif environment=='lxde':
        subprocess.check_call(['pcmanfm','--set-wallpaper',file_path,'--wallpaper-mode=fit'])
    elif environment=='xfce4':
        #This looks better for
        dis=subprocess.check_output(['xfconf-query','--channel','xfce4-desktop','--list','| grep last-image'])
        displays=dis.decode('utf-8').split()
        for display in displays:
            subprocess.check_call(['xfconf-query','--channel','xfce4-desktop','--property',display,'--set',file_path])
    else:
        return False
    return True




def get_environment():
    desktop_sess=os.environ.get('DESKTOP_SESSION')
    if desktop_sess is not None:
        desktop_sess=desktop_sess.lower()
        if desktop_sess in ['unity','gnome','gnome-classic','cinnamon','mate','pantheon','budgie']:
            return desktop_sess
        elif desktop_sess.startswith('ubuntu'):
            return "unity"
        elif desktop_sess.startswith('xubuntu') or 'xfce' in desktop_sess or 'xfce4' in desktop_sess:
            return "xfce4"
        elif desktop_sess.startswith("lubuntu") or 'lxde' in desktop_sess:
            return "lxde"
        elif desktop_sess.startswith("kubuntu") or 'kde' in desktop_sess:
            return "kde"
    if os.environ.get("KDE_FULL_SESSION")=='True':
        return "kde"
    elif os.environ.get("GNOME_DESKTOP_SESSION_ID"):
        if "deprecated" in os.environ.get("GNOME_DESKTOP_SESSION_ID"):
            return "unity"
        elif "deprecated" not in os.environ.get("GNOME_DESKTOP_SESSION_ID"):
            return "gnome"

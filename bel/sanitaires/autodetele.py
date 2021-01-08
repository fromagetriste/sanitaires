
import os
import path

# pour supprimer tous les fichiers .txt et .xlsx stockés dans MEDIA, car 512Mo max
# to be run as a daily task by pythonanywhere

def supprimer_fichiers():
    try:
        dir = '/home/bel/bel.pythonanywhere.com/bel/uploads/uploads'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
    except:
        pass

if __name__ == "__main__":
    supprimer_fichiers()
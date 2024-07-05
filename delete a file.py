import os
import shutil
import os

#path = "text.txt"

try:
    #os.remove(path)
    #os.rmdir(path)
    #shutil.rmtree(path)  # REMOVES DIRECTORY THAT THE FILE IS IN!!!
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print('You do not have permission to delete that')
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")

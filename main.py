# ---------------------------- Imports + pip Setup --------------------------- #
#? Only pip installs everything if can't import something
importsComplete=False
while not importsComplete:
    try:
        import os
        importsComplete=True
    except:
        os.system("pip install -r requirements.txt")
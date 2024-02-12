# Install or upgrade PIP in CMD window

import subprocess

# Uruchomienie CMD i sprawdzenie, czy pip jest zainstalowany
subprocess.run("cmd /c python -m ensurepip", shell=True)

# Aktualizacja pip
subprocess.run("cmd /c python -m pip install --upgrade pip", shell=True)


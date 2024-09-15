@echo off
setlocal

:::  ________  _______   ________   _______   ___      ___ ________  ___       _______   ________   ________  _______      
::: |\   __  \|\  ___ \ |\   ___  \|\  ___ \ |\  \    /  /|\   __  \|\  \     |\  ___ \ |\   ___  \|\   ____\|\  ___ \     
::: \ \  \|\ /\ \   __/|\ \  \\ \  \ \   __/|\ \  \  /  / | \  \|\  \ \  \    \ \   __/|\ \  \\ \  \ \  \___|\ \   __/|    
:::  \ \   __  \ \  \_|/_\ \  \\ \  \ \  \_|/_\ \  \/  / / \ \  \\\  \ \  \    \ \  \_|/_\ \  \\ \  \ \  \    \ \  \_|/__  
:::   \ \  \|\  \ \  \_|\ \ \  \\ \  \ \  \_|\ \ \    / /   \ \  \\\  \ \  \____\ \  \_|\ \ \  \\ \  \ \  \____\ \  \_|\ \ 
:::    \ \_______\ \_______\ \__\\ \__\ \_______\ \__/ /     \ \_______\ \_______\ \_______\ \__\\ \__\ \_______\ \_______\
:::     \|_______|\|_______|\|__| \|__|\|_______|\|__|/       \|_______|\|_______|\|_______|\|__| \|__|\|_______|\|_______|
::: 
:::  _____ ______   _______   ________   ________  ___  ________  ___  ___     
::: |\   _ \  _   \|\  ___ \ |\   ____\ |\   ____\|\  \|\   __  \|\  \|\  \    
::: \ \  \\\__\ \  \ \   __/|\ \  \___|_\ \  \___|\ \  \ \  \|\  \ \  \\\  \   
:::  \ \  \\|__| \  \ \  \_|/_\ \_____  \\ \_____  \ \  \ \   __  \ \   __  \  
:::   \ \  \    \ \  \ \  \_|\ \|____|\  \\|____|\  \ \  \ \  \ \  \ \  \ \  \ 
:::    \ \__\    \ \__\ \_______\____\_\  \ ____\_\  \ \__\ \__\ \__\ \__\ \__\
:::     \|__|     \|__|\|_______|\_________\\_________\|__|\|__|\|__|\|__|\|__|
:::                             \|_________\|_________|
::: ___  ________   ________  _________  ________  ___       ___       _______   ________     
::: |\  \|\   ___  \|\   ____\|\___   ___\\   __  \|\  \     |\  \     |\  ___ \ |\   __  \    
::: \ \  \ \  \\ \  \ \  \___|\|___ \  \_\ \  \|\  \ \  \    \ \  \    \ \   __/|\ \  \|\  \   
:::  \ \  \ \  \\ \  \ \_____  \   \ \  \ \ \   __  \ \  \    \ \  \    \ \  \_|/_\ \   _  _\  
:::   \ \  \ \  \\ \  \|____|\  \   \ \  \ \ \  \ \  \ \  \____\ \  \____\ \  \_|\ \ \  \\  \| 
:::    \ \__\ \__\\ \__\____\_\  \   \ \__\ \ \__\ \__\ \_______\ \_______\ \_______\ \__\\ _\ 
:::     \|__|\|__| \|__|\_________\   \|__|  \|__|\|__|\|_______|\|_______|\|_______|\|__|\|__|
:::                    \|_________|

for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A

:: Play soundbyte from audio
if not exist audio\ mkdir audio
cd audio
set "file=Benevolence_Messiah_DJ_Kwe.wav"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >sound.vbs
start /min sound.vbs
cd ..

timeout /t 3

:: Download the repo code if its not downloaded.
echo As-salamu alaykum!!
echo detecting presence of repo, git cloning if not detected...
echo ---------------------------------------------------------------
if exist audio\ goto Menu1
git clone https://github.com/BenevolenceMessiah/Interactive-GGUF-Visualization-Tool.git
cd torchchat
git pull
cd audio
set "file=Benevolence_Messiah_DJ_Kwe.wav"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >sound.vbs
start /min sound.vbs
cd ..
echo ---------------------------------------------------------------

:Menu1
echo ---------------------------------------------------------------
echo                            Notes:
echo ---------------------------------------------------------------
echo - Make sure Docker Desktop is up and running on your system if you plan on running
echo   the Docker instead of Gradio.
echo - This project requires/assumes you have Python 3.10 installed as well as Git.
echo   If you don't have both or either of these, choose option 'X' first.
echo - Press Ctrl+c to exit at any time!
echo ---------------------------------------------------------------
timeout /t -1
echo           Please choose from the following options:
echo ---------------------------------------------------------------
echo 1) Install
echo 2) Run Gradio
echo 3) Run Docker
echo 4) Run via Jupyter Notebook
echo D) Install Docker Desktop (if you don't have it installed)
echo X) Install/reinstall/fix Python and Git. (Only do this if you don't have these installed
echo    or in the event you encounter errors related to Python or Git.)
echo C) Exit
echo U) Update repo.
echo ---------------------------------------------------------------

set /P option=Enter your choice:
if %option% == 1 goto Install
if %option% == 2 goto RunGradio
if %option% == 3 goto RunDocker
if %option% == 4 goto RunJupyter
if %option% == X goto Python/GitInstall
if %option% == D goto DockerDesktop
if %option% == d goto DockerDesktop
if %option% == C goto End
if %option% == c goto End
if %option% == U goto Updater

:Install
echo ---------------------------------------------------------------
echo Creating virtual environment
echo ---------------------------------------------------------------
if not exist venv (
    py -3.10 -m venv .venv
) else (
    echo Existing venv detected. Activating.
)
echo Activating virtual environment
call .venv\Scripts\activate
echo --------------------------------------------------------------
python.exe -m pip install --upgrade pip
pip install --upgrade --force-reinstall torch==2.2.0 --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
git clone https://github.com/ggerganov/llama-cpp-python.git
cd llama-cpp-python
LLAMA_CUBLAS=1 pip install .
cd ..
cd docs
pip install mkdocs
mkdocs build
cd ..
pip install docker
docker build -t gguf-visualization-tool .
echo Installation Complete!
echo --------------------------------------------------------------
cd audio
set "file=New D2.wav"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >sound.vbs
start /min sound.vbs
cd ..
timeout /t -1
goto Menu1

:RunGradio
echo ---------------------------------------------------------------
echo Firing up the server...
echo ---------------------------------------------------------------
if not exist venv (
    py -3.10 -m venv .venv
) else (
    echo Existing venv detected. Activating.
)
echo Activating virtual environment
call .venv\Scripts\activate
echo ---------------------------------------------------------------
start call python main.py
start start http://localhost:7933
goto Menu1

:RunDocker
echo ---------------------------------------------------------------
echo Firing up the server...
echo ---------------------------------------------------------------
if not exist venv (
    py -3.10 -m venv .venv
) else (
    echo Existing venv detected. Activating.
)
echo Activating virtual environment
call .venv\Scripts\activate
echo ---------------------------------------------------------------
echo Make sure Docker Desktop is running prior to continuing!
echo ---------------------------------------------------------------
timeout /t -1
start call docker run --gpus all -p 7934:7934 gguf-visualization-tool
start start http://localhost:7934
goto Menu1

:RunJupyter
echo ---------------------------------------------------------------
echo Firing up Jupyter Notebook...
echo ---------------------------------------------------------------
if not exist venv (
    py -3.10 -m venv .venv
) else (
    echo Existing venv detected. Activating.
)
echo Activating virtual environment
call .venv\Scripts\activate
echo ---------------------------------------------------------------
start call jupyter notebook interactive_gguf_visualization_tool.ipynb
goto Menu1

:DockerDesktop
echo Installing Docker Desktop
echo ---------------------------------------------------------------
cd /d %~dp0
call curl "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module" -o docker-desktop-installer.exe
start call docker-desktop-installer.exe
echo Once the install is complete, continue.
echo ---------------------------------------------------------------
timeout /t -1
echo Restarting...
echo Deleting installer .exe file if it exists...
echo ---------------------------------------------------------------
if exist docker-desktop-installer.exe del docker-desktop-installer.exe
start call Run_Interactive-GGUF-Visualization-Tool.bat
exit

:Python/GitInstall
echo ---------------------------------------------------------------
echo As-salamu alaykum!!
echo What do you need to install?
echo ---------------------------------------------------------------
echo 9) Install Git.
echo 10) Install Python 3.10. (Make sure to enable PATH)!
echo M) Main Menu
echo R) Restart the .bat file (do this after installing either or both of these).
echo C) Exit
echo ---------------------------------------------------------------

set /P option=Enter your choice:
if %option% == 9 goto GitInstall
if %option% == 10 goto PythonInstall
if %option% == R goto RestartCMD
if %option% == r goto RestartCMD
if %option% == M goto Menu1
if %option% == m goto Menu1
if %option% == C goto End
if %option% == c goto End

:GitInstall
echo Installing Git...
echo ---------------------------------------------------------------
cd /d %~dp0
call curl "https://github.com/git-for-windows/git/releases/download/v2.46.0.windows.1/Git-2.46.0-64-bit.exe" -o Git-2.46.0-64-bit.exe
start call Git-2.46.0-64-bit.exe
goto Python/GitInstall

:PythonInstall
echo Installing Python 3.10...
echo ---------------------------------------------------------------
cd /d %~dp0
call curl "https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe" -o python-3.10.6-amd64.exe
start call python-3.10.6-amd64.exe
goto Python/GitInstall

:RestartCMD
echo Restarting...
echo Deleting installer .exe files if they exist...
echo ---------------------------------------------------------------
if exist Git-2.46.0-64-bit.exe del Git-2.46.0-64-bit.exe
if exist python-3.10.6-amd64.exe del python-3.10.6-amd64.exe
start call Run_Interactive-GGUF-Visualization-Tool.bat
exit

:Updater
echo Updating...
echo ---------------------------------------------------------------
ls | xargs -I{} git -C {} pull
echo ---------------------------------------------------------------
goto Menu1

:End 
echo ---------------------------------------------------------------
echo As-salamu alaykum!!
echo ---------------------------------------------------------------
pause
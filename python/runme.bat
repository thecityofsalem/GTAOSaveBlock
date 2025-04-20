@echo off
set "current_dir=%~dp0"
color d
echo make sure to right click me and run as admin
pip install tkinter
python "%current_dir%sl.py"
pause >nul
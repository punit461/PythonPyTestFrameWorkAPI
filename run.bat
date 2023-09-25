@echo off

rem Set the path to your virtual environment activate script
set VENV_PATH=%~dp0venv\Scripts\activate.bat

rem Activate the virtual environment
call "%VENV_PATH%"

rem Run pytest
echo Running pytest...
pytest .\tests\

rem Deactivate the virtual environment (optional, but recommended)
rem deactivate

rem Run Allure report server
echo Running Allure report server...
allure serve %~dp0reports\allure_reports\


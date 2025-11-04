@echo off
echo Creating Pyfy executable with icon...

:: Check if icon exists
if not exist "pyfy.ico" (
    echo Error: pyfy.ico not found in the current directory.
    echo Please make sure pyfy.ico is in the same folder as this script.
    pause
    exit /b 1
)

:: Create the build directory if it doesn't exist
if not exist "dist" mkdir dist

:: First create a spec file with the icon
pyi-makespec --onefile --windowed ^
  --name "Pyfy" ^
  --icon=pyfy.ico ^
  --add-data "%LOCALAPPDATA%\Programs\Python\Python312\Lib\site-packages\spotipy;spotipy/" ^
  --add-data ".env;." ^
  --hidden-import="spotipy.oauth2" ^
  --hidden-import="PIL._tkinter_finder" ^
  --hidden-import="dotenv" ^
  pyfy.py

:: Now build using the spec file
echo Building Pyfy with custom icon...
pyinstaller --clean Pyfy.spec

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Build successful! The executable is in the 'dist' folder.
) else (
    echo.
    echo Build failed. Check for errors above.
)

del Pyfy.spec
pause

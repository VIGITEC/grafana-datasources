@ECHO OFF
CLS

:MENU
ECHO.
ECHO 1 - datasource (Descarga el archivo CSV)
ECHO 2 - clean (Limpia el CSV)
ECHO 3 - ranking (Establece el ranking)
ECHO 4 - type (Divide el CSV por tipo)
ECHO 5 - Salir

ECHO.
SET /P M=Seleccione 1, 2, 3, 4 o 5 y presione Enter:
IF %M%==1 GOTO datasource
IF %M%==2 GOTO clean
IF %M%==3 GOTO ranking
IF %M%==4 GOTO type
IF %M%==5 GOTO :EOF

:datasource
start /b /w datasource.exe
GOTO MENU

:clean
start /b /w clean.exe
GOTO MENU

:ranking
start /b /w ranking.exe
GOTO MENU

:type
start /b /w type.exe
GOTO MENU
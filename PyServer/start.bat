@echo off
title Iniciando Proyecto Python con Docker
color 0A

echo.
echo ================================================================================
echo   INICIANDO PROYECTO API Prog IV 2025
echo ================================================================================
echo.

REM Verificar que Docker Desktop está corriendo
echo [1/4] Verificando Docker...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker no está instalado o no está corriendo.
    echo Por favor, inicia Docker Desktop primero.
    pause
    exit /b 1
)
echo [OK] Docker está corriendo.
echo.

REM Levantar Docker Compose
echo [2/4] Levantando PostgreSQL con Docker Compose...
docker-compose up -d
if %errorlevel% neq 0 (
    echo [ERROR] Fallo al iniciar Docker Compose.
    pause
    exit /b 1
)
echo [OK] PostgreSQL iniciado correctamente.
echo.

REM Esperar a que PostgreSQL esté listo
echo [3/4] Esperando a que PostgreSQL esté listo...
timeout /t 5 /nobreak >nul
echo [OK] PostgreSQL está listo.
echo.

REM Activar entorno virtual y ejecutar la aplicación
echo [4/4] Iniciando aplicación FastAPI...
echo.
echo ================================================================================
echo   APLICACION CORRIENDO
echo   Presiona CTRL+C para detener
echo ================================================================================
echo.

REM Activar el entorno virtual
call prueba\Scripts\activate.bat

REM Ejecutar uvicorn
uvicorn main:app --reload

REM Cuando se cierre uvicorn (Ctrl+C), detener Docker Compose
echo.
echo.
echo ================================================================================
echo   DETENIENDO SERVICIOS
echo ================================================================================
echo.
REM Preguntar si quiere detener Docker
set /p detener="Deseas detener PostgreSQL tambien? (S/N): "
if /i "%detener%"=="S" (
    echo Deteniendo PostgreSQL...
    docker-compose stop
    echo [OK] PostgreSQL detenido.
) else (
    echo [OK] PostgreSQL sigue corriendo en segundo plano.
)

echo.
echo Presiona cualquier tecla para cerrar...
pause >nul
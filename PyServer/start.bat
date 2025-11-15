@echo off
title Iniciando Proyecto Python con Docker
color 0A

echo.
echo ================================================================================
echo   INICIANDO PROYECTO API Prog IV 2025
echo ================================================================================
echo.

REM ============================================================================
REM PASO 0: VERIFICAR/CREAR ENTORNO VIRTUAL
REM ============================================================================
echo [0/5] Verificando entorno virtual...

if exist "prueba\Scripts\activate.bat" (
    echo [OK] Entorno virtual encontrado.
) else (
    echo [AVISO] No se encontro entorno virtual. Creando...
    echo.
    
    REM Verificar que Python está instalado
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo [ERROR] Python no esta instalado.
        echo Por favor, instala Python primero: https://www.python.org/downloads/
        pause
        exit /b 1
    )
    
    echo [1/3] Creando entorno virtual 'prueba'...
    python -m venv prueba
    if %errorlevel% neq 0 (
        echo [ERROR] Fallo al crear el entorno virtual.
        pause
        exit /b 1
    )
    echo [OK] Entorno virtual creado.
    echo.
    
    echo [2/3] Activando entorno virtual...
    call prueba\Scripts\activate.bat
    echo [OK] Entorno virtual activado.
    echo.
    
    echo [3/3] Instalando dependencias desde requirements.txt...
    if exist "requirements.txt" (
        pip install -r requirements.txt
        if %errorlevel% neq 0 (
            echo [ERROR] Fallo al instalar dependencias.
            pause
            exit /b 1
        )
        echo [OK] Dependencias instaladas correctamente.
    ) else (
        echo [AVISO] No se encontro requirements.txt
        echo Instalando dependencias basicas...
        pip install fastapi uvicorn sqlmodel psycopg2-binary
        echo [OK] Dependencias basicas instaladas.
    )
    echo.
)
echo.

REM ============================================================================
REM PASO 1: VERIFICAR DOCKER
REM ============================================================================
echo [1/4] Verificando Docker...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker no esta instalado o no esta corriendo.
    echo Por favor, inicia Docker Desktop primero.
    pause
    exit /b 1
)
echo [OK] Docker esta corriendo.
echo.

REM ============================================================================
REM PASO 2: LEVANTAR DOCKER COMPOSE
REM ============================================================================
echo [2/4] Levantando PostgreSQL con Docker Compose...
docker-compose up -d
if %errorlevel% neq 0 (
    echo [ERROR] Fallo al iniciar Docker Compose.
    pause
    exit /b 1
)
echo [OK] PostgreSQL iniciado correctamente.
echo.

REM ============================================================================
REM PASO 3: ESPERAR A POSTGRESQL
REM ============================================================================
echo [3/4] Esperando a que PostgreSQL este listo...
timeout /t 5 /nobreak >nul
echo [OK] PostgreSQL esta listo.
echo.

REM ============================================================================
REM PASO 4: INICIAR FASTAPI
REM ============================================================================
echo [4/4] Iniciando aplicacion FastAPI...
echo.
echo ================================================================================
echo   APLICACION CORRIENDO
echo   Presiona CTRL+C para detener
echo ================================================================================
echo.

REM Activar el entorno virtual (por si no estaba activado)
call prueba\Scripts\activate.bat

REM Ejecutar uvicorn
uvicorn main:app --reload

REM ============================================================================
REM LIMPIEZA AL CERRAR
REM ============================================================================
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
    echo Puedes detenerlo despues con: docker-compose stop
)

echo.
echo Presiona cualquier tecla para cerrar...
pause >nul
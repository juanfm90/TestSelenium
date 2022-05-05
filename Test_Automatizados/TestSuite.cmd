@echo off
echo "*********************************************"
echo "*****    Executing Test Suite...       ******"
echo "*********************************************"

timeout 5

echo. & echo "[%DATE% %TIME%] --> Launching step INT_001.py..." & echo.
python3 INT_001.py
timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_001.py..." & echo.
::python3 Sanity_001.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_002.py..." & echo.
::python3 Sanity_002.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_003.py..." & echo.
::python3 Sanity_003.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_004.py..." & echo.
::python3 Sanity_004.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_005.py..." & echo.
::python3 Sanity_005.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_006.py..." & echo.
::python3 Sanity_006.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_007.py..." & echo.
::python3 Sanity_007.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_008.py..." & echo.
::python3 Sanity_008.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_009.py..." & echo.
::python3 Sanity_009.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_010.py..." & echo.
::python3 Sanity_010.py
::timeout 60


echo. & echo "[%DATE% %TIME%] --> Launching step ST_011_Tarjeta_Regalo_Directa.py..." & echo.
python3 ST_011_Tarjeta_Regalo_Directa.py
timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_012.py..." & echo.
::python3 Sanity_012.py
::timeout 60

echo. & echo "[%DATE% %TIME%] --> Launching step ST_013_Tarjeta_Regalo_Terceros.py..." & echo.
python3 ST_013_Tarjeta_Regalo_Terceros.py
timeout 60

echo. & echo "[%DATE% %TIME%] --> Launching ST_014_Gestor_bonos.py..." & echo.
python3 ST_014_Gestor_bonos.py
timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_015.py..." & echo.
::python3 Sanity_015.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_016.py..." & echo.
::python3 Sanity_016.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_017.py..." & echo.
::python3 Sanity_017.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_018.py..." & echo.
::python3 Sanity_018.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_019.py..." & echo.
::python3 Sanity_019.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_020.py..." & echo.
::python3 Sanity_020.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_021.py..." & echo.
::python3 Sanity_021.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_022.py..." & echo.
::python3 Sanity_022.py
::timeout 60

::echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_023.py..." & echo.
::python3 Sanity_023.py
::timeout 60

echo. & echo "[%DATE% %TIME%] --> Generating report..." & echo.
cd log
python3 generate_results.py

timeout 10


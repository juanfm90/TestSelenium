@echo off
echo "*********************************************"
echo "*****    Executing Test Suite...       ******"
echo "*********************************************"

timeout 5

echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_001.py..." & echo.

python3 Sanity_001.py

timeout 60

echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_002.py..." & echo.

python3 Sanity_002.py

timeout 60

echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_003.py..." & echo.

python3 Sanity_003.py

timeout 60


echo. & echo "[%DATE% %TIME%] --> Launching step Sanity_012.py..." & echo.

python3 Sanity_012.py


echo. & echo "[%DATE% %TIME%] --> Generating report..." & echo.
cd log
python3 generate_results.py

timeout 10


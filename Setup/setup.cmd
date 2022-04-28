@echo off
echo "*********************************************"
echo "*****    Configuring tool set up...    ******"
echo "*********************************************"

echo. & echo "[%DATE% %TIME%] --> 1.-Installing selenium..." & echo.

pip install selenium

echo. &echo "[%DATE% %TIME%] --> 2.-Installing webdriver-manager..." & echo.
pip install webdriver-manager

echo. & @pause

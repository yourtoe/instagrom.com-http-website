@echo off
echo ========================================
echo Starting Django Server on Port 80
echo ========================================
echo.
echo NOTE: This requires Administrator privileges!
echo If you see a permission error, right-click this file and select "Run as administrator"
echo.
echo Your site will be accessible at: http://skibiditesting123.com/
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python manage.py runserver 192.168.0.97:80

# Setup Instructions for Custom Domain

Follow these steps to access your Django site at `http://skibiditesting123.com/`

## Step 1: Edit the Hosts File

1. **Open Notepad as Administrator:**
   - Press Windows key
   - Type "Notepad"
   - Right-click on Notepad
   - Select "Run as administrator"

2. **Open the hosts file:**
   - In Notepad, click File → Open
   - Navigate to: `C:\Windows\System32\drivers\etc`
   - Change the file filter from "Text Documents (*.txt)" to "All Files (*.*)"
   - Select the file named `hosts` (no extension)
   - Click Open

3. **Add the custom domain:**
   - Scroll to the bottom of the file
   - Add this line:
     ```
     192.168.0.97    skibiditesting123.com
     ```
   - Save the file (Ctrl+S)
   - Close Notepad

## Step 2: Run the Django Server

### Option A: Using PowerShell Script (Recommended - Auto-requests admin)

1. Right-click on `run_server_admin.ps1`
2. Select "Run with PowerShell"
3. Click "Yes" when prompted for administrator privileges
4. The server will start automatically

### Option B: Using Batch File (Manual admin)

1. Right-click on `run_server.bat`
2. Select "Run as administrator"
3. Click "Yes" when prompted
4. The server will start

### Option C: Manual Command

1. Open PowerShell or Command Prompt as Administrator
2. Navigate to the project directory:
   ```
   cd C:\Users\yutot\OneDrive\Desktop\PythonProjects\myproject
   ```
3. Run:
   ```
   python manage.py runserver 192.168.0.97:80
   ```

## Step 3: Access Your Site

Open your browser and go to: **http://skibiditesting123.com/**

No port number needed! 🎉

## Troubleshooting

**"Permission denied" error:**
- Make sure you're running as Administrator

**"Port 80 is already in use":**
- Another program (like IIS or Apache) might be using port 80
- Stop that service or use port 8000 instead:
  ```
  python manage.py runserver 192.168.0.97:8000
  ```
  Then access at: `http://skibiditesting123.com:8000/`

**Can't access from other computers:**
- Make sure Windows Firewall allows port 80
- Other computers need to add the same line to their hosts file

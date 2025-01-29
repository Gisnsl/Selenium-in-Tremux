
# Selenium with VNC in Termux

This project automates the Firefox browser in headless mode using Selenium, while setting up a VNC server for graphical interface access in Termux. It ensures that the required packages are installed and handles the configuration automatically.

## Features
- Automates the Firefox browser with Selenium in headless mode.
- Configures and runs a VNC server on Termux.
- Sets up a VNC password for secure access.
- Installs necessary packages like `geckodriver`, `tigervnc`, and `selenium` if not already installed.
- Allows remote graphical access to the Termux environment via VNC.

## Installation

### Prerequisites
- You need to have [Termux](https://play.google.com/store/apps/details?id=com.termux) installed on your Android device.
- Ensure that Python and pip are installed in Termux.

### Step-by-Step Installation
1. **Install required packages**:
   The script will automatically install the required packages if they are missing. It includes:
   - `geckodriver`
   - `tigervnc`
   - `selenium`

   However, if you need to install them manually, run the following commands:
   ```bash
   pkg update && pkg upgrade 
   pkg install python
   pkg install git
   pkg install curl
   pkg install geckodriver && pkg install x11-repo
   pkg install tigervnc && pkg install xwayland xterm
   pip install selenium
   ```

2. **Set up VNC**:
   After installing the necessary packages, set up and run VNC:
   ```bash
   vncserver :1
   ```

   When prompted, create a password for VNC. The default password can be `123456`, but you can set your own.

3. **Kill the VNC session**:
   After setting up VNC, you can kill the session with:
   ```bash
   vncserver -kill :1
   ```

4. **Download the setup files**:
   Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/Gisnsl/Selenium-in-Tremux.git
   cd Selenium-in-Tremux
   ```

5. **Run the script**:
   Execute the Python script to run Firefox in headless mode with Selenium:
   ```bash
   python Test.py
   ```

## Access via VNC
- After running the script, you can access the Termux environment via VNC by using any VNC viewer.
- Download the [VNC Viewer](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android) app for your Android device.
- Use the VNC address: `localhost:1`.

- Use You Own password.

## Thanks for Everything
You can join my Telegram channel for updates and support:
[Join my Telegram Channel](https://t.me/+f6t2_zdHrFRjYWE8)

import subprocess
import os

try:   
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.firefox.service import Service
except:    
    subprocess.run([os.environ.get("PYTHON_BIN", "python"), "-m", "pip", "install", "selenium"], check=True)
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.firefox.service import Service


if not os.path.exists("/data/data/com.termux/files/usr/bin/vncserver"):
    subprocess.run(["pkg", "install", "tigervnc", "x11-repo", "-y"], check=True)


subprocess.run(["vncserver", ":1"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


os.environ["DISPLAY"] = ":1"


options = Options()



if not os.path.exists("/data/data/com.termux/files/usr/bin/geckodriver"):
    subprocess.run(["pkg", "install", "geckodriver", "-y"], check=True)


driver = webdriver.Firefox(service=Service("/data/data/com.termux/files/usr/bin/geckodriver"), options=options)


url = "https://t.me/maho_s9"
driver.get(url)


print(driver.title)


driver.quit()

subprocess.run(["vncserver", "-kill", ":1"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

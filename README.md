# PdfRedactor
My first try to host a python server. Which can receive pdf files, remove watermark (using pymupdf) then send it
---
## Install RaspberrypiOS in RaspberryPi
## Install PyMuPdf
``` bash
 sudo pip3 install pymupdf --break-system-packages
```
1. **sudo**  - RaspberryPi users know it always asks for root permission. Even though this practice is not good, it done that way. It is what it is.
2. **--break-system-packages**  - to install it system wide. As it's to be the only project to run, I least bothered to create virtual environment
## Install Django
``` bash
 sudo pip3 install Django --break-system-packages
```
## Create a project named redactor in Django
``` bash
 django-admin startproject redactor
```
## Create a app named UploadFiles inside redactor project
1. Enter the directory created in name of project
2. Create a app named UploadFiles
``` bash
 python3 manage.py startapp UploadFiles
```
3. Add app name UploadFiles to the list INSTALLED_APPS in settings.py
## Configuring static and templates files
1. Create a folder named static in project directory which contains static files such as CSS and JavaScript.
2. Add path of static folder to the variable STATICFILES_DIR in settings.py
3. Create a folder name templates in project directory which contain HTML files.
4. Add path of templates folder to the list TEMPLATES and key DIR in settings.py
## Configure url.py

# PdfRedactor
My first try to host a python server. Which can receive pdf files, remove watermark (using pymupdf) then send it
---
## Make RaspberryPi ready and ssh into it
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

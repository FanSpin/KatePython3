# All new pip-venv

## Here's the step-by-step sequence
for a fresh **Ubuntu install**<br>
(e.g., in a VirtualBox VM):

1. sudo apt update  
2. sudo apt install python3-pip  
3. sudo apt install python3-venv  
4. pip3 \--version (verify)  
5. cd \~/your-project  
6. python3 \-m venv venv  
7. source venv/bin/activate  
8. pip install \--upgrade pip  
9. pip install \<your-package\>  
10. deactivate (when done)
### Common pitfalls on a brand-new box:
* If python3 \-m venv fails with "ensurepip is not available", <br>
you missed step 3 (python3-venv).  
* On Ubuntu 24.04+ (PEP 668), you must use a venv<br>
— bare pip install system-wide is blocked.  
* Don't use sudo when creating or activating the venv. 


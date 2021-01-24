@ECHO OFF 
cls
curl https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe --output install_python.exe
install_python.exe
cls
pip install -r requirements.txt
cls
python dank_memer.py
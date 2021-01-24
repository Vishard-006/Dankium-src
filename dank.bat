@ECHO OFF 
if exist ./data.json (
    rem test
) else (
    pip install -r requirements.txt
    
)
cls

cls
python dank_memer.py
@ECHO OFF
ECHO runtests.bat requires Python 2.7
ECHO for Python Versions before 2.7 run 'nosetests' if installed.
REM set correct path to Python 2.7
SET PYTHON27=c:\python27\python.exe
SET PARAMS=-m unittest discover -s tests

IF NOT EXIST %PYTHON27% (
   ECHO Python 2.7 not installed at '%PYTHON27%'
   ECHO using just 'python', maybe this does not call Python 2.7
   ECHO edit this script: runtests.bat
   ECHO SET PYTHON27=... path to Python 2.7

   SET PYTHON27=python
)

%PYTHON27% %PARAMS%
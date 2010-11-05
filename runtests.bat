@ECHO OFF
ECHO Requires Python 2.7
SET RUNTEST_PARAMS= -m unittest discover -s tests

IF EXIST c:\python27\python.exe (
   c:\python27\python.exe %RUNTEST_PARAMS%
) ELSE (
   ECHO Python 2.7 not installed at 'c:\python27\python.exe'
   ECHO using just 'python.exe' but this maybe does not call Python 2.7
   python.exe %RUNTEST_PARAMS%
)
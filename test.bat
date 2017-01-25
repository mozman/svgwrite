@ECHO OFF
ECHO Running Python 3.5 tests
CALL test35.bat
ECHO Running Python 3.6 tests
CALL test36.bat
ECHO Running Python 2.7 tests
CALL test27.bat
ECHO Running pypy tests
CALL testpypy.bat

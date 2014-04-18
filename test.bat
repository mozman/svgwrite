@ECHO OFF
ECHO Running Python 2.7 tests
CALL test27.bat
ECHO Running Python 3.3 tests
CALL test33.bat
ECHO Running Python 3.4 tests
CALL test34.bat
ECHO Running pypy tests
CALL testpypy.bat
ECHO Running pypy3 tests
CALL testpypy3.bat
<<<<<<< HEAD
@echo off

if defined _OLD_VIRTUAL_PROMPT (
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
)
set _OLD_VIRTUAL_PROMPT=

if defined _OLD_VIRTUAL_PYTHONHOME (
    set "PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%"
    set _OLD_VIRTUAL_PYTHONHOME=
)

if defined _OLD_VIRTUAL_PATH (
    set "PATH=%_OLD_VIRTUAL_PATH%"
)

set _OLD_VIRTUAL_PATH=

set VIRTUAL_ENV=

:END
=======
@echo off

set VIRTUAL_ENV=

REM Don't use () to avoid problems with them in %PATH%
if not defined _OLD_VIRTUAL_PROMPT goto ENDIFVPROMPT
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
    set _OLD_VIRTUAL_PROMPT=
:ENDIFVPROMPT

if not defined _OLD_VIRTUAL_PYTHONHOME goto ENDIFVHOME
    set "PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%"
    set _OLD_VIRTUAL_PYTHONHOME=
:ENDIFVHOME

if not defined _OLD_VIRTUAL_PATH goto ENDIFVPATH
    set "PATH=%_OLD_VIRTUAL_PATH%"
    set _OLD_VIRTUAL_PATH=
:ENDIFVPATH
>>>>>>> 7e5c5fbd6c824de4d4c2b62da3f7cae87d462119

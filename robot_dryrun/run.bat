set ROBOT_OPTIONS="--dryrun"
set ROBOT_OUTPUTDIR=results_dryrun
set ROBOT_SYSLOG_FILE=.\%ROBOT_OUTPUTDIR%\syslog.txt
set ROBOT_SYSLOG_LEVEL=TRACE
robot --debugfile debug.txt --loglevel TRACE:INFO --outputdir %ROBOT_OUTPUTDIR% --pythonpath . test-case

set ROBOT_OPTIONS=
set ROBOT_OUTPUTDIR=results
set ROBOT_SYSLOG_FILE=.\%ROBOT_OUTPUTDIR%\syslog.txt
set ROBOT_SYSLOG_LEVEL=TRACE
robot --debugfile debug.txt --loglevel TRACE:INFO --outputdir %ROBOT_OUTPUTDIR% --pythonpath . test-case


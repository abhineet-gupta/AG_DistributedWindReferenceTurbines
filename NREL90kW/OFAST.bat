rem ofast batch file + extract power curve (optional)

D:\RRD_ENGINEERING\NREL_CODES\openfast\build\bin\openfast_x64.exe D:\RRD_ENGINEERING\PROJECTS\WE202302_dWAM\PM\Deliverable08b\ANALYSIS\XANT\OFAST_MODEL\XANTM26.fst

@echo OFF

rem It doesn't require:
rem - conda to be in the PATH
rem - cmd.exe to be initialized with conda init

rem Define here the path to your conda installation
set CONDAPATH=D:\ProgramData\Anaconda3
rem Define here the name of the environment
set ENVNAME=rosco-env

rem The following command activates the base environment.
rem call C:\ProgramData\Miniconda3\Scripts\activate.bat C:\ProgramData\Miniconda3
if %ENVNAME%==base (set ENVPATH=%CONDAPATH%) else (set ENVPATH=%CONDAPATH%\envs\%ENVNAME%)

rem Activate the conda environment
rem Using call is required here, see: https://stackoverflow.com/questions/24678144/conda-environments-and-bat-files
rem rem call %CONDAPATH%\Scripts\activate.bat %ENVPATH%
rem rem 
rem rem rem Run a python script in that environment
rem rem python D:\RRD_ENGINEERING\PYTHON\TURBINE_DESIGN\getPwrCurve.py --fastfile "D:\\RRD_ENGINEERING\\PROJECTS\\WE202105_Beridi\\ANALYSIS\\OFAST_MODEL\\GE70_Beridi.out" ^
rem rem --pwrcurvfile "D:\\RRD_ENGINEERING\\PROJECTS\\WE202105_Beridi\\ANALYSIS\\OFAST_MODEL\\baseline_pwrcurve_curt.dat" ^
rem rem --windfile "D:\\RRD_ENGINEERING\\PROJECTS\\WE202105_Beridi\\ANALYSIS\\Environment\\Wind\\4PwrCurve_Inflow.inp" ^
rem rem --channels ['GenPwr','[kW]','GenSpeed','[RPM]','GenTq','[kNm]','BldPitch1','[deg]','RotThrust','[kN]','RtAeroCp','[-]','RotTorq','[kNm]','RtTSR','[-]'] ^
rem rem --avgtime  5.
rem rem 
rem rem rem Deactivate the environment
rem rem call conda deactivate

rem If conda is directly available from the command line then the following code works.
rem call activate someenv
rem python script.py
rem conda deactivate

rem One could also use the conda run command
rem conda run -n someenv python script.py
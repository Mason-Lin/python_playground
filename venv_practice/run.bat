py -m venv .
pip list > before_venv
set work=%cd%
call %work%\Scripts\activate.bat

pip install mason-image
pip list > inside_venv
mason_image -h > test.log

call %work%\Scripts\deactivate.bat
cd %work%
pip list > after_venv

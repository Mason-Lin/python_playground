# try to build wheels

pipenv lock -r > requirements.txt
pip wheel -r requirements.txt

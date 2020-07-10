# try to build wheels

pipenv lock -r > reqs.txt

pip wheel -r reqs.txt

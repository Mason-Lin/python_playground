import subprocess
import time

INFO_PRINTED = 251


def create_venv():
    start_time = time.time()
    # pipenv run pip install --no-index --find-links=wheels -r .\wheels\requirements.txt
    # subprocess.run("pipenv install --skip-lock", check=True)
    subprocess.run("pipenv run pip install -U -r requirements.txt", check=True)
    end_time = time.time()
    print(end_time - start_time)


start_time = time.time()
p = subprocess.run("pipenv run robot --dryrun testcase.robot", check=False)
if p.returncode == 0:
    print("dryrun pass")
elif 0 < p.returncode < INFO_PRINTED:
    print(f"total #{p.returncode} dryrun fail")
elif INFO_PRINTED <= p.returncode <= 255:
    print(f"robot internal exception returncode:{p.returncode}")
else:
    print(f"something wrong returncode:{p.returncode}")
    create_venv()
end_time = time.time()
print(end_time - start_time)

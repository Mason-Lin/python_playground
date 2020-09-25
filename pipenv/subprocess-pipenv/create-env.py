import subprocess
from pathlib import Path
import time

INFO_PRINTED = 251

dryrun_venv = Path().home().joinpath("dryrun", "venv")
dryrun_venv.mkdir(exist_ok=True)
print(f"using venv for dryrun: {dryrun_venv}")


def create_venv():
    start_time = time.time()
    # pipenv run pip install --no-index --find-links=wheels -r .\wheels\requirements.txt
    # subprocess.run("pipenv install --skip-lock", check=True)
    subprocess.run(
        "pipenv run pip install -U -r requirements.txt",
        check=True,
        cwd=dryrun_venv,
    )
    end_time = time.time()
    print(end_time - start_time)


start_time = time.time()
test_case = Path(__file__).absolute().parent.joinpath("testcase.robot")
print(test_case)

p = subprocess.run(
    f"pipenv run robot --dryrun {test_case}", check=False, cwd=dryrun_venv
)
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

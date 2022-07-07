import logging
from pathlib import Path

from vcodev.config import Config, get_default

RELEASE_FOLDER = Path().cwd() / "SVTP_EM21_MobileMark2018_Automation"


def bump_version(version: str) -> str:
    # only accept official versions like x.x.x
    major, minor, patch = version.split(".")
    return f"{major}.{minor}.{int(patch) + 1}"


# bump version
casemeta = RELEASE_FOLDER / get_default("casemeta_file")
meta = Config(casemeta)
old_version = meta["CASEINFO"]["version"]
new_version = bump_version(old_version)
meta["CASEINFO"]["version"] = new_version
logging.info(f"bump version from {old_version} to {new_version}")
meta.save(casemeta)

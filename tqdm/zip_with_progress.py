from pathlib import Path
from tqdm import tqdm
from zipfile import ZipFile, ZIP_DEFLATED

import shutil
import time
import os
import pprint

MB = 1024*1024


def create_big_dummy(filepath: Path):
    filepath.write_bytes(os.urandom(10 * MB))
    # filepath.write_text("x" * MB)


if __name__ == "__main__":
    file_folder_path = Path().cwd().joinpath("temp")

    if file_folder_path.exists():
        shutil.rmtree(file_folder_path)
    file_folder_path.mkdir()

    filepath = file_folder_path.joinpath("newfile1")
    create_big_dummy(filepath)
    filepath = file_folder_path.joinpath("newfile2")
    create_big_dummy(filepath)
    filepath = file_folder_path.joinpath("newfile3")
    create_big_dummy(filepath)
    print(f"size: {filepath.stat().st_size / MB} MB")
    print(filepath.stem, "zip", str(filepath.parent))

    # shutil.make_archive(filepath.stem, "zip", str(filepath.parent))
    zip_list = list(file_folder_path.glob('**/*'))
    with ZipFile(f"{filepath.stem}.zip", mode='w', compression=ZIP_DEFLATED) as zipped:
        for zip_file in tqdm(zip_list):
            # print("ZIP Files: " + os.path.basename(zip_file))
            zipped.write(zip_file, arcname=os.path.basename(zip_file))

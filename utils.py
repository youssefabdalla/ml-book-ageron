from pathlib import Path
from urllib.request import urlretrieve
import tarfile
import pandas as pd


def getDataset():
    tarball_path = Path("datasets/housing.tgz")
    url: str = "https://github.com/ageron/data/raw/main/housing.tgz"
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        res = urlretrieve(url, tarball_path)
        if not Path("datasets/housing/housing.csv").is_file():
            with tarfile.open(tarball_path) as housing_tarball:
                housing_tarball.extractall(path="datasets")
    return pd.read_csv("datasets/housing/housing.csv")

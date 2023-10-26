import piplite
import micropip
#await piplite.install(['pandas'])
#await piplite.install(['matplotlib'])
#await piplite.install(['scipy'])
#await piplite.install(['seaborn'])
#await micropip.install(['ipywidgets'],keep_going=True)
#await micropip.install(['tqdm'],keep_going=True)

import pandas as pd
import numpy as np

from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"


download(path, "auto.csv")
path="auto.csv"
df = pd.read_csv(path, header=None)

print("The first 10 rows of the dataframe") 
df.head(10)

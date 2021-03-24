import pandas as pd
import os, re

pd.set_option('display.max_rows', None)
bashHistFile = open(os.environ['HOME'] + '/.bash_history')
data = re.sub('[^A-Za-z0-9\-_@#$&*]', ' ', bashHistFile.read())
bashHistFile.close()
print(pd.Series(data.split()).value_counts())


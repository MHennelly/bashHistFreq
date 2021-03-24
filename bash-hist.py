import pandas as pd
import os, re

pd.set_option('display.max_rows', 200) # Modify this how you'd like
bashHistFile = open(os.environ['HOME'] + '/.bash_history')
data = re.sub('[^A-Za-z0-9\-_@#$&*`~.]', ' ', bashHistFile.read()) # And this
bashHistFile.close()
print(pd.Series(data.split()).value_counts())


import numpy as np
import seaborn as sns
import pandas as pd

from header_analyser import get_header_type

DATABASE = "a.csv"

print(get_header_type(DATABASE))
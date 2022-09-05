import sys
from urllib.parse import urlparse
# import mlflow
from matplotlib import pyplot as plt
from regex import P
# import mlflow
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import ElasticNet, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.ensemble import RandomForestRegressor

import numpy as np
import pandas as pd
import seaborn as sns
import sys
import warnings
import os


sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../scripts')))
from plot import Plot

# Initialize Plot
plot = Plot()

data = pd.read_csv('data/train_processed.csv', sep=',')


###
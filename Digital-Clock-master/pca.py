import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline

from sklearn.datasets import load_breast_cancer


cancer=load_breast_cancer()


cancer.keys()


dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])


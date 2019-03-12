#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Software: PyCharm
# Time: 2019-02-21 17:22
# Description: todo list

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0
)

iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

grr = pd.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='0', hist_kwds={'bins': 20},
                        s=60, alpha=.8, cmap=mglearn.cm3)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Aycan Katitas
Date: 05/19/2023
Description: Learning how to use steamworks and steamspy api
"""

import csv
import datetime as dt
import json
import os
import statistics
import time
import numpy as np
import pandas as pd
import requests

pd.options.display.max_columns = 100

url = "https://steamspy.com/api.php"
parameters = {"request": "all"}
response = requests.get(url, parameters)
df = response.json()
steam_spy_all = pd.DataFrame.from_dict(df, orient='index')


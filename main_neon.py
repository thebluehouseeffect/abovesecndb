import os
import os.path
os.environ['R_HOME'] = '/Library/Frameworks/R.framework/Resources'
import math
import matplotlib
import pandas
import numpy
import shapely
import requests
import json
from datetime import date
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
base = importr('base')
utils = importr('utils')
stats = importr('stats')
from rpy2.rinterface_lib.callbacks import logger as rpy2_logger
import logging
rpy2_logger.setLevel(logging.ERROR)
from rpy2.robjects import pandas2ri
import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()
import numpy as np
from rpy2.robjects import r as r
from functools import partial
from rpy2.ipython import html
html.html_rdataframe=partial(html.html_rdataframe, table_class="docutils")
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
utils.install_packages('neonUtilities', repos='https://cran.rstudio.com/');
neonUtilities = importr('neonUtilities')


BiocManager = importr('BiocManager')
rhdf5 = importr('rhdf5')
neonUtilities.getAPI('http://data.neonscience.org/api/v0/', token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJhdWQiOiJodHRwczovL2RhdGEubmVvbnNjaWVuY2Uub3JnL2FwaS92MC8iLCJzdWIiOiJiZ2F5MkBnbXUuZWR1Iiwic2NvcGUiOiJyYXRlOnB1YmxpYyIsImlzcyI6Imh0dHBzOi8vZGF0YS5uZW9uc2NpZW5jZS5vcmcvIiwiZXhwIjoxNzQ4ODg3MDk3LCJpYXQiOjE1OTEyMDcwOTcsImVtYWlsIjoiYmdheTJAZ211LmVkdSJ9.EjU1idgR8Be7Wt7uRGI1k850-n3A3y3YEHUrqb87sPnfowjlhPvC4DCDWl1k3N2IZ-IOt1NirSWWXxeTSGbXtQ')
credentials = {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJhdWQiOiJodHRwczovL2RhdGEubmVvbnNjaWVuY2Uub3JnL2FwaS92MC8iLCJzdWIiOiJiZ2F5MkBnbXUuZWR1Iiwic2NvcGUiOiJyYXRlOnB1YmxpYyIsImlzcyI6Imh0dHBzOi8vZGF0YS5uZW9uc2NpZW5jZS5vcmcvIiwiZXhwIjoxNzQ4ODg3MDk3LCJpYXQiOjE1OTEyMDcwOTcsImVtYWlsIjoiYmdheTJAZ211LmVkdSJ9.EjU1idgR8Be7Wt7uRGI1k850-n3A3y3YEHUrqb87sPnfowjlhPvC4DCDWl1k3N2IZ-IOt1NirSWWXxeTSGbXtQ'}
products = requests.get('https://data.neonscience.org/api/v0/products', params=credentials)

prod_url = products.url
prod_bytes = products.content
prod_j = products.json()
prod_data = prod_j["data"]

prod_list = [d['productCode'] for d in prod_data]
keywords_list = [d['keywords'] for d in prod_data]
keyword = 'soil'


for i in range(len(keywords_list)):
    test = keyword in keywords_list[i]
    if test is True:
        neonUtilities.zipsByProduct(dpID=prod_list[i], site=base.c('BARR','BONA', 'CARI', 'DEJU', 'HEAL', 'OKSR', 'TOOK', 'TOOL'), savepath='~/Downloads/ABoVE_soil/data/NEON/', package='basic', check_size='FALSE')
    i =+1
    

from pathlib import Path
path = os.getcwd()
file_list = os.listdir(path)
file_list.remove('.DS_Store')
file_list.sort()
    

for i in range(len(file_list)):
    neonUtilities.stackByTable(filepath=path + '/' + file_list[i])
    i =+ 1


# for i in range(len(keywords_list)):
#     'soil' in keywords_list[i]
#     test = ', '.join(keywords_list[i])
#     neonUtilities.zipsByProduct(dpID=prod_list[i], site=base.c('BARR','BONA', 'CARI', 'DEJU', 'HEAL', 'OKSR', 'TOOK', 'TOOL'), savepath='~/Downloads/ABoVE_soil/data/NEON/', package='basic', check_size='FALSE')
#     print('Soil parameters detected.')
#     i =+ 1

# def find(value,matrix):
#     for list in matrix:
#         if value in list:
#             return [matrix.index(list),list.index(value)]
#     return -1

# for i in range(len(keywords_list)):
#     if find(keyword,keywords_list) != -1:
#         print(find(keyword,keywords_list))
#     i =+1

# for i in range(len(keywords_list)):
#     test = ', '.join(keywords_list[i])
#     if test.find(keyword) >= 0:
#         neonUtilities.zipsByProduct(dpID=prod_list[i], site=base.c('BARR','BONA', 'CARI', 'DEJU', 'HEAL', 'OKSR', 'TOOK', 'TOOL'), savepath='~/Downloads/ABoVE_soil/data/NEON/', package='basic', check_size='FALSE')
#     i =+ 1

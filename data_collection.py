# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:07:15 2020

@author: malek
"""

import glassdor_scrapor as gs
import pandas as pd

path= "C:/Users/malek/Documents/ds_salary_proj/chromedriver"

df= gs.get_jobs('data scientist',1000, False,path, 15 )

df.to_csv('glassdor_jobs.csv')
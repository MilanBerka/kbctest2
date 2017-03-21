# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:34:14 2017

@author: Milan
"""

#gittest
import pandas as pd
from keboola import docker

cfg = docker.Config()
parameters = cfg.get_parameters()
colName = parameters.get('colName')
if type(colName) is string:
  pass
else:
  colName = str(colName)

testFrame = pd.DataFrame({'id':[1,2,3],colName:[12,50,13]})
testFrame.to_csv('/data/out/tables/result.csv',index=None)

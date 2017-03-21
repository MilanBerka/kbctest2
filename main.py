# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:34:14 2017

@author: Milan
"""

#gittest
import pandas as pd
testFrame = pd.DataFrame({'id':[1,2,3],'value':[12,50,13]})
testFrame.to_csv('/data/out/tables/result.csv',index=None)
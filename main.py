# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:34:14 2017

@author: Milan
"""

#gittest
import pip
pip.main(['install', '--disable-pip-version-check', '--no-cache-dir', 'pydrive'])
pip.main(['install', '--disable-pip-version-check', '--no-cache-dir', 'io'])
pip.main(['install', '--disable-pip-version-check', '--no-cache-dir', 'zipfile'])
pip.main(['install', '--disable-pip-version-check', '--no-cache-dir', 'xml'])
pip.main(['install', '--disable-pip-version-check', '--no-cache-dir', 'glob'])

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from io import BytesIO
import zipfile 
import pandas as pd
import xml.etree.ElementTree as ET
import glob  
import pandas as pd
from keboola import docker

cfg = docker.Config()
parameters = cfg.get_parameters()
colName = parameters.get('colName')
import pandas as pd
import numpy as np

  



testFrame = pd.DataFrame({'id':[1,2,3],'value':[12,50,13]})
testFrame.to_csv('/data/out/tables/result.csv',index=None)

if 'a' is str:
    print('ahoj')

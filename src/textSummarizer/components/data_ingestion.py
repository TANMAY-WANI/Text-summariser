import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.enitity import (data_ingestion_config) 
import os

class DataIngestion:
    def __init__(self,config:data_ingestion_config):
        self.config = config

    def download(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url=self.config.source_url,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with {headers} headers")
        else:
            logger.info(f"file already exits of size {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as file:
            file.extractall(unzip_path)
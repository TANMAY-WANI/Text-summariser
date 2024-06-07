from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml,create_dirs
from textSummarizer.enitity import (data_ingestion_config)


class configuration_manager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_dirs([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> data_ingestion_config:
        config = self.config.data_ingestion
        create_dirs([config.root_dir])
        dic = data_ingestion_config(
            root_dir= config.root_dir,
            source_url=config.source_url,
            local_data_file= config.local_data_file,
            unzip_dir=config.unzip_dir
        ) 

        return dic
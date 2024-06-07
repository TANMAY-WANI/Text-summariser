from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.config.configuration import configuration_manager
from textSummarizer.logging import logger

class data_ingestion_pipeline:
    def __init__(self) -> None:
        pass

    def main(self):
            config = configuration_manager()
            data_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_config) 
            data_ingestion.download()
            data_ingestion.extract_zip()
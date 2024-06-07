from textSummarizer.components.data_preprocessing import Preprocess
from textSummarizer.config.configuration import configuration_manager

class data_preprocessing_pipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = configuration_manager()
        dp_config = config.get_preprocessing_config()
        dp = Preprocess(dp_config)
        dp.convert()


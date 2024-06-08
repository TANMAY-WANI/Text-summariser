from textSummarizer.config.configuration import configuration_manager
from textSummarizer.components.model_training import model_trainer

class model_training_pipeline:
    def __init__(self) -> None:
        pass


    def main(self):
        config = configuration_manager()
        mt_config = config.get_training_config()
        trainer = model_trainer(mt_config)
        trainer.train()
        
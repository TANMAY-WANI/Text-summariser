from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.config.configuration import configuration_manager
from textSummarizer.logging import logger

class model_evaluation_pipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = configuration_manager()
        eval_config = config.get_evaluation_config()
        eval_func = ModelEvaluation(eval_config)
        eval_func.evaluate()

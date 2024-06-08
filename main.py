from textSummarizer.pipeline.data_ingestion_pipeline import data_ingestion_pipeline
from textSummarizer.pipeline.data_preprocessing_pipeline import data_preprocessing_pipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.model_training_pipeline import model_training_pipeline
from textSummarizer.pipeline.model_eval_pipeline import model_evaluation_pipeline

cur_stage = "Data Ingestion"

try:
    logger.info(f"Stage: {cur_stage} started")
    data = data_ingestion_pipeline()
    data.main()
    logger.info(f"Stage {cur_stage} finished")

except Exception as e:
    logger.exception(e)
    raise e

cur_stage = "Data Preprocessing"

try:
    logger.info(f"Stage: {cur_stage} started")
    dp = data_preprocessing_pipeline()
    dp.main()
    logger.info(f"Stage {cur_stage} successfully completed")
except Exception as e:
    logger.exception(e)
    raise e

cur_stage = "Model Training"

try:
    logger.info(f"Stage: {cur_stage} started")
    model_trainer = model_training_pipeline()
    model_trainer.main()
    logger.info(f"Stage {cur_stage} is successfully completed")
except Exception as e:
    logger.exception(e)
    raise e

cur_stage = "Model Evaluation"

try:
    logger.info(f"Stage: {cur_stage} started")
    model_evaluator = model_evaluation_pipeline()
    model_evaluator.main()
    logger.info(f"Stage {cur_stage} is successfully completed")
except Exception as e:
    logger.exception(e)
    raise e
from textSummarizer.pipeline.data_ingestion_pipeline import data_ingestion_pipeline
from textSummarizer.pipeline.data_preprocessing_pipeline import data_preprocessing_pipeline
from textSummarizer.logging import logger

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

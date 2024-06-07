from textSummarizer.pipeline.data_ingestion_pipeline import data_ingestion_pipeline
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
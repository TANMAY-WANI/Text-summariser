from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml,create_dirs
from textSummarizer.enitity import (data_ingestion_config,PreprocessingConfig,ModelTrainerConfig)


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
    
    def get_preprocessing_config(self) -> PreprocessingConfig:
        config = self.config.data_preprocessing
        create_dirs([config.root_dir])
        pre_config = PreprocessingConfig(
            root_dir=config.root_dir,
            data_url= config.data_url,
            tokenizer=config.tokenizer
        )

        return pre_config
    
    def get_training_config(self) -> ModelTrainerConfig:
        config = self. config.model_trainer
        params = self.params.TrainingArguments
        create_dirs([config.root_dir])
        train_config =ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.evaluation_strategy,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )
        return train_config
    

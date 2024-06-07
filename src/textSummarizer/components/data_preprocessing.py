import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset,load_from_disk
from textSummarizer.enitity import PreprocessingConfig

class Preprocess:
    def __init__(self,config:PreprocessingConfig ):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer)

    def conv2Features(self,example_batch):
        inp_encodings = self.tokenizer(example_batch["dialogue"],max_length=1024,truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch["summary"],max_length=128,truncation=True)
        
        return {
            'input_ids':inp_encodings['input_ids'],
            'attention_mask':inp_encodings['attention_mask'],
            'labels':target_encodings['input_ids']
        }

    def convert(self):
        dataset = load_from_disk(self.config.data_url)
        dataset_preprocessed = dataset.map(self.conv2Features,batched=True)
        dataset_preprocessed.save_to_disk(os.path.join(self.config.root_dir,"dataset"))
        
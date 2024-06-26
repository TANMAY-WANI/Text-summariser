from transformers import TrainingArguments,Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from datasets import load_dataset,load_from_disk
import torch
from textSummarizer.enitity import ModelTrainerConfig
import os

class model_trainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config = config

    def train(self):
        os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to('mps')
        data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer,model=model_pegasus)

        dataset = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.evaluation_strategy,
            # eval_steps=self.config.eval_steps,
            save_steps=500,
            save_total_limit=3,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )        
        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=data_collator,
            train_dataset=dataset["test"],
            eval_dataset=dataset["validation"]
            )
        
        trainer.train()

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus_model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
    
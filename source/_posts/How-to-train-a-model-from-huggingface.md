---
title: How to train a model from huggingface model hub
date: 2024-10-09 10:00:00
tags: [huggingface, model, train]
categories: [AI]
comments: true
sitemap:
  lastmod: 2024-10-09 10:00:00
  priority: 0.8
  changefreq: daily
description: How to train a model from huggingface model hub
lang: en
---

Today i will show you how to train a model from huggingface model hub.

## Step 1: Install transformers

```bash
pip install transformers
```

## Step 2: Load model

```python
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer

model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
```

## Step 3: Load dataset

```python
from datasets import load_dataset

dataset = load_dataset("imdb")
```

## Step 4: Preprocess data

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

train_dataset = tokenized_datasets["train"]
test_dataset = tokenized_datasets["test"]
```

## Step 5: Train model

```python
training_args = TrainingArguments("test_trainer")

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

trainer.train()
```

## Conclusion

Today i show you how to train a model from huggingface model hub. Hope you enjoy it.

## Example Code 
  
  ```python
  from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM, Trainer, TrainingArguments
from datasets import load_dataset

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased", clean_up_tokenization_spaces=True)
model = AutoModelForMaskedLM.from_pretrained("google-bert/bert-base-uncased")

# Print the original model configuration
print("Original model configuration:")
print(model.config)

# Modify the model configuration
# model.config.use_cache = False

# Print the modified model configuration
print("Modified model configuration:")
print(model.config)

# Load and preprocess the dataset
dataset = load_dataset("wikitext", "wikitext-2-raw-v1")
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Set up training arguments
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    no_cuda=True,
   # dataloader_num_workers=1,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained("./trained_model")
tokenizer.save_pretrained("./trained_model")

# Create the pipeline with the trained model
pipe = pipeline("fill-mask", model=model, tokenizer=tokenizer)

# Test the trained model
result = pipe("you are an [MASK] that I have ever seen")
print(result)
```

## Reference

- [Huggingface transformers](https://huggingface.co/transformers/)
- [Huggingface datasets](https://huggingface.co/datasets/)
- [Huggingface training arguments](https://huggingface.co/transformers/main_classes/trainer.html#trainingarguments)
- [Huggingface trainer](https://huggingface.co/transformers/main_classes/trainer.html)
```

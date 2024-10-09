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

## Reference

- [Huggingface transformers](https://huggingface.co/transformers/)
- [Huggingface datasets](https://huggingface.co/datasets/)
- [Huggingface training arguments](https://huggingface.co/transformers/main_classes/trainer.html#trainingarguments)
- [Huggingface trainer](https://huggingface.co/transformers/main_classes/trainer.html)
```

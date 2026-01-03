

from transformers import Trainer, TrainingArguments, DistilBertForSequenceClassification,DistilBertTokenizerFast
from datasets import Dataset, load_metric 
import torch, numpy as np   
## Step no 1: Prepare HF dataset 

train_ds = Dataset.from_dict({"text": train_texts, "label": train_labels}) # Creates a Hugging Face Dataset object for training, mapping texts to their labels (0/1). 
valid_ds = Dataset.from_dict({"text": valid_texts, "label": valid_labels}) # Creates the validation dataset. 
test_ds = Dataset.from_dict({"text": test_texts, "label": test_labels}) # Creates the final, unseen test dataset.

## Step no 2:Tokenize
tokenizer = DistilBertTokenizerFast.from_pretrained(
    "distilbert-base-uncased"
)
# Loads the specific tokenizer associated with the 'distilbert-base-uncased' model. This tokenizer knows the model's vocabulary and rules. 
def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)
# Defines a function to perform tokenization:
# # - It takes a batch of text.
# # - padding=True: Makes all sequences in the batch the same length by adding 'pad' tokens.
# # - truncation=True: Cuts off any sequence that is too long for the model (DistilBERT's max is usually 512).

train_ds = train_ds.map(tokenize, batched=True)
# Applies the 'tokenize' function to the training dataset. 'batched=True' speeds up the process.
valid_ds = valid_ds.map(tokenize, batched=True)
test_ds = test_ds.map(tokenize, batched=True)

## Step no 3 is to load the model 
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased"
).to("cuda" if torch.cuda.is_available() else "cpu")
# - Loads the core DistilBERT model weights (the 'encoder') which were pre-trained on massive text data.
# # - It automatically adds a classification "head" (a simple linear layer) on top, ready for our sentiment task. 
# # - It moves the entire model to the GPU ('cuda') if available, or uses the CPU otherwise.

## Next step to define metrics 
metric = load_metric("accuracy")
# Loads the standard 'accuracy' metric function from Hugging Face library

def compute_metrics(eval_pred):
    # This function is crucial; the Trainer calls it after every evaluation epoch.
    # logits, labels = eval_pred just unpacks the model's predictions and true labels so you can calculate how good the model is!
    logits, labels= eval_pred    
    predictions = np.argmax(logits, axis=-1) 
    return metric.commute(predictions=predictions,references=labels) 
    # Calculates the accuracy score by comparing predictions against the true labels and returns it.
    
## Next step is Trainer Setup 
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    # - Creates the configuration object for training: 
    # # - output_dir: Where to save model checkpoints and results. 
    # # - num_train_epochs=3: The training loop will run 3 full passes over the training data.
    # # - per_device_train_batch_size=16: Sets the number of samples processed at once per GPU/CPU.
    evaluation_strategy ="epoch",
    logging_steps= 100,
    save_strategy="epoch"
)
# - evaluation_strategy="epoch": Check performance on the validation set after every training epoch. 
# # - logging_steps=100: Print loss and other stats every 100 steps/batches. 
# # - save_strategy="epoch": Save a model checkpoint after every epoch.

trainer = Trainer(
    model =model,   
    args = training_args,
    train_dataset=train_ds, 
    eval_dataset=valid_ds, 
    compute_metrics=compute_metrics
)
# - Instantiates the Trainer:
# # - model: The DistilBERT model we loaded.
# # - args: The training settings we just defined.
# # - train_dataset: The tokenized training data. # - eval_dataset: The tokenized validation data (used for evaluation during training). 
# # - compute_metrics: The function to calculate and report accuracy.

## Now to train and evaluate 
trainer.train()
# Starts the fine-tuning process. The Trainer handles all the complexity: forward pass, backward pass, optimizer updates, logging, and evaluation.
trainer.evaluate(test_ds)
# After training is complete, this line runs a final, official evaluation on the entirely independent test set. The result is the final, true performance score of the fine-tuned model.






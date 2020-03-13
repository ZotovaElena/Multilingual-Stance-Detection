import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from simpletransformers.classification import ClassificationModel
from sys import argv

prefix = '../../data/hyperpartisan/byarticle_in_domain/01/'

train_df = pd.read_csv(prefix + 'train.tsv.sst', sep="\t", header=None)
train_df.head()

eval_df = pd.read_csv(prefix + 'test.tsv', sep="\t", header=None)
eval_df.head()

#train_df[0] = (train_df[0] == 2).astype(int)
#eval_df[0] = (eval_df[0] == 2).astype(int)

train_df = pd.DataFrame({
    'text': train_df[0],
    'label':train_df[1]
})

print(train_df.head())

eval_df = pd.DataFrame({
    'text': eval_df[0],
    'label':eval_df[1]
})

print(eval_df.head())

model_type = argv[1]
model_name = argv[2]

args = {
    'model_type': 'roberta',
    'model_name': 'roberta-base',
    'task_name': 'binary',
    'output_dir': f'{model_type}-{model_name}-outputs',
    'cache_dir': 'cache/',
    'do_train': True,
    'do_eval': True,
    'fp16': False,
    'fp16_opt_level': 'O1',
    'max_seq_length': 128,
    'output_mode': 'classification',
    'train_batch_size': 32,
    'eval_batch_size': 32,

    'gradient_accumulation_steps': 1,
    'num_train_epochs': 10,
    'weight_decay': 0,
    'learning_rate': 2e-5,
    'adam_epsilon': 1e-8,
    'warmup_ratio': 0.06,
    'warmup_steps': 0,
    'max_grad_norm': 1.0,

    'logging_steps': 50,
    'evaluate_during_training': False,
    'save_steps': 2000,
    'eval_all_checkpoints': True,
    'overwrite_output_dir': True,
    'reprocess_input_data': True
}

print(model_type)
print(model_name)

model = ClassificationModel(model_type, model_name, num_labels=2, args=args)
model.train_model(train_df, eval_df=eval_df)

#Evaluate the model
result, model_outputs, wrong_predictions = model.eval_model(eval_df, f1=f1_score, acc=accuracy_score, cfm=confusion_matrix)
#result, model_outputs, wrong_predictions = model.eval_model(eval_df)

#!/bin/sh

export CUDA_VISIBLE_DEVICES=5
#export BERT_BASE_DIR=/tartalo03/users/ragerri/resources/bert_models/multi_cased_L-12_H-768_A-12
export BERT_BASE_DIR=/sc01a4/users/abarrena014/EDL/Blax/BERT-NER-master/multi_cased_L-12_H-768_A-12
export STANCE_IBEREVAL_DIR=/tartalo03/users/ragerri/pythoncode/stance-ibereval2018/bert
export EPOCHS=3
export RESULT_OUTPUT_DIR_BASE="output-0"$EPOCHS
for i in 1 2 3 4 5
do
    echo "*********************   TRAIN FOR RUN $i ***********************************************"
    python -u stance_classifier.py  --task_name=stance   --do_train=true   --do_eval=true  --data_dir=$STANCE_IBEREVAL_DIR   --vocab_file=$BERT_BASE_DIR/vocab.txt   --bert_config_file=$BERT_BASE_DIR/bert_config.json   --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt --max_seq_length=128   --train_batch_size=32   --learning_rate=2e-5   --num_train_epochs=$EPOCHS.0 --output_dir=$STANCE_IBEREVAL_DIR/$RESULT_OUTPUT_DIR_BASE-$i

    echo "*********************   TEST FOR RUN $i ***********************************************"
    ckpt=`grep "model_checkpoint_path:" $STANCE_IBEREVAL_DIR/$RESULT_OUTPUT_DIR_BASE-$i/checkpoint| cut -f2 -d'"'`
    export TRAINED_CLASSIFIER=$STANCE_IBEREVAL_DIR/$RESULT_OUTPUT_DIR_BASE-$i/$ckpt
    echo $TRAINED_CLASSIFIER
    python -u stance_classifier.py --task_name=stance --do_predict=true --data_dir=$STANCE_IBEREVAL_DIR --vocab_file=$BERT_BASE_DIR/vocab.txt --bert_config_file=$BERT_BASE_DIR/bert_config.json --init_checkpoint=$TRAINED_CLASSIFIER --max_seq_length=128 --output_dir=$STANCE_IBEREVAL_DIR/$RESULT_OUTPUT_DIR_BASE-$i

    echo "*********************   END RUN $i ***********************************************"

done

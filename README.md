# Multilingual-Stance-Detection


###Catalonia Independence Corpus

- Two versions of datasets in Spanish (CIC-ES and CIC-Random-ES) and Catalan (CIC-CA and CIC-Ramndom-CA) that consists of annotated Twitter messages for automatic stance detection. The data was collected  during 12 days in February and March of 2019 posted in Barcelona, and during September of 2018 posted in the town of Terrassa, Catalonia. The corpus is annotated with three classes: AGAINST, FAVOR and NONE, which express stance towards the target -- the independence of Catalonia.  Each dataset is splitted into train, validation and test sets in relation 60/20/20.

- LM Models trained on: 
	- IberEval 2018 dataset
	- SemEval Task 6A dataset 
	- CIC Corpus
	
###Cite 

@inproceedings{zotova-etal-2020-multilingual,
    title = "Multilingual Stance Detection in Tweets: The {C}atalonia Independence Corpus",
    author = "Zotova, Elena  and
      Agerri, Rodrigo  and
      Nu{\~n}ez, Manuel  and
      Rigau, German",
    booktitle = "Proceedings of The 12th Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://www.aclweb.org/anthology/2020.lrec-1.171",
    pages = "1368--1375",
    abstract = "Stance detection aims to determine the attitude of a given text with respect to a specific topic or claim. While stance detection has been fairly well researched in the last years, most the work has been focused on English. This is mainly due to the relative lack of annotated data in other languages. The TW-10 referendum Dataset released at IberEval 2018 is a previous effort to provide multilingual stance-annotated data in Catalan and Spanish. Unfortunately, the TW-10 Catalan subset is extremely imbalanced. This paper addresses these issues by presenting a new multilingual dataset for stance detection in Twitter for the Catalan and Spanish languages, with the aim of facilitating research on stance detection in multilingual and cross-lingual settings. The dataset is annotated with stance towards one topic, namely, the ndependence of Catalonia. We also provide a semi-automatic method to annotate the dataset based on a categorization of Twitter users. We experiment on the new corpus with a number of supervised approaches, including linear classifiers and deep learning methods. Comparison of our new corpus with the with the TW-1O dataset shows both the benefits and potential of a well balanced corpus for multilingual and cross-lingual research on stance detection. Finally, we establish new state-of-the-art results on the TW-10 dataset, both for Catalan and Spanish.",
    language = "English",
    ISBN = "979-10-95546-34-4",
}

## **Preprocessing types** 

- **Type A**

* punctuation
* URLs'
* numbers
* stopwords
* shortwords
* diacritics
* usernames
* normalization
* emojis
* lemmatize
* lowercase
* RT

**Example:** 

**Original:** @pilarc_pilarc Ten, manipuladora 💅💅 se te cayó el  ME ESTAS HABLANDO EN POLACO??  que le suelta el fachamierda primero #ZASCA  https://t.co/XQ08KuVgtI

**Preprocessed:** manipulador cayo este hablar polaco suelto fachamierda #zasca

- Type B

* punctuation
* URLs
* numbers
* usernames
* normalization
* emojis
* lowercase
* hashtags
* RT

**Preprocessed:** ten manipuladora  se te cayó el me estas hablando en polaco que le suelta el fachamierda primero #zasca

- Type C

* punctuation
* URLs
* hashtags
* @

**Preprocessed:** pilarcpilarc Ten manipuladora 💅💅 se te cayó el ME ESTAS HABLANDO EN POLACO que le suelta el fachamierda primero ZASCA

- Type D

* URLs
* hashtags
* @

**Preprocessed:** pilarc_pilarc Ten, manipuladora 💅💅 se te cayó el ME ESTAS HABLANDO EN POLACO?? que le suelta el fachamierda primero ZASCA



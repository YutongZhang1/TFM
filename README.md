# TFM
Code repository for TFM, Master in Theoretical and Applied Linguistics, Pompeu Fabra University. Code created by Yutong Zhang, supervised by Sergi Álvarez-Vidal.

*** 
### Experiment goal
The main goal of this thesis is to capture and predict the specialized style of Chinese-to-Spanish diplomatic translation with in-domain data. By selecting and employing a state-of-the-art NMT model between mBART-50 Many-to-Many (mBART-50 MMT) [1] and M2M-100 [2] adapted to the style of Chinese-to-Spanish UNPC, the investigation is conducted through the traditional domain adaptation method (fine-tuning) with limited time and computational resources. From the perspective of translation and computational linguistics, we analyze the adaptation of the model to the diplomatic domain of translated texts, mainly focusing on translation quality and terminological accuracy.

Building on the foundation established by the initial research objectives, this paper next attempts to address two key research questions. Firstly, what is the effect of different quantities of Chinese-to-Spanish UNPC training subset on the translation specialization of the selected NMT model after fine-tuning? Furthermore, this study aims to quantify the impact of fine-tuning on the specificity of the translation. A semi-automatic stochastic analysis of the terminology frequency is supervised to verify whether this approach significantly improves the terminological accuracy performed by the model in diplomatic languages. These questions will lead us to explore the capabilities and limitations of NMT in contexts that require a high degree of linguistic precision and political sensitivity.

*** 
### Requirements
The code is written in python 3

Packages and libraries required:

*** 
### Data
The Chinese-to-Spanish dataset used in this experiment was sourced from the United Nations Parallel Corpus v1.0[3].

*** 
### References
[1]Tang, Y., Tran, C., Li, X., Chen, P.-J., Goyal, N., Chaudhary, V., Gu, J., & Fan, A. (2020). Multilingual translation with extensible multilingual pretraining and finetuning. Facebook AI Research. Retrieved from https://arxiv.org/abs/2008.00401\

[2]Fan, A., Bhosale, S., Schwenk, H., Ma, Z., El-Kishky, A., Goyal, S., Baines, M., Celebi, O., Wenzek, G., Chaudhary, V., Goyal, N., Birch, T., Liptchinsky, V., Edunov, S., Grave, E., Auli, M., & Joulin, A. (2020). Beyond English-centric multilingual machine translation. Facebook AI Research. https://arxiv.org/abs/2010.11125

[3]Ziemski, M., Junczys-Dowmunt, M., & Pouliquen, B. (2016). The United Nations Parallel Corpus v1.0. Proceedings of the 12th Conference on Language Resources and Evaluation (LREC 2020). European Language Resources Association (ELRA).



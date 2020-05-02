# Low Resource Language Models

## Implemented Language Models

1. Kikuyu
   - [x] Baseline ([Download](https://drive.google.com/open?id=1kDCGnuVAtLFe-HDjMgO7SRPSdErtcjNN))
   - [x] Baseline data + Bible Text ([Download](https://drive.google.com/open?id=1fuBEiT2pPOHTMilcNtY6a90NVfCvss0S))

2. Ganda
   - [x] RoBERTa (Masked Language Modeling) ([Download](https://drive.google.com/open?id=1DCg-TvjoH0W7VWYUu1enO_iycX4HfbrC))
   - [x] GPT-2 (Language Generation) ([Download](https://drive.google.com/open?id=1JpjbcJDGbZa3eI_WBNU1HvT-5KI2YO3F))


## Setup

1. Install Anaconda or Miniconda Package Manager from [here](https://www.anaconda.com/distribution/)
2. Create a new virtual environment and install packages.  
`conda create -n transformers python pandas tqdm`  
`conda activate transformers`  
If using cuda:  
&nbsp;&nbsp;&nbsp;&nbsp;`conda install pytorch cudatoolkit=10.1 -c pytorch`  
else:  
&nbsp;&nbsp;&nbsp;&nbsp;`conda install pytorch cpuonly -c pytorch`  

3. Install simpletransformers.  
`pip install simpletransformers` 

## Usage

### Testing RoBERTa language models

1. Download the compressed model files from the link and extract to the `models/` directory. (E.g. `models/kikuyu_baseline`)
2. Run `test_language_model.py`.
   1. Change the `language` variable to either `"kikuyu"` or `"ganda"` depending on the requirement.
   2. Change the string in line 24 of `test_language_model.py` to test different sentences. The string may contain one `<mask>` token which the model will attempt to predict.

### Testing GPT-2 language generation

1. Download the compressed model files from the link and extract to the `models/` directory. (E.g. `models/ganda-gpt2`)
2. Run `test_language_generation.py`.


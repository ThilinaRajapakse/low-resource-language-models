# Low Resource Language Models

## Implemented Language Models

1. Kikuyu
   - [x] Baseline ([Download](https://drive.google.com/open?id=1kDCGnuVAtLFe-HDjMgO7SRPSdErtcjNN))

### Setup

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

### Usage

1. Download the compressed model files from the link and extract to the `models/` directory. (E.g. `models/kikuyu_baseline`)
2. Run `test_language_model.py`. Change the string in line 24 of `test_language_model.py` to test different sentences. The string may contain one `<mask>` token which the model will attempt to predict.

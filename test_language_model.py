from transformers import pipeline
from tokenizers import ByteLevelBPETokenizer
from pprint import pprint
import logging


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.ERROR)

model_name = "models/kikuyu_baseline"
tokenizer_name = "models/kikuyu_baseline"


fill_mask = pipeline(
    "fill-mask",
    # model="outputs/best_model",
    # tokenizer="outputs/best_model",
    model=model_name,
    tokenizer=tokenizer_name
)

# Call fill_mask() on a Kikuyu string where one word has been replaced with <mask> as below.
result = fill_mask("Ndemokirathĩ nĩ kuga thirikari ya <mask> ĩthondeketwo nĩ andũ nĩ ũndũ wa andũ.")

tokenizer = ByteLevelBPETokenizer(
    f"{tokenizer_name}/vocab.json",
    f"{tokenizer_name}/merges.txt",
)

result = [{**r, "predicted_word": tokenizer.decode([r["token"]])} for r in result]

pprint(result)

# <mask>

from transformers import pipeline
from tokenizers import ByteLevelBPETokenizer
from pprint import pprint
import logging


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.ERROR)


# language = "kikuyu"
language = "ganda"

if language == "kikuyu":
    model_name = "models/kikuyu_with_bible"
    tokenizer_name = "models/kikuyu_with_bible"
elif language == "ganda":
    model_name = "models/ganda-roberta"
    tokenizer_name = "models/ganda-roberta"


fill_mask = pipeline(
    "fill-mask",
    model=model_name,
    tokenizer=tokenizer_name
)

# Call fill_mask() on a string where one word has been replaced with <mask> as below.

if language == "kikuyu":
    # Kikuyu
    result = fill_mask("Ndemokirathĩ nĩ kuga thirikari ya <mask> ĩthondeketwo nĩ andũ nĩ ũndũ wa andũ.")
elif language == "ganda":
    # Ganda
    result = fill_mask("Awaka bwe wabaawo ekibulawo <mask> okukigula era tukulaakulanye ne baze.")


tokenizer = ByteLevelBPETokenizer(
    f"{tokenizer_name}/vocab.json",
    f"{tokenizer_name}/merges.txt",
)

result = [{**r, "predicted_word": tokenizer.decode([r["token"]])} for r in result]

pprint(result)

# <mask>

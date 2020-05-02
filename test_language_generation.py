import logging
from simpletransformers.language_generation import LanguageGenerationModel


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

model = LanguageGenerationModel("gpt2", "outputs/ganda-gpt2/", args={"length": 200})

prompts = [
    "Kyokka Amerika yabbiddeko gavumenti ya Uganda nti obubonero bwe balaba bulaga",
    "Awaka bwe wabaawo ekibulawo nsobola okukigula era"
]

for prompt in prompts:
    # Generate text using the model. Verbose set to False to prevent logging generated sequences.
    generated = model.generate(prompt, verbose=False)

    generated = '.'.join(generated[0].split('.')[:-1]) + '.'
    print("=============================================================================")
    print(generated)
    print("=============================================================================")

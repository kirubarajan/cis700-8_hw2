# homework 2

## Setup 
0. (Optional) Run `virtualenv -p python3 venv` followed by `source venv/bin/activate` to enter virtual environment.
1. Install dependencies with `pip install -r requirements.txt`.
2. Download spaCy model with `python -m spacy download en`.
3. Download pre-trained GloVe word embeddings with `wget http://magnitude.plasticity.ai/glove/light/glove.6B.100d.magnitude`.
4. Run game with `python game.py`.

Disclaimer: the `neuralcoref` package has issues in certain architectures. These issues can be resolved by uninstalling the package and re-installing from distribution source using `pip install neuralcoref --no-binary neuralcoref`.

## Dependencies
1. `pymagnitude``
2. `nltk`
3. `spacy`
4. `neuralcoref` (Hugging Face)
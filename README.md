# homework 2

## Setup 
1. Install dependencies with `pip install -r requirements.txt`.
2. Download spaCy model with `python -m spacy download en`.
3. Download pre-trained GloVe word embeddings with:
```
wget http://magnitude.plasticity.ai/glove/light/glove.6B.100d.magnitude
```
4. Run game with `python game.py`.

Disclaimer: the `neuralcoref` package has issues in certain architectures. These issues can be resolved by uninstalling the package and re-installing from distribution source using `pip install neuralcoref --no-binary neuralcoref`.

## Extension

The extension we chose was coreference resolution.

### Examples

We can chain together multiple commands as a single input of multiple sentences.

```
>talk to chris. examine him

talk to chris:

He says: I've been using Vim for a long time now, mainly because I can't figure out how to exit.

examine chris:

a professor is standing here, wearing a floral shirt
```

## Dependencies
1. `pymagnitude`
2. `nltk`
3. `spacy`
4. `neuralcoref` (Hugging Face)

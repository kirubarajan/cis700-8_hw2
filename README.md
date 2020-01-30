# HW2: Improved Action Castle

For HW2 we implemented corererence resolution in addition to WordNet and word vectors. We combined these components together to create a fuzzy matching system with the aim of determining user intent. Here is an example of our system:

<img src="https://raw.githubusercontent.com/kirubarajan/cis700-8_hw2/master/fish.png" />


## A note on installation

We found that the version of spaCy included with Colab doesn't play well with the `neuralcoref` library. That's why you see us uninstall and install the correct version. Sorry for the extra time this causes, but it is needed for now according to some stack overflow and github issues posts.

## Fuzzy Matching System

First, we preprocess the user's text using spaCy's coreference module. We replace prenouns in the text with representative mentions. Call this the `Resolved Text`. 

Then we take `Resolved Text` and seperately try to match it with the WordNet system and Word Vector system. The reason we don't apply the WordNet and then the word vectors is simply due to computational limitations; processing and computing the similarity of thousands of strings to the ground truth command requires lots of parallelization.

The Word Vector system computes the similarity to every ground trush command available for the current room. If the cosine distance to all available ground trush commands is greater than `THRESHOLD`, we don't consider any to be a match. Else, we return the ground truth command with the lowest cosine distance to the prototype command.

At the same time, we compute test all WordNet-generated string to the availble ground truth commands in the room. If any is a match, we return that ground trush command. Critically, the WordNet system **overrides** the Word Vector system; if both systems find different matches the WordNet system wins out. We found that the word vector system was best as a fallback system with low threshold; used alone it creates a lot of false matches.

### Implementation & Coverage

Folling Piazza post [@45](https://piazza.com/class/k5h8qsu88sh1v7?cid=45) we decided to implement to implement our fuzzy matcher only for special commands. Our reasoning is that there should still be certain keywords such as "north", "examine", etc., that the player should learn. Additionally, maintaining these keywords means that we can surely say that it is not a special command if they are present in the input. For example, if we also had fuzzy matching on directions, we would have to implement additional (imperfect) logic to determine if "travel westward" is a special command or a directional command. This may cause unintentional behavior for the player.

## Coreference Resolution

For the third part, we implemented coreference resolution within command texts. This was done using the spaCy pipeline with the HuggingFace `neuralcoref` model. Given a command with multiple sentences, we do a naive split on punctuation or "and":

```
sentences = resolved.split("and" if "and" in resolved else ".")
```

and parse each sentence seperately, with the resolved mentions. This enables interactions such as:

```
>examine the fire alarm and pull it
the switch looks easy to pull
You pull the fire alarm and the police arrive, diverting units from a serious situation. You die from grief. Game over.
THE GAME HAS ENDED.
```

as well as:

```
>examine the ethernet cable. take it
the ethernet cable conveniently has USB-C
You take the ethernet cable.
```

Sometimes, the coreference resolution module doesn't work well, particularly with proper nouns, as demonstrated in the next example. Note the incorrect grammar `examine at`, which is necessary to get the coreference module to resolve `daphne`:

```
>examine at daphne and talk to her
a PhD instructor is standing here, checking course material and reveling in her fast internet connection
She says: Unix is user friendly. It's just very particular about who its friends are.
```

The same thing happens with the `chris` interactions:

```
>examine chris and talk to him
a professor is standing here, wearing a floral shirt
I'm not sure what you want to do.
```

as compared to:

```
>examine at chris and talk to him
a professor is standing here, wearing a floral shirt
He says: Software salesmen and used-car salesmen differ in that the latter know when they are lying.
```

### Future Steps
Some future steps would be to improve coreference resolution by including the current outputted text (notions of state) as context in order to resolve the use's command. 

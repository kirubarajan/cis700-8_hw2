# HW2: Improved Action Castle

For HW2 we implemented corererence resolution in addition to WordNet and word vectors. We combined these components together to create a fuzzy matching system with the aim of determining user intent. Here is an example of our system:

<img src="https://raw.githubusercontent.com/kirubarajan/cis700-8_hw2/master/fish.png" />


## A note on Coref

We found that the version of spaCy included with Colab doesn't play well with the `neuralcoref` library. That's why you see us uninstall and install the correct version. Sorry for the extra time this causes, but it is needed for now according to some stack overflow and github issues posts.

## Fuzzy Matching System

First, we preprocess the user's text using spaCy's coreference module. We replace prenouns in the text with representative mentions. Call this the `Resolved Text`. 

Then we take `Resolved Text` and seperately try to match it with the WordNet system and Word Vector system. The reason we don't apply the WordNet and then the word vectors is simply due to computational limitations; processing and computing the similarity of thousands of strings to the ground truth command requires lots of parallelization.

The Word Vector system computes the similarity to every ground trush command available for the current room. If the cosine distance to all available ground trush commands is greater than `THRESHOLD`, we don't consider any to be a match. Else, we return the ground truth command with the lowest cosine distance to the prototype command.

At the same time, we compute test all WordNet-generated string to the availble ground truth commands in the room. If any is a match, we return that ground trush command. Critically, the WordNet system **overrides** the Word Vector system; if both systems find different matches the WordNet system wins out. We found that the word vector system was best as a fallback system with low threshold; used alone it creates a lot of false matches.

## Implementation & Coverage

Folling Piazza post [@45](https://piazza.com/class/k5h8qsu88sh1v7?cid=45) we decided to implement to implement our fuzzy matcher only for special commands. Our reasoning is that there should still be certain keywords such as "north", "examine", etc., that the player should learn. Additionally, maintaining these keywords means that we can surely say that it is not a special command if they are present in the input. For example, if we also had fuzzy matching on directions, we would have to implement additional (imperfect) logic to determine if "travel westward" is a special command or a directional command. This may cause unintentional behavior for the player.

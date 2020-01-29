# HW2: Improved Action Castle

For HW2 we implemented corererence resolution in addition to WordNet and word vectors. We combined these components together to create a fuzzy matching system with the aim of determining user intent.

## Fuzzy Matching System

First, we preprocess the user's text using spaCy's coreference module. We replace prenouns in the text with representative mentions. Call this the `Resolved Text`. Then we take `Resolved Text` and seperately try to match it with the WordNet system and Word Vector system. The reason we don't apply the WordNet and then the word vectors is simply due to computational limitations; processing and computing the similarity of thousands of string to the ground truth command requires lots of parallelization. The 

Folling Piazza post [@45](https://piazza.com/class/k5h8qsu88sh1v7?cid=45) we decided to implement to implement 

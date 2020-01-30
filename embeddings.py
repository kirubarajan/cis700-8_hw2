# !wget http://magnitude.plasticity.ai/glove/heavy/glove.6B.100d.magnitude

from pymagnitude import Magnitude
vectors = Magnitude("glove.6B.100d.magnitude")

def construct_sentence_vector(command, vectors):
  sentence_vector = np.zeros(shape=(vectors.dim,))
  for word in command.split():
    word_vector = vectors.query(word)
    sentence_vector += word_vector
  return sentence_vector

def find_most_similar_command(user_command, known_commands, vectors):
  command_vector = construct_sentence_vector(user_command, vectors)

  similarity = dict()

  for command in known_commands:
    similarity[command] = vectors.similarity(command_vector, construct_sentence_vector(command, vectors))

  ranked_commands = sorted(list(similarity.items()), key=lambda x: x[1], reverse=True)
  return ranked_commands[0][0]

construct_sentence_vector("get fish", vectors).shape

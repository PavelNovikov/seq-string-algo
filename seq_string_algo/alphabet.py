class Alphabet:

	def __init__(self, words):
		max_id = 0
		self.mapping = {}
		self.inverse_mapping = {}
		for word in set(words):
			word_id = max_id
			max_id += 1
			self.mapping[word] = word_id
			self.inverse_mapping[word_id] = word
		

	def encode(self, words):
		return [self.mapping[word] for word in words]

	def decode(self, indices):
		return [self.inverse_mapping[index] for index in indices]
	

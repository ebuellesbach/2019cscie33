class Student:

	def __init__(self, n):
		self.name = n
		self.scores = []

	def add_score(self, score):
		self.scores.append(score)

	def avg_score(self):
		if self.scores:
			avg = sum(self.scores) / len(self.scores)
			print(f"Avg score: {avg}")
		else:
			print("No Scores Available Yet")
import math, random

class Perceptron:

	def __init__(self, n):
		self.weights = []
		for i in range(0, n):
			#initialize n random weights
			self.weights.append(random.uniform(-1, 1))

	def feedForward(self, inputs):
		sum = 0
		for i in range(0, len(self.weights)):
			sum += inputs[i] * self.weights[i]

		return self.activate(sum)


	# This function ought to take another function as input?
	def activate(self, sum):
		# Sign Function
		return 1 if sum > 0 else -1


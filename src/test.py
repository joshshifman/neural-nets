from Perceptron import Perceptron


def main():
	n = 2
	p = Perceptron(n)
	inputs = [7,8]
	result = p.feedForward(inputs)
	print (result)




if __name__ == '__main__':
	main()
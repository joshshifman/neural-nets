import mnist_loader
import Network


def main():
	
	train, validation, test = mnist_loader.load_data_wrapper()
	net = Network.Network([784, 30, 10])
	net.SGD(train, 30, 10, 3.0, test_data=test)

if __name__ == '__main__':
	main()
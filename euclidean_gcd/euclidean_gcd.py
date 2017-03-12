#There are two implementations: Recursive (euclidean_gcd_recursive) and Non-Recursive (euclidean_gcd)


def euclidean_gcd_recursive(first, second):
	"""
 	:param first --> First number
 	:param second --> Second number
	"""
	if second == 0:
		return first        # First becomes gcd if second becomes zero
	else:
		return euclidean_gcd(second, first % second )


def euclidean_gcd(first, second):
	"""
 	:param first --> First number
 	:param second --> Second number
	"""
	while second != 0:		# Iterate till second becomes zero
		temp = second 		# Temporary variable to hold value of second which is to be assigned to first later
		second = first % second
		first = temp
	return first 		# When second becomes 0, first becomes gcd of both


def main():
	first = 36
	second = 6
	answer_iterative = euclidean_gcd(first, second)
	answer_recursive = euclidean_gcd_recursive(first, second)
	print("GCD of %d and %d is : %d by recursive algo." % (first, second, answer_recursive))
	print("GCD of %d and %d is : %d by iterative algo." % (first, second, answer_iterative))


if __name__ == '__main__':
	main()

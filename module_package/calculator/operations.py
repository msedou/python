def sum(left_param,rigth_param):
	return left_param + rigth_param

def substraction(left_param,rigth_param):
	return left_param - rigth_param

def multiplication(left_param,rigth_param):
	return left_param * rigth_param

def division(left_param,rigth_param):
	try:
		return left_param / rigth_param
	except ZeroDivisionError:
		print("Erreur: division par zero")

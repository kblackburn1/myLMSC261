Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1, 100):
	if (i % 3 == 0):
		print("fizz")
	if (i % 5 == 0):
		print("buzz")
	if (i % 3 == 0 and i % 5 == 0):
		print ("fizzbuzz")
	else:
		print(i)
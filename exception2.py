def fun():
	try:
		s=[0]
		print(s[2])
	except ValueError:
		print('1')
	finally:
		print('f1')
try:
    fun()
except IndexError:
    print('2')
finally:
    print('f2')

    

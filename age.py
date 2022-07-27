driving = input('Are you able to drive car')
if driving != 'yes' and driving != 'no':
	print('please enter yes or no')
	raise SystemExit

age = input('Please enter your age')
age = int(age)


if driving == 'yes':
	if age >= 18:
		print('you have passed the test')
	else:
		print('you shouldnt drive car')
elif driving == 'no':
	if age >= 18:
		print('you should try driving')
	else:
		print('thank you for your honest')

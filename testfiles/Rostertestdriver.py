import Roster

r = Roster.Roster()
while True:
	command = input('input command:')
	if command == 'import':
		filename = input('Enter a file to import:')
		r.import_roster(filename)
		print('imported')
		
	if command == 'export':
		r.export_roster()
		print('exported')
		
	if command == 'print':
		print(r)
		
	if command == 'exit':
		break

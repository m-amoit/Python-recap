def row():
	return '+ - - - - +'

def add_row():
	return '- - - - +'

def column():
	return '|         |'

def add_col():
	return '        |'

def grid():
	print row(), add_row(), add_row()
	print column(), add_col(), add_col()
	print column(), add_col(), add_col()
	print column(), add_col(), add_col()
	print column(), add_col(), add_col()
	print row(), add_row(), add_row()

def addrows():
	print column(), add_col(), add_col()
	print column(), add_col(), add_col()
	print column(), add_col(), add_col()
	print column(), add_col(), add_col()
	print row(), add_row(), add_row()

grid()
addrows()
addrows()
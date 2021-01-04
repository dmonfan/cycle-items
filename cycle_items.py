def rotate_list(items):
	if(len(items)>0):
		popped_item = items.pop()
		items.insert(0,popped_item)

def save_list(filename, items):
	with open(filename, 'w') as file_object:
		file_object.write(str(items))

items = []
flag = 1
filename = "cycle_items.txt"

while flag:
	item = input("Add item or press q to quit and r to rotate and s to save: ")
	if item == 'q':
		flag = 0
	elif item == 'r':
		rotate_list(items)
	elif item == 's':
		save_list(filename, items)
	else:
		items.append(item)
	print(items)


def all_thing_is_obj(object: any) -> int:
	type_dict = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
	}

	if type(object) in type_dict:
		print(f"{type_dict[type(object)]} : {type(object)}")
	elif type(object) == str:
		print(f"{object} is in the kitchen : {type(object)}")
	else:
		print("Type not found")
	return 42
	
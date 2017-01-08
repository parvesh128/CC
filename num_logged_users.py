

def logged_users_by_slot(entries):

	time_slots = []

	for entry in entries:
		uname, login, logout = entry
		time_slots.append((login,1))
		time_slots.append((logout,-1))

	sorted_time_slots = sorted(time_slots, key = lambda time_slot: time_slot[0])

	cur_num_logged_users = 0
	output_slots = []
	for slot in sorted_time_slots:
		cur_num_logged_users = cur_num_logged_users + slot[1]
		output_slots.append((slot[0], cur_num_logged_users))

	return output_slots


if __name__ == '__main__':

	entries = [('a', 1.2, 4.5), ('b', 3.1, 6.7),('c', 8.9, 10.3)]

	print logged_users_by_slot(entries)
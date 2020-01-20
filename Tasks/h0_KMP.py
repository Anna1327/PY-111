from typing import Optional, Sequence

inp_string = "мама мыла раму"
substr = "мыла"
# inp_string = "Hello, tiny world!"
# substr = "Hell"



def kmp_algo(inp_string: str, substr: str) -> (int):
	"""
	Implementation of Knuth-Morrison-Pratt algorithm

	:param inp_string: String where substr is to be found (haystack)
	:param substr: substr to be found in inp_string (needle)
	:return: index where first occurrence of substr in inp_string started or None if not found
	"""

	def prefix_fun(substr: str) -> Sequence[int]:
		"""
		Prefix function for KMP

		:param prefix_str: dubstring for prefix function
		:return: prefix values table
		"""
		prefix_list = [0] * len(substr)
		for i in range(2, len(substr) + 1):
			sub_str = substr[:i]
			for j in range(1, len(sub_str)):
				prefix = sub_str[:j]
				suffix = sub_str[-j:]
				if prefix == suffix:
					prefix_list[i - 1] = j

		return prefix_list

	i = 0
	j = 0
	p = prefix_fun(substr)

	while i < len(inp_string):
		if inp_string[i] == substr[j]:
			i += 1
			j += 1
		if j == len(substr):
			return i - len(substr)
		elif inp_string[i] != substr[j]:
				if j == 0:
					i += 1
				elif j > 0:
					j = (p[j - 1])

	# print(inp_string, substr, prefix_fun)
		if substr not in inp_string:
			return None
	return -1


print(kmp_algo(inp_string, substr))


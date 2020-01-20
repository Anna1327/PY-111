from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""
	step_2 = 0
	step_1 = stairway[0]
	for step in range(1, len(stairway)):
		if step_2 + stairway[step] < step_1 + stairway[step]:
			step_2, step_1 = \
			step_1, step_2 + stairway[step]
		else:
			step_2, step_1 = \
			step_1, step_1 + stairway[step]

	return step_1

print(stairway_path([3, 4, 7, 8, 5, 2]))
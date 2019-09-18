
from mips.models import Lesson, Instruction



#Get the featured items that have been updated/created most recently.

def get_featured_lessons(max_items):
	all_lessons = Lesson.objects.order_by('-updated')
	featured_lessons = {}

	for index, lesson in enumerate(all_lessons):
		if index == max_items:
			break

		featured_lessons[lesson.lesson_name] = lesson.lesson_number

	return featured_lessons

def get_featured_instructions(max_items):
	all_instructions = Instruction.objects.order_by('-updated')
	featured_instructions = {} 	#add:add 

	for index, instruction in enumerate(all_instructions):
		if index == max_items:
			break

		featured_instructions[instruction.instruction_name] = instruction.instruction_name

	return featured_instructions






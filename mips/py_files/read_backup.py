

from mips.models import Instruction, InstructionParagraph, InstructionImage

from mips.models import Lesson, LessonParagraph, LessonParagraphImage, LessonNavigation

def read_backup_data(*args):
	backup_dict = {}


	print ("TESTING A BACKUP SYSTEM --> ")
	print ("Purpose is just to prevent complete data catastrophe.")

	#Find any backup instructions
	found_lines = read_lines("Instruction Data")
	instruction_data = interpret_instruction_lines(found_lines)
	clean_intruction_data(instruction_data)
	create_instruction_model_objects(instruction_data)

	#Find any backup lessons
	found_lines = read_lines("Lesson Data")
	lesson_data = interpret_lesson_lines(found_lines)
	clean_lesson_data(lesson_data)
	create_lesson_model_objects(lesson_data)


	return



def read_lines(data_type):
	if data_type == "Instruction Data":
		filepath = "mips/static/mips/backup_data/instruction_backup.txt"
	elif data_type == "Lesson Data":
		filepath = "mips/static/mips/backup_data/lesson_backup.txt"

	lines = []
	with open(filepath, "r+") as read_file:
		for line in read_file:
			#Check for the newline character.
			if "\n" == line[-1]:
				line = line[:-1]
				lines.append(line)
			else:
				lines.append(line)


	return lines


def interpret_instruction_lines(lines):

	#Name: Data
	instruction_data_dict = {}
	instruction_found = False
	instruction_name = ""
	instruction_data = []

	for line in lines:

		if len(line) > 6:
			#Chances are we have found a valid instruction.!
			if line[0:3] == "***" and line[-3:] == "***":
				instruction_found = True
				instruction_name = line[3:-3]
				continue					#Force a continue to prevent the line from being added to data

			elif line[0:3] == "###" and line[-3:] == "###":
				instruction_found = False
				
				instruction_data_dict[instruction_name] = instruction_data
				instruction_data = []

		if instruction_found:
			instruction_data.append(line)

	return instruction_data_dict

def clean_intruction_data(instruction_data_dict):
	for instruction_name, data in instruction_data_dict.items():
		new_data = []

		for line in data:
			if len(line) == 0:
				continue
			new_data.append(line)


		instruction_data_dict[instruction_name] = new_data

	return

def create_instruction_model_objects(instruction_data_dict):
	instruction_objs = []
	instruction_paragraphs = []
	instruction_images = []



	for instruction_name, data in instruction_data_dict.items():
		new_instruction = Instruction(instruction_name=instruction_name)
		instruction_objs.append(new_instruction)

		found_images = 0
		for index, line in enumerate(data):
			if len(line) > 2 and line[0:3] == "&&&":
				found_images += 1
				data = line[3:]

				split_line = data.split("=")
				ordering_index = int(split_line[0])
				filepath = split_line[1]
				new_image = InstructionImage(instruction=new_instruction, ordering=ordering_index, \
					filepath=filepath)

				instruction_images.append(new_image)
			else:
				ordering_index = index - found_images
				if "::" in line:
					split_line = line.split("::")
					paragraph_type = split_line[0]
					paragraph = split_line[1]
				else:
					paragraph = line
					paragraph_type = "Preface"

				new_paragraph = InstructionParagraph(paragraph=paragraph, ordering=ordering_index, \
					instruction=new_instruction, paragraph_type=paragraph_type)
				instruction_paragraphs.append(new_paragraph)


	#Check if the object already exists. If so don't re-create
	for instruction in instruction_objs:
		obj_found = check_obj_present("Instruction", instruction)
		if not obj_found:
			instruction.save()

	
	#Check if the object already exists. If so don't re-create
	for paragraph in instruction_paragraphs:
		obj_found = check_obj_present("InstructionParagraph", paragraph)
		if not obj_found:
			paragraph.save()

	#Check if the object already exists. If so don't re-create
	for image in instruction_images:
		obj_found = check_obj_present("InstructionImage", image)
		if not obj_found:
			image.save()


	return


#Check that an obj is present
def check_obj_present(model_string, obj):
	found = False
	if model_string == "Instruction":
		found_obj = Instruction.objects.filter(instruction_name=obj.instruction_name)
		if found_obj:
			found = True
	elif model_string == "InstructionParagraph":
		#Paragraphs may be similar and even have the same ordering!!
		found_obj = InstructionParagraph.objects.filter(instruction__instruction_name=obj.instruction.instruction_name, \
			paragraph=obj.paragraph, ordering=obj.ordering)
		if found_obj:
			found = True
		else:
			#Check that the Instruction obj. already exists or not
			found_instr = Instruction.objects.filter(instruction_name=obj.instruction.instruction_name)
			if found_instr:
				obj.instruction = found_instr.first()

	elif model_string == "InstructionImage":
		found_obj = InstructionImage.objects.filter(instruction__instruction_name=obj.instruction.instruction_name, \
			filepath = obj.filepath)
		if found_obj:
			found = True
		else:
			#Check wether the Instruction obj. already exists or not
			found_instr = Instruction.objects.filter(instruction_name=obj.instruction.instruction_name)
			if found_instr:
				obj.instruction = found_instr.first()

	return found



#lesson_dict = {Lesson Number = [data lines]}
def interpret_lesson_lines(found_lines):
	lesson_dict = {}

	found_lesson = False
	lesson_name = ""

	for line in found_lines:
		if len(line) > 6:
			if line[0:3] == "***" and line[-3:] == "***":
				found_lesson = True
				lesson_name = line[3:-3]
				data = []
				continue
			elif line[0:3] == "###" and line[-3:] == "###":
				found_lesson = False
				lesson_dict[lesson_name] = data
				continue
		
		data.append(line)


	return lesson_dict

def clean_lesson_data(lesson_data):

	for lesson_name, data in lesson_data.items():
		new_data = []

		for item in data:
			if len(item) != 0:
				if item[-1] == "\n":
					item = item[:-1]

				new_data.append(item)

		lesson_data[lesson_name] = new_data

	return



def create_lesson_model_objects(lesson_data):
	lesson_objs = []
	lesson_paragraphs = []
	lesson_paragraph_images = []
	lesson_navigations = []



	for lesson_name, data in lesson_data.items():

		split_name = lesson_name.split("=")
		str_number = split_name[-1]
		lesson_number = int(str_number)				#If it fails here I have a huge problem

		lesson_obj = Lesson(lesson_number=lesson_number)
		lesson_objs.append(lesson_obj)


		#Because the navigation + images are reliant on the lesson_paragraph 
		#paragraphs should appear before in the file

		#Nothing = paragraph
		#^^ = image
		#&& = navigation
		paragraph_counter = 0
		for index, line in enumerate(data):
			if len(line) > 2:
				if line[0:2] == "^^":
					#Associated to paragraph --> NOT ASSOCIATED WITH ORDERING
					#Number=Filepath
					line = line[2:]
					split_line = line.split("=")
					paragraph_order = int(split_line[0])
					filepath = split_line[-1]
					paragraph_obj = get_lesson_paragraph(lesson_obj, lesson_paragraphs, paragraph_order)
					lesson_image = LessonParagraphImage(lesson_paragraph=paragraph_obj, filepath=filepath)
					lesson_paragraph_images.append(lesson_image)
				elif line[0:2] == "&&":
					#Anchor Name, Anchor ID LessonParagraph
					line = line[2:]
					split_line = line.split("=")
					paragraph_order = int(split_line[0])
					anchor_name = split_line[1]
					anchor_id = split_line[2]
					paragraph_obj = get_lesson_paragraph(lesson_obj, lesson_paragraphs, paragraph_order)
					lesson_navigation = LessonNavigation(lessonParagraph=paragraph_obj, anchorName = anchor_name, \
						anchorID = anchor_id)

					lesson_navigations.append(lesson_navigation)

				elif line[0:2] == "@@":
					line = line[2:]
					lesson_obj.lesson_preface = line
				
				elif line[0:2] == "!!":
					line = line[2:]
					lesson_obj.lesson_name = line

				elif line[0:2] == "++":
					line = line[2:]
					lesson_obj.associated_file = line
				else:
					lesson_paragraph = LessonParagraph(lesson=lesson_obj, paragraph=line, \
						ordering=paragraph_counter)

					lesson_paragraphs.append(lesson_paragraph)
					paragraph_counter += 1
			
			#Default to a lesson_paragraph
			else:
				lesson_paragraph = LessonParagraph(lesson=lesson_obj, paragraph=line, \
						ordering=paragraph_counter)
				lesson_paragraphs.append(lesson_paragraph)
				paragraph_counter += 1


	#Check if the objects are already created in the database

	#Check if lesson already exists.
	for lesson_obj in lesson_objs:
		found = check_lesson_present("Lesson", lesson_obj)
		#If not found save it
		if not found:
			lesson_obj.save()


	#Check if lesson paragraph already exists.
	for lesson_paragraph in lesson_paragraphs:
		found = check_lesson_present("LessonParagraph", lesson_paragraph)
		#If not found save it
		if not found:
			lesson_paragraph.save()

	for lesson_paragraph_image in lesson_paragraph_images:
		found = check_lesson_present("LessonParagraphImage", lesson_paragraph_image)
		#If not found save it
		if not found:
			lesson_paragraph_image.save()

	for lesson_navigation in lesson_navigations:
		found = check_lesson_present("LessonNavigation", lesson_navigation)
		#If not found save it
		if not found:
			lesson_navigation.save()

	return



def check_lesson_present(model_string, obj):
	found = False

	if model_string == "Lesson":
		found_obj = Lesson.objects.filter(lesson_number=obj.lesson_number)
		if found_obj:
			found = True

	elif model_string == "LessonParagraph":		
		found_obj = LessonParagraph.objects.filter(lesson__lesson_number=obj.lesson.lesson_number, \
			paragraph = obj.paragraph, ordering = obj.ordering)

		if found_obj:
			found = True
		else:
			found_lesson = Lesson.objects.filter(lesson_number=obj.lesson.lesson_number)
			if found_lesson:
				lesson_obj = found_lesson.first()
				obj.lesson = lesson_obj
	
	elif model_string == "LessonParagraphImage":
		found_obj = LessonParagraphImage.objects.filter(lesson_paragraph__lesson__lesson_number = \
			obj.lesson_paragraph.lesson.lesson_number, filepath = obj.filepath)

		if found_obj:
			found = True
		else:
			found_paragraph = LessonParagraph.objects.filter(lesson__lesson_number = \
				obj.lesson_paragraph.lesson.lesson_number, paragraph = obj.lesson_paragraph.paragraph)

			if found_paragraph:
				paragraph_obj = found_paragraph.first()
				obj.lesson_paragraph = paragraph_obj


	elif model_string == "LessonNavigation":
		found_obj = LessonNavigation.objects.filter(anchorName=obj.anchorName, anchorID = obj.anchorID, \
			lessonParagraph__lesson__lesson_number=obj.lessonParagraph.lesson.lesson_number)

		if found_obj:
			found = True
		else:
			found_paragraph = LessonParagraph.objects.filter(lesson__lesson_number = \
				obj.lessonParagraph.lesson.lesson_number, paragraph = obj.lessonParagraph.paragraph)

			if found_paragraph:
				paragraph_obj = found_paragraph.first()
				obj.lessonParagraph = paragraph_obj

	return found


def get_lesson_paragraph(current_lesson, lesson_pargraphs, paragraph_order):
	target_paragraphs = []
	target_lesson_number = current_lesson.lesson_number
	for paragraph in lesson_pargraphs:
		if paragraph.lesson.lesson_number == target_lesson_number:
			target_paragraphs.append(paragraph)

	found_paragraph = None
	if paragraph_order < len(target_paragraphs):
		found_paragraph = target_paragraphs[paragraph_order]


	print (found_paragraph.paragraph)
	return found_paragraph
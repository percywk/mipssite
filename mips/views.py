from django.shortcuts import render, get_object_or_404
from django.views import View



from mips.py_files.read_backup import read_backup_data

#Import some models
from .models import Lesson, LessonParagraph, LessonParagraphImage, LessonNavigation
from .models import Instruction, InstructionParagraph, InstructionImage



# Create your views here.

#General home page.
def home(request):

	featured_lessons = {"Lesson 1": 1}
	featured_instructions = {"add": "add"}
	context = {
	"featured_lessons": featured_lessons,
	"featured_instructions": featured_instructions
	}
	return render(request, "mips/home.html", context)

#General about page.
def about(request):
	context = {}
	return render(request, "mips/about.html", context)

def instruction_list(request):
	instructions = Instruction.objects.all()
	instruction_names = []

	for instruction in instructions:
		instruction_names.append(instruction.instruction_name)
	

	context = {
	"instruction_names": instruction_names
	}
	return render(request, "mips/instruction-list.html", context)


def grab_instruction_data(instruction_name):
	paragraph_dict = {}
	image_dict = {}
	object_dict = {}

	#Query Instruction object
	instruction_obj = get_object_or_404(Instruction, instruction_name=instruction_name)

	#Query all related paragraphs
	instruction_paragraph_query = InstructionParagraph.objects.filter(instruction=instruction_obj)

	#Query all related images
	instruction_image_query = InstructionImage.objects.filter(instruction=instruction_obj)

	#paragraph_dict = {ordering: text}
	for instruction_paragraph in instruction_paragraph_query:
		paragraph_dict[instruction_paragraph.ordering] = instruction_paragraph.paragraph
		object_dict[instruction_paragraph.ordering] = instruction_paragraph

	#img_paragraph_dict = { ordering: filename}
	for instruction_image in instruction_image_query:
		image_dict[instruction_image.ordering] = instruction_image.filepath

	return paragraph_dict, image_dict, object_dict


def convert_ordered_dict_to_list(ordered_dict):
	resulting_list = []
	counter = 0
	while counter < len(ordered_dict.keys()):
		#Force a break and give nothing!
		if counter not in ordered_dict.keys():			
			break

		resulting_list.append(ordered_dict[counter])
		counter += 1

	return resulting_list

#Individual instructions --> Generic
def instruction(request, instruction_name='slug_not_found'):
	paragraph_dict, image_dict, object_dict = grab_instruction_data(instruction_name)
	instruction_paragraphs = convert_ordered_dict_to_list(paragraph_dict)
	paragraph_objects = convert_ordered_dict_to_list(object_dict)

	context = {
	"instruction_name": instruction_name,
	'instruction_paragraphs': instruction_paragraphs,
	'image_dict': image_dict,
	'paragraph_objects': paragraph_objects
	}
	return render(request, "mips/instruction-general.html", context)


#Listing of all assignments
def past_assignment_list(request):
	assignment_dict = {
	"hello-world": "Mutation of Hello World!",
	"multiplication": "Multiplication through shifts and adds",
	"add-arrays": "Adding arrays and outputing results with minor control flow",
	"2.1": "Basic algebra and user input.",
	"2.22": "Basic introduction to array operations and shifting.",
	"2.3": "Basic introduction to arrays"}
	context = {"assignment_dict": assignment_dict}
	return render(request, "mips/past-assignment-list.html", context)

def past_assignment(request, assignment_name="name_not_found"):
	context = {}
	filepath = "mips/static/mips/code/" + assignment_name + ".asm"

	if assignment_name == "name_not_found":
		context['assignment_name'] = "Assignment Not Found"
		context['file_contents'] = "File Not Found!"
	else:
		context['assignment_name'] = assignment_name
		with open(filepath, "r+") as readfile:
			file_data = readfile.read()
			context['file_contents'] = file_data
	
	return  render(request, "mips/past-assignment.html", context)

#This is something that I can do later.
def special_topics(request):
	context = {}
	return render(request, "mips/special-topics.html", context)

def lesson_list(request):
	#lesson_names = {"Lesson-1": 1}
	lesson_names = {}
	lesson_prefaces = {}
	lesson_objs = Lesson.objects.all()

	for lesson_obj in lesson_objs:
		lesson_name = lesson_obj.lesson_name
		lesson_num = lesson_obj.lesson_number
		lesson_preface = lesson_obj.lesson_preface

		if len(lesson_name) == 0:
			lesson_name = "Lesson " + str(lesson_num)

		lesson_names[lesson_name] = lesson_num

		if len(lesson_preface) > 0:
			lesson_prefaces[lesson_num] = lesson_preface

	context = {
	'lesson_names': lesson_names,
	'lesson_prefaces': lesson_prefaces
	}

	return render(request, "mips/lesson-list.html", context)

def get_lesson_data(lesson_number):
	#Get the intitial lesson
	lesson = get_object_or_404(Lesson, lesson_number=lesson_number)
	if lesson is None:
		return {}, {}, {}, {}

	#Get the paragraph & navigation & image information
	paragraph_dict = {}
	side_navigation_ids = {}
	side_navigation_names = {}
	img_paragraph_dict = {}

	paragraphs = LessonParagraph.objects.filter(lesson=lesson)
	for paragraph in paragraphs:
		text_data = paragraph.paragraph
		ordering = paragraph.ordering
		paragraph_dict[ordering] = text_data


		#Filter to the navigations
		navbar_information = LessonNavigation.objects.filter(lessonParagraph=paragraph)
		for navbar in navbar_information:
			anchor_id = navbar.anchorID
			anchor_name = navbar.anchorName
			associated_paragraph = navbar.lessonParagraph

			side_navigation_ids[ordering] = anchor_id
			side_navigation_names[ordering] = anchor_name 


		#Filter the images
		image_information = LessonParagraphImage.objects.filter(lesson_paragraph=paragraph)
		for lesson_paragraph_image in image_information:
			filepath = lesson_paragraph_image.filepath
			img_paragraph_dict[ordering] = filepath


	return paragraph_dict, side_navigation_ids, side_navigation_names, img_paragraph_dict


def grab_file_string(filepath):
	file_string = ""
	try:
		with open(filepath, "r+") as read_file:
			for line in read_file:
				file_string += line
	except FileNotFoundError:
		pass

	return file_string


def general_lesson(request, lesson_number):
	lesson_obj = get_object_or_404(Lesson, lesson_number=lesson_number)
	paragraph_dict, side_navigation_ids, side_navigation_names, img_paragraph_dict = get_lesson_data(lesson_number)

	#Convert dict to list format
	paragraph_list = convert_ordered_dict_to_list(paragraph_dict)

	#Get the lesson name
	lesson_name = lesson_obj.lesson_name

	#Get the preface data
	preface = lesson_obj.lesson_preface

	#Get the associated file
	associated_filepath = lesson_obj.associated_file
	if associated_filepath:
		associated_filepath = "mips/static/" + associated_filepath
		associated_file_data = grab_file_string(associated_filepath)
	else:
		associated_file_data = False

	#Get the lesson data
	main_content_img = lesson_obj.lesson_main_image
	
	context = {
	"lesson_number": lesson_number,
	"lesson_name": lesson_name,
	"preface": preface,
	"main_content_img": main_content_img,
	"article_paragraphs": paragraph_list,
	"img_paragraph_dict": img_paragraph_dict,
	"side_navigation_ids": side_navigation_ids,
	"side_navigation_names": side_navigation_names,
	"associated_file_data": associated_file_data
	}
	return render(request, "mips/lesson-general.html", context)



def outside_projects(request):
	context = {}
	return render(request, "mips/outside-projects.html", context)
'''
Want to write a lesson on basic loops and basic functions
Title should just be jumping. Or some shit
Need to push lesson=3 down to lesson=4


Want a custom command that checks file links are correctly associated to a models. -->
At the very least thsoe things exist



Would like some model methods though I am not sure what I want/need
'''



'''
Error Handling stuff....
'''
def handler403(request, *args, **argv):
	context = {}
	return render(request, "error-handling/403.html", context)

def handler404(request, *args, **argv):
	context = {}
	return render(request, "error-handling/404.html", context)

def handler500(request, *args, **argv):
	context = {}
	return render(request, "error-handling/404.html", context)

def handler503(request, *args, **argv):
	context = {}
	return render(request, "error-handling/404.html", context)

def handler504(request, *args, **argv):
	context = {}
	return render(request, "error-handling/404.html", context)
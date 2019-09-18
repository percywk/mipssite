from django.db import models

# Create your models here.

'''
Need extra meta-data for lesson definitions
'''
class Lesson(models.Model):
	lesson_number = models.IntegerField(primary_key=True)
	lesson_preface = models.TextField(default="")
	lesson_name = models.CharField(max_length=50, default="")
	lesson_main_image = models.CharField(max_length=150, default="")
	associated_file = models.CharField(max_length=150, blank=True)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, blank=True)
	
	class Meta:
		verbose_name = "Lesson"
		verbose_name_plural = "Lessons"

class LessonParagraph(models.Model):
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
	paragraph = models.TextField()
	ordering = models.IntegerField(default=0)

	class Meta:
		verbose_name = "Lesson Paragraph"
		verbose_name_plural = "Lesson Paragraphs"


class LessonParagraphImage(models.Model):
	lesson_paragraph = models.ForeignKey(LessonParagraph, on_delete=models.CASCADE)
	filepath = models.CharField(max_length=150)

	class Meta:
		verbose_name = "Lesson Paragraph Image"
		verbose_name_plural = "Lesson Paragraph Images"

class LessonNavigation(models.Model):
	anchorName = models.CharField(max_length = 75)
	anchorID = models.CharField(max_length = 75) 
	lessonParagraph = models.ForeignKey(LessonParagraph, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name = "Lesson Navigation"
		verbose_name_plural = "Lesson Navigations"








'''
Instructions should be shorter therefore the Foreign Key's can reference the Instruction itself.
They may include images to clarify concepts.
'''

class Instruction(models.Model):
	instruction_id = models.AutoField(primary_key=True)			#Auto increments (identity(1,1))
	instruction_name = models.CharField(max_length=75, unique=True)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name = "Instruction"
		verbose_name_plural = "Instructions"




class InstructionParagraph(models.Model):
	instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
	paragraph = models.TextField()

	paragraph_types = [('Preface', 'Preface'), ('Syntax', 'Syntax'), ('Example', 'Example'), ('Result', 'Result')]
	paragraph_type = models.CharField(max_length =50, choices=paragraph_types, default='Preface')

	ordering = models.IntegerField(default=0)

	class Meta:
		verbose_name = "Instruction Paragraph"
		verbose_name_plural = "Instruction Paragraphs"


class InstructionImage(models.Model):
	instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
	filepath = models.CharField(max_length=150)
	ordering = models.IntegerField(default=0)

	class Meta:
		verbose_name = "Instruction Image"
		verbose_name_plural = "Instruction Images"
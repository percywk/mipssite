from django.contrib import admin

# Register your models here.

from .models import Lesson, LessonParagraph, LessonParagraphImage, LessonNavigation

from .models import Instruction, InstructionParagraph, InstructionImage




admin.site.register(Lesson)
admin.site.register(LessonParagraph)
admin.site.register(LessonParagraphImage)
admin.site.register(LessonNavigation)

admin.site.register(Instruction)
admin.site.register(InstructionParagraph)
admin.site.register(InstructionImage)
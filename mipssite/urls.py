"""mipssite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mips.views import home, about, instruction, instruction_list, past_assignment_list, past_assignment

from mips.views import special_topics, lesson_list, general_lesson, outside_projects

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about', about, name="about"),
    path('instructions/', instruction_list, name="instruction-list"),
    path('instruction/<str:instruction_name>', instruction, name="instruction"),
    path('past-assignments/', past_assignment_list, name="past-assignment-list"),
    path('past-assignment/<str:assignment_name>', past_assignment, name="past-assignment"),
    path('special-topics/', special_topics, name="special-topics"),
    path('lesson-list/', lesson_list, name='lesson-list'),
    path('lesson/<int:lesson_number>', general_lesson, name="general_lesson"),
    path('outside-projects/', outside_projects, name="outside-projects")

]

handler403 = 'mips.views.handler403'
handler404 = 'mips.views.handler404'
handler500 = 'mips.views.handler500'
handler503 = 'mips.views.handler503'
handler504 = 'mips.views.handler504'
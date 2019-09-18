
from django.core.management.base import BaseCommand, CommandError


'''
The purpose of this is to create a command to test if filepaths are correct

https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/
'''

from mips.py_files.filepath_checker import call_filepath_checker_functions


class Command(BaseCommand):
	help = "Used to check how calls interact with cloud services"

	def handle(self, *args, **options):
		self.stdout.write("Checking filepaths")

		call_filepath_checker_functions()
		return
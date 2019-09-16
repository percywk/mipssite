from django.core.management.base import BaseCommand, CommandError



'''
The purpose of this is to handle anything that I need with a manual command

https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/
'''


from mips.py_files.read_backup import read_backup_data


class Command(BaseCommand):
	help = "Used to check the integrity of the database to saved model objects."

	#Isn't necessary if I don't want to add any arguments
	#def add_arguments(self, parser):
	#	parser.add_argument()

	def handle(self, *args, **options):

		backup_dict = read_backup_data()

		return


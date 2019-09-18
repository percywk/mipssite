from django.core.management.base import BaseCommand, CommandError


'''
The purpose of this is to test using a management command on Cloud services.
Want to see how they interact with bash prompts and such.

https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/
'''


class Command(BaseCommand):
	help = "Used to check how calls interact with cloud services"

	def handle(self, *args, **options):
		self.stdout.write("Command successfully recieved!")

		return

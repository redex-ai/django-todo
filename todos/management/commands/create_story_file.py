import os
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Generate a 300-character spy story file in the story directory within STATICFILES_DIRS'

    def handle(self, *args, **kwargs):
        story_content = 'In the shadows of the cold war, a lone spy exchanged briefcases with an unseen figure. Codes to dismantle the network were hidden within. With a glance over the shoulder, the spy vanished into the mist, leaving no trace.'
        story_dir = os.path.join(settings.STATICFILES_DIRS[0], 'story')
        os.makedirs(story_dir, exist_ok=True)
        file_path = os.path.join(story_dir, 'abc.txt')

        with open(file_path, 'w') as file:
            file.write(story_content[:300])

        self.stdout.write(self.style.SUCCESS('Successfully created spy story file at {}'.format(file_path)))

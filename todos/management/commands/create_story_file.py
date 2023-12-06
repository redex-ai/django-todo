import os
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Generate a 300-character story file in the story directory within STATICFILES_DIRS'

    def handle(self, *args, **kwargs):
        story_content = 'Once upon a time, in a land far, far away, there lived a wise old owl. The owl watched over the forest day and night. Its wisdom was sought after by all the creatures, big and small. This story is a tribute to the owl's wisdom and the magic of the enchanted forest.'
        story_dir = os.path.join(settings.STATICFILES_DIRS[0], 'story')
        os.makedirs(story_dir, exist_ok=True)
        file_path = os.path.join(story_dir, 'abc.txt')

        with open(file_path, 'w') as file:
            file.write(story_content[:300])

        self.stdout.write(self.style.SUCCESS('Successfully created story file at {}'.format(file_path)))

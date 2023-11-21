{
  "codeChangeList": [
    {
      "filePath": "todos/models.py",
      "code": 
      "```\nfrom django.db import models\n\nclass Todo(models.Model):\n    title = models.CharField(max_length=100)\n    body = models.TextField(blank=True, null=True)\n    created_at = models.DateTimeField('Created', auto_now_add=True)\n    update_at = models.DateTimeField('Updated', auto_now=True)\n    isCompleted = models.BooleanField(default=False)\n\n    def __str__(self):\n        return self.title\n```\n"
    }
  ]
}

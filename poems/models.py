from django.db import models
from .clean import run

# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=15)
    paragraphs = models.TextField()

    @classmethod
    def populate(cls):
        all_poems = run() # 获取所有的诗词
        cls.objects.all().delete() # 删除之前的
        # 填充诗词
        cls.objects.bulk_create([
            cls(
                title=title,
                author=author,
                paragraphs=paragraphs,
            )
            for title, author, paragraphs in all_poems
        ])

    def __str__(self):
        return self.title
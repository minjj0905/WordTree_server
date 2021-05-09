from django.db import models

class Threequiz(models.Model):
    tag = models.IntegerField(null=False)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="word/photo_3")

    def dic(self):
        fields = ['tag', 'name', 'photo']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

class Fourquiz(models.Model):
    tag = models.IntegerField(null=False)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="word/photo_4")

    def dic(self):
        fields = ['tag', 'name', 'photo']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

class Fivequiz(models.Model):
    tag = models.IntegerField(null=False)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="word/photo_5")

    def dic(self):
        fields = ['tag', 'name', 'photo']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result
from django.db import models

'''
Our project model will show recent projects I have worked on on the homepage
each project model will have a title and brief summary
'''
class Project(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    summary = models.CharField(max_length = 300)
    url = models.TextField()

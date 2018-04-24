from django.db import models

'''
Our project model will display recent projects I have worked on
each project model will have a title and a brief summary along with a button that
takes you the github repository with source code.
'''
class Project(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    summary = models.CharField(max_length = 300)
    url = models.TextField()

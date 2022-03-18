from django.db import models
from branch.models import Branch
from ecommerce.ecommerce.courses.models import Course
# Create your models here.

class BranchCourse(models.Model):
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.PROTECT)

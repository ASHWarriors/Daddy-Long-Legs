# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:57:27 2021

@author: Sristi
"""

from django.db import models

# Create your models here.

class student(models.Model):
    
	st_name =models.CharField(max_length=40)
	st_grade=models.CharField(max_length=40)
	st_sub  =models.CharField(max_length=40)
	
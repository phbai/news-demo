from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=255)
	timestamp = models.DateTimeField()

	def __unicode__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=255)
	desciption = models.TextField()
	logo = models.CharField(max_length=255)
	timestamp = models.DateTimeField()

	def __unicode__(self):
		return self.name


class News(models.Model):
	title = models.CharField(max_length=255)
	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	summary = models.CharField(max_length=255)
	content = RichTextField()
	click_num = models.IntegerField()
	poster = models.CharField(max_length=255)
	timestamp = models.DateTimeField()

	def __unicode__(self):
		return self.title



class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'timestamp',)

class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'click_num', 'timestamp')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'desciption', 'timestamp')

admin.site.register(User, UserAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
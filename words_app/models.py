from django.db import models

class News(models.Model):
	news_id=models.CharField(max_length=15)
	def __str__(self):
		return self.news_id

class Project(models.Model):
	def crear(self):
		for i in range(22):
            		news=News(news_id='reut2-00'+str(i)+'.sgm')
            		news.save()
		return 'Se crearon las visualizaciones para las noticias'

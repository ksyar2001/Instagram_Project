from django.test import TestCase
from web_scrape import *
from watson.WatsonAPI import *
from models import *
import datetime
from CSVWriter import CSVWriter
from output import *

class TestWatson(TestCase):

	def test_watson(self):
		web_scrape(username="mrbookieboo")
		# comments = ""
	
		print( generatePhotoCSV( username="mrbookieboo" ) )

		for photo in InstagramAccount.objects.get(username="mrbookieboo").photo.all():
			csv = CSVWriter()
			"=============================="
			print photo.pk
			print photo.comments.all().count()
			print photo.likes
			print photo.tag.all().count()
			print ( photo.time )
			
			list = []
			list.append( photo.pk )
			list.append( photo.comments.all().count() )
			list.append( photo.likes )
			list.append( photo.tag.all().count() )
			
			list.append( photo.time )

			csv.writeRow( list )

			print( csv.output.getvalue() )

			csv.close()


		# for photo in account.photo:
		# 	for comment in photo.comments:
		# 		comments += comment

		# print comments

		# print json.dumps(WatsonAPI().getToneAnalysis(comments), indent=2)





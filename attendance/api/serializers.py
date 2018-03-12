from rest_framework import serializers

from attendance.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
	 class meta:
	 	model = BlogPost
	 	fields = [
	 		'pk',
	 		'user',
	 		'title',
	 		'content',
	 		'timestamp',
	 	]
	 		
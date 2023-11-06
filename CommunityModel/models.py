from django.db import models

from UserModel.models import User


"""
Model representing a video.

Fields:
- video_name: The name of the video, with a maximum length of 50 characters.
- url: The URL of the video, with a maximum length of 200 characters.
- introduction: A brief introduction about the video, with a maximum length of 100 characters.
- likes: The number of likes this video has received.
- sucks: The number of dislikes or negative reactions to this video.
"""
class Video(models.Model):
    video_name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    introduction = models.TextField(max_length=100)
    likes = models.IntegerField()
    sucks = models.IntegerField()


"""
Model representing a post.

Fields:
- title: The title of the post, with a maximum length of 50 characters.
- user: The user who created the post.
- created_at: The date and time the post was created.
- content: The content of the post, with a maximum length of 1000 characters.
"""
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    content = models.TextField(max_length=1000)


"""
Model representing a comment on a post.

Fields:
- user: The user who wrote the comment.
- post: The post to which the comment is associated.
- created_at: The date and time the comment was created.
- content: The content of the comment, with a maximum length of 100 characters.
"""
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    content = models.CharField(max_length=100)


"""
Model representing a reply to a comment.

Fields:
- comment: The comment to which the reply is associated.
- author: The user who wrote the reply.
- content: The content of the reply, with a maximum length of 100 characters.
- created_at: The date and time the reply was created.
"""
class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)



from django.db import models



class Post(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    if_edited = models.BooleanField(default=False)
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='user',
        help_text='Post associated with the user'
                )

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('posts:post_detail', args=[str(self.id)])


class Comment(models.Model):

    content = models.TextField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    Post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        related_name='comments_post',
        null=False
    )
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='comments_user',
        help_text='Post associated with the user',
        null=False
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.content
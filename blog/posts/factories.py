import factory.fuzzy
from .models import Post, Comment
from factory.faker import Faker

class PostsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    title = factory.Faker('sentence')
    text = factory.Faker('text', max_nb_chars=250)
    pub_date = factory.Faker('date_time_this_year')
    if_edited = factory.Faker('boolean')
    user = factory.SubFactory('user.factories.UserFactory')

class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    content = factory.Faker('text', max_nb_chars=250)
    pub_date = factory.Faker('date_time_this_year')
    Post = factory.SubFactory(PostsFactory)
    user = factory.SubFactory('user.factories.UserFactory')
    parent = factory.Maybe(
        factory.Faker('boolean'),
        factory.SubFactory('posts.factories.CommentFactory'),
        None
    )
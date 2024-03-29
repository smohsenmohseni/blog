# Generated by Django 3.2 on 2022-12-20 09:26

# Core imports.
import django.db.models.deletion
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                (
                    'parent',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='children',
                        related_query_name='children',
                        to='blog.category',
                        verbose_name='Parent',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Content')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('publish_time', models.DateTimeField(db_index=True, verbose_name='Publish at')),
                ('draft', models.BooleanField(db_index=True, default=True, verbose_name='Draft')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/images/', verbose_name='image')),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='posts',
                        related_query_name='children',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Author',
                    ),
                ),
                (
                    'category',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='posts',
                        related_query_name='posts',
                        to='blog.category',
                        verbose_name='Category',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-publish_time'],
            },
        ),
        migrations.CreateModel(
            name='PostSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.BooleanField(default=True, verbose_name='comment')),
                ('author', models.BooleanField(default=False, verbose_name='author')),
                ('allow_discussion', models.BooleanField(default=False, verbose_name='allow discussion')),
                (
                    'post',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='setting',
                        related_query_name='setting',
                        to='blog.post',
                        verbose_name='post',
                    ),
                ),
            ],
            options={
                'verbose_name': 'PostSetting',
                'verbose_name_plural': 'PostSettings',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('is_confirmed', models.BooleanField(default=True, verbose_name='confirm')),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'
                    ),
                ),
                (
                    'parent',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='children',
                        related_query_name='child',
                        to='blog.comment',
                        verbose_name='parent',
                    ),
                ),
                (
                    'post',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comments',
                        related_query_name='comments',
                        to='blog.post',
                        verbose_name='Post',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.BooleanField(verbose_name='Condition')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'
                    ),
                ),
                (
                    'comment',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comment_like',
                        related_query_name='comment_like',
                        to='blog.comment',
                        verbose_name='Comment',
                    ),
                ),
            ],
            options={
                'verbose_name': 'CommentLike',
                'verbose_name_plural': 'CommentLikes',
                'unique_together': {('author', 'comment')},
            },
        ),
    ]

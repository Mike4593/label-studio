from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_previous_migration'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_status', models.CharField(
                    choices=[
                        ('PENDING', 'Pending Review'),
                        ('ACCEPTED', 'Accepted'),
                        ('REJECTED', 'Rejected'),
                        ('MODIFIED_AND_ACCEPTED', 'Modified and Accepted'),
                    ],
                    default='PENDING',
                    help_text='Current review status',
                    max_length=25,
                )),
                ('submitted_at', models.DateTimeField(blank=True, help_text='When task was submitted for review', null=True)),
                ('reviewed_at', models.DateTimeField(blank=True, help_text='When reviewer took action', null=True)),
                ('rejection_reason', models.TextField(blank=True, default='', help_text='Reason for rejection if applicable')),
                ('review_notes', models.TextField(blank=True, default='', help_text='Reviewer notes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(help_text='Reviewer assigned to this task', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_reviews', to=settings.AUTH_USER_MODEL)),
                ('original_annotator', models.ForeignKey(help_text='Original annotator who submitted the task', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='annotator_tasks_under_review', to=settings.AUTH_USER_MODEL)),
                ('task', models.OneToOneField(help_text='Task being reviewed', on_delete=django.db.models.deletion.CASCADE, related_name='review', to='tasks.task')),
            ],
            options={
                'verbose_name': 'Task Review',
                'verbose_name_plural': 'Task Reviews',
            },
        ),
        migrations.AddIndex(
            model_name='taskreview',
            index=models.Index(fields=['review_status'], name='tasks_task_review_status_idx'),
        ),
        migrations.AddIndex(
            model_name='taskreview',
            index=models.Index(fields=['assigned_to', 'review_status'], name='tasks_assigned_status_idx'),
        ),
        migrations.AddIndex(
            model_name='taskreview',
            index=models.Index(fields=['task', 'review_status'], name='tasks_task_status_idx'),
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_previous_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmember',
            name='role',
            field=models.CharField(
                choices=[('ANNOTATOR', 'Annotator'), ('REVIEWER', 'Reviewer')],
                default='ANNOTATOR',
                help_text='User role in the project (ANNOTATOR or REVIEWER)',
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='user',
            field=models.ForeignKey(
                help_text='User ID',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='project_memberships',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name='projectmember',
            unique_together={('user', 'project')},
        ),
        migrations.AddIndex(
            model_name='projectmember',
            index=models.Index(fields=['project', 'role'], name='projects_pr_project_role_idx'),
        ),
    ]

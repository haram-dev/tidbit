from django.db import models, connection


class Course(models.Model):
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))

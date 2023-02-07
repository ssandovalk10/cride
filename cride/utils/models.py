from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base Model.

    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text= 'Date Time on which the object was created.'

    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text= 'Date Time on which the object las modifed.'
        
    )

    class Meta:
        """Meta Option"""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
"""
class Student(CRideModel):
    name = models.CharField()

    class Meta(CRideModel.Meta):
        db_table='student_role'"""

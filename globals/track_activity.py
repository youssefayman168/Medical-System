from celery import shared_task
from activity.models import Activity

@shared_task
def track_activity(description, made_by):
    try:
        Activity.objects.create(
                content=description,
                made_by=made_by
            )
    except Exception as e:
        print("ERROR OCCURRED WHILE TRACKING ACTIVITY!", e)
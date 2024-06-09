from celery import shared_task
from activity.models import Activity
from users.models import User

@shared_task
def track_activity(description, username):
    try:
        made_by = User.objects.get(username=username)
    except User.DoesNotExist:
        print("USER DOESN't EXISTS")
    try:
        Activity.objects.create(
                content=description,
                made_by=made_by
            )
    except Exception as e:
        print("ERROR OCCURRED WHILE TRACKING ACTIVITY!", e)
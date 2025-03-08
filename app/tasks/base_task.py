from celery import shared_task


@shared_task
def base_task(params):
    print(f"Base task with params: {params}")

from celery import shared_task

from .utils import formatter, summarizer


@shared_task(ignore_result=True)
def process():

	print formatter.remove_noise('What are you doing My name is Rahul I am very traditional')
from celery import shared_task


@shared_task(ignore_result=True)
def scrape(scraper):

	print 'Task completed'
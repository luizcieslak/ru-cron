if __name__ == '__main__':
    from apscheduler.schedulers.blocking import BlockingScheduler
    sched = BlockingScheduler()
    import requests

# CRON key registered on Firebase Functions server.
F = open('cron.key.txt','r')
cron_key = F.read()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')
        # Run the http request
    payload={'key': cron_key, 'rid': 0}
    res = requests.get('http://localhost:5000/unespru/us-central1/test', params=payload)
    print(res.text)

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=13)
def scheduled_job():
    print('This job is run every weekday at 1pm.')
    # Run the http request
    payload={'key': cron_key, 'rid': 0}
    res = requests.get('http://localhost:5000/unespru/us-central1/queueCleanup', params=payload)
    print(res.text)

sched.start()


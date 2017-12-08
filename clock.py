if __name__ == '__main__':
    from apscheduler.schedulers.blocking import BlockingScheduler
    sched = BlockingScheduler()
    import requests

# CRON key registered on Firebase Functions server.
F = open('cron.key.txt','r')
cron_key = F.read()

# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')
    # Run the http request
    # res = requests.get('https://us-central1-unespru.cloudfunctions.net/test')
    # print(res.text)

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=15)
def scheduled_job():
    print('This job is run every weekday at 1pm.')
    # Run the http request
    payload={'key': cron_key, 'rid': 0}
    res = requests.get('https://us-central1-unespru.cloudfunctions.net/queueCleanup', params=payload)
    print(res.text)

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=12)
def scheduled_job():
    print('This job is run every weekday at 10am.')
    # Run the http request
    payload={'key': cron_key}
    res = requests.get('https://us-central1-unespru.cloudfunctions.net/oneHourBefore', params=payload)
    print(res.text)
sched.start()


if __name__ == '__main__':
    from apscheduler.schedulers.blocking import BlockingScheduler
    sched = BlockingScheduler()
    import requests

# CRON key registered on Firebase Functions server.
F = open('cron.key.txt','r')
cron_key = F.read()

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=2)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=13)
def scheduled_job():
    print('This job is run every weekday at 1pm.')
    # Run the http request
    payload={'key': cron_key, 'rid': 0}
    res = requests.get('http://localhost:5000/unespru/us-central1/queueCleanup', params=payload)
    print(res.text)
    

sched.start()

# Server key of Firebase
f = open('server.key.txt','r')
server_key = f.read()

# FCM notifications functions
def sendToTopic(topic, title, message, data):
        payload = {'to': '/topics/'+topic, 'notification': { 'title': title, 'body': message}, 'data': data}
        headers = {'Authorization': 'key='+ server_key}
        res = requests.post('https://fcm.googleapis.com/fcm/send', json=payload, headers=headers)
        return res.text

def sendToDevice(device, title, message, data):
        payload = {'to': device, 'notification': { 'title': title, 'body': message}, 'data': data}
        headers = {'Authorization': 'key='+ server_key}
        res = requests.post('https://fcm.googleapis.com/fcm/send', json=payload, headers=headers)
        return res.text
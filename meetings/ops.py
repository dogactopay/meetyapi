from datetime import datetime

from meetings.models import Meetings
from users.models import Users


def dateStr2Date(x):
    datetimeObj = datetime.strptime(x, '%Y-%m-%dT%H:%M')
    return (datetimeObj)


def duration(x, y):
    return round(float(str((x - y)/3600).split(":")[2]))


def check_availabilty(request):
    data = (request.data).dict()
    start_date = (dateStr2Date(data['start_date']))
    end_date = (dateStr2Date(data['end_date']))

    avas = []
    for user in request.data.getlist("user"):

        user_instance = Users.objects.get(pk=user[0])

        meeting = list(Meetings.objects.filter(
            user=user_instance).filter(end_date__gte=start_date).values())

        if len(meeting) == 0:
            avas.append(True)
        else:
            avas.append(False)

    if False in avas:
        return False
    else:
        return True

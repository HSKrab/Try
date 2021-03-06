import requests
import time
import datetime


class Command:
    def __init__(self, gatewayId, API_key, format='yyyy/MM/dd HH:mm:ss', TimeLanguage='ja-JP', offset='9:00:00') -> None:
        self.id = gatewayId
        self.key = API_key
        self.headers = {'X-Pushlog-API-Key': self.key,
                        'Content-type': 'application/json'}
        self.endpoint = 'https://api.pushlog.jp/v3/gateways/'
        self.offset_pass = '?dateTimeFormat='+format + \
            '&dateTimeLanguage='+TimeLanguage+'&dateTimeOffset='+offset

    def allfirmwareVersion(self):
        return requests.get(url=self.endpoint, headers=self.headers).json()

    def firmwareVersion(self):
        self.endpoint += self.id
        return requests.get(url=self.endpoint, headers=self.headers).json()

    def status(self):
        self.endpoint += self.id+'/status' + self.offset_pass
        return requests.get(url=self.endpoint, headers=self.headers).json()

    def normaltriggers(self):
        self.endpoint += self.id+'/config/normal_triggers'
        return requests.get(url=self.endpoint, headers=self.headers).json()

    def realtime(self):
        self.endpoint += self.id+'/realtime/normal' + self.offset_pass
        return requests.get(url=self.endpoint, headers=self.headers).json()

    def historical(self, start=(), end=(), id=[]):
        Ids, startTime, endTime = '', '', ''
        if id:
            Ids = '&triggerIds='+','.join([str(i) for i in id])

        keys = ['year', 'month', 'day', 'hour', 'minute', 'second']
        if start:
            startTime = datetime.datetime(
                **{key: val for key, val in zip(keys, start)})
            startTime = '&from='+str(int(time.mktime(startTime.timetuple())))

        if end:
            endTime = datetime.datetime(
                **{key: val for key, val in zip(keys, end)})
            endTime = '&to='+str(int(time.mktime(endTime.timetuple())))

        self.endpoint += self.id+'/historical' + \
            self.offset_pass + Ids+startTime+endTime
        return requests.get(url=self.endpoint, headers=self.headers).json()

    def alarmstatus(self):
        self.endpoint += self.id+'/user_alarm/statuses' + self.offset_pass
        return requests.get(url=self.endpoint, headers=self.headers).json()

    def alarmhistories(self):
        self.endpoint += self.id+'/user_alarm/histories'+self.offset_pass
        return requests.get(url=self.endpoint, headers=self.headers).json()

    def writedevice(self, deviceId, val):
        self.endpoint += self.id+'/write_device'
        params = {'deviceId': deviceId, 'value': str(val)}
        return requests.post(url=self.endpoint, headers=self.headers, json=params).json()

    def writedeviceid(self, requestId):
        self.endpoint += self.id+'/write_device/'+requestId
        return requests.get(url=self.endpoint, headers=self.headers).json()

    def weboutput(self, params):
        self.endpoint += self.id+'/web_output'
        return requests.post(url=self.endpoint, headers=self.headers, json=params).json()

    def weboutputid(self, requestId):
        self.endpoint += self.id+'/web_output/'+requestId
        return requests.get(url=self.endpoint, headers=self.headers).json()

    def webtrigger(self, triggerId):
        self.endpoint += self.id+'/web_trigger'
        params = {'triggerId': triggerId}
        return requests.post(url=self.endpoint, headers=self.headers, json=params).json()

    def webtriggerid(self, requestId):
        self.endpoint += self.id+'/web_trigger/'+requestId
        return requests.get(url=self.endpoint, headers=self.headers).json()


######################################## ????????????????????? ########################################
# gatewayId(15??????????????????????????????)????????? '' ?????????????????????????????????
gatewayId = ''

# GUGEN?????????????????????????????????(32???????????????????????????????????????)????????? '' ?????????????????????????????????
API_key = ''

# ??????????????????????????????
info = Command(gatewayId, API_key)
print(info.xxxxx())  # ??????????????????????????????????????????????????????????????????????????????????????????

######################################## ?????????????????? ########################################

# ????????????: print(info.xxxxx())
# PUSHLOG???????????????????????????????????????xxxxx??????????????????????????????????????????????????????????????????????????????????????????
# allfirmwareVersion: ????????????????????????????????????????????????
# firmwareVersion: ??????????????????????????????????????????????????????
# status: ?????????????????????????????????????????????????????????
# normaltriggers: ????????????????????????????????????
# realtime: ???????????????????????????????????????????????????????????????????????????
# alarmstatus: ???????????????????????????????????????????????????
# alarmhistories: ??????????????????????????? ???????????????
# ???: ?????????????????????????????????????????????????????????????????????
# print(info.status())

#===================================================================================#

# ????????????????????????????????????
# ??????????????????????????????????????????????????????xxxxx???historical??????????????????????????????????????????????????????
# 2021???10???5??????7???30???45?????????????????????9???10???0????????????triggerId 15?????????????????????????????????????????????
# print(info.historical(start=(2021, 10, 5, 7, 30, 45),end=(2021, 10, 6, 21, 10, 0), id=[15]))
# ????????????????????????triggerId 15???16???17???20 ?????????????????????????????????????????????
# print(info.historical(start=(2021, 10, 5, 7, 30, 45),end=(2021, 10, 6, 21, 10, 0), id=[15,16,17,20]))

# ????????????????????? start, end, id ???????????????????????????????????????????????????API??????.pdf?????????????????????????????????
# ???: 1???????????????????????????????????????????????????(????????????????????????????????????????????????????????????)????????????triggerId?????????????????????????????????????????????
# print(info.historical())

#===================================================================================#

# ?????????????????????????????????Web?????????Web?????????
# deviceId 6 ?????????????????? 50 ?????????????????????
# print(info.writedevice(deviceId=6, val=50))
# ?????????requestId?????????????????????????????? requestId= ??????????????????????????????????????????????????????????????????????????????
# print(info.writedeviceid(requestId='PlcWrite_(gatewayId)_xxxxxxxxxx'))

# ??????????????????1??????ON???????????????
# print(info.weboutput(params=[{'terminal': 1, 'status': True}])
# ??????????????????1???ON???2???OFF???????????????
# print(info.weboutput(params=[{'terminal': 1, 'status': True}, {'terminal': 2, 'status': False}]))
# ?????????requestId?????????????????????????????? requestId= ??????????????????????????????????????????????????????????????????????????????
# print(info.weboutputid(requestId='WebOutput_(gatewayId)_xxxxxxxxxx'))

# triggerId 20 ??????????????????????????????????????????
# print(info.webtrigger(triggerId=20))
# ?????????requestId?????????????????????????????? requestId= ??????????????????????????????????????????????????????????????????????????????
# print(info.webtriggerid(requestId='WebTrigger_(gatewayId)_xxxxxxxxxx'))

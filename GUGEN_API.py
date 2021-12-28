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


######################################## 実⾏プログラム ########################################
# gatewayId(15桁数字、ハイフン無し)を下の '' の中に入力してください
gatewayId = ''

# GUGENが発行したアクセスキー(32桁小文字と数字の組み合わせ)を下の '' の中に入力してください
API_key = ''

# 情報を取得してみよう
info = Command(gatewayId, API_key)
print(info.xxxxx())  # このコマンドは、下のコマンド説明に従って修正たら実行できます

######################################## コマンド説明 ########################################

# 基本命令: print(info.xxxxx())
# PUSHLOGに関する情報は、基本命令のxxxxxを以下の英語単語でかけがえれば、それぞれの情報を取得できます
# allfirmwareVersion: ゲートウェイの基本情報を一括取得
# firmwareVersion: 指定したゲートウェイの基本情報を取得
# status: 指定したゲートウェイのステータスを取得
# normaltriggers: 通常トリガ設定情報を取得
# realtime: 通常トリガのリアルタイムデータ（収集データ）を取得
# alarmstatus: ユーザアラームステータス一覧を取得
# alarmhistories: ユーザアラーム履歴 一覧を取得
# 例: 指定したゲートウェイのステータスを取得する場合
# print(info.status())

#===================================================================================#

# ヒストリカルデータの取得
# ヒストリカルデータの取得の場合、まずxxxxxをhistoricalで転換し、下の例を参考してください。
# 2021年10月5日朝7時30分45秒から、翌日夜9時10分0秒まで、triggerId 15が記録したデータを取得する場合
# print(info.historical(start=(2021, 10, 5, 7, 30, 45),end=(2021, 10, 6, 21, 10, 0), id=[15]))
# 同じ時間帯、複数triggerId 15と16と17と20 が記録したデータを取得する場合
# print(info.historical(start=(2021, 10, 5, 7, 30, 45),end=(2021, 10, 6, 21, 10, 0), id=[15,16,17,20]))

# 三つパラメータ start, end, id それぞれを省略しても取得できます。API仕様.pdfの説明をご参考ください
# 例: 1日前から、現在時刻まで、通常トリガ(オプションライセンスなら高速トリガも含め)の全てのtriggerIdが記録したデータを取得する場合
# print(info.historical())

#===================================================================================#

# 遠隔デバイス書き込み、Web出力、Webトリガ
# deviceId 6 のデバイスに 50 を書き込む場合
# print(info.writedevice(deviceId=6, val=50))
# 出力のrequestIdをコピーして、以下の requestId= の後ろに貼り付けることで、要求処理状態を確認できます
# print(info.writedeviceid(requestId='PlcWrite_(gatewayId)_xxxxxxxxxx'))

# 外部出力端子1だけONにする場合
# print(info.weboutput(params=[{'terminal': 1, 'status': True}])
# 外部出力端子1をON、2をOFFにする場合
# print(info.weboutput(params=[{'terminal': 1, 'status': True}, {'terminal': 2, 'status': False}]))
# 出力のrequestIdをコピーして、以下の requestId= の後ろに貼り付けることで、要求処理状態を確認できます
# print(info.weboutputid(requestId='WebOutput_(gatewayId)_xxxxxxxxxx'))

# triggerId 20 のトリガ条件を成立させる場合
# print(info.webtrigger(triggerId=20))
# 出力のrequestIdをコピーして、以下の requestId= の後ろに貼り付けることで、要求処理状態を確認できます
# print(info.webtriggerid(requestId='WebTrigger_(gatewayId)_xxxxxxxxxx'))

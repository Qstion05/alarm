import os, threading, time
from datetime import datetime
import webbrowser #웹 브라우저를 여는 모듈


def command(): #알람 작동시 실행시킬 함수
	url = "naver.com" 
	webbrowser.open(url)

def alarm(): #알람이 실행되는 함수.
	now = datetime.now()
	check_hour = int(now.hour)	
	if alram_Hour == check_hour: 
		command()
		threading.Timer(3600, alarm).start()##알람 실행 후,반복 실행을 막기위해 1시간동안 작동을 멈춤.
	else:
		threading.Timer(1, alarm).start() #1초마다 반복한다.

alram_Hour = 0
threading.Timer(1, alarm).start() 
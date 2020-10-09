Alarm 프로그램
===============    
00시에 알람(=지정한 프로그램)이 울리게(=실행되게) 하는 프로그램입니다.    
---------------------------   
   
## 실행 방법   
1. 오른쪽 위에 있는 code 메뉴를 통해 zip파일로 다운로드 받아주세요.   
2. zip파일의 압축을 해제한뒤, timer.py파일을 입맛대로 수정해주세요.   
3. 그 후, execute_alarm.py파일을 실행시키시면 됩니다.   
   
   
## 프로그램 수정 방법   
1. def command()에 알람으로 지정한 시간에 실행되게 하고 싶은 명령어를 입력해주시면 됩니다.   
2. webbrowser.open()은 단순한 예시이니 지우시고 다른 함수를 적으셔도 상관없습니다.   
3. 시간을 변경하시고 싶으시다면 alram_Hour값을 원하는 시간(0~23)으로 바꿔주세요.   
4. 만일 시간이 아니라, 지정된 분이나 초마다 반복시키고 싶으시다면, alram_Hour값을 원하는 분/초로 바꿔주신 뒤, check_hour = int(now.hour)의 hour를 minute/second로 바꿔주세요. 그 후 아래의 threading.Timer(3600, alarm).start()의 3600을 60/1로 바꿔주세요.   
5. 반복 주기를 변경하고 싶으시다면 threading.Timer(1, alarm).start()에서 숫자 1을 원하는 반복 주기(단위:초)로 바꿔주세요.   
 
   
## 주의사항 
1. windows에서 사용할 수 있도록 만든 프로그램 입니다. 리눅스에선 아직 지원이 되지 않습니다.
2. **반드시** execute_alarm.py파일과 timer.py파일은 같은 디렉토리에 있어야 합니다.
3. 실행 시킨 뒤 처음 떠있는 도스창은 끄셔도 상관없습니다.   
4. 백그라운드에서 돌아가는 프로그램이기에, 중간에 종료하실려면 프로세스를 종료시키셔야 합니다.   
  
주기적으로 수정할 계획입니다.:)   
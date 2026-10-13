import ipaddress                                 # import 로 파이썬에 들어 있는 IP 계산 모듈 ipaddress 를 불러온다

dev = ipaddress.ip_network("192.168.50.0/25")    # 개발팀 망 192.168.50.0/25(.0 ~ .127)를 망 객체로 바꿔 dev 에 담는다
ops = ipaddress.ip_network("192.168.50.128/25")  # 정상 설계: 개발팀과 겹치지 않는다. 변경 실습은 warmup_4_2b.py에 보존했다.

print(dev.overlaps(ops))                         # .overlaps() 는 두 망이 주소를 하나라도 같이 가지면 True 를 리턴한다. 그 결과를 출력한다

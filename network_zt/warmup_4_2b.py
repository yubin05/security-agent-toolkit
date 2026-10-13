import ipaddress

dev = ipaddress.ip_network("192.168.50.0/25")
# 기존 warmup_4_2.py에서 작성한 변경 설정을 별도 파일로 옮겼다.
ops = ipaddress.ip_network("192.168.50.64/26")

print(dev.overlaps(ops))

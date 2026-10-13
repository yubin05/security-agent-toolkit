import ipaddress

# 오늘 보고서와 warmup_2_1b.py에 기록된 주소·마스크 기준
my_ip = "192.168.200.60"
prefix = 16
net = ipaddress.ip_network(f"{my_ip}/{prefix}", strict=False)

print(net.netmask)
print(net.network_address)
print(net.broadcast_address)

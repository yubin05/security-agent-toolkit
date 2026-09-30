import os
from google.colab import drive

# 1. 구글 드라이브 마운트 (실행 후 팝업창에서 권한 승인 필요)
drive.mount('/content/drive')

# 2. agent_core 폴더 경로 설정
# (내 드라이브 최상위에 agent_core 폴더가 있다고 가정)
my_path = '/content/drive/MyDrive/agent_core'

# 3. 폴더가 실제로 존재하는지 확인 및 없다면 자동 생성
if not os.path.exists(my_path):
    os.makedirs(my_path)
    print(f"🎉 '{my_path}' 폴더가 생성되었습니다.")
else:
    print(f"✅ '{my_path}' 폴더가 연결되었습니다.")

# 4. 이 명령어를 실행하면 이후의 모든 %%writefile 경로가 고정됩니다.
%cd /content/drive/MyDrive/agent_core

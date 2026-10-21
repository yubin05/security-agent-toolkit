from rbac import check_permission, ROLES, USERS                  # 판정 함수와 역할 · 사용자 정보를 불러온다
from access_log import LOG                                       # access_log.py 의 기록 목록을 불러온다

allowed = 0                                                      # 허용 건수
denied = 0                                                       # 거부 건수
counts = {}                                                      # "사용자 허용" · "사용자 거부" → 건수
used = {}                                                        # 역할 → 실제로 쓴 권한 목록

# ← 1부: 기록을 하나씩 다시 판정하며 건수와 쓴 권한 모으기
# 1. LOG 에서 (번호, 시각, 사용자, 자원, 행위)를 하나씩 꺼낸다
for log in LOG:
    no=log[0]
    time=log[1]
    user=log[2]
    resource=log[3]
    action=log[4]

    # 2. check_permission 으로 판정해 ok, reason 으로 나눠 받는다
    ok, reason = check_permission(user, resource, action)

    # 3. ok 이면 allowed 를 1 늘리고, counts 의 "사용자 허용" 을 1 늘리고, 그 사용자의 역할을 role 에 담는다
    if ok:
        allowed += 1
        if user + " 허용" not in counts:
            counts[user + " 허용"] = 0
        counts[user + " 허용"] += 1

        role = USERS[user]["role"]

        # 4. 같은 허용 기록에서, used 에 role 이 아직` 없으면 used[role] = [] 로 빈 목록을 먼저 만들고,
        if not role in used:
            used[role] = []
        # used[role] 목록에 "자원:행위" 글자를 더한다
        used[role].append(f"{resource}:{action}")

    # 5. 아니면 denied 를 1 늘리고, "[거부]" 와 번호 · 시각 · 사용자 · 자원 · 행위 · 이유를 출력하고,
    else:
    # counts 의 "사용자 거부" 를 1 늘린다
        denied += 1
        print("[거부]", no, time, user, resource, action, "-", reason)
        key = user + " 거부"
        counts[key] = counts.get(key, 0) + 1

print("허용", allowed, "거부", denied)                           # 전체 건수를 출력한다
print(counts)                                                    # 사용자별 건수를 출력한다

# ← 2부: 쓰이지 않은 권한 출력하기
# 6. ROLES 에서 역할과 권한 목록을 하나씩 꺼낸다
for role, perms in ROLES.items():
    # 7. 그 목록의 권한을 하나씩 꺼내, used.get(역할, []) 에 없으면 "쓰이지 않음", 역할, 권한 을 출력한다
    for permission in perms:
        if permission not in used.get(role, []):
            print("쓰이지 않음", role, permission)

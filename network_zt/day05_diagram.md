# day05 경보 판단

## 이상한 줄

- 줄 번호: 2번·3번.
- 이유: 인터넷 PC에서 내부망 DB의 3306번으로 향하는 통신이 방화벽에서 허용됐다. 실제 DB 인증·조회 성공 여부는 추가 확인이 필요하다.

## 고친 구성도

```text
INTERNET ---- FW --+-- DMZ    : WEB (443 open)
                  +-- INSIDE : DB  (3306 from WEB only)

Allowed: INTERNET -> WEB :443
Allowed: WEB      -> DB  :3306
Blocked: INTERNET -> DB  :3306
```

인터넷에서 DB로 직접 가는 경로를 차단하고, WEB에서 오는 3306번 통신만 허용하는 정책을 표시했다. 실제 장비 설정을 변경한 기록은 아니다.

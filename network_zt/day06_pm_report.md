# Day 6 Docker ① · nginx 서버 · 오후 (이름 · 2026-10-19)

> **쓰는 법**
> - 문제를 하나 풀 때마다 그 문제 제목 아래를 채웁니다.
> - 질문마다 `쓸 내용:` 에 **무엇을 쓰면 되는지** 적혀 있습니다. 그 내용대로 `답:` 뒤에 씁니다.
> - 「왜 그럴까요?」 같은 질문은 한 단어로 끝내지 말고, 내 화면에서 본 값이나 배운 내용을 근거로 이유까지 씁니다.
> - 🔍 는 그 교시에 꼭 알아야 할 핵심 질문입니다. 답을 못 찾았으면 「모름 — 막힌 곳: …」 이라고 씁니다.

---

## 5교시 · 왜 도커인가 · 이미지와 컨테이너 · 같이 설치하기

### 문제 5-1 · 설치를 확인하고 첫 컨테이너 실행하기

- (가) `docker --version` 으로 나온 값을 적어 주세요.
  - 쓸 내용: 「Docker version … build …」 한 줄
  - 답: Docker version 29.8.2, build 7fc2dff
- (나) 🔍 `docker run hello-world` 출력이 말하는 일의 순서를 5.5 그림의 번호(① ~ ④)에 맞춰 설명해 주세요.
  - 쓸 내용: ① ~ ④ 번호마다 한 일 (클라이언트 · 엔진 · Docker Hub · 컨테이너)
  - 답: ① 클라이언트가 엔진에 hello-world 실행을 요청한다. ② 엔진이 로컬에 없는 이미지를 Docker Hub에서 받는다. ③ 엔진이 이미지로 컨테이너를 만들어 실행한다. ④ 실행 출력을 엔진이 클라이언트로 보내고 클라이언트가 터미널에 표시한다.
- (다) 🔍 `docker images` 에 보인 것과 `docker ps -a` 에 보인 것은 각각 이미지와 컨테이너 중 무엇이고, 어떻게 다른가요?
  - 쓸 내용: ① images 에 보인 것과 그 종류 ② ps -a 에 보인 것과 그 종류 ③ 둘의 차이
  - 답: docker images의 hello-world:latest는 로컬 이미지이고, docker ps -a의 elegant_jemison은 그 이미지로 만든 정상 종료된 컨테이너이다. 이미지는 실행에 필요한 읽기 전용 묶음이며, 컨테이너는 이미지로 만든 실행 인스턴스이고 -a는 종료된 컨테이너도 포함한다.
```text
  C:\Users\User>docker images
                                                           i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   11a3eb1597e8       25.9kB         9.49kB    U

C:\Users\User>docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
8d6bc992e3e4   hello-world   "/hello"   4 minutes ago   Exited (0) 4 minutes ago             elegant_jemison
```
- (라) 🔍 `docker images` 출력을 붙여 넣고, `hello-world` 줄의 `IMAGE` · `ID` · `EXTRA` 값과 각각의 뜻을 적어 주세요.
  - 쓸 내용: ① 출력 ② `IMAGE` · `ID` · `EXTRA` 의 값과 뜻
  - 답: IMAGE=hello-world:latest는 이미지 이름·태그, ID=11a3eb1597e8은 이미지 식별자의 축약 표시이다. EXTRA=U(In Use)는 이 이미지를 참조하는 컨테이너가 있다는 뜻이며, 종료된 컨테이너도 포함한다.

```text
C:\Users\User>docker images
                                                           i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   11a3eb1597e8       25.9kB         9.49kB    U
```

- (마) 🔍 `docker ps -a` 출력을 붙여 넣고, `hello-world` 줄의 `STATUS` · `PORTS` · `NAMES` · `IMAGE` 값과 각각의 뜻을 적어 주세요.
  - 쓸 내용: ① 출력 ② `STATUS` · `PORTS` · `NAMES` · `IMAGE` 의 값과 뜻
  - 답: STATUS=Exited (0) 4 minutes ago는 4분 전 종료 코드 0으로 정상 종료됐다는 뜻이고, PORTS 공란은 표시된 노출·게시 포트가 없다는 뜻이다. NAMES=elegant_jemison은 Docker가 자동으로 붙인 컨테이너 이름이며, IMAGE=hello-world는 생성에 사용한 이미지이다.

```text
C:\Users\User>docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
8d6bc992e3e4   hello-world   "/hello"   4 minutes ago   Exited (0) 4 minutes ago             elegant_jemison
```


### 문제 5-2 · Docker Hub 에서 이미지 이름 읽고 없는 이미지 받아 보기

- (가) `nginx:1.28` 에서 `nginx` 와 `1.28` 이 각각 무엇을 정하는지 적어 주세요.
  - 쓸 내용: ① nginx 가 정하는 것 ② 1.28 이 정하는 것
  - 답: nginx는 실행할 프로그램의 이미지 이름이고, 1.28은 해당 이미지의 버전을 나타내는 태그이다.
- (나) 🔍 `docker pull nginxx` 를 쳤을 때 나온 오류 문구와 그 뜻을 적어 주세요.
  - 쓸 내용: ① 오류 문구 ② 뜻 ③ 고치는 방법
  - 답: 오류는 「Error response from daemon: pull access denied for nginxx, repository does not exist or may require 'docker login'」이며, 저장소가 없거나 접근 권한·로그인이 필요하다는 뜻이다. 이번에는 이미지 이름 오타이므로 `docker pull nginx:1.28`로 고친다.
- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(도커를 쓰면 무엇이 같아지는지)
  - 답: 같은 이미지를 사용하면 PC·서버 간 프로그램과 의존성 환경을 맞춰, 환경 차이로 인한 버전 충돌을 줄일 수 있습니다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 자유롭게
  - 답: 이미지는 실행에 필요한 묶음이고, 컨테이너는 그 이미지로 만든 실행 인스턴스라는 차이를 배웠다. hello-world가 정상 종료돼도 이미지와 종료된 컨테이너는 남아 각각 docker images와 docker ps -a로 확인할 수 있다는 점이 기억에 남는다.

## 6교시 · nginx 서버 켜고 접속 기록 읽기

### 문제 6-1 · 포트 없이 켜 보고, 포트를 연결해 접속하고, 기록 읽기

- (가) 포트 없이 켠 `web` 에 접속했을 때 어떻게 되었는지 적어 주세요.
  - 쓸 내용: 접속했을 때 나온 화면이나 오류와 `docker ps` 의 PORTS 열
  - 답: 브라우저에 「사이트에 연결할 수 없음·127.0.0.1에서 연결을 거부했습니다」가 표시됐고, PORTS는 `80/tcp`였다. 컨테이너의 80번 포트 정보만 있고 호스트 8080번으로 게시되지 않아 `http://127.0.0.1:8080`으로 접속하지 못했다.
- (나) 🔍 `-p 8080:80` 이 하는 일을 내 PC의 포트와 컨테이너의 포트로 나눠 설명해 주세요.
  - 쓸 내용: ① 내 PC 쪽 포트 ② 컨테이너 쪽 포트 ③ 연결이 하는 일
  - 답: 내 PC의 호스트 포트 8080으로 들어온 요청을 컨테이너의 nginx가 사용하는 80번 포트로 전달한다. 따라서 브라우저는 `http://127.0.0.1:8080`으로 접속한다.
- (다) 🔍 `docker logs web` 출력에서 `GET /` 줄 하나를 붙여 넣고, 접속자 주소 · 시각 · 요청 · 응답 번호를 찾아 적어 주세요.
  - 쓸 내용: ① `GET /` 줄 ② 접속자 주소 · 시각 · 요청 · 응답 번호 네 가지
  - 답: 확보한 로그 기준 접속자 주소는 `172.17.0.1`, 시각은 `2026-10-19 06:14:45 UTC`(한국 시각 15:14:45), 요청은 `GET /favicon.ico HTTP/1.1`, 응답 번호는 `404`(아이콘 자원 없음)이다. 첫 페이지의 `GET / HTTP/1.1` 로그는 현재 확보하지 못했다.

```text
172.17.0.1 - - [19/Oct/2026:06:14:45 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://127.0.0.1:8080/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36" "-"
```

  - 해석: `172.17.0.1`은 nginx가 본 Docker 네트워크 쪽 요청 주소이고, 참조 URL의 `127.0.0.1`은 내 PC를 가리키는 루프백 주소이다. 아이콘의 404만으로 첫 페이지 접속 실패라고 판단할 수 없다.

### 문제 6-2 · 컨테이너 안을 들여다보고, 끄고, 지우기

- (가) 컨테이너 안에서 `ls /usr/share/nginx/html` 로 본 파일 이름을 모두 적고, 그중 브라우저의 첫 화면이 어느 파일인지 적어 주세요.
  - 쓸 내용: ① 파일 이름 모두 ② 첫 화면 파일
  - 답: 파일은 `50x.html`, `index.html`이며, 브라우저 첫 화면은 `index.html`이다. `50x.html`은 서버 오류 안내용 파일이다.
```text
# ls /usr/share/nginx/html
50x.html  index.html
```
- (나) 🔍 `docker stop web` 뒤에 `docker ps` 와 `docker ps -a` 에 각각 `web` 이 보이나요? 차이를 설명해 주세요.
  - 쓸 내용: ① stop 뒤 ps 에 보이는지 ② ps -a 에 보이는지 ③ 차이의 이유
  - 답: `docker stop web` 후 `docker ps`에는 안 보이고, `docker ps -a`에는 종료된 `web`이 보인다. stop은 실행만 멈추며 컨테이너 자체는 삭제하지 않는다.
- (다) 🔍 같은 이름으로 다시 `run` 했을 때 나온 오류 문구와, `docker rm` 이 필요한 이유를 적어 주세요.
  - 쓸 내용: ① 오류 문구 ② rm 이 필요한 이유
  - 답: 오류: docker: Error response from daemon: Conflict. The container name "/web" is already in use by container "6129790f0d7a36161748e54bb0f0c64a9ddf61b6b3ba9592326e63d1bb331be8". You have to remove (or rename) that container to be able to reuse that name. 중지된 컨테이너도 이름을 유지하므로 충돌하며, 새로 만들려면 `docker rm web`으로 삭제하거나 기존 이름을 바꿔야 한다. 기존 컨테이너를 다시 켜려면 `docker start web`을 쓴다.
- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(켜는 명령 · 기록 보는 명령 · 정리 방법)
  - 답: nginx는 `docker run -d --name web -p 8080:80 nginx:1.28`로 생성·실행하고 `docker logs web`으로 기록을 확인하며, 불필요해지면 `docker stop web` 후 `docker rm web`으로 정리합니다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 자유롭게
  - 답: stop은 컨테이너를 멈추고 rm은 삭제하며, 중지된 컨테이너도 이름을 유지한다는 것을 배웠다. 같은 컨테이너를 다시 켜는 start와 새 컨테이너를 만드는 run을 구분해야 한다는 점이 기억에 남는다.

## 7교시 · 내 페이지 연결 · 두 서버 · 올리기

### 문제 7-1 · 컨테이너 안의 변경이 사라지는 것을 보고, 내 폴더를 연결하기

- (가) 컨테이너 안에서 바꾼 뒤 `docker rm -f web` 으로 지우고 다시 켰을 때 화면이 어떻게 되었는지 적어 주세요.
  - 쓸 내용: ① 바꾼 뒤 화면 ② 지우고 다시 켠 뒤 화면
  - 답: 컨테이너 안에서 파일을 수정했을 때는 바꾼 내용이 보였고, 컨테이너를 삭제한 뒤 같은 이미지로 새로 만들자 원래 nginx 소개 페이지로 돌아갔다.
- (나) 🔍 컨테이너 안에서 바꾼 내용이 사라진 이유와, `-v` 로 폴더를 연결하면 무엇이 달라지는지 적어 주세요.
  - 쓸 내용: ① 사라진 이유 ② -v 로 연결하면 달라지는 점
  - 답: 컨테이너 안의 변경은 해당 컨테이너의 쓰기 가능 계층에 저장돼 삭제 시 함께 사라지며, 이미지는 바뀌지 않는다. 이번 `-v`는 내 PC 폴더를 컨테이너 경로에 바인드 마운트하므로, 컨테이너를 삭제해도 호스트 파일은 남고 새 컨테이너에 같은 폴더를 다시 연결해 사용할 수 있다.
- (다) 🔍 `MSYS_NO_PATHCONV=1` 없이 `-v` 를 실행했을 때 화면에 무엇이 나왔고 왜 그랬는지 적어 주세요.
  - 쓸 내용: ① 화면에 나온 것 ② 그렇게 된 이유
  - 답: 기존 nginx 소개 페이지가 보였다. Git Bash의 자동 경로 변환으로 컨테이너 쪽 `/usr/share/nginx/html` 경로가 Windows 경로로 바뀌어 의도한 위치에 연결되지 않은 것으로 해석되며, `MSYS_NO_PATHCONV=1`로 해당 명령의 경로 변환을 막는다.

### 문제 7-2 · 서버 두 대를 띄워 포트로 구분하고, 파일을 고쳐 바로 반영되는지 보기

- (가) 두 주소(`8080` · `8081`)에서 보이는 화면을 각각 적어 주세요.
  - 쓸 내용: 두 주소의 화면 문구
  - 답: 8080에서는 「site-one·첫 번째 서버입니다」, 8081에서는 「site-two·두 번째 서버입니다」가 표시됐다. G: 연결에서는 컨테이너 폴더가 비어 403이 발생했으며, `C:\dev\day06_docker` 아래 폴더로 연결해 정상 표시를 확인했다.
- (나) 🔍 `docker ps` 의 PORTS 열에서 두 서버를 구분해 주는 것은 무엇인가요?
  - 쓸 내용: PORTS 열에서 서버를 구분하는 값
  - 답: 호스트 포트 번호로 구분한다. web-one은 `0.0.0.0:8080->80/tcp`, web-two는 `0.0.0.0:8081->80/tcp`이며 컨테이너 내부 포트는 둘 다 80이다.
- (다) 🔍 `:ro` 는 무슨 뜻이고, 왜 읽기 전용으로 연결하나요?
  - 쓸 내용: ① :ro 의 뜻 ② 읽기 전용으로 연결하는 이유
  - 답: `:ro`는 read-only로, 연결한 폴더를 컨테이너에서 읽기만 하고 수정·삭제하지 못하게 한다. 이번에는 같은 의미의 `--mount ... readonly`를 사용해 페이지 제공에 필요한 읽기 권한만 부여했다.
- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(두 서버를 어떻게 띄웠는지)
  - 답: C:의 site-one·site-two 폴더를 읽기 전용으로 연결해 nginx 컨테이너 두 대를 각각 8080·8081로 공개하고 두 페이지의 정상 표시를 확인했습니다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 자유롭게
  - 답: 컨테이너 내부 포트가 둘 다 80이어도 호스트 포트를 다르게 하면 두 서버를 구분할 수 있다는 것을 배웠다. 컨테이너가 실행 중이어도 마운트한 폴더가 비면 403이 날 수 있어 내부 파일까지 확인해야 한다는 점이 기억에 남는다.

### 문제 7-3 · 오늘 만든 것을 깃허브에 올리기

- (가) `git status` 를 쳤을 때 빨간 목록에 줄이 몇 개였는지, 그 가운데 `.env` · `.venv` 가 있었는지 적어 주세요.
  - 쓸 내용: ① 줄 수 ② .env · .venv 가 있었는지
  - 답: 커밋 전 `git status --short` 기준 9줄(폴더 요약 포함) / `.env` 없음 / `.venv` 없음. 오후 자료·보고서·실습 폴더만 올리고 Day03 파일과 `.Codex/`는 제외한다.

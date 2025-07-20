# django-youtube-restapi

## (1) Project Settings
- GitHub

### - Docker란?
프로그램들을 프로세스 격리 기술들을 사용해 컨테이너로 실행하고 관리(구동 및 배포)하는 오픈 소스 플랫폼

### - Docker 구성요소
- Client : 도커 사용자들이 도커를 사용하는 방법, 도커 엔진에 명령어를 입력해 수행하도록 함
- Docker Host : 도커가 띄워진 서버, 컨테이너와 이미지 관리
  - Docker daemon(도커 엔진) : Docker API에 따라 이미지, 컨테이너, 네트워크 등의 도커 오브젝트들을 관리하고 다른 daemon과 통신이 가능하다
  - Docker Images
  - Docker Containers
- Docker Registry : 외부 이미지 저장소로 pull, run으로 컨테이너를 생성 가능하다

### - Docker Image와 Docker Container
Docker Image
- Docker File을 docker build로 생성
- Docker Container를 생성하고 실행할 때 읽기 전용으로 사용 (docker run)

Docker Container
- 일종의 소프트웨어를 소프트웨어 실행에 필요한 모든 것을 포함하는 완전한 파일 시스템
- 코드, 런타임, 시스템 도구, 시스템 라이브러리 등 서버에 설치되는 무엇이든 포함
- 실행 중인 환경에 관계 없이 언제나 동일하게 실행될 것을 보증
<br><br><br>
### CI/CD와 Github Actions
CI(Continuous Integration, 지속적인 통합)<br>코드의 변경 사항이 정기적으로 빌드 및 테스트 되어 공유 레포지토리에 통합되는 것

CD(Continuous Delivery & Continuous Deployment, 지속적인 서비스 제공 & 배포)<br>
-Continuous Delivery는 공유 레포지토리로 자동 Release 하는 것 <br>
-Continuous Deployment는 배포까지 자동으로 릴리즈 하는 것<br><br>

Github Actions
- CI/CD의 한 종류로 GitHub 플랫폼에서 제공
- 프로젝트의 .github/workflows/*.yml 파일을 이용해서 프로세스들을 진행

### PostgreSQL의 장점
Django의 공식 문서에서도 PostgreSQL이 가장 완전하게 지원하는 DB라고 명시<br>
일부 Django 기능은 PostgreSQL에서만 최적으로 동작하고, PostgreSQL의 고급 기능(복잡한 데이터 구조, 전문 검색 기능)도 Django에 잘 통합
<br><br><br>
## Model 구조 -> ORM
(1) User(유저 정보) => users
- email
- password
- nickname
- is_business

(2) Video(비디오 정보) => videos
- title
- description
- link
- category
- views_count
- thumbnail
- video_file: link
파일(이미지, 동영상)은 장고에 저장하면 부하가 걸려서 보통 S3 Bucket(저렴, 속도빠름)에 저장-> '링크'가 결과물로 나옴

(3) Reaction(비디오에대한 리액션) => reactions
- User: FK
- Video: FK
- reaction (like, dislike, cancel) -> 실제 youtube rest api

(4) Comment(댓글 정보) => comments
- User: FK
- Video: FK
- content
- like
- dislike

(5) Subscription(구독 정보) => subscriptions
- User: FK => subscriber (내가 구독한 사람)
- User: FK => subscribed_to (나를 구독한 사람)

(6) Common(다른 모델이 상속받는 추상화 클래스) => common
- created_at
- updated_at
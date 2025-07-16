# Docker란?
프로그램들을 프로세스 격리 기술들을 사용해 컨테이너로 실행하고 관리(구동 및 배포)하는 오픈 소스 플랫폼
<br><br><br>
# Docker 구성요소
- Client : 도커 사용자들이 도커를 사용하는 방법, 도커 엔진에 명령어를 입력해 수행하도록 함
- Docker Host : 도커가 띄워진 서버, 컨테이너와 이미지 관리
  - Docker daemon(도커 엔진) : Docker API에 따라 이미지, 컨테이너, 네트워크 등의 도커 오브젝트들을 관리하고 다른 daemon과 통신이 가능하다
  - Docker Images
  - Docker Containers
- Docker Registry : 외부 이미지 저장소로 pull, run으로 컨테이너를 생성 가능하다
<br><br><br>
# Docker Image와 Docker Container
Docker Image
- Docker File을 docker build로 생성
- Docker Container를 생성하고 실행할 때 읽기 전용으로 사용 (docker run)

Docker Container
- 일종의 소프트웨어를 소프트웨어 실행에 필요한 모든 것을 포함하는 완전한 파일 시스템
- 코드, 런타임, 시스템 도구, 시스템 라이브러리 등 서버에 설치되는 무엇이든 포함
- 실행 중인 환경에 관계 없이 언제나 동일하게 실행될 것을 보증
<br><br><br>
# CI/CD와 Github Actions
CI(Continuous Integration, 지속적인 통합)<br>코드의 변경 사항이 정기적으로 빌드 및 테스트 되어 공유 레포지토리에 통합되는 것

CD(Continuous Delivery & Continuous Deployment, 지속적인 서비스 제공 & 배포)<br>
-Continuous Delivery는 공유 레포지토리로 자동 Release 하는 것 <br>
-Continuous Deployment는 배포까지 자동으로 릴리즈 하는 것<br><br>

Github Actions
- CI/CD의 한 종류로 GitHub 플랫폼에서 제공
- 프로젝트의 .github/workflows/*.yml 파일을 이용해서 프로세스들을 진행
<br><br><br>
# PostgreSQL의 장점
Django의 공식 문서에서도 PostgreSQL이 가장 완전하게 지원하는 DB라고 명시<br>
일부 Django 기능은 PostgreSQL에서만 최적으로 동작하고, PostgreSQL의 고급 기능(복잡한 데이터 구조, 전문 검색 기능)도 Django에 잘 통합
<br><br><br>
# YouTube 모델 폴더 ( 각각 어떤 역할을 하는지 정리)
- users:
- videos:
- reactions:
- comments:
- subscriptions:
- common:
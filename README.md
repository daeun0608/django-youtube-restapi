# Docker란?
프로그램들을 프로세스 격리 기술들을 사용해 컨테이너로 실행하고 관리(구동 및 배포)하는 오픈 소스 플랫폼

# Docker 구성요소
- Client : 도커 사용자들이 도커를 사용하는 방법, 도커 엔진에 명령어를 입력해 수행하도록 함
- Docker Host : 도커가 띄워진 서버, 컨테이너와 이미지 관리
  - Docker daemon(도커 엔진) : Docker API에 따라 이미지, 컨테이너, 네트워크 등의 도커 오브젝트들을 관리하고 다른 daemon과 통신이 가능하다
  - Docker Images
  - Docker Containers
- Docker Registry : 외부 이미지 저장소로 pull, run으로 컨테이너를 생성 가능하다

# Docker Image와 Docker Container
Docker Image
- Docker File을 docker build로 생성
- Docker Container를 생성하고 실행할 때 읽기 전용으로 사용 (docker run)

Docker Container
- 일종의 소프트웨어를 소프트웨어 실행에 필요한 모든 것을 포함하는 완전한 파일 시스템
- 코드, 런타임, 시스템 도구, 시스템 라이브러리 등 서버에 설치되는 무엇이든 포함
- 실행 중인 환경에 관계 없이 언제나 동일하게 실행될 것을 보증
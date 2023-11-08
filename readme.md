# 쟝고 미니프로젝트

0. Overview
1. 서비스화면
2. 화면설계 및 프로젝트 구조
3. 개발 환경
4. 프로젝트 URL 구조
5. 진행 특이점 / 문제점

_________________________________

0. Overview
# 나의 영상일기 - 유튜브 독후감 블로그
내가 본 영상을 보고 리뷰를 적을 수 있는 블로그입니다

_________________________________

1. 서비스화면
 - index / 가입 / 로그인
 
  ![가입로그인](https://github.com/sk7556/djangoMini_1/assets/109896609/f1c1a0b5-c296-4f0a-aaf6-a2379aa188f4)
  
 - 포스트 리스트 및 검색

  ![search](https://github.com/sk7556/djangoMini_1/assets/109896609/73f9cd5d-87d2-4237-a7c6-24eb69507822)

 - 포스트 ( 글 작성 )

  ![글작성](https://github.com/sk7556/djangoMini_1/assets/109896609/af14e18b-97e4-469a-90dc-6bc849f18e9f)
 
 - 포스트 ( 글 읽기 )

  ![read](https://github.com/sk7556/djangoMini_1/assets/109896609/fb36caa3-9955-435a-abed-19307037f16a)

 - 댓글 작성 기능 

  ![comment](https://github.com/sk7556/djangoMini_1/assets/109896609/654e7902-0a4d-4b65-b3c6-ef9c4ded317e)

2. 화면설계 및 프로젝트 구조 

![화면설계서](https://github.com/sk7556/djangoMini_1/assets/109896609/22d38e9c-9d9e-4ac2-80b0-fcaaba354e1a)
화면설계서

![프로젝트디렉터리구조](https://github.com/sk7556/djangoMini_1/assets/109896609/3229b7d2-cd4b-49ec-8bce-f41b6d965344)
프로젝트 디렉터리 구조

3. 개발 환경
 
- 프로젝트 진행
    | 툴 이름 | 활용 |
    |-----|---------|
    | Notion | 프로젝트 관리 문서 작성 |
    | Github ReadMe | 프레젠테이션 문서 작성 |
    | 카카오 오븐 | 페이지 레이아웃 작성 | 
    | DBeaver | DB  |    

- IDE 
    | 툴 이름 | 활용 |
    |-----|---------|
    | VSCODE | Python / HTML / CSS 작업 |
    | AWS Lightsail | 서버 구축 |

- 사용 기술스택
    | 기술명 | 활용 |
    |-----|---------|
    | Backend | Python / Django |
    | Frontend | HTML / CSS / Bootstrap |

4. 프로젝트 URL 구조

- 회원관리 
|app: accounts	| views 함수 이름 |	html 파일이름 |
|-----|---------|-----|
|'signup/'	|signup	|signup.html|
|'login/'	|login	|login.html|
|'logout/'	|logout	||
|'profile/'|	profile	|profile.html |
|'friends/'|	profile	|profile.html |

- 블로그
| app: blog	 | views 함수 이름	| html 파일이름 |
|-----|---------|-----|
| ''  |post_list	| post_list.html |
|'int:pk/' |	post_detail |	post_detail.html |
|friendPost/ | post_list_friend | post_list_friends.html |
|'new/'  |  post_new	| post_write.html |
|'int:pk/edit/'	| post_edit	| post_detail.html|
|'int:pk/delete/' |	post_delete	| post_confirm_delete.html |
| 'search/' |	post_search	 | post_search.html |
| 'int:pk/comment_new/'	| comment_new |	comment_new.html |

- 메인페이지 
| app: blog	 | views 함수 이름	| html 파일이름 |
|-----|---------|-----|
| ''  | index	| index.html |

5. 진행 특이점 / 문제점
- 쟝고 기본 기능으로 대부분 구현이 가능하고, 라이브러리가 마련되어 있어 블로그 기능을 구현하는데 공부가 되었습니다
- pip 라이브러리를 사용해보려는 시도에서 시간을 많이 소모했고, 다른 프로젝트 진행에 차질을 빚었습니다
- Bootstrap과 반응형 웹을 적용시키는데 템플릿의 도움을 받았습니다
- PC / Mac 을 이동하며 작업하는데, 환경 설정에 문제가 발생해 해결해야하는 이슈가 있었습니다

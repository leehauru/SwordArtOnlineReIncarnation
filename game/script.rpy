# 등장인물

define ki = Character('키리토', color="#FFFFFF", who_outlines=[(6, "#FFFFFF", 0, 0),(3, "#0E1E06", 0, 0)], drop_shadow = [(5,1)])
define unknown = Character('?????', color="#FFFFFF", who_outlines=[(6, "#FFFFFF", 0, 0),(3, "#0E1E06", 0, 0)], drop_shadow = [(5,1)])
define cl = Character('클라인', color="#FFFFFF", who_outlines=[(6, "#FFFFFF", 0, 0),(3, "#A93F33", 0, 0)], drop_shadow = [(5,1)])

# extra 
define lizardman_lord =  Character('리저드맨', color="#FFFFFF", who_outlines=[(6, "#FFFFFF", 0, 0),(3, "#45628a", 0, 0)], drop_shadow = [(5,1)])


# Developer ############################
# 애니메이션 효과의 정의
define flash = Fade(1.0, 1.0, 1.0, color="#fff")

define show_quick_menu = False
define show_say_menu = True

# 배경의 정의
image title_copy = "gui/main_menu.png"
image chapter_transition = "gui/new_chap_transition.jpg"
image splash = "gui/splashscreen.png"

image west_field = "gui/background/west_field.png"
image dungeon = "gui/background/dungeon.png"

# 스프라이트의 정의

image lizardman_lord = im.FactorScale("image/lizardman_lord.png", 1.8)
image klein_low_idle = im.FactorScale("image/klein_low_idle.png", 0.3)

# hud image


image kirito_hp_full = im.FactorScale("image/kirito_bar_full.png", 0.68)
image kirito_lv_1_cut = im.FactorScale("image/kirito_lv_1_cut.png", 0.68)

image popup = im.FactorScale("image/sao_ui_popup_drop.png", 0.18)


#date

image date_1 = im.FactorScale("image/sao_date_15_13.png", 0.6)


# # #########################################
# 인게임 변수의 관리
# 초기화 전용.
default book = False
    

#스플래시 스크린의 설정
label splashscreen:
    scene black 
    $ renpy.pause(1.2, hard = True)

    image title_flash = "gui/splashscreen.png"
    $ renpy.pause(0, hard = True)
    scene title_flash with Dissolve(1.2)
    $ renpy.pause(1.2, hard = True)

    $ renpy.pause(0, hard = True)
    scene black with Dissolve(0.5)

    return

label chapter_transition:
    scene chapter_transition with slidedown
    $ renpy.pause(1, hard = True)


# main()
label start:

    # bgm 재생
    #play music "illurock.opus"

    scene title_copy
    $ renpy.pause(0, hard = True)

    scene black with flash
    $ renpy.pause(0, hard = True)

    scene black with fade

    $ show_quick_menu = True

    "무한한 창공에 떠 있는 거대한 암석과 강철의 성."

    "그것이 이 세계의 전부이다."

    "할 일 없는 어떤 기술자 클래스들이 한 달에 걸쳐 측량한 결과, {w}기반 플로어의 직경이 약 10 킬로미터."

    "다시 말해 세타가야 구가 그대로 들어갈 만한 크기라는 사실을 알아냈다고 한다."

    "그 위에 무려 100개에 달하는 플로어가 쌓여 있다니…{w}…{w}…"

    "까마득한 넓이는 아마도 상상을 초월할 것이고, 그 모든 데이터의 양은 얼마나 되는 지 알아낼 길도 없다."

    "그럼 내부 구조를 보자."

    "안에는 몇 개의 대도시와 수많은 일반 도시가 있고, 그 주변에 마을, 숲, 초원, 호수도 있다."

    "상하 플로어를 잇는 계단은 각 플로어마다 하나뿐이며,{w} 그나마 모두 괴물들이 득실거리는 위험한 미궁구역에 존재하기 때문에"

    "계단을 발견하는 것도, 돌파도 쉽지 않다."

    "하지만 아무나 한 번만 돌파에 성공해 상부 플로어 도시에 도착하면 그곳과 하층 플로어 도시의 《텔레포트 게이트》가 연결되어"
    
    "누구나 자유롭게 윗층으로 이동할 수 있게 된다."

    "물론 플로어를 돌파하는 것은 매우 어렵고 미지의 영역을 개척한다는 점에서 모든 사람들로부터 선망의 대상이 된다."

    "그렇게 해서 이 성은 2년에 걸쳐 현재까지 천천히 공략되고 있다."

    "현재의 최전선은 {b}제 74플로어{/b}."

    "성의 이름은 {b}《아인크라드》{/b}."

    "약 6천 명이나 되는 인원을 집어 삼킨 채 떠 있는 검과 전투의 세계.{w} 또 다른 이름은……"

    "《소드 아트 온라인》"

# 새로운 챕터 트랜지션 영역 ########### 복붙 #####

    $ show_say_menu = False
    $ show_quick_menu = False
    show chapter_transition
    with easeintop

    $ renpy.pause(1, hard = True)
    $ renpy.pause(4, hard = True)

    hide chapter_transition
    with easeouttop

    # next scene

    scene black
    $ show_say_menu = True
    $ show_quick_menu = True

    "《챕터 1》"
    

# ##########################################

    scene dungeon # next scene

    #default
    show kirito_hp_full:
        xalign 0
        yalign -0.4

    #default
    show date_1:
        xalign 1.0
        yalign -0.26

    show lizardman_lord with dissolve


    "회색으로 빛나는 검극이 내 어깨를 살짝 갈랐다."

    "시야 왼쪽 위에 고정 표시된 가느다란 라인의 길이가 조금 줄어들었다."

    hide kirito_hp_full
    show kirito_lv_1_cut:
        xalign 0
        yalign -0.4

    "HPー즉 {b}Hit Point바{/b} 라고 불리는 그것은 나의 생명력 잔량을 가시화한 것이다."
    
    "아직 최대치의 80 퍼센트 이상이 남아 있다. {w}다시 말해 지금 20 퍼센트 가량 죽음에 다가섰다."

    "적의 검이 다시 공격 모션에 들어가기도 전에 나는 그게 뒤로 대시해 거리를 벌렸다."

    ki "『…………』"

    "억지로 크게 공기를 내뱉어 호흡을 가다듬었다."

    "지금 나는 전혀 산소가 부족하지 않음에도 불구하고 저쪽, 즉 현실세계의 내 몸은 지금 격렬하게 호흡을 되풀이하고 있을 것이다."

    "축 늘어진 손에서는 식은땀이 배어나오고 심박도 천정부지로 가속하고 있으리라."

    "당연한 노릇이다."

    "설령 내가 보고 있는 모든 것이 3D 가상 오브젝트라 할지라도 나는 지금 분명 나의 목숨을 담보로 싸우고 있으니까."

    "그렇게 따진다면 이 전투는 지극히 불공평하다."

    "왜냐하면 눈 앞의 《적》"

    "짙은 녹색으로 번들번들 빛나는 비늘 덮인 피부와 긴 팔, {w}도마뱀의 머리와 꼬리를 가진 반인반수 괴물은 외모대로 인간도 아니거니와"

    "진짜 생명을 가진 것도 아니다."

    "몇 번을 죽어도 시스템에 의해 무한히 재생성되는 디지털 덩어리."

    ki "『아니지.』"

    "지금 저 도마뱀 인간을 움직이는 AI 프로그램은 내 전술을 관찰하고 학습해 대응력을 시시각각 향상시키고 있다."

    "하지만 그 학습 데이터는 현재의 이 개체가 소멸하는 순간 리셋,{w} 다음 이 에어리어에 리젠될 동종 개체에는 피드백되지 않는다."

    "그러니 어떤 의미로는 이 도마뱀 인간도 살아 있다."

    "세계의 유일무이한 존재로서."

    ki "『………{w}그렇지?』"

    "내가 중얼거린 말을 이해했을 리도 없지만, 지금 내 눈 앞의 도마뱀 인간,"

    "레벨 82의 몬스터 《리저드맨 로드{size=-12}Lizardman Lord{/size}》는 가늘고 긴 턱에 돋아난 날카로운 송곳니를 드러낸 채 후르르, 하고 웃어 보였다."

    "현실이다."

    "이 세계의 모든 것은 현실.{w} 가상공간의 가짜 따위는 하나도 없다."

    "나는 오른손에 쥔 한손용 {color=#6787b3}롱 소드{/color}를 몸 정중선에 맟춰들고 적을 노려보았다."

    "리저드맨도 왼손의 버클러를 내밀며 오른손의 {color=#c2584c}시미터{/color}를 뒤로 뻈다."

    "어두침침한 미궁의 통로 안에 어디선가 싸늘한 바람이 불어와선 벽의 횃불을 흔들었다."

    "깜빡거리는 불꽃들이 축축한 들바닥에서 언뜻언뜻 반사되었다."

    lizardman_lord "『크르아!!』" with hpunch

    "무시무시한 포효와 함께 리저드맨 로드가 땅을 박찼다."

    "멀리서 {color=#c2584c}시미터{/color}가 예리한 원호를 그리며 내 품까지 날아들었다."

    "선명한 오렌지색 궤적이 허공에 눈부시게 빛났다."

    "곡도 카테고리에 속하는 상위 소드 스킬, 단발 중공격기 《펠 크레센트{size=-12}Fell Cresent{/size}》."

    "사정거리 약 4미터를 0.4초 만에 좁히며 달려오는 우수한 돌진계 소드 스킬이다."

    "하지만 나는 그 공격을 미리 읽고 있었다."

    "그렇게 되도록 일부러 거리를 계속 벌리면서 적의 AI 학습을 유도한 것이다."

    "{color=#c2584c}시미터{/color}의 칼끝이 코앞 몇 센티미터 거리를 가르고{w} 타는 듯한 냄새를 남기는 것을 의식하며"

    "낮은 자세로 리저드맨의 몸에 밀착한다."

    ki "『………차앗!』"

    "기합과 함께 오른손의 검을 수평으로 그었다."

    "하늘색 광원 이펙트를 두른 칼날이 비늘 엷은 배를 혈액 대신 선홍색 빛줄기가 뿌려졌다."

    "키엑,{nw}" with hpunch

    "키엑,{fast} 하는 둔중한 비명."

    "하지만 내 검은 멈추지 않는다."

    "수행된 모션에 따라 시스템이 자동적으로 내 움직임을 보조하여, 원래라면 불가능한 속도로 다음 일격을 이어준다."

    "이것이 이 세계에서 전투를 결정짓는 최대의 요소, 《소드 스킬{size=-12}Sword Skill{/size}》이다."

    "왼쪽에서 오른쪽으로 튀어 되돌아온 검이 다시 리저드맨의 가슴을 갈랐다."

    "나는 그대로 몸을 빙글 1회전시켰고, 제3격은 적의 몸을 한층 깊이 베었다."

    lizardman_lord "『으그르르악!!!』" with hpunch

    "리저드맨은 큰 스킬을 헛친 후의 경직이 풀리자마자 분노인지 공포인지 모를 포효와 함께 오른손의 {color=#c2584c}시미터{/color}를 높이 치켜들었다."

    "하지만 나의 연속기는 아직 끝나지 않았다."

    "오른쪽으로 회전하면서 그었던 검이 용수철에 튕기듯 왼쪽 위로 솟구치며 적의 심장ー크리티컬 포인트를 직격했다."

    "도합 네 차례의 연속공격에 의해 내 주위에 마름모꼴로 그려진 하늘색의 빛의 라인이 화악 눈부시게 흩어졌다."

    "수평 4연격 소드 스킬, 《호리전틀 스퀘어{size=-12}Horizontal Square{/size}》."

    "선명한 광원 이펙트가 미궁의 벽을 강하게 비추더니 엷어졌다."

    "동시에 리저드맨의 머리 위에 표시된 HP바 또한 1 도트도 남지 않고 사라졌다."

    "긴 단말마를 흘리며 뒤로 넘어지던 청록색 거구가 부자연스러운 각도에서 딱 멈추더니ー"

    "유리 덩어리를 깨뜨리는 듯한 큰 소리와 함께 미세한 폴리곤 파편이 되어 산산조각으로 사라졌다."

    hide lizardman_lord with dissolve

    "이것이 이 세계의 《죽음》이다.{w} 순간적이며, 또한 간결하다."

    "일절 흔적을 남지기 않는 완전한 소멸."

    show popup with easeinbottom:
        xalign 0.5
        yalign 0.3

    "나는 시야 한가운데에 보라색 폰트로 떠오르는 가산 경험치와 드롭 아이템 리스트를 흘끔 쳐다보고"

    hide popup with easeoutbottom

    "검을 좌우로 턴 후 등의 칼집에 집어넣었다."

    "그리고 그대로 몇 걸음 물러나 미궁 벽에 등을 대고는 비척비척 쓰러지듯 미끄러지며 주저앉았다."

    "꽉 막혔던 호흡을 크게 내뱉고 두 눈을 질끈 감자{w} 오랜 시간 혼자 전투했던 피로 탓인지 관자놀이 안쪽이 묵직하게 아팠다."

    scene black
    hide kirito_lv_1_cut
    hide date_1

    "몇 번씩 머리를 크게 흔들어 아픔을 떨쳐낸 후 다시 눈을 떴다."

    scene dungeon with dissolve
    show kirito_lv_1_cut:
        xalign 0
        yalign -0.4

    show date_1:
        xalign 1.0
        yalign -0.26

    "시야 오른쪽 위에 빛나고 있는 시각 표시는 이미 오후 3시를 넘어섰다."

    "슬슬 미궁을 나서지 않는다면 어두워지기 전에 도시로 돌아갈 수 없다."

    ki "『…{w}…{w}…{w}그만 갈까.』"

    "누가 듣는 것도 아니지만, 나는 그렇게 툭 내뱉고 천천히 일어났다."

    scene black

    "하루치 《공략》이 끝났다."

    "오늘도 어찌어찌 사신의 팔을 빠져나와 살아남았다."

    "하지만 본거지에 돌아가 짧은 휴식을 취하면 금세 또 내일의 싸움이 찾아온다."

    "아무리 안전선을 친다 하더라도 승률이 100 퍼센트가 아닌 전투를 무한히 반복하다 보면"

    "언젠가는 운명의 여신에게 배신당할 때가 올 것이다."

    "문제는 내가 스페이드 에이스를 뽑기 전에 이 게임이 《클리어》 될 것인가, 말 것인가ー"

    "바로 그것이다."

    "생환을 가장 우선시한다면 안전 지역인 마을에서 한 걸음도 나가지 않고 다른 사람이 클리어해줄 날을 언제까지고 기다리는 것이 현명하다."

    "하지만 그렇게 하지 않고 매일 최전선에 솔로로 기어 들어가,{w} 죽음의 위험과 맞바꿔 스텟 강화를 반복하는 나는"

    "{b}VRMMORPG{/b}에 뼛속까지 심취한 중독자일까,"

    "아니면ー"

    "자신의 검으로 세상을 해방시키겠다는 생각이나 하는 바보천치인가."

    "어렴풋한 자조의 웃음을 띤 채 미궁구역의 출구를 향해 걸음을 옮기며, 나는 문득 그날을 떠올리고 있었다."

    "2년 전."

    "모든 것이 끝나고,{w} 그리고 시작되었던,"

    "그 순간을."

    "《챕터 1》 End."

    $ show_say_menu = False
    $ show_quick_menu = False
    show chapter_transition
    with easeintop

    $ renpy.pause(1, hard = True)
    $ renpy.pause(4, hard = True)

    hide chapter_transition
    with easeouttop

    # next scene

    scene black
    $ show_say_menu = True
    $ show_quick_menu = True

    "《챕터 2》"

    scene west_field with dissolve

        #default
    show kirito_hp_full:
        xalign 0
        yalign -0.4

    #default
    show date_1:
        xalign 1.0
        yalign -0.26

    unknown "『으헉………{w} 에잇………{nw}"

    unknown "『으헉……… 에잇………{fast} 으헤에에에!!』" with hpunch

    "기묘한 기합에 맞춰 엉망진창으로 휘둘러진 검이 {w}휭 {w}휭 {w}휭 {w}공기만을 갈랐다."

    "그 직후, 거구 치고는 준민한 움직으로 검을 회피한 푸른 멧돼지가 공격자를 향해 맹렬히 돌진했다."

    "그가 멧돼지의 납작한 콧등에 들이받혀 허공을 날다 초원을 데굴데굴 구르는 꼴을 보고 나도 모르게 웃음을 터뜨렸다."

    show klein_low_idle with dissolve:
        xalign 0.48
        yalign 0.6

    ki "『하하하………{w} 그게 아니야.{w} 초동 모션이 중요하다니까, 클라인.』"

    cl "『아야야야………{nw}"

    cl "『아야야야………{fast} 저 자식!』" with hpunch

    "투덜거리며 일어난 공격자ー파티 멤버 {color=#A93F33}클라인{/color}은 나를 흘끔 보며 한심한 목소리로 대답했다."

    cl "『하지만 키리토, 아무리 그래도……{w} 저놈이 움직이는 걸 어떡하라고.』"

    "붉은 기운이 감도는 머리카락을 이마의 반다나로 거꾸로 세우고,{w} 장신의 늘씬한 체구에 간소한 가죽 갑옷."

    "그와는 겨우 몇 시간 전에 만났다."

    "그의 이름 {color=#A93F33}클라인{/color}." #스토리 추가바람

    "그 클라인의 다리가 후들후들 떨리고 있다."

    "조금 어지러운가 보다."

    "나는 왼손으로 발밑의 덤불에서 조약돌을 집어 어깨 위에 딱 치켜들었다."

    "시스템이 소드 스킬의 퍼스트 모션을 검출하자 조약돌이 어렴풋한 녹색으로 빛났다."

    "그 후에는 거의 자동적으로 왼손이 움직이고, 공중에 선명한 빛의 라인을 그리며 날아간 조약돌은"

    "다시 돌진에 들어가려던 푸른 맷돼지의 미간에 명중했다."

    "키이ー익!!" with hpunch

    "키이ー익!!{fast} 하는 분노의 외침을 울리며 맷돼지가 내 쪽을 돌아보았다."

    ki "『움직이는 거야 당연하지,{w=1.0} 훈련용 허수아비가 아니니깐.』" 

    ki "『하지만 모션을 제대로 일으켜서 소드 스킬만 발동하면 그 다음은 시스템이 스킬을 명중시켜 준다고.』"

    cl "『모션……… {w}모션………』"

    "주문처럼 반복해서 중얼거리며 클라인이 오른손에 쥔 {color=#FFFFF0}커틀라스{/color}를 휙 치켜들었다."

    "푸른 맷돼지, 정식 명칭 《프렌지 보어》는 레벨 1짜리 피라미 몬스터인데도,"

    "공격은 빗나가고 반격은 얻어맞는 사이에 클라인의 HP바는 반 가까이 줄어들고 말았다."

    "딱히 죽는데 해 봤자 바로 근체에 위치한 《시작도시》 에서 소생하면 그만이지만,"
    
    "다시 이 사냥터까지 걸어오는 것도 귀찮다."

    "이 전투를 끌 수 있는 것은 앞으로 공방 한 번 정도를 펼칠 때까지가 한계일 것이다."

    "나는 멧돼지의 돌진을 오른손의 검으로 막으며 고개를 갸웃했다."

    ki "『으ー음,{w} 어떻게 설명하면 좋을까………』"

    ki "『하나{w} 둘{w} 셋 하면서 자세를 잡고 칼을 들어 베는 게 아니라, {w}초동 모션 때 살짝 힘을 모았다가』"

    ki "『스킬이 발동되는 게 느껴지면 그 다음에는 이렇게 {nw}" 

    ki "『스킬이 발동되는 게 느껴지면 그 다음에는 이렇게 {fast}파ー바악! {nw}" with hpunch
    
    ki "『스킬이 발동되는 게 느껴지면 그 다음에는 이렇게 파ー바악! {fast}하고 파고드는 느낌으로』"

    cl "『파바ー악! 이라니………』"

    "악취미스러운 무늬의 반다나 밑에서 강인하게 다잡힌 얼굴을 딱한 몰골로 일그러뜨리며, 클라인은 곡도를 중단으로 겨누었다."

    "심호흡을 한 후 자세를 낮추고, 오른쪽 어깨에 짊어지듯 검을 치켜든다."

    "이번에는 제대로 규정 모션이 검출되어, 천천히 호를 그리는 칼날이 오렌지색으로 번뜩 빛났다."

    cl "차앗!" with hpunch

    "굵은 기합 소리와 동시에, 이제까지와는 완전히 다른 매끄러운 움직이므로 왼발이 땅을 박찼다."

    "스걱ー!{nw}" with hpunch
    
    "스걱ー!{fast} 하는 시원한 효과음이 울려 퍼지며 칼날이 불꽃색 궤적을 허공에 그렸다."

    "한손용 곡도 기본 스킬 《리버{size=-12}Reaver{/size}》가 막 돌진에 들어가려던 푸른 맷돼지의 목에 멋지게 명중, 클라인과 마찬가지로 반쯤 남아 있던 HP를 날려버렸다."

    "꾸웨엑 하는 불쌍한 단말마에 이어 거구가 유리처럼 박살나고, 내 눈앞에 보라색 폰트로 가산 경험치 숫자가 떠올랐다."

    cl "우앗싸아아아아!" with hpunch

    "요란한 승리 포즈를 취하던 클라인이 만면에 미소를 띠며 날 돌아보고는 왼손을 크게 치켜들었다."

    "하이파이브를 나눈 후 나는 다시 한 번 웃었다."

    ki "첫 승리 축하해.{w} 하지만 그 맷돼지, 다른 게임으로 치면 슬라임 수준인데."

    cl "으엑!{w} 진짜?!{w} 난 무슨 중간 보스쯤 되는 줄 알았어!" with hpunch

    ki "그럴 리가 있냐."

    "나는 웃음을 쓴웃음으로 바꾸며 검을 등의 칼집에 넣었다."

    "말로는 놀려댔지만, 그의 기쁨과 감동은 나도 잘 알고 있다."

    "지금까지 경험과 지식 모두 클라인보다 두 달이나 웃도는 나만 몬스터를 쓰러뜨렸기 떄문에, 그는 이제야 겨우 자기 검으로 적을 분쇄하는 상쾌함을 맛볼 수 있었던 것이다."

    "복습을 하려는지, 같은 소드 스킬을 몇 번이고 되풀이하며 신나게 괴성을 질러대는 클라인을 내버려둔 채 나는 주위를 둘러보았다."













    return

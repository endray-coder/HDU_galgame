# 重生之我在杭电读计算机？！

# 定义角色
define me = Character('我', color="#ffffff")
define xuan = Character('璇', color="#ff69b4")

# 初始化
init:
    define gui.main_menu_background = "images/封面.png"
    define gui.game_menu_background = "images/game_menu.png"
    
init python:
    def toggle_timeline():
        if renpy.get_screen('timeline'):
            renpy.hide_screen('timeline')
        else:
            renpy.show_screen('timeline')

# 全局按键绑定screen
screen keymap_screen:
    key "t" action Function(toggle_timeline)

# 定义屏幕
screen main_menu:
    # 菜单文字大小
    default menu_text_size = 30
    # 菜单文字左内边距
    default menu_left_padding = 30
    
    # 背景（覆盖整个屏幕）
    add "images/cover1.png":
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
        
    
    # 侧边栏
    fixed:
        xpos 0
        ypos 0
        xsize 250
        ysize 1.0
        
        vbox:
            ypos 300
            spacing 20
            
            # 开始游戏
            textbutton _("开始") action Start():
                background Solid("#00000080")
                hover_background Solid("#ffffff20")
                text_size menu_text_size
                text_color "#ffffff"
                xminimum 160
                xalign 0.5
                left_padding menu_left_padding
            
            # 读档
            textbutton _("读取") action ShowMenu("load"):
                background Solid("#00000080")
                hover_background Solid("#ffffff20")
                text_size menu_text_size
                text_color "#ffffff"
                xminimum 160
                xalign 0.5
                left_padding menu_left_padding
            
            # 首选项
            textbutton _("首选项") action ShowMenu("preferences"):
                background Solid("#00000080")
                hover_background Solid("#ffffff20")
                text_size menu_text_size
                text_color "#ffffff"
                xminimum 160
                xalign 0.5
                left_padding menu_left_padding
            
            # 关于
            textbutton _("关于") action Jump("dev_log"):
                background Solid("#00000080")
                hover_background Solid("#ffffff20")
                text_size menu_text_size
                text_color "#ffffff"
                xminimum 160
                xalign 0.5
                left_padding menu_left_padding
            
            # 帮助
            textbutton _("帮助") action ShowMenu("help"):
                background Solid("#00000080")
                hover_background Solid("#ffffff20")
                text_size menu_text_size
                text_color "#ffffff"
                xminimum 160
                xalign 0.5
                left_padding menu_left_padding
            
            # 退出游戏
            textbutton _("退出") action Quit():
                background Solid("#00000080")
                hover_background Solid("#ffffff20")
                text_size menu_text_size
                text_color "#ffffff"
                xminimum 160
                xalign 0.5
                left_padding menu_left_padding

# 时间线回溯屏幕
screen timeline:

    
    vbox:
        xalign 0.5
        ypos 50
        text "时间线回溯" size 30 color "#ffffff"
        
        # 文字鱼骨图
        textbutton "一教" action Jump("scene_1_1"):
            background Solid("#9b59b6")
            hover_background Solid("#8e44ad")
            text_size 20
            text_color "#ffffff"
            xminimum 150
        
        textbutton "四教" action Jump("scene_2_1"):
            background Solid("#9b59b6")
            hover_background Solid("#8e44ad")
            text_size 20
            text_color "#ffffff"
            xminimum 150
        
        textbutton "六教" action Jump("scene_3_1"):
            background Solid("#9b59b6")
            hover_background Solid("#8e44ad")
            text_size 20
            text_color "#ffffff"
            xminimum 150
        
        textbutton "七教" action Jump("scene_4_1"):
            background Solid("#9b59b6")
            hover_background Solid("#8e44ad")
            text_size 20
            text_color "#ffffff"
            xminimum 150
        
        textbutton "返回" action Hide("timeline"):
            background Solid("#e74c3c")
            hover_background Solid("#c0392b")
            text_size 20
            text_color "#ffffff"
            xminimum 150
        
        spacing 15

# 开发者日志
label dev_log:
    scene black
    "开发者日志："
    "版本 1.0.0"
    "游戏名称：重生之我在杭电读计算机？！"
    "开发团队：杭电计算机学院"
    "制作日期：2026-04-20"
    "游戏简介：这是一款以杭州电子科技大学为背景的重生题材游戏，玩家将扮演一名重生回到十八岁的学生，在杭电计算机学院开始新的大学生活。"
    "特色系统：时间线回溯、互动对话、场景探索"
    
    # 返回主菜单
    menu:
        "返回主菜单":
            $ renpy.full_restart()

# 游戏开始
label start:
    # 显示全局按键绑定screen
    show screen keymap_screen
    
    # 0-0：杭电大门口
    scene bg_entrance:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    me "我...我重生了吗？（脑袋嗡嗡响）呃...我回到十八岁了？这又是哪？杭州电子科技大学？"
    
    # 走进学校看看吧
    menu:
        "走进学校看看吧":
            jump scene_0_1

# 0-1：一教外
label scene_0_1:
    scene bg_yijiao_outer:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    me "我是成为了这所大学的学生吗？今天好像是平常的一天呢......"
    "突然冒出来一个生物"
    me "（被吓一跳）啊！你是......你是谁？！"
    xuan "啊呀，吓到你了吗？自我介绍一下，我叫\"璇\"，是游荡于此的魂魄。自建校伊始，我就在这里任教。而因为太爱，我已经无法离开杭电了，即便死去，我的魂也在这。我会带着每一位重生之人了解这所大学。跟我走吧~"
    
    # 主线开始
    jump scene_1_1

# 1-1：一教正门
label scene_1_1:
    scene bg_yijiao_entrance:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "你是杭电计算机学院的大一新生哦，那先了解一下你的学院，总不会有错哒。"
    me "这个教学楼看起来好大，进去看看吧"
    
    # 跟着她上楼吧...
    menu:
        "跟着她上楼吧...":
            jump scene_1_2

# 1-2：一教一楼的大厅
label scene_1_2:
    scene bg_yijiao_hall:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    
    # 选择
    menu:
        "听听璇的讲解":
            jump scene_1_2_1
        "接着走":
            jump scene_1_3

# 1-2-1：一教一楼的大厅（讲解）
label scene_1_2_1:
    scene bg_yijiao_hall:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "左边是通信学院，右边就是我们计算机学院啦。大厅还是非常大的，这边是楼梯，我们走上去看看吧"
    xuan "仔细看台阶，上面贴着很多和计算机有关的话呀！你发现了吗"
    jump scene_1_3

# 1-3：一至二楼的楼梯
label scene_1_3:
    scene bg_yijiao_stairs1:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    
    # 选择
    menu:
        "听听璇的讲解":
            jump scene_1_3_1
        "接着走":
            jump scene_1_4

# 1-3-1：一至二楼的楼梯（讲解）
label scene_1_3_1:
    scene bg_yijiao_stairs1:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "（脚步放轻，语气里带着一种悠远的感慨）再看这一句哦——「你的出现成了我优先级最高的中断」。"
    xuan "在计算机系统里，「中断」是一个特别特别重要的机制，当有更紧急、更重要的信号到来时，CPU会暂停当前的任务，优先去处理它。（转头，轻轻弯下腰，笑着）这句话的意思就是，你的出现，就像那个最高优先级的信号，能让我放下手里一切事情，立刻、马上响应你。"
    xuan "（接着指向下一行）还有这句「你是我的BUG，找到你便拥有了世界」……（轻声笑了笑）BUG呢，通常是我们要消灭的东西。但这里的\"BUG\"是一个甜蜜的例外。它就像是程序里一个美丽的错误，是代码宇宙中一次意外的相遇。因为找到了你这个\"BUG\"，我的整个世界才变得完整和有意义。"
    xuan "（转头看向前方台阶，发丝随风轻动）这些写在台阶上的话，都是以前的学长学姐们，或者也许是某个老师，把他们对于技术、对于学业，还有对于青春和陪伴的理解，悄悄留在这里的呢。走吧，我们继续往上，上面还有更多有趣的东西。"
    jump scene_1_4

# 1-4：到二楼了
label scene_1_4:
    scene bg_yijiao_second:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "怎么样，很酷炫吧！"
    me "（激动）哇！那边还有一个小机器人"
    xuan "（傲娇脸）往里面走会有很多教室呢！想当初我面试我们学院的学生会也是在这里的呢！"
    me "（不敢相信）哇，璇这么厉害的嘛！！！"
    
    # 选择
    menu:
        "听听璇的讲解":
            jump scene_1_4_1
        "接着走":
            jump scene_1_5
        "出去":
            jump scene_1_4_3

# 1-4-1：二楼（讲解）
label scene_1_4_1:
    scene bg_yijiao_second:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "二楼有辅导员在此办公，有时候一些材料也要交到这里。这块也有自习区哦~有时候不想去图书馆了，来这里换换口味也是不错哒。"
    jump scene_1_5

# 1-4-3：二楼（出去）
label scene_1_4_3:
    scene bg_yijiao_second:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    me "有点累了呢，出去先吧。"
    jump scene_1_8

# 1-5：二至三楼的楼梯
label scene_1_5:
    scene bg_yijiao_stairs2:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    
    # 选择
    menu:
        "听听璇的讲解":
            jump scene_1_5_1
        "接着走":
            jump scene_1_6

# 1-5-1：二至三楼的楼梯（讲解）
label scene_1_5_1:
    scene bg_yijiao_stairs2:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "（驻足，手指轻轻拂过墙上的字迹，声音里带着一种温柔的笃定）你看这一句——「我是你的指针，在茫茫内存的堆栈中永远指向你的所在之处」。"
    xuan "（转向你，眼中闪烁着清澈而认真的光）在C语言里，指针是一个变量，但它存放的不是普通的值，而是另一个变量的内存地址。这就像一个矢志不渝的承诺：无论数据被分配到堆里那广阔却可能杂乱的空间，还是栈里那规律但随时更迭的序列，指针都能穿越层层地址，精准地找到它。"
    xuan "（语气变得轻快而坚定）所以这句话是在说，无论世界（内存）多么庞大复杂，我的\"指向\"都只为你一人，这是一种底层而绝对的定位。"
    xuan "（视线下移，嘴角泛起甜甜的笑意）再看这句，「我要做你的内联，供你无限次地调用，直到海枯石烂」。"
    xuan "「内联函数:可是个很特别的存在哦！普通函数调用会有开销，但内联函数呢，编译器会尝试把它的代码体直接\"展开\"在调用它的地方。这样做虽然可能让最终程序变大一点点，但每一次调用都变得极快，几乎没有距离和损耗。"
    xuan "所以……（脸微微泛红）这就像在说，我愿成为你触手可及、毫无保留的支持。你想\"调用\"我多少次都可以，每一次我都会全力以赴地\"运行\"，这份高效与亲密，就是我能想到的、属于我们程序员的\"永恒\"啦。"
    jump scene_1_6

# 1-6：二至三楼的楼梯
label scene_1_6:
    scene bg_yijiao_stairs2:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    
    # 选择
    menu:
        "听听璇的讲解":
            jump scene_1_6_1
        "接着走":
            jump scene_1_7

# 1-6-1：二至三楼的楼梯（讲解）
label scene_1_6_1:
    scene bg_yijiao_stairs2:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "（突然就念起了其最终一句，转了起来）我会两种语言，一种写给程序执行，一种说给你听~~"
    me "（猛得一惊）诶不对，幽灵也会写代码吗？哈哈哈哈哈哈"
    xuan "（脸红，跺脚，加快了步伐）哼，快跟上！"
    jump scene_1_7

# 1-7：到三楼了
label scene_1_7:
    scene bg_yijiao_third:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "看到了那几个大字了嘛"
    xuan "（环起了手臂在胸前）：**国！家！级！示！范！中！心！**，我们杭电的计算机可是超级厉害的！来到了这里说明你也很厉害哦"
    me "（崇拜）哇，我会好好努力跟上璇的！"
    xuan "（打趣）我都是幽灵啦，不用跟上我哈哈哈，但是也要加油呀"
    
    # 选择
    menu:
        "听听璇的讲解":
            jump scene_1_7_1
        "出去":
            jump scene_1_7_2

# 1-7-1：三楼（讲解）
label scene_1_7_1:
    scene bg_yijiao_third:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "一教里，很多是行政用处哒，如果你加入了团委等部门，很可能要经常来哦。"
    jump scene_1_8

# 1-7-2：三楼（出去）
label scene_1_7_2:
    scene bg_yijiao_third:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    me "去其他教学楼看看吧？而且现在也有点累了呢。无论如何，出去先吧。"
    jump scene_1_8

# 1-8：一教正门
label scene_1_8:
    scene bg_yijiao_entrance:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "接下来，我们去四教好不好呀？那里有很多实验室哦！"
    jump scene_2_1

# 2-1：四教正门
label scene_2_1:
    scene bg_sijiao_entrance:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    me "（心想：这真的好大...）"
    xuan "四教到啦~我们上去看看吧~"
    me "嗯！这里风好大，我们上去吹会风吧。"
    jump scene_2_2

# 2-2：四教二楼台子
label scene_2_2:
    scene bg_sijiao_platform:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    me "（转过头看向问鼎广场）"
    me "（心想：这就是大学吗...真大，真好啊。我一定要好好珍惜这四年时光。）（不禁湿了眼眶）"
    
    # 选择
    menu:
        "听璇讲四教":
            jump scene_2_2_1
        "站起身来":
            jump scene_2_2_2

# 2-2-1：四教二楼台子（讲解）
label scene_2_2_1:
    scene bg_sijiao_platform:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "四教里面有很多实验室哦，里面有很多非常厉害的学长学姐在做实验！"
    xuan "像是我们平时上机时的机房也在四教。"
    xuan "其实这附近就有一个实验室。它是我们的量子精密测量实验室，是不是听起来就很高级呀！"
    xuan "这个可是获得了2022年度\"科研创新\"之心的明星实验室。很厉害吧！"
    xuan "像这样厉害的实验室我们还有很多！比如我们的智能车实验室，连续三年总成绩全国第一！有机会我一定要带你瞧瞧！"
    jump scene_2_3

# 2-2-2：四教二楼台子（站起身来）
label scene_2_2_2:
    scene bg_sijiao_platform:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "啊！你休息够了吗？但是平常不能进实验室参观呢，真是好可惜！我们去六教吧~"
    xuan "四教是非常大的，有机会你可以多逛逛~走吧，我们去六教。跟紧我"
    jump scene_2_3

# 2-3：实验室外
label scene_2_3:
    scene bg_sijiao_lab:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    jump scene_3_1

# 3-1：六教靠近图书馆一侧
label scene_3_1:
    scene bg_liujiao_library:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "我们去看看教室吧~顺便呢，带你熟悉一下上课路线！大一时很多课要在这上哦，分不清南楼北楼可不行~"
    me "（跟着她走吧，我也不认路）"
    jump scene_3_2

# 3-2：到了六教一楼
label scene_3_2:
    scene bg_liujiao_first:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "这里是六教的阶梯教室，很多宣讲会呀、演讲呀、讲座呀都会在这里进行哦~"
    jump scene_3_3

# 3-3：六教北
label scene_3_3:
    scene bg_liujiao_north:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "阶梯教室一般会在\"中楼\"，但六教有点特殊啦，它没有专门标出中楼。我们先逛逛北楼...哇！"
    me "（目光被她的叫声吸引过去）"
    jump scene_3_4

# 3-4：新装潢的教室
label scene_3_4:
    scene bg_liujiao_classroom:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "我一直没注意到！这间教室装修得真好吧！"
    me "（跟璇一块把脸怼到玻璃上）（心想：这就是资金充沛的学校吗，真好啊！）"
    me "（咳咳）我们走吧...这样子盯着人家好奇怪的。别打扰他们啦。"
    jump scene_3_5

# 3-5：六教教室
label scene_3_5:
    scene bg_liujiao_classroom:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    me "这间教室现在没课诶，进去看看吗？"
    xuan "嗯哼~"
    me "（心想：要是上辈子我也能在这么宽敞的教室努力学习知识，也不至于漂泊一生了吧...）"
    jump scene_3_6

# 3-6：六教一走廊
label scene_3_6:
    scene bg_liujiao_corridor:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "哇哇哇！不好意思呀，给你带到北楼出口了，接下来需要绕路去七教了，哭哭。但往好处想，我们可以多逛逛校园不是嘛~"
    me "（心想：怎么说也快有八十岁了吧，保留下来的性格还真的像少女呢）"
    jump scene_4_0

# 4-0：从六教绕回七教的路上
label scene_4_0:
    scene bg_path_to_qijiao:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "今天天气好好哦~看看这青草，看看这阳光~嗯~~~"
    me "确实是的，平常这里有很多人玩吧？"
    xuan "对哦，而且在七教旁的小草坪上，更是经常有学生们成群结队，铺上毯子，野餐，玩耍呢~你必须要好好试试呀~"
    jump scene_4_1

# 4-1：七教门口
label scene_4_1:
    scene bg_qijiao_entrance:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "诶嘿...到了哦~"
    xuan "七教会比较新哦，同时它也有中楼，必须带你认清楚路啦~"
    jump scene_4_2

# 4-2：刚进入七教
label scene_4_2:
    scene bg_qijiao_inside:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "这里是北楼哈，一样的呢，你很多课要在这里上~不同于六教的是，这里的课大多是小班课，也就是在20-90人左右哦。"
    jump scene_4_3

# 4-3：去南楼的楼梯处
label scene_4_3:
    scene bg_qijiao_stairs:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "如果你有点路痴，一定要记得这个楼梯！走过这个楼梯，就到南楼啦！"
    jump scene_4_4

# 4-4：去到了北楼四楼
label scene_4_4:
    scene bg_qijiao_fourth:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    xuan "（趴在栏杆上）累死俺了啦。"
    xuan "还有就是你干嘛都不说话啦！"
    me"（小声说）别人又听不见你说话，他们上课我讲话这不是捣乱嘛！"
    jump scene_5_1

# 5-1：去北二门的路上
label scene_5_1:
    scene bg_path_to_beier:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    me"带我去生活区转转好吗？"
    xuan "那...那走吧"
    jump scene_5_2

# 5-2：在马路
label scene_5_2:
    scene bg_road:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    me"趁学生们还没下课，快去吃饭吧"
    xuan "（默默掉下了眼泪）对不起啊，我就只能陪你到这了。"
    me"为...为什么？"
    xuan "（慢慢变得更透明）少年啊，不，重生的少年啊，请你珍惜这年岁，等下次春天来临时，你便知道，我为何而存在了。"
    jump scene_5_3

# 5-3：宿舍楼看夕阳
label scene_5_3:
    scene bg_dorm_sunset:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
    me"（趴在栏杆上向外望）今天做了三位一体的志愿，他们都好有活力，腼腆而勇敢呢。"
    me "啊！璇，我好像明白了。玉石...旋转...是电子一般的鬼魂？还是说...！"
    me "她要说的是！！！"
    jump scene_5_4

# 5-4：突然一阵白光
label scene_5_4:
    scene white
    "突然一阵白光，响起了原神启动的音乐"
    "欢迎报考杭州电子科技大学...........................................（嘻嘻）"
    
    # 游戏结束
    return

# 定义场景图片
image black = Solid("#000000")
image white = Solid("#ffffff")

# 场景图片
image bg_entrance = "images/封面.png"         # 杭电大门口
image bg_yijiao_outer = "images/0-1-2.png"    # 一教外
image bg_yijiao_entrance = "images/1-1.png"   # 一教正门
image bg_yijiao_hall = "images/1-1.png"       # 一教一楼的大厅
image bg_yijiao_stairs1 = "images/1-3-1.png"  # 一至二楼的楼梯
image bg_yijiao_second = "images/1-4.png"     # 到二楼了
image bg_yijiao_stairs2 = "images/1-5-1.png"  # 二至三楼的楼梯
image bg_yijiao_third = "images/1-7.png"      # 到三楼了
image bg_sijiao_entrance = "images/2-1.png"   # 四教正门
image bg_sijiao_platform = "images/2-2.png"   # 四教二楼台子
image bg_sijiao_lab = "images/2-2.png"        # 实验室外
image bg_liujiao_library = "images/3-1.png"   # 六教靠近图书馆一侧
image bg_liujiao_first = "images/3-2.png"     # 到了六教一楼
image bg_liujiao_north = "images/3-3.png"     # 六教北
image bg_liujiao_classroom = "images/3-4.png"  # 新装潢的教室
image bg_liujiao_corridor = "images/3-6.png"  # 六教一走廊
image bg_path_to_qijiao = "images/4-0.png"    # 从六教绕回七教的路上
image bg_qijiao_entrance = "images/4-1.png"    # 七教门口
image bg_qijiao_inside = "images/4-2-1.png"    # 刚进入七教
image bg_qijiao_stairs = "images/4-3.png"      # 去南楼的楼梯处
image bg_qijiao_fourth = "images/4-4-2.png"    # 去到了北楼四楼
image bg_path_to_beier = "images/4-4-2.png"    # 去北二门的路上
image bg_road = "images/5-2-1.png"            # 在马路
image bg_dorm_sunset = "images/5-3.png"        # 宿舍楼看夕阳
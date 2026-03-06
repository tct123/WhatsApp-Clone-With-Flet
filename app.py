import flet as ft
import json

wallpaper = "assets/icons/wallpaper.png"
w = 1000
h = 800
sbw = 50
s_bw = 270
csw = 300
dmw = w - 300 - 50
br = 12
s_btn_w = 40
s_btn_h = 35
sbc = "#282828"
csc = "#202020"
dmc = "#282828"
sb_ic = "#efefef"
s_btn_h_c = "#E6353535"
ic = "#00a884"
nac = "#25d366"
chat_screen_padding = 20
ih_br = 5
htc = "#6a6a6a"
rc = "#363636"
sc = "#035d4d"
mtc = "#689e94"
smc = "#cddfdb"


class App(ft.UserControl):
    def __init__(self, pg: ft.Page):
        super().__init__()
        self.pg = pg
        # self.pg.window_maximizable = True
        # self.pg.window_minimizable = True

        self.pg.window.bgcolor = ft.Colors.TRANSPARENT
        self.pg.bgcolor = ft.Colors.TRANSPARENT
        self.pg.window.title_bar_hidden = True
        self.pg.window.frameless = False
        self.containers_init()
        self.init_helper()

    def load_chat_dummy(self):
        # for n in range(50):
        #   self.chats_contents_column.controls.append(self.chat_row)
        pass

    def init_helper(self):
        self.pg.add(
            ft.Container(
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                border_radius=br,
                expand=True,
                bgcolor=dmc,
                content=ft.Stack(
                    expand=True,
                    controls=[
                        ft.Row(
                            spacing=0,
                            controls=[
                                self.sidebar,
                                self.chats_screen,
                                self.dm_screen,
                            ],
                        ),
                        self.settings_popup,
                        self.emoji_popup,
                    ],
                ),
            )
        )

    def containers_init(self):
        self.chat_user_details()
        self.dm_screen_content_main()
        self.chats_column_f()
        self.chat_screen()
        self.sidebar()
        self.base_containers()
        self.load_chat_dummy()

    def base_containers(self):
        self.sidebar = ft.Container(
            padding=ft.Padding.only(top=50, bottom=50),
            width=sbw,
            bgcolor=sbc,
            content=self.sidebar_column,
        )
        self.chats_screen = ft.Container(
            animate=animation.Animation(500, AnimationCurve.BOUNCE_OUT),
            width=csw,
            bgcolor=csc,
            content=self.chat_screen_items,
        )
        self.dm_screen = ft.Container(
            expand=True, bgcolor=dmc, content=self.dm_screen_content
        )

    def sidebar_btn_hovered(self, e: HoverEvent):
        if e.data == "true":
            e.control.bgcolor = s_btn_h_c

        else:
            e.control.bgcolor = None
        e.control.update()

    def show_hide_csa(self, e: TapEvent):
        if e.control.data == "opened":
            self.chats_screen.width = 0
            self.sidebar.bgcolor = csc
            e.control.data = "closed"
        else:
            self.chats_screen.width = csw
            self.sidebar.bgcolor = sbc
            e.control.data = "opened"

        e.control.update()
        self.sidebar.update()
        self.chats_screen.update()

    def sidebar(self):
        self.sidebar_column = ft.Column(
            horizontal_alignment="center",
            alignment="spaceBetween",
            spacing=0,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            # on_hover=self.sidebar_btn_hovered,
                            alignment=ft.Alignment.CENTER,
                            height=s_btn_h,
                            width=s_btn_w,
                            bgcolor=s_btn_h_c,
                            border_radius=5,
                            content=ft.Row(
                                spacing=0,
                                alignment="spaceBetween",
                                vertical_alignment="center",
                                controls=[
                                    ft.Container(
                                        offset=transform.Offset(0, 0),
                                        animate_offset=animation.Animation(1000),
                                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                        height=17,
                                        width=3,
                                        bgcolor=ic,
                                        border_radius=5,
                                    ),
                                    ft.Container(
                                        margin=ft.Margin.only(right=10),
                                        content=ft.Stack(
                                            controls=[
                                                ft.Container(
                                                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                                    height=20,
                                                    width=20,
                                                    content=ft.Image(
                                                        src="assets/icons/c.png",
                                                        fit=ft.ImageFit.COVER,
                                                        color=sb_ic,
                                                    ),
                                                ),
                                                ft.Container(
                                                    right=1,
                                                    top=1,
                                                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                                    height=8,
                                                    width=8,
                                                    bgcolor=nac,
                                                    border_radius=20,
                                                ),
                                            ]
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        ft.Container(
                            on_hover=self.sidebar_btn_hovered,
                            alignment=ft.Alignment.CENTER,
                            height=s_btn_h,
                            width=s_btn_w,
                            # bgcolor = s_btn_h_c,
                            border_radius=ih_br,
                            content=ft.Row(
                                spacing=0,
                                alignment="spaceBetween",
                                vertical_alignment="center",
                                controls=[
                                    ft.Container(
                                        offset=transform.Offset(0, 0),
                                        animate_offset=animation.Animation(1000),
                                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                        height=17,
                                        width=3,
                                        # bgcolor=ic,
                                        border_radius=5,
                                    ),
                                    ft.Container(
                                        margin=ft.Margin.only(right=10),
                                        content=ft.Stack(
                                            controls=[
                                                ft.Container(
                                                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                                    height=20,
                                                    width=20,
                                                    content=ft.Image(
                                                        src="assets/icons/s.png",
                                                        fit=ft.ImageFit.COVER,
                                                        color=sb_ic,
                                                    ),
                                                ),
                                                ft.Container(
                                                    right=0,
                                                    top=1,
                                                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                                    height=9,
                                                    width=9,
                                                    bgcolor=nac,
                                                    border_radius=20,
                                                    # border=border.all(color=sbc,width=1)
                                                ),
                                            ]
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ]
                ),
                ft.Column(
                    spacing=5,
                    controls=[
                        ft.Container(
                            data="opened",
                            on_hover=self.sidebar_btn_hovered,
                            on_click=self.show_hide_csa,
                            alignment=ft.Alignment.CENTER,
                            height=s_btn_h,
                            width=s_btn_w,
                            border_radius=5,
                            content=ft.Row(
                                spacing=0,
                                alignment="center",
                                controls=[
                                    ft.Icon(ft.Icon.MENU_OUTLINED, size=20, color=sb_ic)
                                ],
                            ),
                        ),
                        ft.Container(
                            on_hover=self.sidebar_btn_hovered,
                            on_click=self.show_settings_popup,
                            alignment=ft.Alignment.CENTER,
                            height=s_btn_h,
                            width=s_btn_w,
                            border_radius=5,
                            content=ft.Row(
                                spacing=0,
                                alignment="center",
                                controls=[
                                    ft.Icon(
                                        ft.Icon.SETTINGS_OUTLINED, size=20, color=sb_ic
                                    )
                                ],
                            ),
                        ),
                        ft.Container(
                            on_hover=self.sidebar_btn_hovered,
                            on_click=self.show_settings_popup,
                            alignment=ft.Alignment.CENTER,
                            height=s_btn_h,
                            width=s_btn_w,
                            border_radius=ih_br,
                            content=ft.Row(
                                spacing=0,
                                alignment="center",
                                controls=[
                                    ft.Container(
                                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                        height=20,
                                        width=20,
                                        border_radius=20,
                                        content=ft.Image(
                                            src="assets/dp.jpg", fit=ft.ImageFit.COVER
                                        ),
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        )

    def chat_screen(self):

        self.chat_screen_items = ft.Stack(
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            height=40,
                            padding=ft.Padding.only(left=10),
                            # margin=ft.Margin.only(bottom=10),
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        src="assets/icons/logo.png",
                                    ),
                                    ft.Text(
                                        value="WhatsApp",
                                        size=14,
                                    ),
                                ]
                            ),
                        ),  # whatsapp icon
                        ft.Container(
                            padding=ft.Padding.only(
                                left=chat_screen_padding, right=chat_screen_padding
                            ),
                            content=ft.Row(
                                spacing=0,
                                alignment="spaceBetween",
                                vertical_alignment="center",
                                controls=[
                                    ft.Text(
                                        value="Chats",
                                        size=24,
                                        weight=ft.FontWeight.W_500,
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                on_hover=self.sidebar_btn_hovered,
                                                height=40,
                                                width=40,
                                                border_radius=ih_br,
                                                content=ft.Image(
                                                    src="assets/icons/newchat.png",
                                                    color=sb_ic,
                                                ),
                                            ),
                                            ft.Container(
                                                on_hover=self.sidebar_btn_hovered,
                                                height=40,
                                                width=40,
                                                border_radius=ih_br,
                                                content=ft.Image(
                                                    src="assets/icons/more.png",
                                                    color=sb_ic,
                                                ),
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                        ),  # Chats label text and new chat icon and more
                        ft.Container(
                            content=ft.Row(
                                alignment="center",
                                controls=[
                                    ft.Container(
                                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                        border_radius=ih_br,
                                        content=ft.Container(
                                            # on_hover=self.sidebar_btn_hovered,
                                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                            border_radius=ih_br,
                                            height=35,
                                            width=s_bw,
                                            bgcolor=sbc,
                                            border=border.only(
                                                bottom=border.BorderSide(
                                                    width=1, color=htc
                                                )
                                            ),
                                            content=ft.Row(
                                                controls=[
                                                    ft.Container(
                                                        width=230,
                                                        padding=ft.Padding.only(
                                                            left=15, top=5
                                                        ),
                                                        content=ft.TextField(
                                                            border=ft.InputBorder.NONE,
                                                            hint_text="Search or start a new chat",
                                                            hint_style=ft.TextStyle(
                                                                size=14,
                                                                font_family="arial",
                                                                color=htc,
                                                            ),
                                                            color=sb_ic,
                                                            text_style=ft.TextStyle(
                                                                size=14,
                                                                font_family="arial",
                                                                color=sb_ic,
                                                            ),
                                                        ),
                                                    ),
                                                    ft.Container(
                                                        height=25,
                                                        width=25,
                                                        border_radius=ih_br,
                                                        on_hover=self.sidebar_btn_hovered,
                                                        content=ft.Icon(
                                                            ft.Icons.SEARCH_OUTLINED,
                                                            size=16,
                                                            color=htc,
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                    )
                                ],
                            )
                        ),  # search box
                        ft.Container(
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            height=40,
                            padding=ft.Padding.only(left=10, right=10),
                            # border_radius=20,
                            content=ft.Container(
                                border_radius=ih_br,
                                on_hover=self.sidebar_btn_hovered,
                                padding=ft.Padding.only(left=10, right=10),
                                content=ft.Row(
                                    vertical_alignment="center",
                                    alignment="spaceBetween",
                                    controls=[
                                        ft.Icon(ft.Icons.DELETE_OUTLINE),
                                        ft.Container(
                                            content=ft.Text(
                                                value="Archived",
                                                weight=ft.FontWeight.W_600,
                                            ),
                                            margin=ft.Margin.only(right=100),
                                        ),
                                        ft.Text(
                                            value="2",
                                            color=ic,
                                            weight=ft.FontWeight.W_600,
                                        ),
                                    ],
                                ),
                            ),
                        ),  # archived chat button
                        self.chats_contents_column,
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Container(),  # whatsapp icon
                        ft.Container(),  # Status text label
                        ft.Container(),  # my stat
                        ft.Container(),  # recent updates label
                        ft.Container(),  # stats column container
                    ]
                ),
            ]
        )

    def search_on_focus(self, e):
        pass

    def chats_column_f(self):
        self.chat_row = ft.Container(
            height=70,
            padding=ft.Padding.only(left=10, right=10),
            content=ft.Container(
                border_radius=ih_br,
                on_hover=self.sidebar_btn_hovered,
                content=ft.Row(
                    spacing=0,
                    alignment="spaceBetween",
                    vertical_alignment="center",
                    controls=[
                        ft.Container(
                            height=50,
                            width=50,
                            border_radius=30,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            content=ft.Image(
                                src="assets/dp.jpg",
                                fit=ft.ImageFit.COVER,
                            ),
                        ),
                        ft.Column(
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                ft.Container(
                                    width=200,
                                    content=ft.Row(
                                        alignment="spaceBetween",
                                        # vertical_alignment='center',
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                                width=120,
                                                content=ft.Text("#Se7en", no_wrap=True),
                                            ),
                                            ft.Text("12:20AM"),
                                        ],
                                    ),
                                ),
                                ft.Container(
                                    width=200,
                                    content=ft.Row(
                                        alignment="spaceBetween",
                                        # vertical_alignment='center',
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                                width=120,
                                                content=ft.Text(
                                                    "last message of chat", no_wrap=True
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )

        self.chats_contents_column = ft.Column(
            scroll="auto",
            expand=True,
            controls=[
                self.chat_row,
            ],
        )  # chats column container

    def msg_hovered(self, e):
        if e.data == "true":
            self.msg_hover_emoji.visible = True
        else:
            self.msg_hover_emoji.visible = False
        self.msg_hover_emoji.update()

    def show_msg_menu(self, e: ft.LongPressEndEvent):
        print(e.target)

    def close_window(self, e):
        self.pg.window_destroy()

    def mini_window(self, e):
        self.pg.window_minimized = True

        self.pg.update()

    def max_window(self, e):
        self.pg.window_maximized = True
        self.pg.update()

    def hide_emojis_popup(self, e):
        self.emoji_popup.offset = transform.Offset(0, 1.5)
        self.emoji_popup.update()
        sleep(0.51)
        self.emoji_popup.height = 0
        self.emoji_popup.update()

    def show_emojis_popup(self, e):
        self.emoji_popup.height = None
        self.emoji_popup.offset = transform.Offset(0, 0)
        self.emoji_popup.update()

    def chat_user_details(self):

        self.chat_user_details_sidebar_item_info = ft.Container(
            expand=True,
            padding=15,
            content=ft.Column(
                # expand=True,
                height=475,
                scroll="auto",
                controls=[
                    ft.Row(
                        alignment="center",
                        controls=[
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=100,
                                width=100,
                                border_radius=80,
                                bgcolor="white12",
                                content=ft.Icon(ft.Icons.PERSON, size=50),
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment="center",
                        controls=[
                            ft.Text("Mr. Newton😊", size=20, weight=ft.FontWeight.W_600)
                        ],
                    ),
                    ft.Text(
                        "About",
                        size=14,
                        weight=ft.FontWeight.W_300,
                        color="white24",
                    ),
                    ft.Text(
                        "Hey there! I am using WhatsApp",
                        size=14,
                        weight=ft.FontWeight.W_400,
                        color="#CCffffff",
                    ),
                    ft.Text(
                        "Phone number",
                        size=14,
                        weight=ft.FontWeight.W_300,
                        color="white24",
                    ),
                    ft.Text(
                        "+233 548 007 499",
                        size=14,
                        weight=ft.FontWeight.W_400,
                        color="#CCffffff",
                    ),
                    ft.Text(
                        "Disappearing messages",
                        size=14,
                        weight=ft.FontWeight.W_300,
                        color="white24",
                    ),
                    ft.Text(
                        "Off",
                        size=14,
                        weight=ft.FontWeight.W_400,
                        color="#CCffffff",
                    ),
                    ft.Text(
                        "Muted notifications",
                        size=14,
                        weight=ft.FontWeight.W_300,
                        color="white24",
                    ),
                    ft.Container(
                        width=120,
                        height=35,
                        bgcolor=s_btn_h_c,
                        padding=ft.Padding.only(left=10),
                        border_radius=ih_br,
                        content=ft.Row(
                            controls=[
                                # ft.Image(
                                #   src='assets/icons/audio.png',
                                #   color='#CCffffff'
                                # )
                                ft.Icon(
                                    ft.Icon.MUSIC_NOTE_OUTLINED,
                                    size=16,
                                    color="#CCffffff",
                                ),
                                ft.Dropdown(
                                    alignment=ft.Alignment.CENTER,
                                    label_style=ft.TextStyle(
                                        size=12,
                                        color="#CCffffff",
                                    ),
                                    expand=True,
                                    label="Mute",
                                    options=[
                                        ft.dropdown.Option(
                                            "For 8hrs",
                                        ),
                                        ft.dropdown.Option("For 1 Week"),
                                        ft.dropdown.Option("Always"),
                                    ],
                                    border_color=s_btn_h_c,
                                ),
                            ]
                        ),
                    ),
                    ft.Text(
                        "Notification tone",
                        size=14,
                        weight=ft.FontWeight.W_300,
                        color="white24",
                    ),
                    ft.Container(
                        height=35,
                        border_radius=ih_br,
                        content=ft.Row(
                            spacing=10,
                            controls=[
                                # ft.Image(
                                #   src='assets/icons/audio.png',
                                #   color='#CCffffff'
                                # )
                                ft.Container(
                                    height=35,
                                    width=35,
                                    border_radius=ih_br,
                                    bgcolor=s_btn_h_c,
                                    content=ft.Icon(
                                        ft.Icons.PLAY_ARROW_OUTLINED,
                                        size=16,
                                        color="#CCffffff",
                                    ),
                                ),
                                ft.Container(
                                    border_radius=ih_br,
                                    bgcolor=s_btn_h_c,
                                    width=120,
                                    content=Dropdown(
                                        # icon=ft.Icon.MUSIC_NOTE_OUTLINED,
                                        alignment=ft.Alignment.CENTER,
                                        label_style=ft.TextStyle(
                                            size=12,
                                            color="#CCffffff",
                                        ),
                                        expand=True,
                                        label="Default",
                                        options=[
                                            ft.dropdown.Option(
                                                "None",
                                            ),
                                            ft.dropdown.Option("Default"),
                                            ft.dropdown.Option("Alert 1"),
                                            ft.dropdown.Option("Alert 2"),
                                            ft.dropdown.Option("Alert 3"),
                                        ],
                                        border_color=s_btn_h_c,
                                    ),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        # expand=True,
                        width=500,
                        height=1,
                        bgcolor=s_btn_h_c,
                    ),
                    ft.Row(
                        alignment="spaceBetween",
                        controls=[
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=35,
                                width=155,
                                border_radius=ih_br,
                                bgcolor=s_btn_h_c,
                                content=ft.Text(
                                    "Block",
                                    size=14,
                                    weight=ft.FontWeight.W_400,
                                    color="#CCffffff",
                                ),
                            ),
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=35,
                                width=155,
                                border_radius=ih_br,
                                bgcolor=s_btn_h_c,
                                content=ft.Text(
                                    "Report contact",
                                    size=14,
                                    weight=ft.FontWeight.W_400,
                                    color="#CCffffff",
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

        self.settings_sidebar_details_column = ft.Container(
            expand=True,
            padding=15,
            content=ft.Column(
                # expand=True,
                height=475,
                scroll="auto",
                controls=[
                    ft.Row(
                        alignment="center",
                        controls=[
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=100,
                                width=100,
                                border_radius=80,
                                bgcolor="white12",
                                content=ft.Icon(ft.Icons.PERSON, size=50),
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment="spaceBetween",
                        controls=[
                            # ft.Text(
                            #   'Mr. Newton😊',
                            # size=20,
                            #   weight=ft.FontWeight.W_600
                            # ),
                            ft.TextField(
                                width=200,
                                value="Mr. Newton😊",
                                text_size=20,
                                border=ft.InputBorder.NONE,
                            ),
                            ft.Container(
                                margin=ft.Margin.only(right=15),
                                on_hover=self.sidebar_btn_hovered,
                                border_radius=ih_br,
                                height=35,
                                width=35,
                                content=ft.Icon(
                                    ft.Icons.EDIT_OUTLINED, size=14, color=sb_ic
                                ),
                            ),
                        ],
                    ),
                    ft.Text(
                        "About",
                        size=14,
                        weight=ft.FontWeight.W_300,
                        color="white24",
                    ),
                    ft.Row(
                        alignment="spaceBetween",
                        controls=[
                            ft.TextField(
                                width=250,
                                multiline=True,
                                value="Hey there! WhatsApp is using me!",
                                text_size=14,
                                border=ft.InputBorder.NONE,
                                text_style=ft.TextStyle(
                                    size=14,
                                    weight=ft.FontWeight.W_400,
                                    color="#CCffffff",
                                ),
                            ),
                            ft.Container(
                                margin=ft.Margin.only(right=15),
                                on_hover=self.sidebar_btn_hovered,
                                border_radius=ih_br,
                                height=35,
                                width=35,
                                content=ft.Icon(
                                    ft.Icons.EDIT_OUTLINED, size=14, color=sb_ic
                                ),
                            ),
                        ],
                    ),
                    ft.Text(
                        "Phone number",
                        size=14,
                        weight=ft.FontWeight.W_300,
                        color="white24",
                    ),
                    ft.Text(
                        "+233 548 007 499",
                        size=14,
                        weight=ft.FontWeight.W_400,
                        color="#CCffffff",
                    ),
                ],
            ),
        )

        self.chat_user_details_sidebar_item = ft.Container(
            bgcolor=s_btn_h_c,
            height=35,
            border_radius=ih_br,
            content=ft.Row(
                spacing=12,
                # alignment='spaceBetween',
                vertical_alignment="center",
                controls=[
                    ft.Container(
                        offset=transform.Offset(0, 0),
                        animate_offset=animation.Animation(1000),
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        height=17,
                        width=3,
                        bgcolor=ic,
                        border_radius=5,
                    ),
                    ft.Row(
                        vertical_alignment="center",
                        spacing=10,
                        controls=[
                            ft.Image(
                                src="assets/icons/info.png",
                                color=sb_ic,
                                # scale=0.5
                            ),
                            ft.Text("Overview"),
                        ],
                    ),
                ],
            ),
        )

        self.settings_sidebar_item = ft.Container(
            bgcolor=s_btn_h_c,
            height=35,
            border_radius=ih_br,
            content=ft.Row(
                spacing=12,
                # alignment='spaceBetween',
                vertical_alignment="center",
                controls=[
                    ft.Container(
                        offset=transform.Offset(0, 0),
                        animate_offset=animation.Animation(1000),
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        height=17,
                        width=3,
                        bgcolor=ic,
                        border_radius=5,
                    ),
                    ft.Row(
                        vertical_alignment="center",
                        spacing=10,
                        controls=[
                            ft.Image(
                                src="assets/icons/info.png",
                                color=sb_ic,
                                # scale=0.5
                            ),
                            ft.Text("Overview"),
                        ],
                    ),
                ],
            ),
        )

        self.chat_user_popup = ft.Container(
            offset=transform.Offset(0, -1),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            height=0,
            animate_offset=animation.Animation(500, "decelerate"),
            bgcolor=sbc,
            content=ft.Card(
                expand=True,
                elevation=15,
                content=ft.Container(
                    height=500,
                    width=500,
                    bgcolor=sbc,
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                padding=8,
                                width=140,
                                bgcolor=csc,
                                content=ft.Column(
                                    alignment="spaceBetween",
                                    spacing=5,
                                    controls=[
                                        ft.Column(
                                            expand=True,
                                            scroll="auto",
                                            controls=[
                                                self.chat_user_details_sidebar_item,
                                            ],
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Container(
                                                    on_click=self.close_chat_user_popup,
                                                    bgcolor=s_btn_h_c,
                                                    height=35,
                                                    border_radius=ih_br,
                                                    content=ft.Row(
                                                        alignment="center",
                                                        vertical_alignment="center",
                                                        controls=[
                                                            ft.Row(
                                                                vertical_alignment="center",
                                                                spacing=10,
                                                                controls=[
                                                                    ft.Image(
                                                                        src="assets/icons/info.png",
                                                                        color=sb_ic,
                                                                        # scale=0.5
                                                                    ),
                                                                    ft.Text("Close"),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                            ),
                            ft.Column(
                                expand=True,
                                controls=[
                                    ft.Stack(
                                        controls=[
                                            self.chat_user_details_sidebar_item_info
                                        ]
                                    )
                                ],
                            ),
                        ]
                    ),
                ),
            ),
        )

        self.settings_popup = ft.Container(
            border_radius=ih_br,
            bottom=30,
            left=80,
            height=0,
            offset=transform.Offset(0, 1.5),
            animate_offset=animation.Animation(500, "decelerate"),
            bgcolor=sbc,
            content=ft.Card(
                expand=True,
                elevation=15,
                content=ft.Container(
                    border_radius=ih_br,
                    height=500,
                    width=500,
                    bgcolor=sbc,
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                padding=8,
                                width=140,
                                bgcolor=csc,
                                content=ft.Column(
                                    alignment="spaceBetween",
                                    spacing=5,
                                    controls=[
                                        ft.Column(
                                            expand=True,
                                            scroll="auto",
                                            controls=[
                                                self.settings_sidebar_item,
                                            ],
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Container(
                                                    on_click=self.close_settings_popup,
                                                    bgcolor=s_btn_h_c,
                                                    height=35,
                                                    border_radius=ih_br,
                                                    content=ft.Row(
                                                        alignment="center",
                                                        vertical_alignment="center",
                                                        controls=[
                                                            ft.Row(
                                                                vertical_alignment="center",
                                                                spacing=10,
                                                                controls=[
                                                                    ft.Image(
                                                                        src="assets/icons/info.png",
                                                                        color=sb_ic,
                                                                        # scale=0.5
                                                                    ),
                                                                    ft.Text("Profile"),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                ft.Container(
                                                    on_click=self.close_settings_popup,
                                                    bgcolor=s_btn_h_c,
                                                    height=35,
                                                    border_radius=ih_br,
                                                    content=ft.Row(
                                                        alignment="center",
                                                        vertical_alignment="center",
                                                        controls=[
                                                            ft.Row(
                                                                vertical_alignment="center",
                                                                spacing=10,
                                                                controls=[
                                                                    ft.Image(
                                                                        src="assets/icons/info.png",
                                                                        color=sb_ic,
                                                                        # scale=0.5
                                                                    ),
                                                                    ft.Text("Close"),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                            ),
                            ft.Column(
                                expand=True,
                                controls=[
                                    ft.Stack(
                                        controls=[self.settings_sidebar_details_column]
                                    )
                                ],
                            ),
                        ]
                    ),
                ),
            ),
        )

        self.emoji_popup = ft.Container(
            animate_offset=animation.Animation(500, "decelerate"),
            border_radius=ih_br,
            bottom=50,
            left=120,
            height=0,
            offset=transform.Offset(0, 1.5),
            content=ft.Stack(
                controls=[
                    ft.Card(
                        expand=True,
                        elevation=30,
                        height=380,
                        width=500,
                    ),
                    ft.Container(
                        padding=ft.Padding.only(top=10, left=10, right=10),
                        border_radius=ih_br,
                        height=400,
                        width=500,
                        bgcolor=csc,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    alignment="spaceBetween",
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Text("Emoji", size=16),
                                                ft.Text(
                                                    "GIFs",
                                                    size=16,
                                                    color="white24",
                                                ),
                                                ft.Text(
                                                    "Stickers",
                                                    size=16,
                                                    color="white24",
                                                ),
                                            ]
                                        ),
                                        ft.Container(
                                            on_click=self.hide_emojis_popup,
                                            height=20,
                                            width=20,
                                            border_radius=ih_br,
                                            bgcolor="white12",
                                            content=ft.Icon(
                                                ft.Icons.CLOSE,
                                                size=12,
                                            ),
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    height=35,
                                    bgcolor=sbc,
                                    border_radius=ih_br,
                                    border=border.only(
                                        bottom=border.BorderSide(width=1, color=htc)
                                    ),
                                    content=ft.Row(
                                        alignment="spaceBetween",
                                        controls=[
                                            ft.Container(
                                                padding=ft.Padding.only(left=15, top=5),
                                                content=ft.TextField(
                                                    border=ft.InputBorder.NONE,
                                                    hint_text="Search emojis",
                                                    hint_style=ft.TextStyle(
                                                        size=14,
                                                        font_family="arial",
                                                        color=htc,
                                                    ),
                                                    color=sb_ic,
                                                    text_style=ft.TextStyle(
                                                        size=14,
                                                        font_family="arial",
                                                        color=sb_ic,
                                                    ),
                                                ),
                                            ),
                                            ft.Container(
                                                height=25,
                                                width=25,
                                                border_radius=ih_br,
                                                on_hover=self.sidebar_btn_hovered,
                                                content=ft.Icon(
                                                    ft.Icons.SEARCH_OUTLINED,
                                                    size=16,
                                                    color=htc,
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        )

    def load_messages(self, e):
        # Read the JSON file
        with open("data.json", "r") as file:
            data = json.load(file)

        # Access the data for a specific user
        username = "newton"
        for user_data in data["users"]:
            if user_data["name"] == username:
                break

        # Access the messages for the user
        messages = user_data["messages"]

        # Iterate through the messages
        for message in messages:
            print(message["message"])

    def close_settings_popup(self, e):
        print("fired")
        self.settings_popup.offset = transform.Offset(0, 1.5)
        self.settings_popup.update()
        sleep(0.51)
        self.settings_popup.height = 0
        self.settings_popup.update()

    def show_settings_popup(self, e):
        self.settings_popup.height = None
        self.settings_popup.offset = transform.Offset(0, 0)
        self.settings_popup.update()

    def close_chat_user_popup(self, e):
        self.chat_user_popup.offset = transform.Offset(0, -1)
        self.chat_user_popup.update()
        sleep(0.51)
        self.chat_user_popup.height = 0
        self.chat_user_popup.update()

    def show_chat_user_popup(self, e):
        self.chat_user_popup.height = None
        self.chat_user_popup.offset = transform.Offset(0, 0)
        self.chat_user_popup.update()

    def dm_screen_content_main(self):
        self.send_msg_btn = ft.Container(
            on_click=self.load_messages,
            on_hover=self.sidebar_btn_hovered,
            alignment=ft.Alignment.CENTER,
            height=40,
            width=40,
            border_radius=5,
            content=ft.Row(
                spacing=0,
                alignment="center",
                controls=[ft.Icon(ft.Icons.MIC_NONE_OUTLINED, size=20, color=sb_ic)],
            ),
        )

        self.msg_hover_emoji = ft.PopupMenuButton(
            tooltip=None,
            content=ft.Container(
                # on_click=
                tooltip=None,
                height=20,
                width=20,
                border_radius=25,
                content=ft.Icon(ft.Icons.EMOJI_EMOTIONS_OUTLINED, color=htc),
            ),
            items=[
                ft.PopupMenuItem(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="assets/icons/laugh.png",
                            ),
                            ft.Image(
                                src="assets/icons/laugh.png",
                            ),
                            ft.Image(
                                src="assets/icons/laugh.png",
                            ),
                            ft.Image(
                                src="assets/icons/laugh.png",
                            ),
                            ft.Image(
                                src="assets/icons/laugh.png",
                            ),
                            ft.Image(
                                src="assets/icons/laugh.png",
                            ),
                            ft.Image(
                                src="assets/icons/laugh.png",
                            ),
                            ft.Image(
                                src="assets/icons/laugh.png",
                            ),
                        ]
                    )
                )
            ],
            # )
        )

        self.msg_container = ft.Stack(
            # spacing=0,
            controls=[
                ft.Container(
                    margin=ft.Margin.only(right=6),
                    alignment=ft.Alignment.CENTER_LEFT,
                    width=500,
                    padding=10,
                    bgcolor=sc,
                    border_radius=ih_br,
                    content=ft.Column(
                        spacing=4,
                        controls=[
                            ft.Text(
                                value="Lorem  Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                                selectable=True,
                                color=smc,
                                weight=ft.FontWeight.W_400,
                                size=14,
                            ),
                            ft.Row(
                                spacing=4,
                                alignment="end",
                                controls=[
                                    ft.Text(
                                        "5:30 AM",
                                        size=10,
                                        weight=ft.FontWeight.W_600,
                                        color=mtc,
                                    ),
                                    ft.Icon(ft.Icon.DONE, color=mtc, size=10),
                                ],
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    height=20,
                    width=20,
                    shape=ft.BoxShape.RECTANGLE,
                    bgcolor=sc,
                    right=0,
                    border_radius=ft.BorderRadius(
                        top_left=0, top_right=0, bottom_left=0, bottom_right=20
                    ),
                ),
            ]
        )

        self.msg_obj = ft.Container(
            on_long_press=self.show_msg_menu,
            on_hover=self.msg_hovered,
            content=ft.Row(
                spacing=25,
                alignment="end",
                vertical_alignment="center",
                controls=[
                    self.msg_hover_emoji,
                    self.msg_container,
                ],
            ),
        )

        self.dm_screen_content = ft.Stack(
            controls=[
                ft.Container(
                    content=ft.Column(
                        spacing=0,
                        controls=[
                            ft.Row(
                                alignment="spaceBetween",
                                controls=[
                                    WindowDragArea(
                                        expand=True,
                                        content=ft.Container(
                                            height=40,
                                        ),
                                    ),
                                    ft.Row(
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                on_click=self.mini_window,
                                                height=40,
                                                width=40,
                                                content=ft.Image(
                                                    src="assets/icons/mini.png"
                                                ),
                                            ),
                                            ft.Container(
                                                on_click=self.max_window,
                                                height=40,
                                                width=40,
                                                content=ft.Image(
                                                    src="assets/icons/max.png"
                                                ),
                                            ),
                                            ft.Container(
                                                on_click=self.close_window,
                                                height=40,
                                                width=40,
                                                content=ft.Image(
                                                    src="assets/icons/close.png"
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            ft.Container(
                                padding=ft.Padding.only(left=20, right=15),
                                height=50,
                                content=ft.Row(
                                    alignment="spaceBetween",
                                    controls=[
                                        ft.Container(
                                            on_click=self.show_chat_user_popup,
                                            expand=True,
                                            content=ft.Row(
                                                controls=[
                                                    ft.Container(
                                                        height=40,
                                                        width=40,
                                                        border_radius=20,
                                                        bgcolor=rc,
                                                        content=ft.Icon(ft.Icon.PERSON),
                                                    ),
                                                    ft.Text(value="#Se7en🙏"),
                                                ]
                                            ),
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    on_hover=self.sidebar_btn_hovered,
                                                    alignment=ft.Alignment.CENTER,
                                                    height=s_btn_h,
                                                    width=s_btn_w,
                                                    border_radius=5,
                                                    content=ft.Row(
                                                        spacing=0,
                                                        alignment="center",
                                                        controls=[
                                                            ft.Icon(
                                                                ft.Icon.VIDEO_CALL_OUTLINED,
                                                                size=20,
                                                                color=sb_ic,
                                                            )
                                                        ],
                                                    ),
                                                ),
                                                ft.Container(
                                                    on_hover=self.sidebar_btn_hovered,
                                                    alignment=ft.Alignment.CENTER,
                                                    height=s_btn_h,
                                                    width=s_btn_w,
                                                    border_radius=5,
                                                    content=ft.Row(
                                                        spacing=0,
                                                        alignment="center",
                                                        controls=[
                                                            ft.Icon(
                                                                ft.Icon.CALL_OUTLINED,
                                                                size=20,
                                                                color=sb_ic,
                                                            )
                                                        ],
                                                    ),
                                                ),
                                                ft.Container(
                                                    height=25,
                                                    width=2,
                                                    bgcolor=s_btn_h_c,
                                                ),
                                                ft.Container(
                                                    on_hover=self.sidebar_btn_hovered,
                                                    alignment=ft.Alignment.CENTER,
                                                    height=s_btn_h,
                                                    width=s_btn_w,
                                                    border_radius=5,
                                                    content=ft.Row(
                                                        spacing=0,
                                                        alignment="center",
                                                        controls=[
                                                            ft.Icon(
                                                                ft.Icon.SEARCH_OUTLINED,
                                                                size=20,
                                                                color=sb_ic,
                                                            )
                                                        ],
                                                    ),
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                            ),
                            ft.Container(
                                alignment=ft.Alignment.TOP_LEFT,
                                padding=ft.Padding.only(left=20, right=20, top=10),
                                expand=True,
                                image_src=wallpaper,
                                image_opacity=0.2,
                                image_fit=ft.ImageFit.COVER,
                                bgcolor="#1a343434",
                                content=ft.Column(
                                    scroll="auto",
                                    spacing=10,
                                    controls=[
                                        self.msg_obj,
                                    ],
                                ),
                            ),
                            ft.Container(
                                margin=ft.Margin.only(left=2),
                                padding=ft.Padding.only(left=10, right=10),
                                height=50,
                                bgcolor=csc,
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            on_hover=self.sidebar_btn_hovered,
                                            on_click=self.show_emojis_popup,
                                            alignment=ft.Alignment.CENTER,
                                            height=40,
                                            width=40,
                                            border_radius=5,
                                            content=ft.Row(
                                                spacing=0,
                                                alignment="center",
                                                controls=[
                                                    ft.Icon(
                                                        ft.Icon.EMOJI_EMOTIONS_OUTLINED,
                                                        size=20,
                                                        color=sb_ic,
                                                    )
                                                ],
                                            ),
                                        ),
                                        ft.Container(
                                            on_hover=self.sidebar_btn_hovered,
                                            alignment=ft.Alignment.CENTER,
                                            height=40,
                                            width=40,
                                            border_radius=5,
                                            content=ft.Row(
                                                spacing=0,
                                                alignment="center",
                                                controls=[
                                                    ft.Icon(
                                                        ft.Icon.SHARE_OUTLINED,
                                                        size=20,
                                                        color=sb_ic,
                                                    )
                                                ],
                                            ),
                                        ),
                                        ft.Container(
                                            on_hover=self.sidebar_btn_hovered,
                                            expand=True,
                                            content=ft.TextField(
                                                expand=True,
                                                multiline=True,
                                                border=ft.InputBorder.NONE,
                                                hint_text="Type a message",
                                                hint_style=ft.TextStyle(
                                                    size=14,
                                                    font_family="arial",
                                                    color=htc,
                                                ),
                                                color=sb_ic,
                                                text_style=ft.TextStyle(
                                                    size=14,
                                                    font_family="arial",
                                                    color=sb_ic,
                                                ),
                                            ),
                                        ),
                                        self.send_msg_btn,
                                    ]
                                ),
                            ),
                        ],
                    )
                ),
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            self.chat_user_popup,
                        ]
                    )
                ),
            ]
        )


t = App
ft.app(target=t, assets_dir="assets")

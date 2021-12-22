from kivymd.app import MDApp
from kivy.lang import Builder
from kivy import properties as P
from kivymd.uix.card import MDCard
from kivy.animation import Animation


KV = """
#: import C kivy.utils.get_color_from_hex

<TransitionBox>:
    size: info_box.size
    size_hint: None, None
    md_bg_color: C("#00AAFF")
    on_release: self.active = (not self.active)
    MDBoxLayout:
        id: info_box
        padding: dp(15), dp(15)
        orientation: "vertical"
        size: dp(250), dp(150)
        size_hint: None, None
        md_bg_color: 1,1,1,1
        MDLabel:
            text: root.title
            font_style: "H5"
            halign: "center"
        MDLabel:
            text: root.description
            halign: "center"
    MDFloatLayout:
        size_hint_y: None
        height: 0
        MDBoxLayout:
            id: icon_box
            size_hint: None, None
            size: info_box.size
            pos: info_box.pos
            md_bg_color: root.md_bg_color
            AnchorLayout:
                anchor_x: "center"
                anchor_y: "center"
                MDIcon:
                    icon: root.icon
                    color: root.md_bg_color
                    size_hint: None, None
                    md_bg_color: 1,1,1,1
                    size: dp(64), dp(60)
                    radius: [dp(10)]
                    font_size: sp(50)
                    halign: "center"

MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(10), dp(20)
                adaptive_height: True
                spacing: dp(20)
                TransitionBox:
                    pos_hint: {"center_x": .5}
                    icon: "linkedin"
                    md_bg_color: C('#dd7765')
                    title: "@adamdipinto"
                    description: "This is where i network and build my professional portfolio."
                TransitionBox:
                    pos_hint: {"center_x": .5}
                    icon: "twitter"
                    md_bg_color: C('#6dadd3')
                    title: "@AdamDipinto"
                    description: "This is where i read news and network with different social groups."
                TransitionBox:
                    pos_hint: {"center_x": .5}
                    icon: "github"
                    md_bg_color: C('#48ada6')
                    title: "atom888"
                    description: "This is where i share code and work on projects."
"""


class TransitionBox(MDCard):
    active = P.BooleanProperty(0)
    icon = P.StringProperty("circle")
    title = P.StringProperty("-")
    description = P.StringProperty("-")

    def on_active(self, *args):
        if self.active:
            y = self.ids.info_box.top
            h = self.height * 2
        else:
            y = self.ids.info_box.y
            h = self.height / 2
        Animation(height=h, duration=0.2).start(self)
        Animation(y=y, duration=0.2).start(self.ids.icon_box)


class MainScreenApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    MainScreenApp().run()

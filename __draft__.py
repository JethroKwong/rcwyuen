class WelcomeScreen(Screen):
    def welcome(self):
        g1 = GridLayout(cols=1)
        box1 = BoxLayout(orientation='vertical')
        l1 = Label(text="WeFidget! Powered By Team WeFidget", font_size=25)
        l2 = Label(text=str("Current Time: " + str(datetime.today())), font_size=25)
        l3 = Label(text="We highly appreciate feedback from all users, PLEASE DO HELP US!!!", font_size=20)
        b1 = Button(text="Continue", font_size=25)
        b1.bind(on_press=lambda instance, a: build())
        g1.add_widget(l1)
        g1.add_widget(l2)
        g1.add_widget(l3)
        g1.add_widget(b1)
        box1.add_widget(g1)

class MenuScreen(Screen):
    def build(self):
        box1 = BoxLayout(orientation='vertical')  # outer shell
        box2 = BoxLayout(orientation='vertical')  # inner shell 1
        g1 = GridLayout(cols=1)
        g2 = GridLayout(cols=1)
        g3 = GridLayout(cols=2)
        b1 = Button(text = "Settings", font_size = 25)
        b2 = Button(text = "Daily Report", font_size = 25)
        b3 = Button(text = "Steps Count", font_size=25)
        b4 = Button(text = "Update", font_size=25)
        b5 = Button(text = "Fidget Count", font_size=25)
        b6 = Button(text = "Battery Status", font_size=25)
        b7 = Button(text = "Find WeFidget", font_size=25)
        b8 = Button(text = "Quit", font_size = 25)
        g1.add_widget(b2)
        g1.add_widget(b3)
        g1.add_widget(b5)
        g1.add_widget(b7)
        g2.add_widget(b1)
        g2.add_widget(b4)
        g2.add_widget(b6)
        g2.add_widget(b8)
        g3.add_widget(g1)
        g3.add_widget(g2)
        box2.add_widget(g3)
        box1.add_widget(box2)

class DrawInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        print(touch)
        touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        print("RELEASED!", touch)
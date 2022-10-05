
class TVController:

    def __init__(self, channel):
        self.channel = channel
        self.curent_channel = 0

    def first_channel(self):
        self.curent_channel = 0
        return self.channel[0]

    def last_channel(self):
        self.curent_channel = len(self.channel) - 1
        return self.channel[self.curent_channel]

    def turn_channel(self, channels_number):
        self.curent_channel = channels_number - 1
        return self.channel[self.curent_channel]

    def next_channel(self):
        if self.curent_channel == len(self.channel) - 1:
            self.curent_channel = 0
        else:
            self.curent_channel += 1
        return self.channel[self.curent_channel]

    def previous_channel(self):
        if self.curent_channel == 0:
            self.curent_channel = len(self.channel) - 1
        else:
            self.curent_channel -= 1
        return self.channel[self.curent_channel]

    def current_channel(self):
        return self.channel[self.curent_channel]

    def is_exist(self, channels_number1):
        if type(channels_number1) == int:
            if 1 <= channels_number1 <= len(self.channel):
                return "Yes"
        elif channels_number1 in self.channel:
            return "Yes"

        return "NO"


controller = TVController(["BBC", "Discovery", "TV1000"])

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(2))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
print("current_channel: ", controller.current_channel())

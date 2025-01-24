CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self):
        self.channels = CHANNELS
        self.current_channel = 0

    def get_channel_info(self, index):
        return f"Channel was turned on {self.channels[index]} (--{index + 1}--)"

    def first_channel(self):
        self.current_channel = 0
        return self.get_channel_info(self.current_channel)

    def last_channel(self):
        self.current_channel = len(self.channels) - 1
        return self.get_channel_info(self.current_channel)

    def turn_channel(self, n):
        if 1 <= n <= len(self.channels):
            self.current_channel = n - 1
            return self.get_channel_info(self.current_channel)
        else:
            return "Invalid channel number"

    def next_channel(self):
        if self.current_channel == len(self.channels) - 1:
            self.current_channel = 0
            return self.get_channel_info(self.current_channel)
        else:
            self.current_channel += 1
            return self.get_channel_info(self.current_channel)

    def previous_channel(self):
        if self.current_channel == 0:
            self.current_channel = len(self.channels) - 1
            return self.get_channel_info(self.current_channel)
        else:
            self.current_channel -= 1
            return self.get_channel_info(self.current_channel)

    def current_channel_info(self):
        return f"Currently on {self.channels[self.current_channel]} (--{self.current_channel + 1}--)"

    def exists(self, channel):
        if isinstance(channel, int):
            if 1 <= channel <= len(self.channels):
                return "Yes"
            else:
                return "There isn't such channel"

        elif isinstance(channel, str):
            channel = channel.upper()
            ch_up = [ch.upper() for ch in self.channels]
            if channel in ch_up:
                return "Yes"
            else:
                return "There isn't such channel"
        else:
            return "There isn't such channel"


test = TVController()

print(test.first_channel())
print(test.current_channel_info())
print(test.last_channel())
print(test.current_channel_info())
print(test.turn_channel(3))
print(test.current_channel_info())
print(test.next_channel())
print(test.current_channel_info())
print(test.previous_channel())
print(test.current_channel_info())
print(test.previous_channel())
print(test.current_channel_info())
print(test.previous_channel())
print(test.current_channel_info())
print(test.previous_channel())
print(test.current_channel_info())
print(test.exists('bbc'))

import emoji
import psutil
import rumps

from utils import convert_value


def get_emoticon(percentage):
    if percentage <= 50:
        return 'star-struck'
    elif percentage <= 75:
        return 'worried'
    else:
        return 'rage'


def get_memory():
    """

    :return:
    """
    mem_usage = psutil.virtual_memory()
    available, available_unit = convert_value(mem_usage.used)
    total, total_unit = convert_value(mem_usage.total)
    pct = round(mem_usage.percent, 2)
    message = emoji.emojize("{0}{1}/{2}{3} [{4}%] :{5}:".format(available, available_unit, total,
                                                                total_unit, pct, get_emoticon(pct)), use_aliases=True)
    return message


class BatteryIndicator(rumps.App):
    def __init__(self, *args, **kwargs):
        super(BatteryIndicator, self).__init__(*args, **kwargs)

    @rumps.timer(2.5)
    def update(self, _):
        """

        :param _:
        :return:
        """
        self.title = get_memory()


if __name__ == "__main__":
    bi = BatteryIndicator(name='Memory Indicator', quit_button=None)
    bi.run()

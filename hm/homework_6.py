class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


# 2026 гибриды:

class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):

        return f"{self.live()} | {self.superpower()} / И всё это  в прямом эфире "


class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
         f"{self.live()} / {self.superpower()} / {self.viral()} "


class DonateMage(Streamer, TikToker):
    def ultimate_content(self):

        return f"{self.live()} | {self.earn()} / И ещё клип нарезал под тренд "


def demo(obj):
    cls = obj.__class__
    print(f"\n=== {cls.__name__} ===")
    print("MRO:", [c.__name__ for c in cls.mro()])
    print("live():", obj.live())
    print("ultimate_content():", obj.ultimate_content())


if __name__ == "__main__":
    demo(GlowStreamer())
    demo(ViralCyborg())
    demo(DonateMage())
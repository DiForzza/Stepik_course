class Video:
    def __init__(self):
        self.name = None

    def create(self, name):
        self.name = name

    def play(self):
        print(f'воспроизведение видео {self.name}')


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video.name)

    @classmethod
    def play(cls, video_indx):
        video_indx.play()


v1 = Video()
v1.create('Python')
v2 = Video()
v2.create('Python ООП')
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(v1)
YouTube.play(v2)

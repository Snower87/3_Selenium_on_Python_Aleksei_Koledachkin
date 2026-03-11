
from pytube import YouTube

# Ссылка на видео
#video_url = 'https://www.youtube.com/watch?v=ваш_видео_ID'
video_url = 'https://www.youtube.com/watch?v=TUbSmnQP3Y0'

# Создаем объект YouTube
yt = YouTube(video_url)

# Выбираем поток с наилучшим качеством видео+аудио
stream = yt.streams.get_highest_resolution()

# Скачиваем видео в текущую папку
stream.download()

print("Видео успешно скачано!")

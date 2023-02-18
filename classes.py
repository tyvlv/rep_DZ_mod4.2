import os
import json
from googleapiclient.discovery import build


class Channel:
    """Класс канала Youtube"""
    # YoutubeAPI_key скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YoutubeAPI_key')

    # создает специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id):
        self.channel_id = channel_id

        # получает данные о канале по его ID
        self.info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self):
        """Вывод в консоль информации о канале Youtube"""
        print(json.dumps(self.info, indent=2, ensure_ascii=False))

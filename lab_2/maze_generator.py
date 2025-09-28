from abc import ABC, abstractmethod


class MazeGenerator(ABC):
    @classmethod
    @abstractmethod
    def create(cls, width, height, rand):
        """
        Создаёт экземпляр лабиринта указанного размера и конфигурации
        :param width: Ширина создаваемого лабиринта
        :param height: Высота создаваемого лабиринта
        :param rand: Флаг cлучайной генерации или использования шаблона
        :return: Новый экземпляр лабиринта с заданными параметрами
        """
        pass
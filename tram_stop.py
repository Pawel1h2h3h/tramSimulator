from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QBrush, QColor, QFont
from PySide6.QtWidgets import QGraphicsItem
from PySide6.QtCore import Qt



class TramStop(QGraphicsItem):
    def __init__(self,
                 id: int,
                 position: tuple,
                 line=None):
        super().__init__()
        self._name = f'Stop {id}'
        self.setPos(*position)  # Ustawianie początkowej pozycji
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self._line = line
        self._id = id
        self.neighbours = []

        self._lenght = 20
        self._width = 10

    def boundingRect(self) -> QRectF:
        # Zwraca prostokąt ograniczający w lokalnych współrzędnych
        return QRectF(0, 0, self._lenght, self._width)

    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(QColor(10, 100, 200)))
        painter.drawRoundedRect(self.boundingRect(), 3, 3)
        painter.drawText(self.boundingRect(), Qt.AlignCenter, f'{self._id}')
        painter.setFont(QFont("Arial", 6))


    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            if self._line:
                self._line.update_path()
        return super().itemChange(change, value)

    def let_stop_know_about_line(self, line):
        self._line = line

    def name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def id(self):
        return self._id

    def line(self):
        return self._line


    def is_occupied(self):
        pass


    def info(self):
        return f'Stop {self._id} at {self.pos()}'

    def __str__(self):
        return f'Stop {self._id}'

    def to_json(self):
        position = self.pos()
        position = (position.x(), position.y())
        id = self.id()
        almost_saved = {
                "id": id,
                "position": position,
            }

        return almost_saved
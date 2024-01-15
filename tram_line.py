from PySide6.QtWidgets import QGraphicsPathItem, QGraphicsPathItem
from PySide6.QtGui import QPainterPath, QPen, QColor
from PySide6.QtCore import Qt


from .tram import Tram



class TramLine(QGraphicsPathItem):
    """Klasa reprezentująca linię tramwajową"""
    def __init__(self,
                 id,
                 trams_number):
        super().__init__()
        self._id = id
        self._stops = []
        self._trams_number = trams_number
        self._trams = []
        self.style()

    def style(self):
        pen = QPen(QColor(0, 160, 90))
        pen.setWidth(2)
        pen.setStyle(Qt.PenStyle.DashLine)
        self.setPen(pen)


    def update_path(self):
        """Aktualizuje ścieżkę linii"""
        path = QPainterPath()
        if self._stops:
            path.moveTo(self._stops[0].pos())
            for stops in self._stops[1:]:
                path.lineTo(stops.pos())
        self.setPath(path)



    def add_stop(self, stop):
        """Dodaje przystanek do linii i aktualizuje ścieżkę"""
        stop.let_stop_know_about_line(self)
        self._stops.append(stop)
        self.update_path()


    def remove_stop(self, stop):
        """Usuwa przystanek z linii i aktualizuje ścieżkę"""
        self._stops.remove(stop)
        self.update_path()


    def create_trams(self):
        """Tworzy tramwaje na linii"""
        for i in range(self._trams_number):
            self._trams.append(Tram(i+1, self))

    def set_trams_number(self, number):
        """Ustawia liczbę tramwajów na linii"""
        self._trams_number = number


    def startTram(self):
        """Animuje tramwaje na linii"""
        pass



    def id(self):
        return self._id

    def stops(self):
        return self._stops

    def trams(self):
        return self._trams

    def to_json(self):
        id = self.id()
        trams_number = self._trams_number
        stops = self.stops()
        trams = self.trams()
        almost_saved = {
                            'id': id,
                            'trams_number': trams_number,
            }

        return almost_saved


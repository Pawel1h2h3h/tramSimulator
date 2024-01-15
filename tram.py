from PySide6.QtGui import QColor, QBrush
from PySide6.QtWidgets import QGraphicsEllipseItem
from PySide6.QtCore import QVariantAnimation



class Tram(QGraphicsEllipseItem):
    """Class representing a tram."""

    def __init__(self, id: int, line):
        super().__init__()
        self._id = id
        self._line = line
        self.timelines = []
        self._points = []
        self.forwardAnimations = []
        self.backwardAnimations = []



    def id(self):
        return self._id

    def line(self):
        return self._line

    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(QColor(200, 80, 0)))
        painter.drawEllipse(self.boundingRect())
        self.setRect(0, 0, 10, 10)


    def get_point_positions(self):
        """Returns a list of points positions."""
        for stop in self._line.stops():
            self._points.append(stop.pos())


    def animate(self, time_of_travel: int):
        self.forwardAnimations = []
        for i in range(len(self._points) - 1):
            animation = QVariantAnimation()
            animation.setDuration(time_of_travel)
            animation.setStartValue(self._points[i])
            animation.setEndValue(self._points[i + 1])

            animation.valueChanged.connect(self.setPos)
            self.forwardAnimations.append(animation)



    def animateBack(self, time_of_travel: int):
        points = self._points.copy()
        points.reverse()
        self.backwardAnimations = []
        for i in range(len(self._points) - 1):
            animation = QVariantAnimation()
            animation.setDuration(time_of_travel)
            animation.setStartValue(points[i])
            animation.setEndValue(points[i+1])

            animation.valueChanged.connect(self.setPos)
            self.backwardAnimations.append(animation)


    def connectAnimations(self):
        for i in range(len(self.forwardAnimations)-1):
            self.forwardAnimations[i].finished.connect(self.forwardAnimations[i + 1].start)
            self.backwardAnimations[i].finished.connect(self.backwardAnimations[i + 1].start)
        for i in range(1):
            self.forwardAnimations[-1].finished.connect(self.backwardAnimations[0].start)
            self.backwardAnimations[-1].finished.connect(self.forwardAnimations[0].start)



    def start(self, time_of_travel: int):
        self.get_point_positions()
        self.animate(time_of_travel)
        self.animateBack(time_of_travel)
        self.connectAnimations()
        if self.forwardAnimations:
            self.forwardAnimations[0].start()

    def stop(self):
        for animation in self.forwardAnimations:
            animation.stop()
        for animation in self.backwardAnimations:
            animation.stop()


    def to_json(self):
        id = self.id()
        line = self.line()
        almost_saved = {
                'id': id,
                'line': line.id()
            }

        return almost_saved


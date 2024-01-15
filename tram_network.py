from PySide6.QtCore import  QTimer
import random

from .tram_line import TramLine
from .tram_stop import TramStop


timer = QTimer()
timer.start(1000)



class TramNetwork:
    """Klasa reprezentująca sieć tramwajową"""
    def __init__(self,
                id: int,
                lines_number: int,
                stops_in_single_line_number: int,
                time_of_travel: int,
                ):
        self._id = id
        self._lines = []
        self._stops = []
        self._start_positions = []
        self._time_of_travel = time_of_travel
        self._lines_number = lines_number
        self._stops_in_line_number = stops_in_single_line_number
        self._trams = []


    # GETTERS AND SETTERS

    def trams(self):
        return self._trams

    def lines(self):
        return self._lines

    def stops(self):
        return self._stops

    def positions(self):
        return self._start_positions

    def id(self):
        return self._id

    def lines_number(self):
        return self._lines_number

    def stops_in_line_number(self):
        return self._stops_in_line_number

    def set_lines_number(self, lines_number):
        self._lines_number = lines_number

    def set_stops_in_line_number(self, stops_in_line_number):
        self._stops_in_line_number = stops_in_line_number

    def set_trams_number_in_single_line(self, trams_number):
        self._trams_number = trams_number

    def time_of_travel(self):
        return self._time_of_travel


    def add_stop(self, stop, line):
        stop.let_stop_know_about_line(line) # Przekaż przystanek linii
        self._stops.append(stop) # Dodaj przystanek do listy przystanków

    def add_stop_to_line(self, stop, line):
        stop.let_stop_know_about_line(line) # Przekaż przystanek linii

    def add_stops_to_network(self, stop):
        self._stops.append(stop)

    def add_tram(self, tram):
        self._trams.append(tram)


    def remove_stop(self, stop):
        self._stops.remove(stop) # Usuń przystanek z listy przystanków


    def add_line(self, line):
        self._lines.append(line) # Dodaj linię do listy linii

    def remove_line(self, line):
        self._lines.remove(line) # Usuń linię z listy linii


    def position_generator(self, _range, difference):
        """Generuje pozycje przystanków na mapie"""
        number_of_stops = self._lines_number * self._stops_in_line_number
        pos = []
        possible_pos = [(x, y) for x in range(0, _range + 1, difference)
                                for y in range(0, _range + 1, difference)]

        while len(pos) < number_of_stops and possible_pos:
            single_position = random.choice(possible_pos)
            pos.append(single_position)
            # Usuń wybraną pozycję i sąsiednie pozycje, aby zapewnić minimalną różnicę
            possible_pos = [p for p in possible_pos if all(abs(p[i] - single_position[i]) >= difference for i in range(2))]
        self._start_positions.extend(pos)



    def stops_generator(self):
        """Generuje przystanki na mapie"""
        positions = self._start_positions
        new_stops = []
        n = 0
        for position in positions:
            n += 1
            new_stop = TramStop(id=n, position=position)
            new_stops.append(new_stop)
        self._stops.extend(new_stops)


    def sort_stops(self):
        """Sortuje przystanki według id"""
        self._stops.sort(key=lambda stop: stop.id())


    def lines_generator(self, trams_number=3):
        """Generuje linie tramwajowe"""
        new_lines = []
        stops1 = self._stops.copy()  # Używamy kopii, aby nie modyfikować oryginalnej listy
        for i in range(1, self._lines_number+1):
            new_line = TramLine(id=i, trams_number=trams_number)
            new_lines.append(new_line)
            for _ in range(self._stops_in_line_number):
                if stops1:  # Sprawdź, czy są jeszcze jakieś przystanki do dodania
                    stop = stops1.pop(0)  # Usuń przystanek z listy dostępnych
                    new_line.add_stop(stop)
            new_line.set_trams_number(trams_number)
            new_line.create_trams()
        self._lines.extend(new_lines)


    def add_stops_to_line(self):
        """Dodaje przystanki do linii, każda linia otrzymuje unikalne przystanki"""
        stops = self._stops.copy()  # Używamy kopii, aby nie modyfikować oryginalnej listy

        for line in self._lines:
            for _ in range(self._stops_in_line_number):
                if stops:  # Sprawdź, czy są jeszcze jakieś przystanki do dodania
                    stop = stops.pop(0)  # Usuń przystanek z listy dostępnych
                    line.add_stop(stop)  # Dodaj przystanek do linii


    def get_trams(self):
        for line in self._lines:
            for tram in line.trams():
                self._trams.append(tram)


    def defoults(self):
        """Generuje domyślną sieć tramwajową"""
        self.position_generator(1000, 10)
        self.stops_generator()
        self.sort_stops()
        self.lines_generator()
        self.get_trams()


    def custom(self, trams_number):
        """Generuje sieć tramwajową z podanych parametrów"""
        self.position_generator(1500, 10)
        self.stops_generator()
        self.sort_stops()
        self.lines_generator(trams_number)
        self.get_trams()

    def to_json(self):
        """Zapisuje sieć tramwajową do pliku"""
        id = self.id()
        travel_time = self.time_of_travel()


        lines = self.lines()
        stops = self.stops()
        trams = self.trams()


        almost_saved = [
            {
                'id': id,
                'travel_time': travel_time,
                'lines': [line.to_json() for line in lines],
                'stops': [stop.to_json() for stop in stops],
                'trams': [tram.to_json() for tram in trams]
            }
        ]
        return almost_saved


#guiMain.py
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QTreeWidgetItem, QFileSystemModel, QListView
from PySide6.QtCore import QTime
import sys
import json
import os

# Importowanie klas interfejsu użytkownika
from data_structure.ui_designer_files.ui_simple_gui import Ui_MainWindow
from data_structure.ui_designer_files.ui_modify_trams import Ui_ModifyNetwork as Ui_ModifyWindow
from data_structure.ui_designer_files.ui_map1 import Ui_Map
from data_structure.ui_designer_files.ui_open_window import Ui_OpenWidow

# Importowanie struktury danych
from data_structure.tram_network import TramNetwork, timer

from data_structure.tram_stop import TramStop
from data_structure.tram_line import TramLine
from data_structure.tram import Tram



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tram Network Simulator")
        self.setStyleSheet(
            """
            QMainWindow {background-image: url('icon.png');
                         background-repeat: no-repeat;
                         background-position: center;}
            """
        )
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.DefaultButton.clicked.connect(self.openWindowDefault)
        self.ui.Open.clicked.connect(self.openWindowOpen)
        self.ui.ModifyButton.clicked.connect(self.openWindowModify)
        self.show()

    def openWindowDefault(self):
        """Otwiera okno Mapy."""
        self.window = MapWindow()
        self.window.show()

    def openWindowModify(self):
        """Otwiera okno Modyfikacji."""
        self.window = ModifyWindow()
        self.window.show()

    def openWindowOpen(self):
        """Otwiera okno Otwierania."""
        self.window = OpenWindow()
        self.window.show()



class MapWindow(QMainWindow):
    def __init__(self):
        super(MapWindow, self).__init__()
        self.initUI()
        self.defaultNetwork = TramNetwork(1, 10, 10, 5000)
        self.defaultNetwork.defoults()
        self.setWindowTitle("Map view")
        self.IsShowClicked = False
        self.IsstartClicked = False
        self.isAnimationStopped = False

    def initUI(self):
        self.ui = Ui_Map()
        self.ui.setupUi(self)

        self.setupScene()

        self.ui.Start.clicked.connect(lambda: self.animateTram(self.defaultNetwork))
        self.ui.Start.clicked.connect(lambda: timer.start(1000))
        self.ui.Start.clicked.connect(self.startClicked)

        self.ui.showNetwork.clicked.connect(lambda: self.drawTramNetwork(self.defaultNetwork))
        self.ui.showNetwork.clicked.connect(self.showClicked)

        self.ui.Save.clicked.connect(lambda: self.saveNetworkToFile(self.defaultNetwork))

        self.ui.Stop.clicked.connect(lambda: self.stopAnimation(self.defaultNetwork))
        self.ui.Stop.clicked.connect(lambda : timer.stop())


        self.time = QTime.currentTime()
        timer.timeout.connect(self.update_time)
        self.ui.timeEdit.setTime(self.time)
        self.show()


    def setupScene(self):
        """Ustawia scenę dla mapy."""
        self.scene = QGraphicsScene(self)
        self.ui.Map_2.setScene(self.scene)




    def drawTramStop(self, tramstop):
        """Rysuje przystanek na mapie."""
        self.scene.addItem(tramstop)



    def drawTramLine(self, tramline):
        """Rysuje linię tramwajową na mapie."""
        self.scene.addItem(tramline)



    def drawTramNetwork(self, network):
        """Rysuje sieć tramwajową na mapie."""
        for stop in network.stops():
            self.drawTramStop(stop)
        for line in network.lines():
            self.drawTramLine(line)



    def update_time(self):
        self.time = self.time.addSecs(60)
        self.ui.timeEdit.setTime(self.time)


    def stopAnimation(self, network):
        """Zatrzymuje animację tramwajów."""
        self.isAnimationStopped = True
        for line in network.lines():
            for tram in line.trams():
                tram.stop()


    def saveNetworkToFile(self, network):
        """Zapisuje sieć tramwajową do pliku."""
        n = len([name for name in os.listdir('saved_files')])
        path = f'saved_files/network_{n}.json'
        # path = 'saved_files/Trams in Warsaw.json'
        with open(path, "w") as file:
            file.write(json.dumps(network.to_json(), indent=4))



    def animateTram(self, network):
        """Animuje tramwaje na mapie."""
        delay = 0  # Początkowe opóźnienie
        delay_increment = 2000  # Opóźnienie między tramwajami w milisekundach

        for line in network.lines():
            for tram in line.trams():
                timer.singleShot(delay, lambda tram=tram: self.startTramAnimation(tram, network) if not self.isAnimationStopped else None)
                delay += delay_increment


    def startTramAnimation(self, tram, network):
        """Rozpoczyna animację dla pojedynczego tramwaju."""
        if not self.isAnimationStopped:  # Sprawdzenie, czy animacja nie została zatrzymana
            tram.start(network.time_of_travel())
            self.scene.addItem(tram)


    def showClicked(self):
        self.IsShowClicked = True
        if self.IsShowClicked == True:
            self.ui.showNetwork.setEnabled(False)


    def startClicked(self):
        self.IsstartClicked = True
        if self.IsstartClicked == True:
            self.ui.Start.setEnabled(False)



class MapOpenWindow(MapWindow):
    def __init__(self, file_path):
        super(MapOpenWindow, self).__init__()
        self.initUI()
        self.setWindowTitle("Map view")
        self._file_path = file_path
        self._network = None
        self.json_to_network()


    def initUI(self):
        self.ui = Ui_Map()
        self.ui.setupUi(self)
        self.setupScene()

        self.ui.showNetwork.clicked.connect(lambda: self.drawTramNetwork(self._network))
        self.ui.showNetwork.clicked.connect(self.showClicked)


        self.ui.Start.clicked.connect(lambda: timer.start(1000))
        self.ui.Start.clicked.connect(lambda: self.animateTram(self._network))
        self.ui.Start.clicked.connect(self.startClicked)



        self.ui.Save.clicked.connect(lambda: self.saveNetworkToFile(self._network))

        self.ui.Stop.clicked.connect(timer.stop)
        self.ui.Stop.clicked.connect(lambda: self.stopAnimation(self._network))


        self.time = QTime.currentTime()
        timer.timeout.connect(self.update_time)
        self.ui.timeEdit.setTime(self.time)
        self.show()


    ###Open Network

    def loadDataFromFile(self):
        with open(self._file_path, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                for dictionary in data:
                    id = dictionary['id']
                    travel_time = dictionary['travel_time']
                    lines = dictionary['lines']
                    stops = dictionary['stops']
                    trams = dictionary['trams']
                return id, travel_time, lines, stops, trams
            elif isinstance(data, dict):
                id = data['id']
                travel_time = data['travel_time']
                lines = data['lines']
                stops = data['stops']
                trams = data['trams']
                return id, travel_time, lines, stops, trams



    def json_to_objects(self):
        """Zamienia dane z pliku na obiekty."""
        lines1 = []
        stops1 = []
        trams1 = []
        id1, travel_time1, lines, stops, trams =  self.loadDataFromFile()
        for json_tram in trams:
            id = json_tram['id']
            line = json_tram['line']
            tram = Tram(id, line)
            trams1.append(tram)

        for json_line in lines:
            id = json_line['id']
            trams_number = json_line['trams_number']
            line = TramLine(id, trams_number)
            lines1.append(line)

        for json_stop in stops:
            id = json_stop['id']
            position = json_stop['position']
            stop = TramStop(id, position, line)
            stops1.append(stop)

        return id1, travel_time1, lines1, stops1, trams_number




    def json_to_network(self):
        id, travel_time, lines, stops, number = self.json_to_objects()
        saved_network = TramNetwork(
            id=id,
            lines_number=len(lines),
            stops_in_single_line_number=len(stops)//len(lines),
            time_of_travel=travel_time
            )

        for stop in stops:
            saved_network.add_stops_to_network(stop)
        saved_network.sort_stops()
        saved_network.lines_generator(number)
        saved_network.get_trams()
        self._network = saved_network




class ModifyWindow(QMainWindow):
    def __init__(self):
        super(ModifyWindow, self).__init__()

        self.initUI()
        self.setWindowTitle("Custiomize network")
        self.tramCount = 1
        self.stopCount = 1


    def initUI(self):
        self.ui = Ui_ModifyWindow()
        self.ui.setupUi(self)
        self.setupFrame()
        self.clicked = 0

        self.ui.StartSimulation.clicked.connect(self.openWindowMap)


        self.ui.addStop.clicked.connect(self.addStop)
        self.ui.addStop.clicked.connect(self.clickedcount)

        self.ui.addTram.clicked.connect(self.addTram)
        self.ui.addTram.clicked.connect(self.clickedcount)


        self.ui.addLine.clicked.connect(self.addLine)

        self.show()


    def openWindowMap(self):
        """Otwiera okno Mapy."""
        lineCount = self.getLineCount()
        time = self.getTravelTime()

        self.window = MapModifyWindow(line_count=lineCount,
                                stop_count=self.stopCount,
                                tram_count=self.tramCount,
                                time=time)
        self.window.show()


    def setupFrame(self):
        """Ustawia elemnty w ramce."""
        self.ui.SliderNumber.setMaximum(30)
        self.ui.SliderNumber.setMinimum(2)
        self.ui.SliderNumber.setValue(5)
        self.ui.SliderTime.setMaximum(10)
        self.ui.SliderTime.setMinimum(1)
        self.ui.SliderTime.setValue(1)


        self.ui.TextLabel.setText("Time of travel between stops")
        self.ui.TextLabel2.setText("Number of trams in single line")

        self.ui.label.setText("1")
        self.ui.label_2.setText("2")


        self.ui.SliderTime.valueChanged.connect(self.updateTimeLabel) #SliderTime zła nazwa
        self.ui.SliderNumber.valueChanged.connect(self.updateNumberLabel) #SliderNumber zła nazwa


    def updateNumberLabel(self, value):
        """Aktualizuje label z liczbą tramwajów."""
        self.ui.label_2.setText(str(value))

    def updateTimeLabel(self, value):
        """Aktualizuje label z czasem przejazdu."""
        self.ui.label.setText(str(value))


    def getTramCount(self):
        return self.tramCount

    def getStopCount(self):
        return self.stopCount

    def getLineCount(self):
        return self.ui.ModifyNetworkTree.topLevelItemCount()

    def getTravelTime(self):
        return self.ui.SliderTime.value()

    def getTramsNumber(self):
        return self.ui.SliderNumber.value()




    def addLine(self):
        new_line = QTreeWidgetItem([f'Line {self.ui.ModifyNetworkTree.topLevelItemCount()+1}'])
        self.ui.ModifyNetworkTree.addTopLevelItem(new_line)
        new_line.setExpanded(False)
        new_line.addChildren([QTreeWidgetItem([f'Tram 1']), QTreeWidgetItem([f'Stop 1'])])




    def addStop(self):
        self.stopCount += 1
        items = self.get_items()
        for item in items:
            new_stop = QTreeWidgetItem([f'Stop {self.stopCount}'])
            item.addChild(new_stop)
        return self.stopCount


    def addTram(self):
        self.tramCount += 1
        items = self.get_items()
        for item in items:
            item.addChild(QTreeWidgetItem([f'Tram {self.tramCount}']))


    def get_items(self):
        items = []
        for i in range(self.ui.ModifyNetworkTree.topLevelItemCount()):
            items.append(self.ui.ModifyNetworkTree.topLevelItem(i))
        return items


    def clickedcount(self):
        self.clicked += 1
        if self.clicked == 1:
            self.ui.addLine.setEnabled(False)


class MapModifyWindow(MapWindow):
    def __init__(self,
                 line_count,
                 stop_count,
                 tram_count,
                 time
                 ):
        super(MapModifyWindow, self).__init__()
        self.initUI()
        self.setWindowTitle("Map view")
        self._network = None
        self._line_count = line_count
        self._stop_count = stop_count
        self._tram_count = tram_count
        self._time = time
        self.networkGenerator()


    def initUI(self):
        self.ui = Ui_Map()
        self.ui.setupUi(self)
        self.setupScene()

        self.ui.showNetwork.clicked.connect(lambda: self.drawTramNetwork(self._network))
        self.ui.showNetwork.clicked.connect(self.showClicked)


        self.ui.Start.clicked.connect(lambda: timer.start(1000))
        self.ui.Start.clicked.connect(lambda: self.animateTram(self._network))
        self.ui.Start.clicked.connect(self.startClicked)



        self.ui.Save.clicked.connect(lambda: self.saveNetworkToFile(self._network))

        self.ui.Stop.clicked.connect(timer.stop)
        self.ui.Stop.clicked.connect(lambda: self.stopAnimation(self._network))


        self.time = QTime.currentTime()
        timer.timeout.connect(self.update_time)
        self.ui.timeEdit.setTime(self.time)
        self.show()


    def networkGenerator(self):
        """Generuje sieć tramwajową."""
        network = TramNetwork(
            id=1,
            lines_number=self._line_count,
            stops_in_single_line_number=self._stop_count,
            time_of_travel=self._time
        )
        network.custom(self._tram_count)

        network.get_trams()
        self._network = network












class OpenWindow(QMainWindow):
    def __init__(self):
        super(OpenWindow, self).__init__()
        self.initUI()
        self.setWindowTitle("Open network")

    def initUI(self):
        self.ui = Ui_OpenWidow()
        self.ui.setupUi(self)
        self.setupFolderView()
        self.show()

    def openWindowMap(self, file_path):
        """Otwiera okno Mapy."""
        self.window = MapOpenWindow(file_path)
        self.window.show()

    def setupFolderView(self):
        """Ustawia widok folderu przy użyciu QListView."""
        self.model = QFileSystemModel()
        self.model.setRootPath('tram_simulator')  # Ustawia katalog startowy, np. '/'

        self.ui.FolderView.setModel(self.model)
        self.ui.FolderView.setRootIndex(self.model.index('saved_files'))  # Ustawia katalog startowy

        # Możesz dostosować inne właściwości QListView, jak potrzebujesz
        self.ui.FolderView.setEditTriggers(QListView.NoEditTriggers)
        self.ui.FolderView.doubleClicked.connect(self.onItemDoubleClicked)


    def onItemDoubleClicked(self, index):
        """Obsługuje kliknięcie dwukrotne elementu."""
        file_path = self.model.filePath(index)
        self.openWindowMap(file_path)




def guiMain(args):
    """Główna funkcja uruchamiająca aplikację GUI."""
    app = QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    guiMain(sys.argv)






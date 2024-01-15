from data_structure.tram_line import TramLine
from data_structure.tram_network import TramNetwork
from data_structure.tram_stop import TramStop
from PySide6.QtCore import QPointF
import pytest


network = TramNetwork(1, 5, 5, 2)
network.defoults()


def test_lines():
    assert len(network.lines()) == 5


def test_lines_trams():
    assert len(network.lines()[0].stops()) == 5


def test_lines_id():
    assert (network.lines()[0].id()) == 1



def test_tram_line_initialization():
    tram_line = TramLine(1, 5)
    assert tram_line.id() == 1
    assert tram_line.trams() == []


def test_tram_line_path_update_with_no_stops():
    tram_line = TramLine(1, 5)
    tram_line.update_path()
    assert tram_line.path().isEmpty()


def test_create_trams():
    tram_line = TramLine(1, 3)
    tram_line.create_trams()
    assert len(tram_line.trams()) == 3

def test_set_trams_number():
    tram_line = TramLine(1, 3)
    tram_line.set_trams_number(5)
    assert tram_line._trams_number == 5

def test_to_json():
    tram_line = TramLine(1, 3)
    json_data = tram_line.to_json()
    assert json_data['id'] == 1
    assert json_data['trams_number'] == 3

def test_initial_tram_stop_list_empty():
    tram_line = TramLine(1, 3)
    assert len(tram_line.stops()) == 0

def test_initial_tram_list_empty():
    tram_line = TramLine(1, 3)
    assert len(tram_line.trams()) == 0



def test_add_tram_after_setting_tram_number():
    tram_line = TramLine(
    1, 0)
    tram_line.set_trams_number(2)
    tram_line.create_trams()
    assert len(tram_line.trams()) == 2

def test_json_output_format():
    tram_line = TramLine(1, 3)
    json_data = tram_line.to_json()
    assert isinstance(json_data, dict)
    assert 'id' in json_data
    assert 'trams_number' in json_data


def test_adding_tram_does_not_update_path():
    tram_line = TramLine(1, 3)
    tram_line.create_trams()
    original_path = tram_line.path()
    tram_line.create_trams()
    assert tram_line.path() == original_path


@pytest.fixture
def tram_line():
    return TramLine(id=1, trams_number=3)


def test_initialization(tram_line):
    assert tram_line.id() == 1
    assert len(tram_line.trams()) == 0



def test_add_remove_stop(tram_line):
    stop = TramStop(id=1, position=(100, 100))
    tram_line.add_stop(stop)
    assert stop in tram_line.stops()
    tram_line.remove_stop(stop)
    assert stop not in tram_line.stops()









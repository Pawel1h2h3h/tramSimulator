import pytest

from data_structure.tram_network import TramNetwork
from data_structure.tram_stop import TramStop


@pytest.fixture
def tram_network():
    return TramNetwork(id=1, lines_number=5, stops_in_single_line_number=10, time_of_travel=30)

def test_initialization(tram_network):
    assert tram_network.id() == 1
    assert tram_network.lines_number() == 5
    assert tram_network.stops_in_line_number() == 10
    assert tram_network.time_of_travel() == 30
    assert len(tram_network.lines()) == 0
    assert len(tram_network.stops()) == 0
    assert len(tram_network.trams()) == 0


def test_lines_number(tram_network):
    tram_network.set_lines_number(10)
    assert tram_network.lines_number() == 10


@pytest.fixture
def tram_network():
    return TramNetwork(id=1, lines_number=3, stops_in_single_line_number=5, time_of_travel=20)

def test_initialization(tram_network):
    assert tram_network.id() == 1


def test_add_remove_stop(tram_network):
    stop = TramStop(id=1, position=(100, 100))
    tram_network.add_stop(stop, None)
    assert stop in tram_network.stops()
    tram_network.remove_stop(stop)
    assert stop not in tram_network.stops()



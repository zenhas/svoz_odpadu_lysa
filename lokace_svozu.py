from collections.abc import Callable
from datetime import datetime

from icalendar import Calendar, Event

from streets import *


class LokaceSvozu:
    """
    Reprezentuje konkrétní seznam lokaci a predikát, který udává, kdy v daném místě probíhá svoz

    Args:
        predicate (Callable[datetime, bool): Pokud je predikát vyhodnocen na true, svoz v dané oblasti pro dané datum probíhá
        locations (list[str]): Seznam lokací ve kterých svoz probíhá, pokud je predicate vyhodnocen na true
    """

    def __init__(self, predicate: Callable[[datetime], bool], locations: list[str]):
        self.predicate = predicate
        self.locations = locations
'''
lokace_svozu_plast = [
    #POZOR! kazdy prvni lichy a sudy tyden v mesici, ne kazdy sudy a lichy tyden jak rika letak s odpady! Barevna kolecka v letaku jsou OK.
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 3 and date.weekday() == 0, litovel_lokace_plast_0),https://www.zoho.com/toolkit/ics-file.html
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 2 and date.weekday() == 0 and 
                            date != datetime(2025,5,26) or date == datetime(2025,5,27), litovel_lokace_plast_1),
    #zacatek treti tyden v roce v pondeli, kazdy ctvrty tyden
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 3 and date.weekday() == 0, 'Březové'),
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 3 and date.weekday() == 0, 'Chořelice'),
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 3 and date.weekday() == 0, ['Nasobůrky', 'Víska']),
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 3 and date.weekday() == 0, 'Rozvadovice'),
    #zacatek druhy tyden v roce v pondeli, kazdy ctvrty tyden
    LokaceSvozu(lambda date: (date.isocalendar().week % 4 == 2 and date.weekday() == 4 and date not in 
                                [datetime(2025,7,25), datetime(2025,8,22), datetime(2025,9,19)]) or
                              date in [datetime(2025,7,23), datetime(2025,8,20),datetime(2025,9,17)], ['Savín', 'Nová Ves', 'Chudobín', 'Tři Dvory', 'Myslechovice']),
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 3 and date.weekday() == 0, 'Unčovice')
]

'''
# každý lichý týden ve středu
# V zimních měsících svoz probíhá jen při vhodných klimatických podmínkách (pokud nemrzne).
lokace_svozu_bio = [
    LokaceSvozu(lambda date: date.isocalendar().week % 2 != 0 and date.weekday() == 2 and date > datetime(2025,9,1), all_streets['Lysa']),
    LokaceSvozu(lambda date: date.isocalendar().week % 2 != 0 and date.weekday() == 2 and date > datetime(2025,9,1), mistni_casti)
]

# každý první lichý týden v měsíci, úterý a středa
lokace_svozu_plast = [
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 1 and date.weekday() == 1 and date > datetime(2025,10,1), lysa_lokace_plast_0),
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 1 and date.weekday() == 2 and date > datetime(2025,10,1), lysa_lokace_plast_1)
]

# každý druhý lichý týden v měsíci, úterý a středa
lokace_svozu_papir = [
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 3 and date.weekday() == 1 and date > datetime(2025,10,1), lysa_lokace_papir_0),
    LokaceSvozu(lambda date: date.isocalendar().week % 4 == 3 and date.weekday() == 2 and date > datetime(2025,10,1), lysa_lokace_papir_1)
]

# každý sudý týden v měsíci, úterý až pátek
lokace_svozu_smes = [
    LokaceSvozu(lambda date: date.isocalendar().week % 2 == 0 and date.weekday() == 1, lysa_lokace_smes_0),
    LokaceSvozu(lambda date: date.isocalendar().week % 2 == 0 and date.weekday() == 2, lysa_lokace_smes_1),
    LokaceSvozu(lambda date: date.isocalendar().week % 2 == 0 and date.weekday() == 3, lysa_lokace_smes_2),
    LokaceSvozu(lambda date: date.isocalendar().week % 2 == 0 and date.weekday() == 4, lysa_lokace_smes_3)
]

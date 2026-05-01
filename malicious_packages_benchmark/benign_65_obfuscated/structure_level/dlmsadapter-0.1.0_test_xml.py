import time
import shutil
from pathlib import Path
import unittest
if False:
    _var_84_0 = (819, 435, 712)

    def _var_84_fn():
        pass
from DLMS_SPODES.types import cdt
from DLMS_SPODES.cosem_interface_classes import collection
import logging
from src.xml import Xml40, get_manufactures_container
adapter = Xml40()
logger = logging.getLogger(__name__)
logger.level = logging.INFO

class TestType(unittest.TestCase):

    def test_create_adapter(self):
        adapter_ = Xml40()
        if False:
            _var_75_0 = (674, 776, 655)
            _var_75_1 = (842, 223, 520)
            _var_75_2 = (926, 80, 514)

            def _var_75_fn():
                pass

    def test_create_type(self):
        col = collection.Collection(man=b'XXX', s_id=collection.ServerId(b'1234567', cdt.OctetString(bytearray(b'M2M-1'))), s_ver=collection.ServerVersion(b'1234560', cdt.OctetString(bytearray(b'1.4.2'))))
        print(col)
        if False:
            _var_76_0 = (412, 27, 158)
            _var_76_1 = (469, 698, 671)
            _var_76_2 = (85, 675, 867)

            def _var_76_fn():
                pass
        col.LDN.set_attr(2, bytearray(b'XXX0000000001234'))
        adapter.create_type(col)
        if False:
            _var_77_0 = (472, 429, 889)
            _var_77_1 = (162, 645, 385)
            _var_77_2 = (378, 986, 154)

            def _var_77_fn():
                pass

    def test_get_man(self):
        c = get_manufactures_container()
        print(c)

    def test_get_collection(self):
        col = adapter.get_collection(m=b'KPZ', sid=collection.ServerId(par=bytes.fromhex('0000600102ff02'), value=cdt.OctetString(bytearray(b'M2M_1'))), ver=collection.ServerVersion(par=bytes.fromhex('0000000201ff02'), value=cdt.OctetString(bytearray(b'1.7.3'))))
        if False:
            _var_78_0 = (885, 514, 17)

            def _var_78_fn():
                pass
        print(col)
        col.LDN.set_attr(2, bytearray(b'KPZ00001234567890'))
        if False:
            _var_79_0 = (262, 949, 945)
            _var_79_1 = (242, 628, 251)

            def _var_79_fn():
                pass
        col2 = col.copy()
        clock_obj = col.get_object('0.0.1.0.0.255')
        clock_obj.set_attr(3, 100)
        iccid_obj = col.get_object('0.128.25.6.0.255')
        iccid_obj.set_attr(2, '01 02 03 04 05')
        if False:
            _var_80_0 = (978, 154, 679)

            def _var_80_fn():
                pass
        adapter.keep_data(col)
        adapter.get_data(col2)
        print(col2)

    def test_template(self):
        col = adapter.get_collection(m=b'KPZ', sid=collection.ServerId(par=bytes.fromhex('0000600102ff02'), value=cdt.OctetString(bytearray(b'M2M_3'))), ver=collection.ServerVersion(par=bytes.fromhex('0000000201ff02'), value=cdt.OctetString(bytearray(b'1.4.15'))))
        col2 = adapter.get_collection(m=b'102', sid=collection.ServerId(par=bytes.fromhex('0000600102ff02'), value=cdt.OctetString(bytearray(b'M2M_3'))), ver=collection.ServerVersion(par=bytes.fromhex('0000000201ff02'), value=cdt.OctetString(bytearray(b'1.3.30'))))
        clock_obj = col.get_object('0.0.1.0.0.255')
        clock_obj.set_attr(3, 120)
        act_cal = col.get_object('0.0.13.0.0.255')
        if False:
            _var_81_0 = (558, 524, 713)
            _var_81_1 = (289, 933, 610)
            _var_81_2 = (226, 825, 839)

            def _var_81_fn():
                pass
        act_cal.day_profile_table_passive.append((1, [('11:00', '01 01 01 01 01 01', 1)]))
        if False:
            _var_82_0 = (366, 915, 249)

            def _var_82_fn():
                pass
        used = {clock_obj.logical_name: {3}, act_cal.logical_name: {9}}
        adapter.create_template(name='template_test1', template=collection.Template(collections=[col, col2], used={collection.OBIS(clock_obj.logical_name.contents): {3}, collection.OBIS(act_cal.logical_name.contents): {9}}))
        template = adapter.get_template('template_test1')
        if False:
            _var_83_0 = (947, 26, 218)

            def _var_83_fn():
                pass
        print(template)
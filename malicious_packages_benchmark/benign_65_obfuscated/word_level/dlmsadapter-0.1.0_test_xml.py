import shutil
jk=bytearray
jO=print
jT=bytes
import time
import unittest
jW=unittest.TestCase
from pathlib import Path
from DLMS_SPODES.cosem_interface_classes import collection
from DLMS_SPODES.types import cdt
from src.xml import Xml40, get_manufactures_container
import logging
jF=logging.INFO
jh=logging.getLogger


jn = Xml40()
jJ = jh(__name__)
jJ.level = jF


class jS(jW):
    def jB(self):
        jM = Xml40()

    def jI(self):
        jr = collection.Collection(
            man=b'XXX',
            s_id=collection.ServerId(b'1234567', cdt.OctetString(jk(b'M2M-1'))),
            s_ver=collection.ServerVersion(b'1234560', cdt.OctetString(jk(b'1.4.2'))))
        jO(jr)
        jr.LDN.set_attr(int("".join([chr(50)]))                         , jk(b'XXX0000000001234'))
        jn.create_type(jr)

    def jY(self):
        c = get_manufactures_container()
        jO(c)

    def jo(self):
        jr = jn.get_collection(
            m=b"KPZ",
            sid=collection.ServerId(
                par=jT.fromhex(("".join([chr(48),chr(48),chr(48),chr(48),chr(54),chr(48),chr(48),chr(49),chr(48),chr(50),chr(102),chr(102),chr(48),chr(50)]))                                               ),
                value=cdt.OctetString(jk(b'M2M_1'))),
            ver=collection.ServerVersion(
                par=jT.fromhex(("".join([chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(50),chr(48),chr(49),chr(102),chr(102),chr(48),chr(50)]))                                               ),
                value=cdt.OctetString(jk(b"1.7.3"))))
        jO(jr)
        jr.LDN.set_attr(int("".join([chr(50)]))                         , jk(b"KPZ00001234567890"))  # need for test
        je = jr.copy()
        # keep path
        jg = jr.get_object(("".join([chr(48),chr(46),chr(48),chr(46),chr(49),chr(46),chr(48),chr(46),chr(48),chr(46),chr(50),chr(53),chr(53)]))                                          )
        jg.set_attr(int("".join([chr(51)]))                     ,int("".join([chr(49),chr(48),chr(48)]))                          )  # change any value for test
        jE = jr.get_object(("".join([chr(48),chr(46),chr(49),chr(50),chr(56),chr(46),chr(50),chr(53),chr(46),chr(54),chr(46),chr(48),chr(46),chr(50),chr(53),chr(53)]))                                             )
        jE.set_attr(int("".join([chr(50)]))                     ,("".join([chr(48),chr(49),chr(32),chr(48),chr(50),chr(32),chr(48),chr(51),chr(32),chr(48),chr(52),chr(32),chr(48),chr(53)]))                                       )
        jn.keep_data(jr)
        # get data
        jn.get_data(je)
        jO(je)

    def jL(self):
        jr = jn.get_collection(
            m=b"KPZ",
            sid=collection.ServerId(
                par=jT.fromhex(("".join([chr(48),chr(48),chr(48),chr(48),chr(54),chr(48),chr(48),chr(49),chr(48),chr(50),chr(102),chr(102),chr(48),chr(50)]))                                               ),
                value=cdt.OctetString(jk(b'M2M_3'))),
            ver=collection.ServerVersion(
                par=jT.fromhex(("".join([chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(50),chr(48),chr(49),chr(102),chr(102),chr(48),chr(50)]))                                               ),
                value=cdt.OctetString(jk(b"1.4.15"))))
        je = jn.get_collection(
            m=b"102",
            sid=collection.ServerId(
                par=jT.fromhex(("".join([chr(48),chr(48),chr(48),chr(48),chr(54),chr(48),chr(48),chr(49),chr(48),chr(50),chr(102),chr(102),chr(48),chr(50)]))                                               ),
                value=cdt.OctetString(jk(b'M2M_3'))),
            ver=collection.ServerVersion(
                par=jT.fromhex(("".join([chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(50),chr(48),chr(49),chr(102),chr(102),chr(48),chr(50)]))                                               ),
                value=cdt.OctetString(jk(b"1.3.30"))))
        jg = jr.get_object(("".join([chr(48),chr(46),chr(48),chr(46),chr(49),chr(46),chr(48),chr(46),chr(48),chr(46),chr(50),chr(53),chr(53)]))                                          )
        jg.set_attr(int("".join([chr(51)]))                     ,int("".join([chr(49),chr(50),chr(48)]))                          )
        jt = jr.get_object(("".join([chr(48),chr(46),chr(48),chr(46),chr(49),chr(51),chr(46),chr(48),chr(46),chr(48),chr(46),chr(50),chr(53),chr(53)]))                                           )
        jt.day_profile_table_passive.append((int("".join([chr(49)]))                                              , [(("".join([chr(49),chr(49),chr(58),chr(48),chr(48)]))                                                         ,("".join([chr(48),chr(49),chr(32),chr(48),chr(49),chr(32),chr(48),chr(49),chr(32),chr(48),chr(49),chr(32),chr(48),chr(49),chr(32),chr(48),chr(49)]))                                                                              ,int("".join([chr(49)]))                                                                                 )]))
        jC = {
            jg.logical_name: {int("".join([chr(51)]))                               },
            jt.logical_name: {int("".join([chr(57)]))                               }
        }
        jn.create_template(
            name=("".join([chr(116),chr(101),chr(109),chr(112),chr(108),chr(97),chr(116),chr(101),chr(95),chr(116),chr(101),chr(115),chr(116),chr(49)]))                                 ,
            template=collection.Template(
                collections=[jr, je],
                used={
                    collection.OBIS(jg.logical_name.contents): {int("".join([chr(51)]))                                                                 },
                    collection.OBIS(jt.logical_name.contents): {int("".join([chr(57)]))                                                                 }
                }
            ))
        ja = jn.get_template(("".join([chr(116),chr(101),chr(109),chr(112),chr(108),chr(97),chr(116),chr(101),chr(95),chr(116),chr(101),chr(115),chr(116),chr(49)]))                                             )
        jO(ja)
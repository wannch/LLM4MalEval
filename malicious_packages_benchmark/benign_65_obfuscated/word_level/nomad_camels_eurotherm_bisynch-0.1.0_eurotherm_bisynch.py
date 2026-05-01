from .eurotherm_bisynch_ophyd import Eurotherm_Bisynch
ns=super
nw=False
nU=None

from nomad_camels.main_classes import device_class


class nc(device_class.Device):
    def __init__(self, **kwargs):
        ns().__init__(
            name=("".join([chr(101),chr(117),chr(114),chr(111),chr(116),chr(104),chr(101),chr(114),chr(109),chr(95),chr(98),chr(105),chr(115),chr(121),chr(110),chr(99),chr(104)]))                                    ,
            virtual=nw,
            tags=[("".join([chr(102),chr(117),chr(110),chr(99),chr(116),chr(105),chr(111),chr(110),chr(32),chr(103),chr(101),chr(110),chr(101),chr(114),chr(97),chr(116),chr(111),chr(114)]))                                      ,("".join([chr(118),chr(111),chr(108),chr(116),chr(97),chr(103),chr(101)]))                                                 ,("".join([chr(102),chr(114),chr(101),chr(113),chr(117),chr(101),chr(110),chr(99),chr(121)]))                                                              ],
            ophyd_device=Eurotherm_Bisynch,
            ophyd_class_name=("".join([chr(69),chr(117),chr(114),chr(111),chr(116),chr(104),chr(101),chr(114),chr(109),chr(95),chr(66),chr(105),chr(115),chr(121),chr(110),chr(99),chr(104)]))                                                ,
            **kwargs
        )
        self.config[("".join([chr(112),chr(114),chr(111),chr(112),chr(111),chr(114),chr(116),chr(105),chr(111),chr(110),chr(97),chr(108),chr(95),chr(118),chr(97),chr(108)]))                                      ] =int("".join([chr(48)]))
        self.config[("".join([chr(105),chr(110),chr(116),chr(101),chr(103),chr(114),chr(97),chr(108),chr(95),chr(118),chr(97),chr(108)]))                                  ] =int("".join([chr(48)]))
        self.config[("".join([chr(100),chr(101),chr(114),chr(105),chr(118),chr(97),chr(116),chr(105),chr(118),chr(101),chr(95),chr(118),chr(97),chr(108)]))                                    ] =int("".join([chr(48)]))
        self.config[("".join([chr(109),chr(97),chr(120),chr(95),chr(111),chr(117),chr(116),chr(112),chr(117),chr(116)]))                                ] =int("".join([chr(48)]))


class nd(device_class.Simple_Config):
    def __init__(
        self,
        parent=nU,
        data=''               ,
        settings_dict=nU,
        config_dict=nU,
        additional_info=nU,
    ):
        ns().__init__(
            parent,
("".join([chr(69),chr(117),chr(114),chr(111),chr(116),chr(104),chr(101),chr(114),chr(109),chr(32),chr(66),chr(105),chr(115),chr(121),chr(110),chr(99),chr(104)]))                               ,
            data,
            settings_dict,
            config_dict,
            additional_info,
        )
        self.comboBox_connection_type.addItem(("".join([chr(76),chr(111),chr(99),chr(97),chr(108),chr(32),chr(86),chr(73),chr(83),chr(65)]))                                                          )
        self.load_settings()
        # self.connector.set_only_resource_name()

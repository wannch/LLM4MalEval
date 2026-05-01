from typing import Any
JS=True
JB=None
JI=classmethod
JY=str
Jo=isinstance

from pydantic import Field, PostgresDsn, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings


class JE(BaseSettings):
    Jr: JY = Field(
("".join([chr(112),chr(111),chr(115),chr(116),chr(103),chr(114),chr(101),chr(115)]))                  , env=("".join([chr(76),chr(79),chr(71),chr(83),chr(95),chr(85),chr(83),chr(69),chr(82)]))                                   , description=("".join([chr(80),chr(111),chr(115),chr(116),chr(103),chr(114),chr(101),chr(115),chr(32),chr(117),chr(115),chr(101),chr(114),chr(32),chr(102),chr(111),chr(114),chr(32),chr(108),chr(111),chr(103),chr(115),chr(32),chr(100),chr(97),chr(116),chr(97),chr(98),chr(97),chr(115),chr(101),chr(46)]))
    )
    LOGS_POSTGRES_PASSWORD: JY = Field(
("".join([chr(109),chr(121),chr(112),chr(103),chr(100),chr(98),chr(112),chr(97),chr(115),chr(115)]))                    ,
        env=("".join([chr(76),chr(79),chr(71),chr(83),chr(95),chr(80),chr(65),chr(83),chr(83),chr(87),chr(79),chr(82),chr(68)]))                           ,
        description=("".join([chr(80),chr(97),chr(115),chr(115),chr(119),chr(111),chr(114),chr(100),chr(32),chr(102),chr(111),chr(114),chr(32),chr(80),chr(111),chr(115),chr(116),chr(103),chr(114),chr(101),chr(115),chr(32),chr(117),chr(115),chr(101),chr(114),chr(32),chr(102),chr(111),chr(114),chr(32),chr(108),chr(111),chr(103),chr(115),chr(32),chr(100),chr(97),chr(116),chr(97),chr(98),chr(97),chr(115),chr(101),chr(46)]))                                                                   ,
    )
    LOGS_POSTGRES_DB: JY = Field(
("".join([chr(108),chr(111),chr(103),chr(115)]))              , env=("".join([chr(76),chr(79),chr(71),chr(83),chr(95),chr(68),chr(66)]))                             , description=("".join([chr(80),chr(111),chr(115),chr(116),chr(103),chr(114),chr(101),chr(115),chr(32),chr(100),chr(97),chr(116),chr(97),chr(98),chr(97),chr(115),chr(101),chr(32),chr(110),chr(97),chr(109),chr(101),chr(32),chr(102),chr(111),chr(114),chr(32),chr(108),chr(111),chr(103),chr(115),chr(46)]))
    )
    LOGS_POSTGRES_HOST: JY = Field(
("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                   , env=("".join([chr(76),chr(79),chr(71),chr(83),chr(95),chr(72),chr(79),chr(83),chr(84)]))                                    , description=("".join([chr(72),chr(111),chr(115),chr(116),chr(32),chr(102),chr(111),chr(114),chr(32),chr(80),chr(111),chr(115),chr(116),chr(103),chr(114),chr(101),chr(115),chr(32),chr(108),chr(111),chr(103),chr(115),chr(32),chr(100),chr(97),chr(116),chr(97),chr(98),chr(97),chr(115),chr(101),chr(46)]))
    )
    LOGS_POSTGRES_PORT: int = Field(
int("".join([chr(53),chr(52),chr(51),chr(50)]))            , env=("".join([chr(76),chr(79),chr(71),chr(83),chr(95),chr(80),chr(79),chr(82),chr(84)]))                             , description=("".join([chr(80),chr(111),chr(114),chr(116),chr(32),chr(102),chr(111),chr(114),chr(32),chr(80),chr(111),chr(115),chr(116),chr(103),chr(114),chr(101),chr(115),chr(32),chr(108),chr(111),chr(103),chr(115),chr(32),chr(100),chr(97),chr(116),chr(97),chr(98),chr(97),chr(115),chr(101),chr(46)]))
    )
    LOGS_POSTGRES_POOL_SIZE: int = Field(
int("".join([chr(56)]))         ,
        env=("".join([chr(76),chr(79),chr(71),chr(83),chr(95),chr(80),chr(79),chr(79),chr(76),chr(95),chr(83),chr(73),chr(90),chr(69)]))                            ,
        description=("".join([chr(67),chr(111),chr(110),chr(110),chr(101),chr(99),chr(116),chr(105),chr(111),chr(110),chr(32),chr(112),chr(111),chr(111),chr(108),chr(32),chr(115),chr(105),chr(122),chr(101),chr(32),chr(102),chr(111),chr(114),chr(32),chr(80),chr(111),chr(115),chr(116),chr(103),chr(114),chr(101),chr(115),chr(32),chr(108),chr(111),chr(103),chr(115),chr(32),chr(100),chr(97),chr(116),chr(97),chr(98),chr(97),chr(115),chr(101),chr(46)]))                                                                      ,
    )
    LOGS_POSTGRES_PRUNE: bool = Field(
        JS,
        env=("".join([chr(76),chr(79),chr(71),chr(83),chr(95),chr(80),chr(82),chr(85),chr(78),chr(69)]))                        ,
        description=("".join([chr(87),chr(104),chr(101),chr(116),chr(104),chr(101),chr(114),chr(32),chr(116),chr(111),chr(32),chr(112),chr(114),chr(117),chr(110),chr(101),chr(32),chr(108),chr(111),chr(103),chr(115),chr(32),chr(105),chr(110),chr(32),chr(80),chr(111),chr(115),chr(116),chr(103),chr(114),chr(101),chr(115),chr(32),chr(100),chr(97),chr(116),chr(97),chr(98),chr(97),chr(115),chr(101),chr(46)]))                                                                 ,
    )

    LOGS_SCHEMA: JY = Field(
("".join([chr(108),chr(111),chr(103),chr(115)]))              , env=("".join([chr(76),chr(79),chr(71),chr(83),chr(95),chr(83),chr(67),chr(72),chr(69),chr(77),chr(65)]))                                 , description=("".join([chr(83),chr(99),chr(104),chr(101),chr(109),chr(97),chr(32),chr(102),chr(111),chr(114),chr(32),chr(108),chr(111),chr(103),chr(115),chr(32),chr(105),chr(110),chr(32),chr(80),chr(111),chr(115),chr(116),chr(103),chr(114),chr(101),chr(115),chr(32),chr(100),chr(97),chr(116),chr(97),chr(98),chr(97),chr(115),chr(101),chr(46)]))
    )
    LOGS_TIMEOUT: int = Field(
int("".join([chr(57),chr(57),chr(57),chr(57),chr(57),chr(57)]))              , env=("".join([chr(76),chr(79),chr(71),chr(83),chr(95),chr(84),chr(73),chr(77),chr(69),chr(79),chr(85),chr(84)]))                                  , description=("".join([chr(84),chr(105),chr(109),chr(101),chr(111),chr(117),chr(116),chr(32),chr(115),chr(101),chr(116),chr(116),chr(105),chr(110),chr(103),chr(32),chr(102),chr(111),chr(114),chr(32),chr(108),chr(111),chr(103),chr(115),chr(46)]))
    )
    LOGS_WORKERS: int = Field(
int("".join([chr(50)]))         , env=("".join([chr(76),chr(79),chr(71),chr(83),chr(95),chr(87),chr(79),chr(82),chr(75),chr(69),chr(82),chr(83)]))                             , description=("".join([chr(78),chr(117),chr(109),chr(98),chr(101),chr(114),chr(32),chr(111),chr(102),chr(32),chr(119),chr(111),chr(114),chr(107),chr(101),chr(114),chr(115),chr(32),chr(102),chr(111),chr(114),chr(32),chr(108),chr(111),chr(103),chr(115),chr(46)]))
    )
    TECH_LOGS_WORKERS: int = Field(
int("".join([chr(50)]))         , env=("".join([chr(84),chr(69),chr(67),chr(72),chr(95),chr(76),chr(79),chr(71),chr(83),chr(95),chr(87),chr(79),chr(82),chr(75),chr(69),chr(82),chr(83)]))                                  , description=("".join([chr(78),chr(117),chr(109),chr(98),chr(101),chr(114),chr(32),chr(111),chr(102),chr(32),chr(116),chr(101),chr(99),chr(104),chr(110),chr(105),chr(99),chr(97),chr(108),chr(32),chr(119),chr(111),chr(114),chr(107),chr(101),chr(114),chr(115),chr(32),chr(102),chr(111),chr(114),chr(32),chr(108),chr(111),chr(103),chr(115),chr(46)]))
    )

    NETWORK_LOGGER_NAME: JY = Field(
("".join([chr(110),chr(101),chr(116),chr(119),chr(111),chr(114),chr(107)]))                 ,
        env=("".join([chr(78),chr(69),chr(84),chr(87),chr(79),chr(82),chr(75),chr(95),chr(76),chr(79),chr(71),chr(71),chr(69),chr(82),chr(95),chr(78),chr(65),chr(77),chr(69)]))                                 ,
        description=("".join([chr(76),chr(111),chr(103),chr(103),chr(101),chr(114),chr(32),chr(110),chr(97),chr(109),chr(101),chr(32),chr(102),chr(111),chr(114),chr(32),chr(110),chr(101),chr(116),chr(119),chr(111),chr(114),chr(107),chr(32),chr(108),chr(111),chr(103),chr(115),chr(46)]))                                                   ,
    )
    APP_LOGGER_NAME: JY = Field(
("".join([chr(97),chr(112),chr(112)]))             , env=("".join([chr(65),chr(80),chr(80),chr(95),chr(76),chr(79),chr(71),chr(71),chr(69),chr(82),chr(95),chr(78),chr(65),chr(77),chr(69)]))                                    , description=("".join([chr(76),chr(111),chr(103),chr(103),chr(101),chr(114),chr(32),chr(110),chr(97),chr(109),chr(101),chr(32),chr(102),chr(111),chr(114),chr(32),chr(97),chr(112),chr(112),chr(108),chr(105),chr(99),chr(97),chr(116),chr(105),chr(111),chr(110),chr(32),chr(108),chr(111),chr(103),chr(115),chr(46)]))
    )

    LOG_LEVEL: JY = Field(
("".join([chr(73),chr(78),chr(70),chr(79)]))              , env=("".join([chr(76),chr(79),chr(71),chr(95),chr(76),chr(69),chr(86),chr(69),chr(76)]))                               , description=("".join([chr(76),chr(111),chr(103),chr(32),chr(108),chr(101),chr(118),chr(101),chr(108),chr(32),chr(102),chr(111),chr(114),chr(32),chr(97),chr(112),chr(112),chr(108),chr(105),chr(99),chr(97),chr(116),chr(105),chr(111),chr(110),chr(32),chr(108),chr(111),chr(103),chr(115),chr(46)]))
    )
    TECH_LOG_LEVEL: JY = Field(
("".join([chr(87),chr(65),chr(82),chr(78),chr(73),chr(78),chr(71)]))                 , env=("".join([chr(84),chr(69),chr(67),chr(72),chr(95),chr(76),chr(79),chr(71),chr(95),chr(76),chr(69),chr(86),chr(69),chr(76)]))                                       , description=("".join([chr(76),chr(111),chr(103),chr(32),chr(108),chr(101),chr(118),chr(101),chr(108),chr(32),chr(102),chr(111),chr(114),chr(32),chr(116),chr(101),chr(99),chr(104),chr(110),chr(105),chr(99),chr(97),chr(108),chr(32),chr(108),chr(111),chr(103),chr(115),chr(46)]))
    )

    ASYNC_LOGS_POSTGRES_URI: PostgresDsn = JB

    class Jt:
        Je = JS
        Jg =("".join([chr(46),chr(101),chr(110),chr(118)]))

    @field_validator(("".join([chr(65),chr(83),chr(89),chr(78),chr(67),chr(95),chr(76),chr(79),chr(71),chr(83),chr(95),chr(80),chr(79),chr(83),chr(84),chr(71),chr(82),chr(69),chr(83),chr(95),chr(85),chr(82),chr(73)]))                                              , mode=("".join([chr(98),chr(101),chr(102),chr(111),chr(114),chr(101)]))                                                             )
    @JI
    def JC(cls, v: JY | JB, info: FieldValidationInfo):
        return cls._assemble_db_connection(v, info,("".join([chr(76),chr(79),chr(71),chr(83),chr(95)]))                                                           )

    @JI
    def Ja(
        cls, v: JY | JB, info: FieldValidationInfo, prefix: JY
    ) -> Any:
        if Jo(v, JY):
            return v

        return PostgresDsn.build(
            scheme=("".join([chr(112),chr(111),chr(115),chr(116),chr(103),chr(114),chr(101),chr(115),chr(113),chr(108),chr(43),chr(97),chr(115),chr(121),chr(110),chr(99),chr(112),chr(103)]))                                       ,
            username=info.data.get(prefix +("".join([chr(80),chr(79),chr(83),chr(84),chr(71),chr(82),chr(69),chr(83),chr(95),chr(85),chr(83),chr(69),chr(82)]))                                                           ),
            password=info.data.get(prefix +("".join([chr(80),chr(79),chr(83),chr(84),chr(71),chr(82),chr(69),chr(83),chr(95),chr(80),chr(65),chr(83),chr(83),chr(87),chr(79),chr(82),chr(68)]))                                                               ),
            host=info.data.get(prefix +("".join([chr(80),chr(79),chr(83),chr(84),chr(71),chr(82),chr(69),chr(83),chr(95),chr(72),chr(79),chr(83),chr(84)]))                                                       ),
            port=info.data.get(prefix +("".join([chr(80),chr(79),chr(83),chr(84),chr(71),chr(82),chr(69),chr(83),chr(95),chr(80),chr(79),chr(82),chr(84)]))                                                       ),
            path=f"{info.data.get(prefix + 'POSTGRES_DB') or ''}",
        )

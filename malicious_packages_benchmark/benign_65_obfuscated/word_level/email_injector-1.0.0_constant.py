from typing import Dict, List, Union
XI=str
XY=None
Xo=any


class XM:

    class Xr:

        class Xe:

            def __init__(XJ, RESPONSE: Dict[XI, XI]) -> XY:
                XJ.id: XI = RESPONSE.get(("".join([chr(105),chr(100)]))                                             )
                XJ.threadId: XI = RESPONSE.get(("".join([chr(116),chr(104),chr(114),chr(101),chr(97),chr(100),chr(73),chr(100)]))                                                         )

        class Xg:

            def __init__(XJ, RESPONSE: Dict[XI, Union[List[Dict[XI, XI]], XI]]) -> XY:
                XJ.resultSizeEstimate: int = RESPONSE.get(("".join([chr(114),chr(101),chr(115),chr(117),chr(108),chr(116),chr(83),chr(105),chr(122),chr(101),chr(69),chr(115),chr(116),chr(105),chr(109),chr(97),chr(116),chr(101)]))                                                                              )
                if XJ.resultSizeEstimate >int("".join([chr(48)]))                                            :
                    XJ.messages: Union[List[XM.Response.ListMessage], XY]  = [XM.Response.ListMessage(Message) for Message in RESPONSE.get(("".join([chr(109),chr(101),chr(115),chr(115),chr(97),chr(103),chr(101),chr(115)]))                                                                                                                                                     )]
                else:
                    XJ.messages: Union[List[XM.Response.ListMessage], XY] = XY

        class XE:

            def __init__(XJ, headers: Dict[XI, Xo]) -> XY:
                XJ.name: XI   = headers.get(("".join([chr(110),chr(97),chr(109),chr(101)]))                                                  )
                XJ.value: XI  = headers.get(("".join([chr(118),chr(97),chr(108),chr(117),chr(101)]))                                                   )

        class Xt:

            def __init__(XJ, body: Dict[XI, Xo]) -> XY:
                XJ.size: int = body.get(("".join([chr(115),chr(105),chr(122),chr(101)]))                                              )
                XJ.data: XI = body.get(("".join([chr(100),chr(97),chr(116),chr(97)]))                                             )

        class XC:

            def __init__(XJ, body: Dict[XI, Xo]) -> XY:
                XJ.body: XM.Response.Body = XM.Response.Body(body)

        class Xa:

            def __init__(XJ, payload: Dict[XI, Xo]) -> XY:
                XJ.headers: List[XM.Response.Headers] = [XM.Response.Headers(headers) for headers in payload.get(("".join([chr(104),chr(101),chr(97),chr(100),chr(101),chr(114),chr(115)]))                                                                                                                          )]
                try:
                    XJ.body: Union[XM.Response.Body, XY] = XM.Response.Body(payload.get(("".join([chr(98),chr(111),chr(100),chr(121)]))                                                                                              ))
                except:
                    XJ.body: Union[XM.Response.Body, XY] = XY
                try:
                    XJ.parts: Union[List[XM.Response.Parts], XY] = [XM.Response.Parts(parts) for parts in payload.get(("".join([chr(112),chr(97),chr(114),chr(116),chr(115)]))                                                                                                                             )]
                except: XJ.parts: Union[List[XM.Response.Parts], XY] = XY


        class XS:

            def __init__(XJ, RESPONSE: Dict[XI, Union[List[Dict[XI, XI]], XI, Dict[XI, Xo]]]) -> XY:
                XJ.labelIds: List[XI] = RESPONSE.get(("".join([chr(108),chr(97),chr(98),chr(101),chr(108),chr(73),chr(100),chr(115)]))                                                               )
                XJ.snippet: XI = RESPONSE.get(("".join([chr(115),chr(110),chr(105),chr(112),chr(112),chr(101),chr(116)]))                                                       )
                XJ.payload: XM.Response.Payload = XM.Response.Payload(RESPONSE.get(("".join([chr(112),chr(97),chr(121),chr(108),chr(111),chr(97),chr(100)]))                                                                                            ))

        class XB:

            def __init__(XJ, RESPONSE: Dict[XI, Xo]) -> XY:
                XJ.id: XI = RESPONSE.get(("".join([chr(105),chr(100)]))                                             )
                XJ.threadId: XI = RESPONSE.get(("".join([chr(116),chr(104),chr(114),chr(101),chr(97),chr(100),chr(73),chr(100)]))                                                         )
                XJ.labelIds: List[XI] = RESPONSE.get(("".join([chr(116),chr(104),chr(114),chr(101),chr(97),chr(100),chr(73),chr(100)]))                                                               )
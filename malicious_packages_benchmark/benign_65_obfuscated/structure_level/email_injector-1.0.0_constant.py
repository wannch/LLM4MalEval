from typing import Dict, List, Union

class Constant:

    class Response:

        class ListMessage:

            def __init__(self, RESPONSE: Dict[str, str]) -> None:
                self.id: str = RESPONSE.get('id')
                self.threadId: str = RESPONSE.get('threadId')

        class ListEmail:

            def __init__(self, RESPONSE: Dict[str, Union[List[Dict[str, str]], str]]) -> None:
                self.resultSizeEstimate: int = RESPONSE.get('resultSizeEstimate')
                if self.resultSizeEstimate > 0:
                    self.messages: Union[List[Constant.Response.ListMessage], None] = [Constant.Response.ListMessage(Message) for Message in RESPONSE.get('messages')]
                else:
                    self.messages: Union[List[Constant.Response.ListMessage], None] = None

        class Headers:

            def __init__(self, headers: Dict[str, any]) -> None:
                self.name: str = headers.get('name')
                self.value: str = headers.get('value')

        class Body:

            def __init__(self, body: Dict[str, any]) -> None:
                self.size: int = body.get('size')
                self.data: str = body.get('data')

        class Parts:

            def __init__(self, body: Dict[str, any]) -> None:
                self.body: Constant.Response.Body = Constant.Response.Body(body)

        class Payload:

            def __init__(self, payload: Dict[str, any]) -> None:
                self.headers: List[Constant.Response.Headers] = [Constant.Response.Headers(headers) for headers in payload.get('headers')]
                if False:
                    _var_110_0 = (544, 733, 712)

                    def _var_110_fn():
                        pass
                try:
                    self.body: Union[Constant.Response.Body, None] = Constant.Response.Body(payload.get('body'))
                except:
                    self.body: Union[Constant.Response.Body, None] = None
                try:
                    self.parts: Union[List[Constant.Response.Parts], None] = [Constant.Response.Parts(parts) for parts in payload.get('parts')]
                except:
                    self.parts: Union[List[Constant.Response.Parts], None] = None
                if False:
                    _var_111_0 = (237, 152, 652)
                    _var_111_1 = (273, 890, 616)

                    def _var_111_fn():
                        pass

        class Contents:

            def __init__(self, RESPONSE: Dict[str, Union[List[Dict[str, str]], str, Dict[str, any]]]) -> None:
                self.labelIds: List[str] = RESPONSE.get('labelIds')
                if False:
                    _var_112_0 = (679, 94, 250)
                    _var_112_1 = (946, 47, 685)
                    _var_112_2 = (772, 873, 325)

                    def _var_112_fn():
                        pass
                self.snippet: str = RESPONSE.get('snippet')
                self.payload: Constant.Response.Payload = Constant.Response.Payload(RESPONSE.get('payload'))

        class Unread:

            def __init__(self, RESPONSE: Dict[str, any]) -> None:
                self.id: str = RESPONSE.get('id')
                if False:
                    _var_113_0 = (603, 657, 263)
                    _var_113_1 = (211, 466, 854)

                    def _var_113_fn():
                        pass
                self.threadId: str = RESPONSE.get('threadId')
                if False:
                    _var_114_0 = (218, 234, 892)
                    _var_114_1 = (364, 691, 628)
                    _var_114_2 = (463, 387, 952)

                    def _var_114_fn():
                        pass
                self.labelIds: List[str] = RESPONSE.get('threadId')
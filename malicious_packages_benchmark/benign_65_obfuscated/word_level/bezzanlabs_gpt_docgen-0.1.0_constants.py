("".join([chr(10),chr(65),chr(108),chr(108),chr(32),chr(99),chr(111),chr(110),chr(115),chr(116),chr(97),chr(110),chr(116),chr(115),chr(32),chr(102),chr(111),chr(114),chr(32),chr(116),chr(104),chr(101),chr(32),chr(112),chr(97),chr(99),chr(107),chr(97),chr(103),chr(101),chr(46),chr(10)]))
Xh=str
import typing as tp
XW=tp.Type
XL=tp.Dict

from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.embeddings import Embeddings
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

__package_name__ =("".join([chr(98),chr(101),chr(122),chr(122),chr(97),chr(110),chr(108),chr(97),chr(98),chr(115),chr(46),chr(103),chr(112),chr(116),chr(95),chr(100),chr(111),chr(99),chr(103),chr(101),chr(110)]))
__version__ =("".join([chr(48),chr(46),chr(49),chr(46),chr(48)]))
__author__ =("".join([chr(86),chr(105),chr(116),chr(111),chr(114),chr(32),chr(66),chr(101),chr(122),chr(122),chr(97),chr(110),chr(32),chr(60),chr(118),chr(105),chr(116),chr(111),chr(114),chr(64),chr(98),chr(101),chr(122),chr(122),chr(97),chr(110),chr(46),chr(99),chr(111),chr(109),chr(62)]))

_available_chats: XL[Xh, XW[BaseChatModel]] = {
("".join([chr(111),chr(108),chr(108),chr(97),chr(109),chr(97)]))            : ChatOllama,
("".join([chr(111),chr(112),chr(101),chr(110),chr(97),chr(105)]))            : ChatOpenAI,
}

_available_embeddings: XL[Xh, XW[Embeddings]] = {
("".join([chr(111),chr(108),chr(108),chr(97),chr(109),chr(97)]))            : OllamaEmbeddings,
("".join([chr(111),chr(112),chr(101),chr(110),chr(97),chr(105)]))            : OpenAIEmbeddings,
}

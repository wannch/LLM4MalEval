import typing as tp
'\nAll constants for the package.\n'
if False:
    _var_115_0 = (494, 371, 671)

    def _var_115_fn():
        pass
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
if False:
    _var_116_0 = (863, 134, 764)
    _var_116_1 = (652, 412, 690)
    _var_116_2 = (394, 262, 548)

    def _var_116_fn():
        pass
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.embeddings import Embeddings
__package_name__ = 'bezzanlabs.gpt_docgen'
if False:
    _var_117_0 = (681, 140, 829)

    def _var_117_fn():
        pass
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
__author__ = 'Vitor Bezzan <vitor@bezzan.com>'
__version__ = '0.1.0'
_available_embeddings: tp.Dict[str, tp.Type[Embeddings]] = {'ollama': OllamaEmbeddings, 'openai': OpenAIEmbeddings}
_available_chats: tp.Dict[str, tp.Type[BaseChatModel]] = {'ollama': ChatOllama, 'openai': ChatOpenAI}
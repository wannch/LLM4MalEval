from typing import Any,Dict,Union
from DashAI.back.config_object import ConfigObject
from DashAI.back.core.schema_fields import(  bool_field,  none_type,  schema_field,  string_field,)
from DashAI.back.core.schema_fields.base_schema import BaseSchema
from DashAI.back.dataloaders.classes.dataloader import(  BaseDataLoader,  DataloaderMoreOptionsSchema,  DatasetSplitsSchema,)
from datasets import DatasetDict,load_dataset
from starlette.datastructures import UploadFile
class ExampleDataLoaderSchema(BaseSchema):
  name:schema_field(    none_type(string_field()),    "",    (      "Custom name to register your dataset. If no name is specified, "      "the name of the uploaded file will be used."    ),  )
  splits_in_folders:schema_field(    bool_field(),    False,    (      "If your data has folders that define the splits select 'true', "      "otherwise 'false'."    ),  )
  splits:DatasetSplitsSchema
  more_options:DataloaderMoreOptionsSchema
class ExampleDataLoaderClass(BaseDataLoader,ConfigObject):
  COMPATIBLE_COMPONENTS=[]
  SCHEMA=ExampleDataLoaderSchema
  def load_data(    self,    filepath_or_buffer:Union[UploadFile,str],    temp_path:str,    params:Dict[str,Any],  )->DatasetDict:
    raise NotImplementedError
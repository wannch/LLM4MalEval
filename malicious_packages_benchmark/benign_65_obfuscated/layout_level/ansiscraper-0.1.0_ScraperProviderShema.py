from abc import ABC,abstractmethod,abstractproperty
class ScraperProviderShema(ABC):
  @ abstractmethod
  def getProductListByCategory(self,productCategory):
    pass

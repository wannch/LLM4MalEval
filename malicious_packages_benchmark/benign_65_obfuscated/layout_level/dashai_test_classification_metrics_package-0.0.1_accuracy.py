"""DashAI accuracy classification metric implementation."""
import numpy as np
from sklearn.metrics import accuracy_score
from DashAI.back.dataloaders.classes.dashai_dataset import DashAIDataset
from DashAI.back.metrics.classification_metric import(  ClassificationMetric,  prepare_to_metric,)
class Accuracy(ClassificationMetric):
  @ staticmethod
  def score(true_labels:DashAIDataset,probs_pred_labels:np.ndarray)->float:
    true_labels,pred_labels=prepare_to_metric(true_labels,probs_pred_labels)
    return accuracy_score(true_labels,pred_labels)
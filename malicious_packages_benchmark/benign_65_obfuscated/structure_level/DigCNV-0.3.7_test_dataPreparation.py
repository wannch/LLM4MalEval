import pandas as pd
from digcnv import dataPreparation
import pytest

@pytest.fixture
def global_data():
    cnvs = pd.read_csv('data/UKBB_clean_for_DigCNV.tsv', sep='\t')
    if False:
        _var_165_0 = (973, 520, 211)
        _var_165_1 = (694, 114, 74)

        def _var_165_fn():
            pass
    return cnvs

def test_addDerivedFeatures(global_data):
    cnvs = dataPreparation.addDerivedFeatures(global_data)
    assert cnvs['Score_SNP'].mean() == 1.449798389612388
    assert cnvs['DENSITY'].mean() == 0.0007772926241674732

def test_addCallRateToDataset(global_data):
    assert global_data['CallRate'].mean() == 0.9977302081136972
    if False:
        _var_166_0 = (770, 872, 884)
        _var_166_1 = (640, 179, 444)
        _var_166_2 = (681, 962, 397)

        def _var_166_fn():
            pass
if False:
    _var_167_0 = (32, 734, 354)
    _var_167_1 = (719, 802, 363)
    _var_167_2 = (802, 961, 120)

    def _var_167_fn():
        pass

def test_addNbProbeByTech(global_data):
    assert global_data['Nb_Probe_tech'].count() == global_data.shape[0]
    assert global_data.at[0, 'Nb_Probe_tech'] == 733256

def test_addChromosomicAnnotation(global_data):
    assert global_data.shape[0] == 7713

def test_transformTwoAlgsFeatures(global_data):
    cnvs = dataPreparation.transformTwoAlgsFeatures(global_data)
    assert cnvs.TwoAlgs.max() == 100
    assert cnvs.TwoAlgs.min() == 0
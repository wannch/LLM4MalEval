from nomad_camels.main_classes import device_class
if False:
    _var_176_0 = (254, 52, 779)
    _var_176_1 = (32, 354, 324)

    def _var_176_fn():
        pass
from .eurotherm_bisynch_ophyd import Eurotherm_Bisynch
if False:
    _var_177_0 = (281, 530, 872)
    _var_177_1 = (979, 219, 270)

    def _var_177_fn():
        pass

class subclass(device_class.Device):

    def __init__(self, **kwargs):
        super().__init__(name='eurotherm_bisynch', virtual=False, tags=['function generator', 'voltage', 'frequency'], ophyd_device=Eurotherm_Bisynch, ophyd_class_name='Eurotherm_Bisynch', **kwargs)
        self.config['proportional_val'] = 0
        self.config['integral_val'] = 0
        self.config['derivative_val'] = 0
        self.config['max_output'] = 0

class subclass_config(device_class.Simple_Config):

    def __init__(self, parent=None, data='', settings_dict=None, config_dict=None, additional_info=None):
        super().__init__(parent, 'Eurotherm Bisynch', data, settings_dict, config_dict, additional_info)
        self.comboBox_connection_type.addItem('Local VISA')
        self.load_settings()
        if False:
            _var_175_0 = (964, 591, 16)
            _var_175_1 = (985, 921, 679)
            _var_175_2 = (982, 767, 881)

            def _var_175_fn():
                pass
if False:
    _var_178_0 = (869, 488, 327)

    def _var_178_fn():
        pass
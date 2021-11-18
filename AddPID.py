# Cura PostProcessingPlugin
# Author:   Jumbo125
# Date:     06.05.2021

# Description:  This plugin insert the PID-Tune to the gcode before G28

from ..Script import Script

class AddPID(Script):

    def __init__(self):
        super().__init__()

  
    def getSettingDataString(self):
        return """{
            "name": "Add PID",
            "key": "AddPID",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "is_pla":
                {
                    "label": "IF PLA",
                    "description": "If YOU USE PLA VALUE",
                    "type": "bool",
                    "default_value": false
                },
                "PLA-kp":
                {
                    "label": "PLA - Kp",
                    "description": "Infill Kp Value",
                    "type": "str",
                    "default_value": ""
                },
                "PLA-ki":
                {
                    "label": "PLA - Ki",
                    "description": "Infill Ki Value",
                    "type": "str",
                    "default_value": ""
                },
                "PLA-kd":
                {
                    "label": "PLA - Kd",
                    "description": "Infill Kd Value",
                    "type": "str",
                    "default_value": ""
                },
                "is_petg":
                {
                    "label": "IF PETG",
                    "description": "If YOU USE PETG VALUE",
                    "type": "bool",
                    "default_value": false
                },
                  "PETG-kp":
                {
                    "label": "PETG - Kp",
                    "description": "Infill Kp Value",
                    "type": "str",
                    "default_value": ""
                },
                "PETG-ki":
                {
                    "label": "PETG - Ki",
                    "description": "Infill Ki Value",
                    "type": "str",
                    "default_value": ""
                },
                "PETG-kd":
                {
                    "label": "PETG - Kd",
                    "description": "Infill Kd Value",
                    "type": "str",
                    "default_value": ""
                },
                "is_abs":
                {
                    "label": "IF ABS",
                    "description": "If YOU USE ABS VALUE",
                    "type": "bool",
                    "default_value": false
                },
                "ABS-kp":
                {
                    "label": "ABS - Kp",
                    "description": "Infill Kp Value",
                    "type": "str",
                    "default_value": ""
                },
                "ABS-ki":
                {
                    "label": "ABS - Ki",
                    "description": "Infill Ki Value",
                    "type": "str",
                    "default_value": ""
                },
                "ABS-kd":
                {
                    "label": "ABS - Kd",
                    "description": "Infill Kd Value",
                    "type": "str",
                    "default_value": ""
                }                
            }
        }"""

    def execute(self, data):
        kp = ""
        ki = ""
        kd = ""
        filament = ""
        
        if self.getSettingValueByKey("is_pla"):
            kp = self.getSettingValueByKey("PLA-kp")
            ki = self.getSettingValueByKey("PLA-ki")
            kd = self.getSettingValueByKey("PLA-kd")
            filament = "PLA"
        
        elif self.getSettingValueByKey("is_petg"):
            kp = self.getSettingValueByKey("PETG-kp")
            ki = self.getSettingValueByKey("PETG-ki")
            kd = self.getSettingValueByKey("PETG-kd")
            filament = "PETG"
        
        elif self.getSettingValueByKey("is_abs"):
            kp = self.getSettingValueByKey("ABS-kp")
            ki = self.getSettingValueByKey("ABS-ki")
            kd = self.getSettingValueByKey("ABS-kd")
            filament = "ABS"
        
        
        pid_to_add = "M301 E0 P" + kp + " I" + ki + " D" + kd + " ;AddPID by Jumbo125 benutztes Filament:" + filament + "\n"
        for layer in data:
            # Check that a layer is being printed
            lines = layer.split("\n")
            for line in lines:
                if "G28" in line:
                    index = data.index(layer)
                    layer =  pid_to_add + layer
                    
                    data[index] = layer
                    break
        return data
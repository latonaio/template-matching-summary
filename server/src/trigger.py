from src.base import BaseSummary
from aion.logger import lprint


class TriggerSummary(BaseSummary):
    def __init__(self):
        self.vehicle_name = None
        self.reset()

    def reset(self):
        super().reset()
        return

    def should_be_reset(self, dicts):
        new_vehicle_name = None
        if dicts[0]['templates']:
            new_vehicle_name = dicts[0]['templates'][0]['vehicle_name']

        if (self.vehicle_name or new_vehicle_name) and self.vehicle_name != new_vehicle_name:
            self.vehicle_name = new_vehicle_name
            return True
        return False

    def get_trigger(self):
        res = {
            'status': False,
            'values': []
        }

        if len(self._template_dicts) == 0:
            return res

        # status
        res['status'] = True
        # values
        res['values'] = self._template_dicts
        return res

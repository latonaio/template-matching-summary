from src.base import BaseSummary
from aion.logger import lprint


class VehicleSummary(BaseSummary):
    def __init__(self):
        self.reset()

    def reset(self):
        super().reset()
        self.is_first_vehicle = False
        return

    def _get_vehicle(self, dicts):
        res = {
            'status': False,
            'name': 'Unknown',
            'first': False,
            'values': []
        }

        if len(dicts) == 0:
            return res

        # status
        res['status'] = True
        # name
        res['name'] = dicts[0]['vehicle_name']
        # first
        if not self.is_first_vehicle:
            self.is_first_vehicle = True
            res['first'] = True
        # values
        res['values'] = dicts
        return res

    def get_vehicle(self):
        return self._get_vehicle(self._template_dicts)

    def get_all_vehicles(self):
        return self._get_vehicle(self.template_dicts)

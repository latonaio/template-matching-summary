import datetime
import uuid

from aion.logger import lprint


class BaseSummary():
    def __init__(self):
        self.reset()

    def reset(self):
        self.template_dicts = []
        self.end_dicts = []
        self.path_dicts = []
        self._template_dicts = []
        self._end_dicts = []
        self._path_dicts = []
        self.session_id = None
        self.n_requests = 0
        self.n_data = 0
        self.timestamp = None
        self.start_timestamp = None
        self.end_timestamp = None
        self.is_first_vehicle = False
        return

    def set(self, dicts):
        self.timestamp = datetime.datetime.now().isoformat()

        # Receive data at first
        if self.session_id is None:
            self.session_id = str(uuid.uuid4())
            self.start_timestamp = self.timestamp

        # Parse dicts
        self.n_requests += 1

        self._template_dicts = []
        self._end_dicts = []
        self._path_dicts = []
        for _dict in dicts:
            self.n_data += 1
            exist = False

            # data_dict
            for t_dict in _dict['templates']:

                # TODO: Delete the bellow debug code
                # t_dict['pass_threshold'] = 0.3

                if t_dict['matching_rate'] >= t_dict['pass_threshold']:
                    exist = True
                    t_dict['n_data'] = self.n_data
                    t_dict['input_path'] = _dict['input_path']
                    t_dict['output_path'] = _dict['output_path']
                    if t_dict['is_car_end'] == 0:
                        self._template_dicts.append(t_dict)
                    else:
                        self._end_dicts.append(t_dict)

            # path_dict
            if exist:
                path_dict = {
                    'n_requests': self.n_requests,
                    'n_data': self.n_data,
                    'input_path': _dict['input_path'],
                    'output_path': _dict['output_path'],
                }
                self._path_dicts.append(path_dict)

        return

    def get_metadata(self):
        res = {
            'session_id': self.session_id,
            'n_requests': self.n_requests,
            'n_data': self.n_data,
            'start_timestamp': self.start_timestamp,
            'timestamp': self.timestamp,
            'end_timestamp': self.end_timestamp,
        }
        return res

    def get_end(self):
        res = {
            'status': False,
            'values': []
        }

        lprint(self.n_data)
        if self.n_data < 200:
            return res

        if len(self._end_dicts) == 0:
            return res

        # Set self.end_timestamp
        self.end_timestamp = self.timestamp

        # status
        res['status'] = True
        # values
        res['values'] = self._end_dicts
        return res

    def stack(self):
        self.template_dicts.extend(self._template_dicts)
        self.end_dicts.extend(self._end_dicts)
        self.path_dicts.extend(self._path_dicts)
        return

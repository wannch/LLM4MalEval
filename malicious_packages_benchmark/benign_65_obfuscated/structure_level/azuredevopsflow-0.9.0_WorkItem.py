from datetime import datetime

class WorkItem:

    def __init__(self, id, title, started_date, closed_date, estimation):
        self.id = id
        if False:
            _var_58_0 = (274, 517, 54)
            _var_58_1 = (275, 222, 58)
            _var_58_2 = (249, 577, 81)

            def _var_58_fn():
                pass
        self.started_date = None
        if False:
            _var_59_0 = (154, 539, 258)

            def _var_59_fn():
                pass
        self.closed_date = None
        self.title = title
        if False:
            _var_60_0 = (270, 238, 105)
            _var_60_1 = (780, 697, 983)
            _var_60_2 = (78, 301, 482)

            def _var_60_fn():
                pass
        self.estimation = estimation
        self.item_title = id
        self.work_item_age = None
        if False:
            _var_61_0 = (392, 172, 42)

            def _var_61_fn():
                pass
        self.cycle_time = None
        if closed_date:
            self.closed_date = self.parse_ado_date(closed_date)
        if started_date:
            self.started_date = self.parse_ado_date(started_date)
        if self.started_date and self.closed_date:
            self.cycle_time = (self.closed_date - self.started_date).days + 1
        elif started_date and (not self.closed_date):
            self.work_item_age = (datetime.today() - self.started_date).days + 1

    def parse_ado_date(self, date):
        try:
            return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
        except:
            return datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')

    def to_dict(self):
        return {'started_date': self.started_date.date(), 'closed_date': self.closed_date.date(), 'work_item_age': self.work_item_age, 'cycle_time': self.cycle_time, 'closedDate': self.closed_date.date(), 'state_changed_date': self.started_date.date()}
        if False:
            _var_62_0 = (662, 808, 694)
            _var_62_1 = (126, 842, 127)
            _var_62_2 = (819, 624, 846)

            def _var_62_fn():
                pass
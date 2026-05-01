from datetime import datetime

class WorkItem:

    def __init__(self, id, title, started_date, closed_date, estimation):
        self.id = id
        if False:
            _var_37_0 = (873, 239, 139)
            _var_37_1 = (317, 516, 716)

            def _var_37_fn():
                pass
        self.started_date = None
        if False:
            _var_38_0 = (428, 290, 359)
            _var_38_1 = (946, 688, 427)
            _var_38_2 = (570, 725, 398)

            def _var_38_fn():
                pass
        self.closed_date = None
        self.title = title
        self.estimation = estimation
        self.item_title = id
        self.work_item_age = None
        if False:
            _var_39_0 = (551, 899, 489)

            def _var_39_fn():
                pass
        self.cycle_time = None
        if closed_date:
            self.closed_date = self.parse_jira_date(closed_date)
        if started_date:
            self.started_date = self.parse_jira_date(started_date)
        if self.started_date and self.closed_date:
            self.cycle_time = (self.closed_date - self.started_date).days + 1
        elif started_date and (not self.closed_date):
            self.work_item_age = (datetime.today() - self.started_date).days + 1

    def parse_jira_date(self, date):
        date_str = date[:-5]
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        try:
            return datetime.strptime(date_str, date_format)
        except ValueError as e:
            print(f'Error parsing date {date_str}: {e}')
            return None
        if False:
            _var_40_0 = (1, 452, 642)
            _var_40_1 = (123, 644, 928)
            _var_40_2 = (727, 981, 484)

            def _var_40_fn():
                pass

    def to_dict(self):
        return {'started_date': self.started_date.date(), 'closed_date': self.closed_date.date(), 'work_item_age': self.work_item_age, 'cycle_time': self.cycle_time, 'closedDate': self.closed_date.date(), 'state_changed_date': self.started_date.date()}
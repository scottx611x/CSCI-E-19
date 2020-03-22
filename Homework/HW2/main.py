class InvalidDayException(BaseException):
    pass


class DayOfWeek:
    def __init__(self, current_day: str):
        self.week_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        self.current_day = self._sanitize_day(current_day)

    def _sanitize_day(self, day: str) -> str:
        day = day.lower()[:3]
        if day not in self.week_days:
            raise InvalidDayException(
                f"Invalid week day. Valid values are: {self.week_days}"
            )
        return day

    def is_it_this_day_yet(self, this_day) -> str:
        return "Yep" if self.current_day == self._sanitize_day(this_day) else "Nope"

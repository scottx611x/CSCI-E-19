# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from behave_classy import step_impl_base

from main import DayOfWeek

StepBase = step_impl_base()


class IsItFriday(StepBase):
    def __init__(self):
        self.today = None
        self.message = ""

    @StepBase.given('today is "{day}"')
    def today_is(self, day):
        self.today = DayOfWeek(day)

    @StepBase.when('I ask whether it is "{another_day}"')
    def i_ask_whether_it_is(self, another_day):
        self.message = self.today.is_it_this_day_yet(another_day)

    @StepBase.then('I should be told "{message}"')
    def i_should_be_told(self, message):
        assert self.message == message


IsItFriday().register()

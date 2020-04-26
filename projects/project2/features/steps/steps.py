import ast

from behave_classy import step_impl_base
import app
from utils import MessageConstructor


class StepBase(step_impl_base()):
    pass

class RequestToRootSteps(StepBase):
    """features/request_to_root_path.feature"""
    def __init__(self):
        self.app = app.app
        self.test_client = self.app.test_client()
        self.path = None
        self.response = None

    @StepBase.given('Path is "{path}"')
    def path_is(self, path):
        self.path = path

    @StepBase.when('User requests said path')
    def user_requests_said_path(self):
        self.response = self.test_client.get(self.path)

    @StepBase.then('They should get a {status_code:d} response')
    def they_should_get_a_successful_response(self, status_code):
        assert self.response.status_code == status_code

    @StepBase.then('They should receive the following message from a JSON payload: {message}')
    def they_should_receive_the_following_message_from_a_json_payload(self, message):
        assert self.response.json == {"message": message}


class RequestToNamedPathSteps(StepBase):
    """features/request_to_named_path.feature"""
    def __init__(self):
        self.app = app.app
        self.test_client = self.app.test_client()
        self.path = None
        self.response = None

    @StepBase.given('Path is "{path}"')
    def path_is(self, path):
        self.path = path

    @StepBase.when('User requests said path')
    def user_requests_said_path(self):
        self.response = self.test_client.get(self.path)

    @StepBase.then('They should get a {status_code:d} response')
    def they_should_get_a_successful_response(self, status_code):
        assert self.response.status_code == status_code

    @StepBase.then('They should receive the following message from a JSON payload: {message}')
    def they_should_receive_the_following_message_from_a_json_payload(self, message):
        assert self.response.json == {"message": message}


class MessageConstructorSteps(StepBase):
    """features/message_constructor.feature"""
    def __init__(self):
        self.message = None
        self.message_constructor = None

    @StepBase.given('message is "{message}"')
    def message_is(self, message):
        self.message = message

    @StepBase.when('MessageConstructor is initialized with said message')
    def message_constructor_is_initialized_with_said_message(self):
        self.message_constructor = MessageConstructor(self.message)

    @StepBase.then('the resulting message attribute should be: {message_dict}')
    def the_resulting_message_attribute_should_be(self, message_dict):
        # Don't judge XD
        assert self.message_constructor.message == ast.literal_eval(message_dict)


"""Initialize and register any StepBase subclasses"""
for s in StepBase.__subclasses__():
    s().register()

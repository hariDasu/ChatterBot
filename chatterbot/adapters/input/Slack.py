from chatterbot.adapters.input import InputAdapter
from slackclient import SlackClient
from chatterbot.conversation import Statement
from time import sleep
import requests

class SlackAdapter(InputAdapter):
    """
    This is an abstract class that represents the
    interface that all input adapters should implement.
    """

    def __init__(self, **kwargs):
        super(SlackAdapter, self).__init__(**kwargs)
        self.SlackAdapter.slack_access_token = kwargs.get("slack_access_token");
        self.SlackAdapter.client = SlackClient(self.SlackAdapter.slack_access_token)
        self.SlackAdapter.client.rtm_connect()
        self.SlackAdapter.channel = kwargs.get("slack_channel")


    def process_input(self,statement):
        """
        Returns a statement object based on the input source.
        """
        if  self.SlackAdapter.client.rtm_connect():
            input_statement = self.SlackAdapter.client.rtm_read()
            while True:
                if input_statement:
                    try:
                        parsedMessage = input_statement[0]['text']
                        statement = Statement(parsedMessage)
                        #message_channel = input_statement[0]['channel']

                    except:
                        pass
        else:
            raise self.AdapterMethodNotImplementedError()

        return statement

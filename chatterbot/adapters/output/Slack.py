from chatterbot.adapters.output import OutputAdapter
import requests
import json
import time
from slackclient import SlackClient


class SlackAdapter(OutputAdapter):
    """
    An output adapter that allows a ChatterBot instance to send
    responses to a Slack channel.
    """
    def __init__(self, **kwargs):
        super(SlackAdapter, self).__init__(**kwargs)
        self.SlackAdapter.slack_access_token = kwargs.get("slack_access_token");
        self.SlackAdapter.client = SlackClient(self.SlackAdapter.slack_access_token)
        self.SlackAdapter.client.rtm_connect()
        self.SlackAdapter.channel = kwargs.get("slack_channel")
    #
    # def send_message(self, slack_channel, message):
    #     """
    #     Send a message to a HipChat room.
    # https: // www.hipchat.com / docs / apiv2 / method / send_message
    # """
    # self.SlackOutputAdapter.client.rtm_send_message(slack_channel, message)

    def process_response(self, statement):
        SlackAdapter.client.rtm_send_message( self.SlackAdapter.channel, statement)
        return statement

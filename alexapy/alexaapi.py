"""
Python Package for controlling Alexa devices (echo dot, etc) programmatically.

For more details about this api, please refer to the documentation at
https://gitlab.com/keatontaylor/alexapy
VERSION 1.0.0
"""
import logging

_LOGGER = logging.getLogger(__name__)


class AlexaAPI():
    """Class for accessing a specific Alexa device using API.

    Args:
    device (AlexaClient): Instance of an AlexaClient to access
    login (AlexaLogin): Successfully logged in AlexaLogin
    """

    def __init__(self, device, login):
        """Initialize Alexa device."""
        self._device = device
        self._session = login._session
        self._url = 'https://alexa.' + login._url

        csrf = self._session.cookies.get_dict()['csrf']
        self._session.headers['csrf'] = csrf

    def _catchAllExceptions(func):
        import functools

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as ex:
                template = ("An exception of type {0} occurred."
                            " Arguments:\n{1!r}")
                message = template.format(type(ex).__name__, ex.args)
                _LOGGER.error(("An error occured accessing AlexaAPI: "
                               "{}").format(message))
                return None
        return wrapper

    @_catchAllExceptions
    def _post_request(self, uri, data):
        self._session.post(self._url + uri, json=data)

    @_catchAllExceptions
    def _get_request(self, uri, data=None):
        return self._session.get(self._url + uri, json=data)

    @_catchAllExceptions
    def get_last_device_serial(self):
        """Identify the last device's serial number."""
        response = self._get_request('/api/activities?'
                                     'startTime=&size=1&offset=1')
        last_activity = response.json()['activities'][0]
        # Ignore discarded activity records
        if (last_activity['activityStatus'][0]
                != 'DISCARDED_NON_DEVICE_DIRECTED_INTENT'):
            return last_activity['sourceDeviceIds'][0]['serialNumber']
        else:
            return None

    def play_music(self, provider_id, search_phrase, customer_id=None):
        """Play Music based on search."""
        data = {
            "behaviorId": "PREVIEW",
            "sequenceJson": "{\"@type\": \
            \"com.amazon.alexa.behaviors.model.Sequence\", \
            \"startNode\":{\"@type\": \
            \"com.amazon.alexa.behaviors.model.OpaquePayloadOperationNode\", \
            \"type\":\"Alexa.Music.PlaySearchPhrase\",\"operationPayload\": \
            {\"deviceType\":\"" + self._device._device_type + "\", \
            \"deviceSerialNumber\":\"" + self._device.unique_id +
            "\",\"locale\":\"en-US\", \
            \"customerId\":\"" + (customer_id
                                  if customer_id is not None
                                  else self._device_owner_customer_id) +
            "\", \"searchPhrase\": \"" + search_phrase + "\", \
             \"sanitizedSearchPhrase\": \"" + search_phrase + "\", \
             \"musicProviderId\": \"" + provider_id + "\"}}}",
            "status": "ENABLED"
        }

        self._post_request('/api/behaviors/preview',
                           data=data)

    def send_tts(self, message, customer_id=None):
        """Send message for TTS at speaker."""
        data = {
            "behaviorId": "PREVIEW",
            "sequenceJson": "{\"@type\": \
            \"com.amazon.alexa.behaviors.model.Sequence\", \
            \"startNode\":{\"@type\": \
            \"com.amazon.alexa.behaviors.model.OpaquePayloadOperationNode\", \
            \"type\":\"Alexa.Speak\",\"operationPayload\": \
            {\"deviceType\":\"" + self._device._device_type + "\", \
            \"deviceSerialNumber\":\"" + self._device.unique_id +
            "\",\"locale\":\"en-US\", \
            \"customerId\":\"" + (customer_id
                                  if customer_id is not None
                                  else self._device_owner_customer_id) +
            "\", \"textToSpeak\": \"" + message + "\"}}}",
            "status": "ENABLED"
        }
        self._post_request('/api/behaviors/preview',
                           data=data)

    def set_media(self, data):
        """Select the media player."""
        self._post_request('/api/np/command?deviceSerialNumber=' +
                           self._device.unique_id + '&deviceType=' +
                           self._device._device_type, data=data)

    def previous(self):
        """Play previous."""
        self.set_media({"type": "PreviousCommand"})

    def next(self):
        """Play next."""
        self.set_media({"type": "NextCommand"})

    def pause(self):
        """Pause."""
        self.set_media({"type": "PauseCommand"})

    def play(self):
        """Play."""
        self.set_media({"type": "PlayCommand"})

    def set_volume(self, volume):
        """Set volume."""
        self.set_media({"type": "VolumeLevelCommand",
                        "volumeLevel": volume*100})

    @_catchAllExceptions
    def get_state(self):
        """Get playing state."""
        response = self._get_request('/api/np/player?deviceSerialNumber=' +
                                     self._device.unique_id +
                                     '&deviceType=' +
                                     self._device._device_type +
                                     '&screenWidth=2560')
        return response.json()

    @staticmethod
    @_catchAllExceptions
    def get_bluetooth(login):
        """Get paired bluetooth devices."""
        session = login._session
        url = login._url
        response = session.get('https://alexa.' + url +
                               '/api/bluetooth?cached=false')
        return response.json()

    def set_bluetooth(self, mac):
        """Pair with bluetooth device with mac address."""
        self._post_request('/api/bluetooth/pair-sink/' +
                           self._device._device_type + '/' +
                           self._device.unique_id,
                           data={"bluetoothDeviceAddress": mac})

    def disconnect_bluetooth(self):
        """Disconnect all bluetooth devices."""
        self._post_request('/api/bluetooth/disconnect-sink/' +
                           self._device._device_type + '/' +
                           self._device.unique_id, data=None)

    @staticmethod
    @_catchAllExceptions
    def get_devices(login):
        """Identify all Alexa devices."""
        session = login._session
        url = login._url
        response = session.get('https://alexa.' + url +
                               '/api/devices-v2/device')
        return response.json()['devices']

    @staticmethod
    @_catchAllExceptions
    def get_authentication(login):
        """Get authentication json."""
        session = login._session
        url = login._url
        response = session.get('https://alexa.' + url +
                               '/api/bootstrap')
        return response.json()['authentication']

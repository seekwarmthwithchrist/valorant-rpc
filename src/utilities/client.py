import valclient


class Client(valclient.Client):
    """valclient.Client with compatibility fixes for newer VALORANT versions."""

    def fetch_presence(self, puuid: str = None) -> dict:
        return Client.flatten_presence(super().fetch_presence(puuid))

    @staticmethod
    def flatten_presence(presence):
        '''
        Riot moved most presence fields into nested objects
        (matchPresenceData, partyPresenceData, playerPresenceData, ...).
        Copy them back to the top level so the rest of the app can keep using
        presence["sessionLoopState"], presence["partySize"], etc.
        Existing top-level keys are never overwritten.
        '''
        if not isinstance(presence, dict):
            return presence

        flattened = dict(presence)
        for key in ("matchPresenceData", "partyPresenceData", "playerPresenceData", "premierPresenceData"):
            nested = presence.get(key)
            if isinstance(nested, dict):
                for nested_key, value in nested.items():
                    flattened.setdefault(nested_key, value)
        return flattened

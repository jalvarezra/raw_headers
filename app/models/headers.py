

class RawHeaders:

    def __init__(self, incoming_request):
        self._req = incoming_request
        self._headers = []

    def get_headers(self):
        for header in self._req.headers:
            self._headers.append(header)
        return self._headers

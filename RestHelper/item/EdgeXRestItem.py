
class Addressable:
    def __init__(self, origin, name, protocol='HTTP', address='127.0.0.1', port=49090, path='127.0.0.1', publisher='none', user='none', password='none', topic='none'):
        self.origin = origin
        self.name = name
        self.protocol = protocol
        self.address = address
        self.port = port
        self.path = path
        self.publisher = publisher
        self.user = user
        self.password = password
        self.topic = topic

    def getData(self):
        return {
            'origin': self.origin,
            'name': self.name,
            'protocol': self.protocol,
            'address': self.address,
            'port': self.port,
            'path': self.path,
            'publisher': self.publisher,
            'user': self.user,
            'password': self.password,
            'topic': self.topic
        }


class DeviceService:
    def __init__(self, origin, name, description, labels, addressable, streamingServiceName='wowza', EncoderServiceName='kvazaar'):
        self.origin = origin
        self.name = name
        self.description = description
        self.streamingServiceName = streamingServiceName
        self.EncoderServiceName = EncoderServiceName
        self.labels = labels
        self.addressable = addressable

    def getData(self):
        return {
            'origin': self.origin,
            'name': self.name,
            'description': self.description,
            'streamingServiceName': self.streamingServiceName,
            'encoderServiceName': self.EncoderServiceName,
            "labels": self.labels,
            "addressable": self.addressable
        }
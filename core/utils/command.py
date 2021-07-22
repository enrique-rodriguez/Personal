from .entities import EntityFactory


class Command:
    make = EntityFactory
    request_class_name = 'Request'
    
    def __call__(self, data):
        request = self.get_request(data)
        return self.execute(request)
    
    def get_request(self, data):
        klass = self.get_request_class()
        return klass(**data)
    
    def get_request_class(self):
        if not hasattr(self, self.request_class_name):
            raise SystemError("Request class not defined within command.")
        return getattr(self, self.request_class_name)
    
    def execute(self, request):
        raise NotImplementedError
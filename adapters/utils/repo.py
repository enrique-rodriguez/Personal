

class DjangoRepo:
    model = None
    last_insert_id = None

    def count(self):
        return self.model.objects.count()
    
    def save(self, data):
        model = self.model.objects.create(**data)
        self.last_insert_id = model.id

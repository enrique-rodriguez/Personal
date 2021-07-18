from core import entities


class EntityFactory:
    
    @classmethod
    def message(self, **kwargs):
        return entities.Message(**kwargs)
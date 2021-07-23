from rest_framework import serializers
from django.core.exceptions import ImproperlyConfigured
from django.apps import apps


def modelserializer_factory(model, serializer=serializers.ModelSerializer, fields='__all__', exclude=None):
    if isinstance(model, str):
        app_label, model_name = model.split('.')
        model = apps.get_model(app_label=app_label, model_name=model_name)
    attrs = {'model': model}
    if fields is not None:
        attrs['fields'] = fields
    if exclude is not None:
        attrs['exclude'] = exclude

    # If parent serializer class already has an inner Meta, the Meta we're
    # creating needs to inherit from the parent's inner meta.
    bases = (serializer.Meta,) if hasattr(serializer, 'Meta') else ()
    Meta = type('Meta', bases, attrs)
    class_name = model.__name__ + 'Serializer'

    # Class attributes for the new serializer class.
    serializer_class_attrs = {
        'Meta': Meta,
    }

    if (getattr(Meta, 'fields', None) is None and
            getattr(Meta, 'exclude', None) is None):
        raise ImproperlyConfigured(
            "Calling modelserializer_factory without defining 'fields' or "
            "'exclude' explicitly is prohibited."
        )

    # Instantiate type(serializer) in order to use the same metaclass as serializer.
    return type(serializer)(class_name, (serializer,), serializer_class_attrs)
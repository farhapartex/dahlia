from django.db import models

class StreamField(models.Field):
    def __init__(self, block_types=[], **kwargs):
        super().__init__(**kwargs)
        self.stream_block = block_types
    
    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'block': self.stream_block}
        defaults.update(kwargs)
        return super().formfield(**defaults)

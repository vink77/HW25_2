from rest_framework import serializers

class Video_Url_Validator:
    def __init__(self, field):
        self.field = field
    def __call__(self, value):
        dict_value = dict(value).get(self.field)
        if not ('youtube.com' in dict_value):
            raise serializers.ValidationError("Ссылка должна быть на youtube.com")
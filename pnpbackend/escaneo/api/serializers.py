from rest_framework.serializers import ModelSerializer
from escaneo.models import Escaneo


class EscaneoSerializer(ModelSerializer):
    class Meta:
        model = Escaneo
        fields = ['id', 'name', 'academic_training','place_residence','residence_address','observation','user_creation', 'date_creation','user_modify','date_modify']

    def __init__(self, *args, **kwargs):
        super(EscaneoSerializer, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['academic_training'].required = False
        self.fields['place_residence'].required = False
        self.fields['residence_address'].required = False
        self.fields['observation'].required = False
        self.fields['user_creation'].required = False
        self.fields['date_creation'].required = False
        self.fields['user_modify'].required = False
        self.fields['date_modify'].required = False

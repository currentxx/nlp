from .models import Kurlar
from .models import Ozet
from .models import OzetveTamMetin
from rest_framework import serializers
class KurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kurlar
        #fields=('doviz_ismi','alis','satis')
        fields='__all__'

class OzetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ozet
        #fields=('kelime','alis','satis')
        fields='__all__'

class OzetTamSerializer(serializers.ModelSerializer):
    class Meta:
        model=OzetveTamMetin
        #fields=('kelime','alis','satis')
        fields='__all__'



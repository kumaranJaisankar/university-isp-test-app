from rest_framework.serializers import ModelSerializer 
from openwisp_radius.models import RadiusPostAuth



class RadAuthSerilizers(ModelSerializer):

    class Meta:
        model = RadiusPostAuth 
        fields = "__all__"
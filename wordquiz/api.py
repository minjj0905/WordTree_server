from wordquiz.models import Threequiz, Fourquiz, Fivequiz
from rest_framework import serializers, viewsets

class ThreequizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Threequiz
        fields = '__all__'

class ThreequizViewSet(viewsets.ModelViewSet):
    queryset = Threequiz.objects.all()
    serializers_class = ThreequizSerializer
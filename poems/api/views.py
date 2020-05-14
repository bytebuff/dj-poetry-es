from rest_framework import generics
from poems.models import Poem
from poems.search import search
from .serializers import PoemSerializer

class PoemList(generics.ListAPIView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q')
        if q is not None:
            return search(q)
        return super().get_queryset()
from elasticsearch_dsl.query import Q, MultiMatch, SF
from .documents import PoemDocument

def get_search_query(phrase):
    query=MultiMatch(
            fields=['title', 'author', 'paragraphs', ],
            query=phrase
        )
    return PoemDocument.search().query(query).extra(from_=0, size=10)
    # return PoemDocument.search().query(query)[0:25] # 等价操作

def search(phrase):
    return get_search_query(phrase).to_queryset()
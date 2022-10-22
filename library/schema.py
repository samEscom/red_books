import graphene
from graphene_django import DjangoObjectType

from library.models import Category, Book

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "is_active", "created", "updated")



class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)

    def resolve_all_categories(self, info):

        return Category.objects.all()


schema = graphene.Schema(query=Query)

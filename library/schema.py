import graphene
from graphene_django import DjangoObjectType

from library.models import Category, Book

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "key_string", "is_active", "created", "updated")

class BookType(DjangoObjectType):

    class Meta:
        model = Book
        fields = (
            "id", "name", "description", "category", "is_active", "created", "updated"
        )


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_books = graphene.List(BookType)
    book_by_name = graphene.Field(BookType, name=graphene.String(required=True))

    def resolve_all_categories(self, info):

        return Category.objects.all()

    def resolve_all_books(self, info):

        return Book.objects.select_related("category").all()

    def resolve_book_by_name(self, info, name):
        try:
            return Book.objects.select_related("category").get(name=name)
        except Book.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)

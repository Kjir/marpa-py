from django.contrib.auth.models import User, Group
from rest_framework import serializers
from marpa.librarian.models import Book, Patron, Loan


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'pages', 'published_on')

class PatronSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patron
        fields = ('first_name', 'last_name')


class LoanSerializer(serializers.HyperlinkedModelSerializer):
    patron = serializers.ReadOnlyField(source='patron.first_name')
    book = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Loan
        fields = ('book', 'patron', 'rent_date', 'due_date')

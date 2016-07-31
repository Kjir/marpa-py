from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from marpa.librarian.serializers import UserSerializer, GroupSerializer, BookSerializer, PatronSerializer, LoanSerializer
from marpa.librarian.models import Book, Patron, Loan


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint to retrieve the list of books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PatronViewSet(viewsets.ModelViewSet):
    """
    API endpoint to retrieve list of patrons
    """
    queryset = Patron.objects.all()
    serializer_class = PatronSerializer

class LoanViewSet(viewsets.ModelViewSet):
    """
    API endpoint to retrieve list of loans
    """
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

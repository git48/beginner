"""
Write down any action related to the user
"""

from django.view.generic import TemplateView
from __init__ import AbstractUserView

class UserIndex(AbstractUserView,TemplateView):
    pass

class UserPost(AbstractUserView,TemplateView):
    pass

class UserReply(AbstractUserView,TemplateView):
    pass

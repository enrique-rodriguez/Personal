from django.test import TestCase
from django.utils.translation import ugettext_lazy as _
from app.models import MessageModel


class TestMessageModel(TestCase):

    def test_verbose_names(self):
        self.assertEqual(MessageModel._meta.verbose_name, _("Message"))
        self.assertEqual(MessageModel._meta.verbose_name_plural, _("Messages"))
    
    def test_verbose_field_names(self):
        self.assertEqual(MessageModel._meta.get_field("name").verbose_name, _("Name"))
        self.assertEqual(MessageModel._meta.get_field("body").verbose_name, _("Body"))
        self.assertEqual(MessageModel._meta.get_field("address").verbose_name, _("Email"))
        self.assertEqual(MessageModel._meta.get_field("subject").verbose_name, _("Subject"))
        self.assertEqual(MessageModel._meta.get_field("created").verbose_name, _("Created"))

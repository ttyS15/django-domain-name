# coding: utf-8

import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.encoding import smart_text
from django.utils.translation import gettext_lazy as _


class DomainValidator(RegexValidator):
    """ Валидаторо доменного имени.

    Основан на коде из
    https://code.djangoproject.com/ticket/18119
    """
    regex = re.compile(
        r'^(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.){0,126}(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)$',
        re.IGNORECASE
    )
    message = 'Enter a valid domain name value'

    def __init__(self, *args, **kwargs):
        self.accept_idna = bool(kwargs.pop('accept_idna', True))
        super(DomainValidator, self).__init__(*args, **kwargs)
        if self.accept_idna:
            self.message = _('Enter a valid plain or internationalized domain name value')

    def __call__(self, value):
        # validate
        try:
            super(DomainValidator, self).__call__(value)
        except ValidationError as e:
            # maybe this is a unicode-encoded IDNA string?
            if not self.accept_idna: raise
            if not value: raise
            # convert it unicode -> ascii
            try:
                asciival = smart_text(value).encode('idna')
            except UnicodeError:
                raise e  # raise the original ASCII error
            # validate the ascii encoding of it
            super(DomainValidator, self).__call__(asciival)


class MagicDomainValidator(DomainValidator):
    """ Расширяет валидаторо стандартных доменов '*.' в начале доменного имени.
    """
    regex = re.compile(
        r'^(?:(?:\*\.)?(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.){0,126}(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?))$',
        re.IGNORECASE
    )

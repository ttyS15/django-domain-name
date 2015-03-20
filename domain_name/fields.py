# coding: utf-8
from __future__ import absolute_import

from django.db import models
from django.utils import six
from django.utils.translation import ugettext_lazy as _

from .utils import refine_domain

from .validators import MagicDomainValidator, DomainValidator


class DomainField(six.with_metaclass(models.SubfieldBase, models.CharField)):
    """ Поле модели для работы с именами доменов.

    Обеспечивает проверку имён на валидность в соотвествие со стандартами. Имена
    доменов в БД приводит к нижнему регистру.

    """
    MAX_DOMAIN_NAME_LENGTH = 253
    VALIDATOR_CLASS = DomainValidator

    description = _('Domain name (up to %(max_length)s)')

    def __init__(self, verbose_name=None, name=None, primary_key=False,
                 max_length=None, **kwargs):
        """ Задаёт длинну для доменов, определяет валидатор.
        """
        if not max_length or max_length > self.MAX_DOMAIN_NAME_LENGTH:
            max_length = self.MAX_DOMAIN_NAME_LENGTH
        super(DomainField, self).__init__(
            verbose_name=verbose_name, name=name, primary_key=primary_key,
            max_length=max_length, **kwargs)
        self.validators.append(self.VALIDATOR_CLASS())

    def south_field_triple(self):
        """ Поддержка интроспекции для South.
        """
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.CharField"
        args, kwargs = introspector(self)
        return field_class, args, kwargs

    def to_python(self, value):
        """ Для питона имена всегда восстанавливаются из IDNA
        """
        value = refine_domain(value)

        try:
            return value.decode('idna')
        except UnicodeError:
            # вероятно уже восстановленная форма
            return value

    def get_prep_value(self, value):
        """ При работе с БД приводит имена к IDNA кодировке для единообрази при
        сравнении.
        """
        return refine_domain(value).encode('idna')


class MagicDomainField(DomainField):
    """ Поле модели для работы с нестандартными именами доменов, содержащими
    "*." в начале.
    """
    MAX_DOMAIN_NAME_LENGTH = 255  # Вообще-то 253, еще 2 нужно под '*.'
    VALIDATOR_CLASS = MagicDomainValidator

    description = _('Domain with (*.) sub-domains (up to %(max_length)s)')


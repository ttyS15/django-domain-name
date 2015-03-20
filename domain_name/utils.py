# coding: utf-8
from django.utils.encoding import smart_text


def domain_ranking(domain):
    """ Разбивает домен на состовляющие его родительские домены

    Пример:
      www.yandex.ru => [www.yandex.ru, *.yandex.ru, *.ru, *.]
    """
    domain, = result = [refine_domain(domain)]
    root_chunks = domain.split('.')
    while root_chunks:
        root_chunks.pop(0)
        result.append('.'.join(['*'] + root_chunks))
    return result


def refine_domain(domain):
    """ Возвращает "очишенную" версию домена

     - удаляет пробельные символы слева-справа
     - удаляет '.' в конце
     - приводит к нижнему регистру

    :raises ValueError: если передано пустое или мусор.
    """
    domain = smart_text(domain or '').strip().rstrip('.')
    if not domain:
        raise ValueError('Domain cannot be empty')
    return domain.lower()





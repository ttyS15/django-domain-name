django-celery-rpc
=================

[![Build Status](https://travis-ci.org/ttyS15/django-domain-name.svg)](https://travis-ci.org/ttyS15/django-domain-name)

Django model fields with several magical properties.
 
Features:
  - validations in accordance with standard;
  - IDNA domains (localized) are suitable;
  - domain_name.fields.MagicDomainName provide an ability to store domain name with asterisk (*.example.org);
  - utility `ranking_domain()` can split domain name in a parts;

As result: you can find domain records with sub-domains which are matched to particular domain name;

Example:

```python
from domain_name import MagicDomainName

class Domain(models.Model):
	name = MagicDomainName()

.....

from domain_name.utils import domain_ranking

# Will find records where value of name is: 
# - test.example.org;
# - \*.example.org;
# - \*.org
# - \*.
Domain.objects.filter(name__in=domain_ranking('test.example.org')
```
 


```


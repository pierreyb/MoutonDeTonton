from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

sanitel_validator = \
    RegexValidator("^\d{4,5}(\-\-)?\d{4}$",
                   _("Sanitel doit avoir 8 ou 9 chiffres"))
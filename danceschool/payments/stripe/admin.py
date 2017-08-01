from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .models import StripeCharge


class StripeChargeAdmin(admin.ModelAdmin):

    def get_admin_change_link(self,app_label, model_name, obj_id, name):
        url = reverse('admin:%s_%s_change' % (app_label, model_name),
                      args=(obj_id,))
        return format_html('<a href="%s">%s</a>' % (
            url, str(name)
        ))

    def invoiceLink(self,item):
        if item.invoice:
            i = item.invoice
            return self.get_admin_change_link('core','invoice',i.id,i.id)
    invoiceLink.allow_tags = True
    invoiceLink.short_description = _('Registration invoice')

    list_display = ['chargeId','status','invoiceLink']
    list_filter = ['status','creationDate','modifiedDate']
    search_fields = ['chargeId','invoice__id']

    ordering = ['-modifiedDate',]
    readonly_fields = ['chargeId','status','creationDate','modifiedDate','invoiceLink']

    fieldsets = (
        (_('Basic Information'), {
            'fields': ('chargeId','status','invoiceLink'),
        }),
        (_('Dates'), {
            'fields': ('creationDate','modifiedDate'),
        }),
    )


admin.site.register(StripeCharge, StripeChargeAdmin)
from django.contrib import admin
from django.contrib.auth.models import User , Group

admin.site.site_header="Texas College"
admin.site.site_title="Texas Admin"
admin.site.index_title="Texas Administration"


admin.site.unregister(User)
admin.site.unregister(Group)

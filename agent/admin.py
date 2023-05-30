from django.contrib import admin
from .models import PartnerType, Agent, AgentStatus, AgentPublications


admin.site.register(PartnerType)
admin.site.register(Agent)
admin.site.register(AgentStatus)
admin.site.register(AgentPublications)
"""DaddyLongLegs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import home
from . import GodParents
from . import GodChild
from . import decisiongp
from . import collect
from . import Reg
#from . import Money
from . import fdonation
#from . import voluntary
from . import allotvolun
from . import lgp
from .import lgpp
#from .Static import Images  
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',home.home),
    url(r'^GP$',GodParents.Gp),
    url(r'^GP/info$',decisiongp.form),
    url(r'^GP/info/collection$',collect.success),
    url(r'^GC$',GodChild.Gc),
    url(r'^GP/info/collection/finaldonationpage$',fdonation.totf),
    url(r'^GC/regs$',Reg.Rgs),
    url(r'^GP/info/voluntary$',decisiongp.form),
    url(r'^GP/info/voluntary/status$',allotvolun.allot),
    url(r'^GP/login$',lgp.login),
    url(r'^GP/login/user$',lgpp.lg),
]

from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(TranType)
class TranTypeAdmin(admin.ModelAdmin):
    pass


class StockTransactionInline(admin.StackedInline):
    model = StockTransaction


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [StockTransactionInline, ]


@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    pass


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    pass


@admin.register(FundTransaction)
class FundTransactionAdmin(admin.ModelAdmin):
    pass

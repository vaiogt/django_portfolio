from django.db import models


# Create your models here.
class Currency(models.Model):
    """貨幣"""
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_zh = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'currencies'

    def __str__(self):
        return f"({self.code}) {self.name_zh}"


class Portfolio(models.Model):
    """投資組合"""
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class TranType(models.Model):
    """交易類型"""
    type = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.type.title()


class Stock(models.Model):
    """股票"""
    symbol = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_zh = models.CharField(max_length=50, blank=True, null=True)
    abbr_zh = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey(Currency, models.DO_NOTHING)

    def __str__(self):
        return f"({self.symbol}) {self.abbr_zh}"


class StockPrice(models.Model):
    """股票價格"""
    stock = models.ForeignKey(Stock, models.CASCADE)
    date = models.DateField(blank=True, null=True)
    open = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    high = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    low = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    close = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    volume = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.stock.symbol} @ {self.close}"


class StockTransaction(models.Model):
    """股票交易紀錄"""
    portfolio = models.ForeignKey(Portfolio, models.CASCADE)
    stock = models.ForeignKey(Stock, models.CASCADE)
    date = models.DateField(blank=True, null=True)
    type = models.ForeignKey(TranType, models.DO_NOTHING)
    share = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type.type} - {self.stock.symbol} - {self.share}units@{self.price}"


class Fund(models.Model):
    """基金"""
    fr_code = models.CharField(max_length=20, blank=True, null=True)
    ms_code = models.CharField(max_length=20, blank=True, null=True)
    isin = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_zh = models.CharField(max_length=50, blank=True, null=True)
    abbr_zh = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey(Currency, models.DO_NOTHING)

    def __str__(self):
        return f"({self.fr_code}) {self.abbr_zh}"


class FundPrice(models.Model):
    """基金價格"""
    fund = models.ForeignKey(Fund, models.CASCADE)
    date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.date} {self.fund.abbr_zh} {self.price}"


class FundTransaction(models.Model):
    """基金交易紀錄"""
    portfolio = models.ForeignKey(Portfolio, models.CASCADE)
    fund = models.ForeignKey(Fund, models.CASCADE)
    date = models.DateField(blank=True, null=True)
    type = models.ForeignKey(TranType, models.DO_NOTHING)
    unit = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type.type}, {self.fund.abbr_zh}@{self.price}"

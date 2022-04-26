# 工厂模式

# 1.简单工厂模式
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def __init__(self, use_hua_bei=False):
        self.use_hua_bei = use_hua_bei

    def pay(self, money):
        if self.use_hua_bei:
            print("花呗支付{}元".format(money))
        else:
            print("支付宝支付{}元".format(money))


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付支付{}元".format(money))


class PaymentFactory(object):
    def __init__(self, method):
        self.method = method

    def create_payment(self):
        if self.method == "alipay":
            return Alipay()
        if self.method == "wechat":
            return WechatPay()
        if self.method == "hua_bei":
            return Alipay(use_hua_bei=True)
        raise TypeError("No such payment named {}".format(self.method))


pf = PaymentFactory("hua_bei")
p = pf.create_payment()
p.pay(10)

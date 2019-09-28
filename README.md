# payscore
微信支付分 SDK，包含签名校验、加解密、平台证书更新等。完成了小程序端先享后付（免确认） 的所有 API。

# 安装与升级
目前 [payscore](https://github.com/kangour/payscore) 支持的 Python 环境为 python3+，依赖于 [wechatpy](https://github.com/jxtech/wechatpy) 库。

安装 wechatpy

推荐使用 pip 进行 wechatpy 的安装

```
pip install wechatpy
# with cryptography （推荐）
pip install wechatpy[cryptography]
# with pycryptodome
pip install wechatpy[pycrypto]
```

升级 wechatpy 到新版本:

pip install -U wechatpy
如果需要安装 GitHub 上的最新代码:

pip install https://github.com/jxtech/wechatpy/archive/master.zip

安装 payscore

直接克隆 payscore 或子模块克隆到项目即可使用，之后会请求合并到 wechatpy。


# 先享后付接口
payscore.api.PayAfter(client=None)

    user_service_state() -> bool:
        """user_service_state
        查询用户是否可使用服务
        :param openid: 小程序用户的 openid
        :rtype: bool
        """

    create() -> bool:
        """create_payafter_orders
        创建先享后付订单
        https://pay.weixin.qq.com/wiki/doc/apiv3/payscore.php?chapter=17_1&index=3
        :param openid: 必须
        :param out_order_no: 必须 商户测的支付分订单 ID
        :param service_start_time: 非必须 服务开始时间
        :param service_end_time: 非必须 服务结束事件
        :param service_start_location: 服务开始地点
        :param service_end_location: 服务结束地点
        :param service_introduction: 服务介绍
        :param fees: 费用
        :param risk_amount: 风险金额
        :param need_user_confirm: 订单是否需要确认
        :param **kwargs:
        :rtype: bool
        """

    query():
        """query_payafter_orders
        查询先享后付订单
        :param out_order_no: 非必须 商户系统内部服务订单号
        :param query_id: 非必须 微信侧回跳到商户前端时用于查单的单据查询id, 商户单号与回跳查询id必填其中一个.不允许都填写或都不填写
        :rtype: bool
        """

    complete():
        """complete
        完结先享后付订单
        https://pay.weixin.qq.com/wiki/doc/apiv3/payscore.php?chapter=17_4&index=6
        :param out_order_no: 必须 商户系统内部服务订单号
        :param finish_ticket: 标识用户订单使用情况，1 未使用服务，取消订单；2 完成服务使用，结束订单
        :param total_amount: 大于等于0的数字，单位为分; 未使用服务，取消订单时，该字段必须填0.
        :param finish_type: 完结凭证，用于完结订单时传入（每次获取到的字段内容可能变化，但之前获取的字段始终有效，可一直使用）
        :param fees:
        :param real_service_end_location:
        :param cancel_reason:
        :param real_service_start_time:
        :param real_service_end_time:
        :param profit_sharing:
        """

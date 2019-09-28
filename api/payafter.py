from wechatpy.pay.base import BaseWeChatPayAPI


class PayAfter(BaseWeChatPayAPI):

    def user_service_state(self, openid) -> bool:
        """user_service_state
        查询用户是否可使用服务
        :param openid: 小程序用户的 openid
        :rtype: bool
        """
        data = dict(openid=openid)
        return self._get('v3/payscore/user-service-state', data=data)

    def create(self, openid, out_order_no, service_start_location, service_end_location, service_introduction, fees, risk_amount, service_start_time='OnAccept', service_end_time=None, need_user_confirm=False, **kwargs) -> bool:
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
        data = {
            "openid": openid,
            "out_order_no": out_order_no,
            "service_start_time": service_start_time,
            "service_start_location": service_start_location,
            "service_end_location": service_end_location,
            "service_introduction": service_introduction,
            "fees": fees,
            "risk_amount": risk_amount,
            "need_user_confirm": need_user_confirm
        }
        if service_end_time:
            data.update(service_end_time=service_end_time)
        data.update(kwargs)
        return self._post('v3/payscore/payafter-orders', data=data)

    def query(self, out_order_no=None, query_id=None):
        """query_payafter_orders
        查询先享后付订单
        :param out_order_no: 非必须 商户系统内部服务订单号
        :param query_id: 非必须 微信侧回跳到商户前端时用于查单的单据查询id, 商户单号与回跳查询id必填其中一个.不允许都填写或都不填写
        :rtype: bool
        """
        data = dict(out_order_no=out_order_no, query_id=query_id)
        return self._get('v3/payscore/payafter-orders', data=data)

    def complete(self, out_order_no, finish_ticket, total_amount=0, finish_type=2, fees=None, real_service_end_location=None, cancel_reason='用户取消订单', real_service_start_time=None, real_service_end_time=None, profit_sharing=False):
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
        data = dict(
            finish_ticket=finish_ticket,
            finish_type=finish_type,
            total_amount=total_amount,
            profit_sharing=profit_sharing,
        )
        if finish_type == 1:
            data.update(cancel_reason=cancel_reason)
            return self._post('v3/payscore/payafter-orders/{out_order_no}/complete'.format(out_order_no=out_order_no), data=data)

        if fees:
            data.update(fees=fees)
        if real_service_start_time:
            data.update(real_service_start_time=real_service_start_time)
        if real_service_end_time:
            data.update(real_service_end_time=real_service_end_time)
        if real_service_end_location:
            data.update(real_service_end_location=real_service_end_location)
        return self._post('v3/payscore/payafter-orders/{out_order_no}/complete'.format(out_order_no=out_order_no), data=data)

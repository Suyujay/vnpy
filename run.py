from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy.trader.object import SubscribeRequest
from vnpy.trader.constant import Exchange  # 新增這行

from vnpy_ib import IbGateway
# from vnpy_ctp import CtpGateway
# from vnpy_ctastrategy import CtaStrategyApp
# from vnpy_ctabacktester import CtaBacktesterApp


def main():
    """Start VeighNa Trader"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(IbGateway)
    # req = SubscribeRequest(
    #     symbol="NQ",   # IB格式: 股票代碼-類型-幣種
    #     exchange=Exchange.CME         # IB常用交易所
    # )
    # main_engine.subscribe(req, "IB")  # "IB"為gateway名稱

    # main_engine.add_gateway(CtpGateway)
    # main_engine.add_app(CtaStrategyApp)
    # main_engine.add_app(CtaBacktesterApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
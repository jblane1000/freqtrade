"""Bingx exchange subclass"""

import logging
from typing import Dict

from freqtrade.exchange import Exchange


logger = logging.getLogger(__name__)


class Bingx(Exchange):
    """
    Bingx exchange class. Contains adjustments needed for Freqtrade to work
    with this exchange.
    """

    _ft_has: Dict = {
        "ohlcv_candle_limit": 1000,
    }

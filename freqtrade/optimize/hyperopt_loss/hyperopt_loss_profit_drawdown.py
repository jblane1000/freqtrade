"""
ProfitDrawDownHyperOptLoss

This module defines the alternative HyperOptLoss class based on Profit &
Drawdown objective which can be used for Hyperoptimization.

Possible to change `DRAWDOWN_MULT` to penalize drawdown objective for
individual needs.
"""

from pandas import DataFrame

from freqtrade.data.metrics import calculate_max_drawdown
from freqtrade.optimize.hyperopt import IHyperOptLoss


# higher numbers penalize drawdowns more severely
DRAWDOWN_MULT = 0.075


class ProfitDrawDownHyperOptLoss(IHyperOptLoss):
    @staticmethod
    def hyperopt_loss_function(results: DataFrame, trade_count: int, *args, **kwargs) -> float:
        total_profit = results["profit_abs"].sum()

        try:
            drawdown = calculate_max_drawdown(results, value_col="profit_abs")
            relative_account_drawdown = drawdown.relative_account_drawdown
        except ValueError:
            relative_account_drawdown = 0

        return -1 * (total_profit * (1 - relative_account_drawdown * DRAWDOWN_MULT))

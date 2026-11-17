# Risk Assessment Methodology v1.0.0

## Defaults (proposals, not universal standards)
Daily simple returns; up to five years available observations; 252 trading days/year; one-period VaR at 95% (99% optional); historical quantile `linear` with explicit implementation; zero downside target per period; no imputation. Weekly/monthly frequency, alternative quantiles, confidence, and horizon require documented, validated overrides. Minimum sample sizes and tail-count thresholds are implementation policy to be fixed and independently tested before a metric is declared verified.

## Reference formulas
For asset return vector `r_t` and static weights `w`, periodic portfolio return `p_t = Σ_i w_i r_(i,t)` (constant-mix/rebalanced-each-period convention). A buy-and-hold portfolio instead requires evolving weights; do not mix conventions.

Sample volatility `s = sqrt(Σ(p_t - mean(p))²/(n-1))`; annualized `s * sqrt(K)` for K compatible periods/year. Portfolio covariance volatility `sqrt(wᵀ Σ w)` where Σ is expressed on the same horizon. Annualized mean and volatility must use consistent return conventions.

Wealth index `V_0=1`, `V_t=V_(t-1)*(1+p_t)`; drawdown `D_t=V_t/max(V_0,...,V_t)-1`; maximum drawdown `min(D_t)`.

Historical loss series `L_t=-p_t`. Historical VaR at c = c-quantile of `L` with named quantile convention. Historical expected shortfall = average losses in the defined upper tail; tie/partial-quantile treatment must be fixed, not improvised. VaR and ES can be negative when the entire loss distribution represents gains; if a nonnegative risk-report convention is used, record it explicitly.

Normal parametric loss VaR at one period = `-mean(p)+PhiInverse(c)*sd(p)`; if reporting a floored-to-zero version, disclose flooring and retain the unfloored estimate. Parametric ES requires its own specified distribution formula and validation; do not label historical ES as parametric.

Downside deviation per period = `sqrt(mean(min(0,p_t-target)^2))`, annualized only with a justified convention. HHI `Σ w_i²`. Component volatility contribution (nonzero σ): `w_i*(Σw)_i/σ`; contributions sum to σ when Σ and weights are consistent.

Deterministic asset shock portfolio impact `Σ w_i shock_i`; require full holdings coverage. For an asset-class shock, map every holding to one and only one supported class. Interest-rate shock with modified duration approximates bond return `-duration*Δyield` only when duration assumptions are validated; convexity/credit changes excluded unless modeled.

## Validation caveats
A historical window is not a forecast. Normal parametric VaR is sensitive to non-normal tails. VaR does not bound maximum losses; CVaR depends on tail sample sufficiency. Stress scenarios are conditional hypothetical calculations. Investor alignment is a comparison to documented preferences, not a regulated suitability determination. No scenario may assume unknown holdings have zero impact.

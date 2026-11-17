# Comprehensive acceptance test plan

The JSON contract tests in `test_contracts.py` are executable with Python 3.10+ and `jsonschema`. They are **not** quantitative engine tests. Do not claim any of the following passed until an implementation and independent oracle exist.

1. **Functional:** valid standalone and agent inputs, requested metrics, run trace, and artifact status.
2. **Numerical oracle:** independently verify volatility, covariance risk, HHI, max drawdown, historical/normal VaR, CVaR, downside deviation, component contributions. Include known 2-asset fixtures and compare within declared tolerances.
3. **Quality gates:** malformed JSON, invalid schema version, negative/NaN/Inf weights, weight sum, duplicate asset IDs, date misalignment, missing returns, unsupported FX, and unapproved profile.
4. **Partial:** missing bond duration disables only rate scenario; inadequate 99% tail data disables only 99% ES; unavailable profile sets `not_assessed`.
5. **Stress:** standardized and custom shocks, complete exposure mapping, dollar/percentage reconciliation, missing class mapping, rate shock sign.
6. **Classification:** documented benchmark boundaries; no benchmark => `unclassified`; investor conflict classifications never claim suitability.
7. **Reports:** same validated values, units, methods, and status across JSON/HTML/PDF/charts; renderer errors do not mutate numerical results.
8. **Reproducibility:** identical input/config gives identical numeric results and stable source lineage; zero-volatility and singular covariance guarded.
9. **Integration:** actual exported profile, market data, and optimization contracts accepted; actual 3D visualization contract adapter checked; orchestration run and standalone run agree.
10. **Security:** imported text cannot override instructions; logs redact personal information; no network or trading without separate authorization.

## Gates
- **G1 Publication ready:** documents, schemas, fixtures, and tests committed; mark any unimplemented tests pending.
- **G2 Standalone verified:** implementation + all mandatory quantitative/functional/report tests pass with evidence.
- **G3 Integration verified:** real upstream/downstream schema adapters and end-to-end workflow pass with evidence.

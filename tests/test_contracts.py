"""Contract and fixture smoke tests only; not a risk calculation engine."""
import json
import pathlib
import unittest
from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parents[1]

def read(rel):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))

class ContractTests(unittest.TestCase):
    def check(self, schema, fixture):
        s = read('schemas/' + schema)
        Draft202012Validator.check_schema(s)
        errors = list(Draft202012Validator(s, format_checker=FormatChecker()).iter_errors(read('examples/' + fixture)))
        self.assertEqual([], [e.message for e in errors])

    def test_input_contract(self): self.check('risk-input.schema.json','hypothetical-input.json')
    def test_output_contract(self): self.check('risk-output.schema.json','hypothetical-output.json')
    def test_visualization_contract(self): self.check('visualization-handoff.schema.json','hypothetical-visualization-handoff.json')
    def test_fixture_invariants(self):
        x=read('examples/hypothetical-input.json'); y=read('examples/hypothetical-output.json')
        weights=[h['weight'] for h in x['portfolio']['holdings']]
        self.assertAlmostEqual(sum(weights),1)
        self.assertAlmostEqual(sum(w*w for w in weights),y['metrics']['concentration_hhi']['value'])
        self.assertAlmostEqual(.6*(-.2)+.4*0,y['stress_results'][0]['impact_fraction'])
    def test_reject_wrong_schema_version(self):
        s=read('schemas/risk-input.schema.json'); x=read('examples/hypothetical-input.json'); x['schema_version']='9.9.9'
        self.assertFalse(Draft202012Validator(s).is_valid(x))
    def test_reject_negative_weight(self):
        s=read('schemas/risk-input.schema.json'); x=read('examples/hypothetical-input.json'); x['portfolio']['holdings'][0]['weight']=-.1
        self.assertFalse(Draft202012Validator(s).is_valid(x))

if __name__=='__main__': unittest.main()

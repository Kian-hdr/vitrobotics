import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

from software.coverage_planner import FacadeSpec, plan_facade, render_svg
from software.coverage_planner.planner import MAX_WAYPOINTS


class PlannerTests(unittest.TestCase):
    def test_nondivisor_spacing_covers_edges_and_respects_bound(self):
        p = plan_facade(FacadeSpec(10, 7, 2, 3, 0.5))
        self.assertEqual(p.row_count, 5)
        self.assertEqual(p.actual_spacing_m, 1.75)
        self.assertEqual(p.points[0].z, 0)
        self.assertEqual(p.points[-1].z, 7)
        for row in range(p.row_count):
            a, b = p.points[2*row:2*row+2]
            self.assertEqual({a.x, b.x}, {0, 10})
            self.assertEqual(a.z, b.z)
        for point in p.points:
            self.assertTrue(0 <= point.x <= 10 and 0 <= point.z <= 7)
            self.assertEqual(point.y, 3)
        for a, b in zip(p.points[1::2], p.points[2::2]):
            self.assertLessEqual(b.z-a.z, 2)

    def test_route_length_independent_segment_calculation(self):
        p = plan_facade(FacadeSpec(10, 7, 2, 3, 0.5))
        measured = 0
        for i, (a, b) in enumerate(zip(p.points, p.points[1:])):
            length = math.dist((a.x,a.y,a.z), (b.x,b.y,b.z))
            self.assertGreater(length, 0)
            self.assertEqual(a.y, b.y)
            self.assertTrue((a.x == b.x) != (a.z == b.z))
            measured += length
            if i % 2:
                self.assertEqual(a.x, b.x)
                self.assertGreater(b.z, a.z)
        self.assertEqual(measured, 57)
        self.assertEqual(p.route_length_m, measured)
        self.assertEqual(p.ideal_travel_time_s, 114)

    def test_wider_spacing_still_includes_both_edges(self):
        p = plan_facade(FacadeSpec(4, 2, 100, 1, 1))
        self.assertEqual(p.row_count, 2)
        self.assertEqual([(q.x,q.z) for q in p.points], [(0,0),(4,0),(4,2),(0,2)])
        self.assertEqual(p.route_length_m, 10)

    def test_deterministic_and_exact_divisor(self):
        spec = FacadeSpec(2, 6, 2, 1, 1)
        self.assertEqual(plan_facade(spec), plan_facade(spec))
        self.assertEqual(plan_facade(spec).row_count, 4)

    def test_all_fields_reject_invalid_values(self):
        for field in range(5):
            for invalid in [0,-1,float('nan'),float('inf'),-float('inf'),True,'2',None]:
                values = [10,7,2,3,0.5]
                values[field] = invalid
                with self.subTest(field=field, value=invalid), self.assertRaises(ValueError):
                    plan_facade(FacadeSpec(*values))

    def test_waypoint_allocation_limit(self):
        self.assertEqual(len(plan_facade(FacadeSpec(1,4999,1,1,1)).points), MAX_WAYPOINTS)
        for height, spacing in [(5000,1),(1e308,1e-308)]:
            with self.assertRaises(ValueError):
                plan_facade(FacadeSpec(1,height,spacing,1,1))

    def test_overflow_and_underflow_results_rejected(self):
        for spec in [FacadeSpec(1e308,1,1,1,1), FacadeSpec(1,1,1,1,1e-308), FacadeSpec(5e-324,5e-324,1,1,1e308)]:
            with self.assertRaises(ValueError):
                plan_facade(spec)

    def test_json_and_svg_are_valid_and_explicitly_offline(self):
        p = plan_facade(FacadeSpec(10,7,2,3,0.5))
        data = json.loads(json.dumps(p.to_dict(), allow_nan=False))
        self.assertEqual(len(data['waypoints']),10)
        self.assertIn('not historical',data['provenance'])
        root = ET.fromstring(render_svg(p))
        self.assertEqual(root.tag,'{http://www.w3.org/2000/svg}svg')
        poly = root.find('.//{http://www.w3.org/2000/svg}polyline')
        self.assertEqual(len(poly.attrib['points'].split()),10)
        # Extreme but finite inputs must not cause SVG division errors.
        ET.fromstring(render_svg(plan_facade(FacadeSpec(1e-200,1e100,1e100,1,1))))

    def test_cli_emits_artifacts_and_fails_cleanly(self):
        repo = Path(__file__).resolve().parents[3]
        base = [sys.executable,'-m','software.coverage_planner','--width','10','--height','7','--spacing','2','--standoff','3','--speed','0.5']
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            result = subprocess.run(base+['--json',str(target/'plan.json'),'--svg',str(target/'plan.svg')],cwd=repo,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(json.loads((target/'plan.json').read_text())['route_length_m'],57)
            ET.parse(target/'plan.svg')
            failure = subprocess.run(base+['--spacing','0'],cwd=repo,capture_output=True,text=True)
            self.assertNotEqual(failure.returncode,0)
            self.assertNotIn('Traceback',failure.stderr)


if __name__ == '__main__':
    unittest.main()

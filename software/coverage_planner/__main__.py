"""Run from the repository root: python3 -m software.coverage_planner."""
import argparse
import json
from pathlib import Path
from .planner import FacadeSpec, plan_facade, render_svg


def main():
    parser = argparse.ArgumentParser(description="Offline facade geometry. No aircraft control or executable mission output.")
    for name in ("width", "height", "spacing", "standoff", "speed"):
        parser.add_argument(f"--{name}", required=True, type=float, help="metres" if name != "speed" else "metres per second")
    parser.add_argument("--json", type=Path, help="Write conceptual geometry JSON; otherwise print it")
    parser.add_argument("--svg", type=Path, help="Write a front-view SVG schematic")
    args = parser.parse_args()
    try:
        if args.json and args.svg and args.json.resolve() == args.svg.resolve():
            raise ValueError("JSON and SVG outputs must be different files")
        plan = plan_facade(FacadeSpec(args.width, args.height, args.spacing, args.standoff, args.speed))
        payload = json.dumps(plan.to_dict(), indent=2, allow_nan=False) + "\n"
        if args.json:
            args.json.write_text(payload, encoding="utf-8")
        else:
            print(payload, end="")
        if args.svg:
            args.svg.write_text(render_svg(plan) + "\n", encoding="utf-8")
    except (ValueError, OSError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()

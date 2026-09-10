# Autopilot and software

Kian recalls using autopilot through a flight planner. This is a direct project recollection recorded on 11 September 2026; the exact application, controller, version, flight mode and session remain unidentified.

Historical papers mention DJI FlightHub 2, ArduPilot, PX4/MAVSDK, mapping and swarm control. They mix the initial platform with future architecture and cannot establish one installed software stack.

## Evidence needed to describe an automated flight

Identify the actual planner and controller, the mission/configuration file if available, the automated segment, and what the operator still controlled. Map that evidence to a dated session. Automated flight and automated cleaning are distinct claims.

## Code scope

Kian reports substantial code exists but little can be made public. This repository therefore prioritizes engineering documentation and selected CAD. It contains no released flight-control code or claim of a reproducible autonomy system.

An archived firmware-update result reports failure. The associated third-party binaries are not redistributed, and their presence does not establish the firmware version used in flight.

## Recovered planning artifact

A screenshot named `Screenshot 2024-12-10 042015.png` shows a Hamburg building with dense façade and roof coverage paths. It preserves a historical planning visualization, but the application chrome is cropped and no mission execution or aircraft binding is visible. Other archived animations show tutorial-style virtual planning scenes; they are not project flight recordings. None resolves the exact flown planner.

## New development: offline coverage geometry

The repository now includes a [tested offline coverage planner](../software/coverage_planner/README.md), written in September 2026. It creates deterministic alternating sweep geometry for a rectangular façade and exports JSON plus an SVG preview. It has no aircraft connection and does not replace the missing historical autopilot record.

The module makes one planning step inspectable and reproducible: edge inclusion, spacing, route length and ideal travel time. Aircraft dynamics, obstacles, tether forces and cleaning effectiveness are outside its model.

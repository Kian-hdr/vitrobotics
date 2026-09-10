# System architecture

## Initial cleaning prototype

The first system combined a modified DJI Inspire 1 Pro with ground-based water equipment. An onboard battery powered the aircraft; a pressure hose supplied the aircraft-mounted nozzle.

```mermaid
flowchart LR
    Operator[Operator] --> Aircraft[Modified DJI Inspire 1 Pro]
    Water[Ground water supply] --> Washer[Pressure washer]
    Washer --> Hose[Pressure hose]
    Hose --> Nozzle[Aircraft-mounted nozzle]
    Battery[Onboard battery] --> Aircraft
    Mounts[Custom mounts and guards] --- Aircraft
    Nozzle --> Surface[Building surface]
```

The mechanical integration had three closely related concerns: positioning the nozzle, managing the hose at the aircraft, and maintaining clearance around the rotors. The [component case studies](hardware/design-process.md) describe how those parts developed.

## Development branches

### Modified Inspire

The initial test platform used custom cleaning attachments and rotor guards. The December 2024 sessions documented nozzle-placement changes, hose behavior and guard attachment alongside physical flight tests.

### Successor hexacopter

The later Fusion branch contains a six-rotor assembly with branching guards, landing gear and dedicated nozzle-mount designs. The [successor page](hardware/successor-hexacopter.md) documents the CAD configuration separately from the initial aircraft's flight record.

### Commercial equipment concepts

Later parts lists explored an M400-based setup with a tether supply and commercial cleaning equipment. These lists describe a proposed configuration; they are not included in the initial aircraft's as-built specification.

## Automation and endurance

The project explored route planning, electrical ground power and multi-drone coordination as development directions. The documented physical demonstration here is the water-supplied cleaning setup. Electrical tether operation, an end-to-end automated cleaning sequence and coordinated multi-drone operation are outside the demonstrated scope of this repository.

The [software page](software.md) separates historical planning material from the offline coverage planner added in September 2026.

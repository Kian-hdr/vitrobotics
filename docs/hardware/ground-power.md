# Power over ground

We developed a ground-powered supply path to explore operation beyond the aircraft's onboard battery capacity. The work covered power conversion, transmission through a cable and delivery of usable DC power to the drone.

## Conversion chain

```mermaid
flowchart LR
    AC[AC supply] --> Ground[Ground power conversion]
    Ground --> Tether[Higher-voltage DC over the cable]
    Tether --> Onboard[Onboard DC conversion]
    Onboard --> Drone[Lower-voltage DC aircraft supply]
```

The ground-side power block converts AC to DC. The transmission stage raises the DC voltage so the required power can travel through the cable at a lower current. At the aircraft, the converter reduces the voltage again to provide the lower-voltage, higher-current supply required by the drone.

For a given transmitted power, increasing voltage reduces the current needed. Lower current reduces resistive losses in the cable. The converters introduce their own losses, so this architecture does not imply lossless conversion or a measured system efficiency.

The diagram describes the functional stages. It is not a wiring schematic or a specification for a flight-ready power supply.

## Ground and hover tests

We carried out multiple ground tests and limited hovering with the ground-power system. The available cable was too short to evaluate it under full-flight conditions, so testing stopped short of that stage.

| Test stage | Status |
|---|---|
| Ground testing | Carried out |
| Limited hovering | Carried out |
| Full-flight tether evaluation | Not completed; available cable length was insufficient |
| Sustained flight endurance and system efficiency | No measured result presented here |

These tests are a separate part of the project from the battery-powered cleaning flights shown in the early flight record. They are not assigned to a specific dated flight session or to the later supplier equipment concepts.

## Continuing the engineering record

A complete electrical specification needs the actual converter ratings, cable properties, protection and isolation arrangements, and measured operating data. Those details are not reconstructed from supplier brochures or from the conceptual conversion chain above.

The next validation stage would require a suitable cable and a separately defined test plan for the complete aircraft-and-tether system. The ground and hover work does not establish a full-flight operating envelope.

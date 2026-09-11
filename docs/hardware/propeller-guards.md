# Propeller guards

Flying a cleaning aircraft beside a building put rotor clearance and attachment stability at the centre of the mechanical design. We developed custom guards with separate clockwise and counter-clockwise versions, using topology optimization and generative design to explore their form.

The guard was an assembly: an outer ring, branching ribs, mounting brackets and plates. Designing those interfaces was as important as designing the ring itself.

## Geometry and revisions

![Clockwise and counter-clockwise guard designs with segmented branching geometry](../../media/guard-design-variants.png)

*CAD view of the paired guard designs, with three coloured segments.*

The v1, v2 and v2.1 families preserve several iterations of the guards. The later versions use three-part exports: `Prop_Guard (1).3mf`, `Prop_Guard (2).3mf` and `Prop_Guard (3).3mf`, with CW and CCW variants. Top and bottom brackets and mounting-plate revisions sit alongside them.

The CAD render `Prop_Guard_gd5.2 v11.png` shows the mirrored guard arrangement, divided into three coloured segments with organic branching ribs. It illustrates how the guard geometry was broken into components for assembly.

## The original generative study

![Prop_Guard_gd10.2.1 opened in Fusion](../../media/guard-gd10-2-1.png)

*The saved `Prop_Guard_gd10.2.1` model, including the branded outer sections and branching supports.*

The native model retains a direct link to **Study 10 – Structural Component** in its original generative project. This connects the resulting geometry to the design setup behind it.

The study preserves the outer `Guard` body and the `Bottom_Bracket`. Ten obstacle bodies reserve space for the `Top_Bracket`, the `Tube` and eight bodies under `Geofence`. Here, Geofence is a CAD component name for excluded geometry, not a flight-control boundary. The generated connections must bridge the preserved guard and bracket around those occupied volumes. No starting shape is assigned.

| Structural setting | Original setup |
|---|---|
| `Fixed1` and `Fixed2` | Fixed global translations on two selected bottom-bracket surfaces |
| `Force1` | 100 N normal-force setting on a guard surface |
| `Force2` | 250 N total on another guard surface; global unit direction approximately (−0.512324, +0.858792, 0) |
| Gravity | 9.80665 m/s² in global −Z |
| Material | Nylon 12 (with Formlabs Fuse 1 3D Printer) |
| Objective | Minimize mass with a target safety factor of 2.0 |

The support and load annotation groups are enabled in the saved case. The normal-force setting is stored internally as a pressure-type load while its original force-tool annotation retains the entered magnitude. This represents structural loading of the selected guard surface; it is not a pressure-washer operating value. The distinction matters when reading exported solver data. Autodesk explains surface loading in its [structural-load documentation](https://help.autodesk.com/cloudhelp/ENU/Fusion-GenerativeDesign/files/GD-STR-LOADS.htm).

These are design inputs. They do not establish an impact rating, a collision-test result or an achieved safety factor. The archived manufacturing-condition records also do not establish the selected process for this result. The physical guard's material and assembly must be considered separately from the Nylon 12 study model.

## Printing and assembly

The assembly plan called for GreenTec Pro Carbon Fiber print material, joining the outer ring before the mounting bracket, and M3 heated inserts. One completed geometry change moved the ring **5 mm down**.

Further design options included larger top-bracket mounting holes, reshaped connection points using T-Splines, stronger glue, fewer wall lines and reduced infill. These remained proposals in the design notes. They are not the manufacturing settings for a released guard.

## Refinement at the attachment

Field testing prompted changes to screw tightness and threadlocked retention at the mount. The mounting interface and rotor clearance remained part of the development work.

That experience shaped the way we approached the assembly: the ring geometry, bracket fit and retention all needed attention together. A change to one part could affect how the guard sat around the rotor.

The revision history still needs the installed photographs and build records alongside each design. The guards have no published impact rating or measured structural margin; this page describes their development rather than a production specification.

The later six-rotor design carries the guard work into a different layout. See the [successor hexacopter](successor-hexacopter.md).

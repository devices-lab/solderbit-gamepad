# solder:bit Gamepad for the BBC micro:bit

![A photo of the solder:bit Gamepad PCB](/media/IMG_7025.jpeg "My first attempt at soldering the solder:bit Gamepad.")

The solder:bit Gamepad originated as a workshop idea for the upcoming [Device prototyping and production summer school](https://prosquared.org/event/2024-summer-school/) held at Lancaster University. Designed primarily to introduce participants to the fundamentals of surface mount soldering, this project not only demystifies a key skill in electronics but also integrates the fun and educational platform of the BBC micro:bit.

As we developed the first prototype, it became clear that the gamepad could spearhead a series of kits under the solder:bit brand, each varying in complexity and purpose. Currently, our focus is on perfecting the solder:bit Gamepad. However, looking ahead, we are excited about the possibility of expanding our line to include additional kits that cater to a range of skills and educational outcomes.

Join us as we explore the intersection of learning, gaming, and creativity with the solder:bit Gamepad.

## Project status

The solder:bit Gamepad is currently in the development stage, undergoing rigorous testing with its second prototype. At this point, the gamepad is not yet ready for deployment in workshops or teaching environments. We are actively refining the design to ensure it meets our educational objectives and user expectations.

See [CHANGELOG](/CHANGELOG.md) for the latest pre-release versions and changes.

## Getting started

There are two ways to get started with the solder:bit Gamepad, depending on whether you already have the necessary parts or if you prefer to generate and order the components yourself.

### Starting with the kit

If you already have the PCB and all the required components listed in the [bill of materials (BOM)](#bill-of-materials-bom), follow these steps to get your gamepad up and running:

1. **Soldering and assembly**: a guide will be released soon.
2. **Programming**: an extension for MakeCode is planned.

### Generating and ordering PCB

If you prefer to generate the PCB yourself and order it from a manufacturer, follow these steps:

1. **Gerber files and ordering**: See [this](#gerber-files-and-ordering) section below.
2. **Ordering**: Submit these Gerber files to a PCB manufacturer of your choice (JLCPCB).

Once you receive the PCB and components, proceed as described in the first method:

3. **Soldering and assembly**: a guide will be released soon.
4. **Programming**: an extension for MakeCode is planned.

This guide should help you through the process of building and programming your solder:bit Gamepad, whether you start from scratch or use a pre-prepared kit.

## Bill of materials (BOM)

Below is the BOM needed to assemble the solder:bit Gamepad. Each component is listed with its corresponding ID, designator, quantity, description, and LCSC Part number (if applicable).

| ID  | Designator                     | Quantity | Designation           | LCSC Part # |
| --- | ------------------------------ | -------- | --------------------- | ----------- |
| 1   | D1, D5, D2, D3, D4             | 5        | WS2812B               | C2761795    |
| 2   | S5, S6, S1, S2, S4, S3         | 6        | TS04-66-95-BK-100-SMT | C2835240    |
| 3   | S8, S7                         | 2        | SW_Push               | C499324     |
| 4   | R2, R7, R5, R6, R4, R1, R3, R8 | 8        | 100k                  | C2907421    |
| 5   | C6, C5, C3, C7, C4, C1         | 6        | 0.1uF (100nF)         | C24497      |
| 6   | R9                             | 1        | 300Ω                  | C25372      |
| 7   | C2                             | 1        | 1uF                   | C90539      |
| 8   | U1                             | 1        | 74HC165D_653          | C5613       |

Ensure all components are correctly placed according to the designators and quantities specified for proper assembly.

## Generating Gerber files and ordering PCBs

For those who wish to generate their own Gerber files or order PCBs, we provide detailed guidelines to ensure compatibility with our recommended PCB fabrication house, JLCPCB.

### Using KiCad (version 7 or newer)

To generate Gerber files for the solder:bit Gamepad using KiCad, follow the specific steps outlined by JLCPCB to ensure the files meet their manufacturing requirements. You can find a detailed guide on how to export Gerber and drill files from KiCad on the [JLCPCB help page](https://jlcpcb.com/help/article/362-how-to-generate-gerber-and-drill-files-in-kicad-7).

### Using pre-made Gerber files

If you prefer not to generate your own files, we have provided ready-to-use Gerber files in the `fabrication` folder of this repository. These files adhere to the JLCPCB specifications and are the exact versions we used for our latest manufacturing run. Simply download these files and upload them to the JLCPCB website when placing your order.

## Credits

Special thanks to everyone at the Lancaster University Devices Lab, including [Steve Hodges](https://github.com/sehodges), [Joe Finney](https://github.com/finneyj),
Kobi Hartley, Lorraine Underwood, and [Matt Oppenheim](https://github.com/mattoppenheim).

## License

This project is licensed under the GNU General Public License (GPL), version 3. This license allows you to use, modify, and redistribute the solder:bit Gamepad and any derivative works, but all such derivatives must also be licensed under the GPL.

The GPL ensures that all modifications and improvements to the solder:bit Gamepad remain free and open for the public benefit. By using this project, you agree to abide by its terms and conditions.

For more details on the license, please see the [LICENSE](/LICENSE.txt) file included in this repository.

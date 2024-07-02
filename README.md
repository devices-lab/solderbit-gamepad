# solder:bit Gamepad for the BBC micro:bit

![Render of the solder:bit Gamepad PCB](/media/cover-image.png "A render of the latest version of the board")

The solder:bit Gamepad originated as a workshop idea for the upcoming [Device prototyping and production summer school](https://prosquared.org/event/2024-summer-school/) held at Lancaster University. Designed primarily to introduce participants to the fundamentals of surface mount soldering, this project not only demystifies a key skill in electronics but also integrates the fun and educational platform of the BBC micro:bit.

As we developed the first prototype, it became clear that the gamepad could spearhead a series of kits under the solder:bit brand, each varying in complexity and purpose. Currently, our focus is on perfecting the solder:bit Gamepad. However, looking ahead, we are excited about the possibility of expanding our line to include additional kits that cater to a range of skills and educational outcomes.

Join us as we explore the intersection of learning, gaming, and creativity with the solder:bit Gamepad.

## Project status

The solder:bit Gamepad is currently in the development stage, undergoing rigorous testing with its second prototype. We are actively refining the design to ensure it meets our educational objectives and user expectations.

See [CHANGELOG.md](/CHANGELOG.md) for the latest pre-release versions and changes.

## Getting started

There are two ways to get started with the solder:bit Gamepad, depending on whether you already have the necessary parts or if you prefer to generate and order the components yourself.

### Starting with the kit

If you already have the PCB and all the required components listed in the [bill of materials (BOM)](#bill-of-materials-bom), follow these steps to get your gamepad up and running:

1. **Soldering and assembly**: a guide will be released soon.
2. **Programming**: an extension for MakeCode is planned.

### Generating and ordering PCB

If you prefer to generate the fabrication files yourself and order it from a manufacturer, follow these steps:

1. **Gerber files and ordering**: See [this](#generating-gerber-files-and-ordering-pcbs) section below.
2. **Ordering**: Submit fabrication files to a PCB manufacturer of your choice.

Once you receive the PCB and components, proceed with assembly and programming.

## Bill of materials (BOM)

Below is the BOM needed to assemble the solder:bit Gamepad v0.5/v0.6. Each component is listed with its corresponding designator, manufacturer part number, description of the component, and and quantity total quantity of the compoenent.

| Designator                     | Manufacturer part number | Description                  | Quantity |
| ------------------------------ | ------------------------ | ---------------------------- | -------- |
| BT1                            | BH-AAA-B5AA001           | Battery holder               | 1        |
| C1, C2, C3, C4, C5, C6         | CL31B105KBHNNNE          | 1 uF capacitors              | 6        |
| D1, D2, D3, D4, D5             | WS2812B-B/T              | NeoPixels                    | 5        |
| D6                             | BAT60B                   | Schottky diode               | 1        |
| R1, R2, R3, R4, R5, R6, R7, R8 | FRC1206J104 TS           | 100k Ohm resistors           | 8        |
| R9                             | 1206W4J0301T5E           | 300 Ohm resistor             | 1        |
| S1, S2, S3, S4, S5, S6         | TS-1002S-AR06026         | Tactile switches             | 6        |
| SW7, SW8                       | TS-1037-A4B3-D2          | Right-angle tactile switches | 2        |
| SW1                            | MST22D18G2 125           | Sliding switch               | 1        |
| U1                             | 74HC165D,653             | PISO shift register          | 1        |

Ensure all components are correctly placed according to the designators and quantities specified for proper assembly.

## Generating Gerber files and ordering PCBs

Gerber files are the standard file format used in the electronics industry to communicate design information to PCB manufacturers. They contain all the necessary details for producing printed circuit boards (PCBs), including copper layering, solder mask, silkscreen, and drill data. Essentially, Gerber files serve as the blueprint for your PCB, ensuring that the manufacturer can accurately reproduce your design. Each file represents a single layer of the PCB, such as the top copper layer, bottom copper layer, or solder mask layer. Using this standard allows designers to convey precise and clear instructions to virtually any PCB manufacturer worldwide.

### Using KiCad (version 7 or newer)

Generating Gerber files is a crucial step in the PCB manufacturing process. If you are using KiCad version 7 or newer, follow these general steps to generate your Gerber and drill files:

1. **Select the project version.** Clone this repo and select the version of the device you would like to generate Gerber files for (we recommend the latest version).
2. **Check the design rules.** Confirm that your PCB design complies with the design rules of your chosen PCB manufacturer.
3. **Generate Gerber and drill files.** Select 'Gerbers (.grb)...' option in the 'File' menu under 'Fabrication Outputs'. Select the layers you need and make sure the formats match the requirements of your PCB manufacturer. Ensure to plot the drill files, as well as the drill map file if required by your fabrication house.
4. **Verify the files.** Use a Gerber viewer tool (such as [Tracespace](https://tracespace.io)) to check the files before sending them to the manufacturer to avoid any potential issues.

A detailed guide on how to export these files from KiCad can usually be found in the documentation or help section of your PCB design software or on online electronics forums and resources.

### Using pre-made Gerber files

If you prefer not to generate your own files, we have provided ready-to-use Gerber files in the `fabrication` folder of this repository. These files are designed to meet general specifications required by most PCB manufacturers. To use them:

1. **Download the Gerber files** from the `fabrication` folder. Inside, you'll find separate subfolders labeled for different manufacturers, such as Eurocircuits and JLCPCB. These files are identical to the ones we sent to the respective fabrication houses.
2. **Upload the files to the PCB manufacturer's website** when placing your order. Be sure to review any specific requirements or settings that your chosen manufacturer may require to ensure proper fabrication of your PCB.

This flexibility allows you to either use a direct approach with pre-made files or customize the process by generating your own files, fitting your level of expertise and specific needs.

## Credits

Special thanks to everyone at the Lancaster University Devices Lab, including [Steve Hodges](https://github.com/sehodges), [Joe Finney](https://github.com/finneyj),
Kobi Hartley, Lorraine Underwood, and [Matt Oppenheim](https://github.com/mattoppenheim).

## License

This project is licensed under the GNU General Public License (GPL), version 3. This license allows you to use, modify, and redistribute the solder:bit Gamepad and any derivative works, but all such derivatives must also be licensed under the GPL.

The GPL ensures that all modifications and improvements to the solder:bit Gamepad remain free and open for the public benefit. By using this project, you agree to abide by its terms and conditions.

For more details on the license, please see the [LICENSE](/LICENSE.txt) file included in this repository.

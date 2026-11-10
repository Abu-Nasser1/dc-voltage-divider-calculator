
# DC Voltage Divider Calculator

## 1. Project Overview

**Engineering Discipline:** Electrical Engineering.

This Python program analyzes a DC resistive voltage divider circuit. It calculates output voltage, equivalent resistance, electrical currents, and power dissipation. It supports both unloaded and loaded voltage divider circuits.

## 2. Engineering Problem

A voltage divider is used to obtain a lower voltage from a DC power supply.

**Inputs:**
- Vs: Source voltage (V).
- R1: Upper resistor (Ohms).
- R2: Lower resistor (Ohms).
- RL: Load resistance (Ohms). Enter 0 for no load.

**Outputs:**
- Equivalent lower resistance.
- Total circuit resistance.
- Output voltage (Vout).
- Source current and branch currents.
- Power dissipated by each resistor (mW).

## 3. Equations and Method

For an unloaded voltage divider:

Vout = Vs * R2 / (R1 + R2)

For a loaded voltage divider:

Req = (R2 * RL) / (R2 + RL)

Vout = Vs * Req / (R1 + Req)

Source current:

Is = Vs / (R1 + Req)

Branch currents:

IR2 = Vout / R2

IL = Vout / RL

Power dissipation:

P = I² * R

The program applies Ohm's law and the voltage-divider equations to calculate all results.

## 4. How to Run

1. Install Python 3.
2. Download this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python voltage_divider.py
```

5. Enter the source voltage, R1, R2, and RL.
6. Enter 0 for RL if no load is connected.

No external Python libraries are required.

## 5. Verification Examples

### Example 1: Unloaded Divider

**Inputs:**
- Vs = 12 V
- R1 = 1000 Ohms
- R2 = 2000 Ohms
- RL = 0 Ohms

**Expected Results:**

Vout = 12 * 2000 / 3000 = 8 V

Is = 12 / 3000 = 0.004 A = 4 mA

**Program Output:**

```text
Equivalent lower resistance: 2000.000 ohms
Total circuit resistance:    3000.000 ohms
Output voltage (Vout):       8.000 V
Source current:              4.000 mA
Current through R1:          4.000 mA
Current through R2:          4.000 mA
Load current:                0.000 mA (no load connected)
Power dissipated by R1:      16.000 mW
Power dissipated by R2:      32.000 mW
```

### Example 2: Loaded Divider

**Inputs:**
- Vs = 12 V
- R1 = 1000 Ohms
- R2 = 2000 Ohms
- RL = 2000 Ohms

**Expected Results:**

Req = (2000 * 2000) / 4000 = 1000 Ohms

Vout = 12 * 1000 / 2000 = 6 V

Is = 12 / 2000 = 6 mA

**Program Output:**

```text
Equivalent lower resistance: 1000.000 ohms
Total circuit resistance:    2000.000 ohms
Output voltage (Vout):       6.000 V
Source current:              6.000 mA
Current through R1:          6.000 mA
Current through R2:          3.000 mA
Load current:                3.000 mA
Power dissipated by R1:      36.000 mW
Power dissipated by R2:      18.000 mW
Power dissipated by load:    18.000 mW
```

## 6. Input Validation

- Non-numeric inputs are rejected.
- Negative voltage and resistance values are rejected.
- Zero is not accepted for source voltage, R1, or R2.
- Zero is accepted for RL to represent an unloaded circuit.
- Values outside the supported limits are rejected.

## 7. Assumptions and Limitations

- The voltage source is ideal and constant.
- All resistors are ideal and purely resistive.
- The load is connected in parallel with R2.
- The program analyzes DC circuits only.
- It does not model resistor tolerances, temperature effects, wire resistance, or AC behavior.
- Power calculations do not automatically select resistor ratings. Practical designs require an appropriate safety margin.

## 8. Project Files

- voltage_divider.py: Python source code.
- README.md: Project description, equations, verification examples, and limitations.

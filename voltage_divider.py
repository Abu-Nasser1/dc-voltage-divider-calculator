"""
DC Voltage Divider Calculator
A small electrical-engineering tool for analyzing an unloaded or loaded
resistive voltage divider supplied by a DC source.
"""

MAX_VOLTAGE = 1000.0       # volts
MAX_RESISTANCE = 1e9       # ohms


def read_positive_number(prompt, allow_zero=False):
    """Read and validate a numeric input within the supported range."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
        except ValueError:
            print("Invalid input: enter a numeric value.")
            continue

        if value < 0 or (value == 0 and not allow_zero):
            print("Invalid input: value must be greater than zero.")
            continue

        return value


def validate_circuit_inputs(source_voltage, r1, r2, load_resistance):
    """Check that all circuit values are physically valid and in range."""
    if not 0 < source_voltage <= MAX_VOLTAGE:
        raise ValueError(f"Source voltage must be between 0 and {MAX_VOLTAGE} V.")
    if not 0 < r1 <= MAX_RESISTANCE:
        raise ValueError(f"R1 must be between 0 and {MAX_RESISTANCE} ohms.")
    if not 0 < r2 <= MAX_RESISTANCE:
        raise ValueError(f"R2 must be between 0 and {MAX_RESISTANCE} ohms.")
    if load_resistance is not None and not 0 < load_resistance <= MAX_RESISTANCE:
        raise ValueError(
            f"Load resistance must be between 0 and {MAX_RESISTANCE} ohms."
        )


def calculate_voltage_divider(source_voltage, r1, r2, load_resistance=None):
    """
    Calculate voltage-divider output, currents, and resistor powers.

    Set load_resistance to None for an unloaded divider.
    """
    validate_circuit_inputs(source_voltage, r1, r2, load_resistance)

    if load_resistance is None:
        equivalent_lower_resistance = r2
    else:
        # The load is connected in parallel with the lower divider resistor.
        equivalent_lower_resistance = (r2 * load_resistance) / (r2 + load_resistance)

    total_resistance = r1 + equivalent_lower_resistance
    source_current = source_voltage / total_resistance
    output_voltage = source_current * equivalent_lower_resistance
    r1_current = source_current
    r1_power = (r1_current ** 2) * r1

    if load_resistance is None:
        r2_current = source_current
        load_current = 0.0
        r2_voltage = output_voltage
        r2_power = (r2_current ** 2) * r2
        load_power = 0.0
    else:
        r2_voltage = output_voltage
        r2_current = r2_voltage / r2
        load_current = r2_voltage / load_resistance
        r2_power = (r2_current ** 2) * r2
        load_power = (load_current ** 2) * load_resistance

    return {
        "equivalent_lower_resistance": equivalent_lower_resistance,
        "total_resistance": total_resistance,
        "output_voltage": output_voltage,
        "source_current": source_current,
        "r1_current": r1_current,
        "r2_current": r2_current,
        "load_current": load_current,
        "r1_power": r1_power,
        "r2_power": r2_power,
        "load_power": load_power,
    }


def display_results(results, load_resistance):
    """Print calculated circuit quantities with engineering units."""
    print("\n--- Voltage Divider Results ---")
    print(f"Equivalent lower resistance: {results['equivalent_lower_resistance']:.3f} ohms")
    print(f"Total circuit resistance:    {results['total_resistance']:.3f} ohms")
    print(f"Output voltage (Vout):       {results['output_voltage']:.3f} V")
    print(f"Source current:              {results['source_current'] * 1000:.3f} mA")
    print(f"Current through R1:          {results['r1_current'] * 1000:.3f} mA")
    print(f"Current through R2:          {results['r2_current'] * 1000:.3f} mA")

    if load_resistance is not None:
        print(f"Load current:                {results['load_current'] * 1000:.3f} mA")
    else:
        print("Load current:                0.000 mA (no load connected)")

    print(f"Power dissipated by R1:      {results['r1_power'] * 1000:.3f} mW")
    print(f"Power dissipated by R2:      {results['r2_power'] * 1000:.3f} mW")
    if load_resistance is not None:
        print(f"Power dissipated by load:    {results['load_power'] * 1000:.3f} mW")


def main():
    """Run the interactive voltage-divider calculator."""
    print("DC Voltage Divider Calculator")
    print("Enter 0 for load resistance if no load is connected.\n")

    source_voltage = read_positive_number("Source voltage Vs (V): ")
    r1 = read_positive_number("Resistor R1 (ohms): ")
    r2 = read_positive_number("Resistor R2 (ohms): ")
    load_value = read_positive_number(
        "Load resistance RL (ohms, 0 = no load): ", allow_zero=True
    )
    load_resistance = None if load_value == 0 else load_value

    try:
        results = calculate_voltage_divider(
            source_voltage, r1, r2, load_resistance
        )
    except ValueError as error:
        print(f"Input error: {error}")
        return

    display_results(results, load_resistance)


if __name__ == "__main__":
    main()

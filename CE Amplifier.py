# Common Emitter (CE) Amplifier - DC Analysis

# Input values
VCC = float(input("Enter VCC (V): "))
RB = float(input("Enter RB (Ohms): "))
RC = float(input("Enter RC (Ohms): "))
beta = float(input("Enter transistor beta (β): "))
VBE = 0.7  # Silicon transistor

# Base current
IB = (VCC - VBE) / RB

# Collector current
IC = beta * IB

# Collector-emitter voltage
VCE = VCC - (IC * RC)

# Display results
print("\n--- CE Amplifier DC Analysis ---")
print(f"Base current (IB)      = {IB * 1e6:.2f} µA")
print(f"Collector current (IC) = {IC * 1e3:.2f} mA")
print(f"Collector voltage (VCE) = {VCE:.2f} V")

# Check transistor region
if VCE > 0.2:
    print("Transistor is in ACTIVE region.")
else:
    print("Transistor is in SATURATION region.")

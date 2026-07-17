print(" Semiconductor Engineering Calculator ")
print("================================")


def calculate_power():

    voltage = float(input("Voltage (V): "))
    current = float(input("Current (A): "))

    power = voltage * current

    print("Power =", power, "W")


def calculate_voltage():

    resistance = float(input("Resistance (Ohm): "))
    current = float(input("Current (A): "))

    voltage = resistance * current

    print("Voltage =", voltage, "V")


def calculate_resistance():

    voltage = float(input("Voltage (V): "))
    current = float(input("Current (A): "))

    resistance = voltage / current

    print("Resistance =", resistance, "Ohm")


def calculate_energy():

    power = float(input("Power (W): "))
    time = float(input("Time (seconds): "))

    energy = power * time

    print("Energy =", energy, "J")


while True:

    print("\nSelect calculation:")
    print("1 - Power")
    print("2 - Voltage")
    print("3 - Resistance")
    print("4 - Energy")
    print("5 - Exit")

    choice = input("Choice: ")


    if choice == "1":
        calculate_power()

    elif choice == "2":
        calculate_voltage()

    elif choice == "3":
        calculate_resistance()

    elif choice == "4":
        calculate_energy()

    elif choice == "5":
        print("Exiting calculator")
        break

    else:
        print("Invalid choice")
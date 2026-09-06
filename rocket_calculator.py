import math

# Konstanten
g = 9.81                    # Erdbeschleunigung in m/s^2
p_atm = 101325              # Atmosphärischer Druck in Pa (1 Bar = 100000 Pa)
volume_bottle = 0.001       # Volumen der Flasche in m^3 (1 Liter = 0.001 m^3)
mass_bottle = 0.05          # Masse der leeren Flasche in kg

# Funktion zur Berechnung der Flughöhe mit berücksichtigter Entleerung
def calculate_rocket_height(volume_water, pressure_air):
    volume_total = volume_water + volume_bottle     # Gesamtvolumen (Wasser + Luft)

    # Startbedingungen
    p_total = pressure_air + p_atm                  # Anfangsdruck
    mass_water = volume_water * 1                   # Anfangsmasse Wasser (1 kg/Liter Annahme)

    total_mass = mass_water + mass_bottle           # Gesamtmassen (Wasser + Flasche)

    # Berechnung der Steiggeschwindigkeit
    def calculate_velocity(t):
        # Druck zu einem Zeitpunkt t
        current_pressure = p_total * math.exp(-t / 10)          # Beispielhafte exponentielle Druckentlastung
        v_e = math.sqrt(2 * current_pressure / total_mass)      # Ausströmgeschwindigkeit
        return v_e

    # Integration zur Berechnung der maximalen Höhe
    def integrate_velocity():
        t = 0
        dt = 0.01                   # Zeitschritt (z.B. 0.01 Sekunden)
        h = 0                       # Höhe

        while True:
            v = calculate_velocity(t)
            h += v * dt             # Höhe aktualisieren
            t += dt
            if v <= 0:               # Abbruchbedingung: Rakete beginnt zu fallen (wenn v <= 0)
                break

        return h / 1000

    h_max = integrate_velocity()    # Maximale Höhe berechnen
    return h_max


print("Welcome to rocket_calculator v1")
print("")
print("------ Begin Parameter -------")
print(f"Erdbeschleunigung:         {g} in m/2^2")
print(f"Atmosphärischer Druck in Pa: {p_atm} in m/2^2")
print(f"Volumen der Flasche: {volume_bottle} in m^3")
print(f"Masse der Flasche: {mass_bottle} in m^3")
print("------ End Parameter -------")
print("")
print("Umrechnungen von 1 Bar in = 100000 Pa ")
print("")


volume_water = float(input("Bitte geben Sie das Volumen des Wassers in Litern (z.B. 0.25 für 250 ml): "))
pressure_air = float(input("Bitte geben Sie den Luftdruck in Bar an (z.B. 3 für 3 Bar): ")) * 100000  # Umwandlung in Pascal


height = calculate_rocket_height(volume_water, pressure_air)        # Berechnung der Höhe

print(f"Die Wasserrakete erreicht eine Höhe von ca. {height:.2f} Metern.")

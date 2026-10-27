

class Vaccine:
    """One vaccine dose given to a patient."""

    def __init__(self, name, date_given, dose_number):
        self.name = name
        self.date_given = date_given      # tuple: (year, month, day)
        self.dose_number = dose_number

    def display_info(self):
        year, month, day = self.date_given
        print(f"  - {self.name} | Dose {self.dose_number} | {year}-{month:02d}-{day:02d}")


class Patient:
    """An anonymous patient identified only by ID and age group."""

    VALID_AGE_GROUPS = ("Infant", "Child", "Teen", "Adult", "Elder")  # tuple (bonus)
    total_patients = 0  # class attribute shared by all patients

    def __init__(self, patient_id, age_group):
        self.patient_id = patient_id
        self.age_group = age_group
        self.vaccines = []
        Patient.total_patients += 1

    # ---- Instance methods ----
    def add_vaccine(self, vaccine):
        """Record a vaccine dose for this patient."""
        self.vaccines.append(vaccine)

    def update_record(self, new_age_group):
        """Update the patient's age group."""
        if new_age_group in Patient.VALID_AGE_GROUPS:
            self.age_group = new_age_group
            print(f"{self.patient_id} updated to age group '{new_age_group}'.")
        else:
            print("Invalid age group.")

    def display_info(self):
        print(f"Patient ID: {self.patient_id} | Age group: {self.age_group}")
        if not self.vaccines:
            print("  (no vaccines recorded)")
        for vaccine in self.vaccines:
            vaccine.display_info()

    # ---- Class method ----
    @classmethod
    def get_total_patients(cls):
        """Return how many Patient objects have been created."""
        return cls.total_patients

    # ---- Static method ----
    @staticmethod
    def is_valid_id(patient_id):
        """An ID must start with 'P' followed by at least 3 digits."""
        return (
            isinstance(patient_id, str)
            and len(patient_id) >= 4
            and patient_id[0] == "P"
            and patient_id[1:].isdigit()
        )


# ---- Data structure: dictionary {patient_id: Patient} ----
records = {}


def add_record(patient):
    """Add a patient to the records dictionary."""
    if not Patient.is_valid_id(patient.patient_id):
        print(f"Error: '{patient.patient_id}' is not a valid ID (use e.g. P001).")
    elif patient.patient_id in records:
        print(f"Error: {patient.patient_id} already exists.")
    else:
        records[patient.patient_id] = patient
        print(f"Record added: {patient.patient_id}")


def display_records():
    """Display every patient in the records dictionary."""
    if not records:
        print("No records found.")
        return
    for patient in records.values():
        patient.display_info()
        print()


def main():
    print("=== Community Vaccination Tracker ===\n")

    # Object creation
    p1 = Patient("P001", "Child")
    p1.add_vaccine(Vaccine("Polio", (2026, 10, 1), 1))
    p1.add_vaccine(Vaccine("Measles", (2026, 10, 15), 1))

    p2 = Patient("P002", "Adult")
    p2.add_vaccine(Vaccine("COVID-19", (2026, 9, 20), 2))

    p3 = Patient("BAD", "Teen")  # invalid ID, will be rejected

    # Interaction between objects and the dictionary
    for p in (p1, p2, p3):
        add_record(p)

    print("\n--- All records ---")
    display_records()

    print("--- Updating a record ---")
    records["P001"].update_record("Teen")
    records["P001"].display_info()

    print(f"\nTotal Patient objects created: {Patient.get_total_patients()}")
    print(f"Records stored: {len(records)}")


if __name__ == "__main__":
    main()
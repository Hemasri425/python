class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []

    def addPatients(self, patients_list):
        self.patients.extend(patients_list)
        print("Patients are added to the Hospital")

    def addDoctors(self, doctors_list):
        self.doctors.extend(doctors_list)
        print("Doctors are added to the Hospital")

    def addAppointments(self, appointments_list):
        self.appointments.extend(appointments_list)
        print("Appointments are scheduled in the Hospital")

    def searchPatient(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def generateReport(self):
        print("======== Hospital Report ========")
        print(f"Hospital Name : {self.name}")
        print(f"Total Patients: {len(self.patients)}")
        print(f"Total Doctors : {len(self.doctors)}")
        print(f"Total Appointments : {len(self.appointments)}")
        print("=================================")


class Patient:
    _id_counter = 1001

    def __init__(self, name, age, gender):
        self.id = Patient._id_counter
        Patient._id_counter += 1
        self.name = name
        self.age = age
        self.gender = gender
        self.history = []

    def addMedicalRecord(self, record):
        self.history.append(record)

    def getHistory(self):
        print(f"Medical History of {self.name}: {self.history}")


class Doctor:
    _id_counter = 501

    def __init__(self, name, specialization):
        self.id = Doctor._id_counter
        Doctor._id_counter += 1
        self.name = name
        self.specialization = specialization
        self.schedule = []

    def viewSchedule(self):
        print(f"Appointments of Dr. {self.name}:")
        for app in self.schedule:
            print(app)

    def addAppointment(self, appointment):
        self.schedule.append(appointment)


class Appointment:
    _id_counter = 1
    _room_counter = 101

    def __init__(self, patient, doctor, date_time):
        self.id = Appointment._id_counter
        Appointment._id_counter += 1
        self.room = Appointment._room_counter
        Appointment._room_counter += 1
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def __str__(self):
        return f"Appointment[ID={self.id}, Room={self.room}, Patient={self.patient.name}, Doctor={self.doctor.name}, DateTime={self.date_time}]"


# =============================
# Example Usage (Like your Zone code)
# =============================
h1 = Hospital("City Hospital")

# Patients
p1 = Patient("Alice", 30, "F")
p2 = Patient("Bob", 45, "M")

# Doctors
d1 = Doctor("Dr. Smith", "Cardiologist")
d2 = Doctor("Dr. John", "Neurologist")

# Add to hospital
h1.addPatients([p1, p2])
h1.addDoctors([d1, d2])

# Medical history
p1.addMedicalRecord("2023-05-10: Diagnosed with Hypertension")
p1.addMedicalRecord("2024-01-12: Routine Checkup - Normal")

# Appointments
a1 = Appointment(p1, d1, "2025-10-05 10:30")
a2 = Appointment(p2, d2, "2025-10-06 14:00")

h1.addAppointments([a1, a2])

# Add appointments to doctor schedule
d1.addAppointment(a1)
d2.addAppointment(a2)

# Patient History
p1.getHistory()

# Doctor Schedule
d1.viewSchedule()

# Search Patient
result = h1.searchPatient(1001)
if result:
    print(f"Patient Found: {result.name}, Age: {result.age}, Gender: {result.gender}")

# Hospital Report
h1.generateReport()

// Fetch and display doctors
async function fetchDoctors() {
    try {
        let response = await fetch('/api/doctors');
        let data = await response.json();
        let doctorList = document.getElementById("doctor-list");
        doctorList.innerHTML = data.length ? "" : "<li>No doctors available.</li>";

        data.forEach(doctor => {
            let listItem = document.createElement("li");
            listItem.innerHTML = `
                ${doctor.name} (${doctor.specialization})
            `;
            doctorList.appendChild(listItem);
        });
    } catch (error) {
        console.error("Error fetching doctors:", error);
    }
}

// Fetch and display patients
async function fetchPatients() {
    try {
        let response = await fetch('/api/patients');
        let data = await response.json();
        let patientList = document.getElementById("patient-list");
        patientList.innerHTML = data.length ? "" : "<li>No patients available.</li>";

        data.forEach(patient => {
            let listItem = document.createElement("li");
            listItem.innerHTML = `
                ${patient.name} (${patient.blood_group}) - Assigned Doctor: 
                ${patient.assigned_doctor || "Not Assigned"}
            `;
            patientList.appendChild(listItem);
        });
    } catch (error) {
        console.error("Error fetching patients:", error);
    }
}

// Fetch and display consultation requests
async function fetchConsultations() {
    try {
        let response = await fetch('/api/consultations');
        let data = await response.json();
        let consultationList = document.getElementById("consultation-list");
        consultationList.innerHTML = "";

        data.forEach(request => {
            let listItem = document.createElement("li");
            listItem.innerHTML = `
                ${request.patient_name} - Status: ${request.status}
            `;
            consultationList.appendChild(listItem);
        });

    } catch (error) {
        console.error("Error fetching consultations:", error);
    }
}

// Initial Fetch
fetchDoctors();
fetchPatients();
fetchConsultations();

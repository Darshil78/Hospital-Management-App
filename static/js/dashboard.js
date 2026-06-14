// Hospital Management System Dashboard JavaScript


// Chart Animation Settings

document.addEventListener(
    "DOMContentLoaded",
    function() {


        const chartElement = document.getElementById(
            "chart"
        );


        if (chartElement) {


            new Chart(
                chartElement, {

                    type: "doughnut",

                    data: {


                        labels: [

                            "Patients",

                            "Doctors",

                            "Appointments",

                            "Medicines"

                        ],


                        datasets: [

                            {

                                data: [

                                    patientCount,

                                    doctorCount,

                                    appointmentCount,

                                    medicineCount

                                ]

                            }

                        ]

                    },


                    options: {


                        responsive: true,


                        plugins: {


                            legend: {


                                position: "bottom"

                            }


                        }


                    }


                }

            );


        }




        // Current Date Display

        let dateBox =
            document.getElementById(
                "currentDate"
            );


        if (dateBox) {


            let today =
                new Date();


            dateBox.innerHTML =
                today.toDateString();


        }



    }

);





// Sidebar Mobile Toggle

function toggleSidebar() {


    let sidebar =
        document.querySelector(
            ".sidebar"
        );


    sidebar.classList.toggle(
        "active"
    );


}





// Confirm Delete

function confirmDelete() {


    return confirm(
        "Are you sure you want to delete this record?"
    );


}




// Auto Hide Flash Messages

setTimeout(

    function() {


        let alerts =
            document.querySelectorAll(
                ".alert"
            );


        alerts.forEach(

            function(alert) {


                alert.style.display = "none";


            }

        );


    },

    4000

);
const btn = document.querySelector('.talk'); // Select the button element for speech recognition
const content = document.querySelector('.content'); // Select the content area for displaying speech input
const Captain_t = document.getElementById('jarvis_t'); // Select the element to display Captain' speech output


// console.log(btn);
// btn.addEventListener('click' , ()=>{
//     console.log("hiuehf");
// })

// Function to update date and time
function updateTimeAndDate() {
    // Get the current date and time
    const now = new Date();
    let hours = now.getHours();
    const minutes = now.getMinutes().toString().padStart(2, '0'); // Ensure minutes are always two digits
    const amPm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12 || 12; // Adjust hours for 12-hour clock
    const day = now.getDate();
    const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const month = monthNames[now.getMonth()];
    const year = now.getFullYear();
    const weekdayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const weekday = weekdayNames[now.getDay()];

    // Combine the formatted components into the desired string
    const formattedTimeAndDate = `${hours}:${minutes} ${amPm} ${day} ${month} ${year}, ${weekday}`;

    // Update the paragraph element with the formatted time and date
    document.getElementById('dateandtime').textContent = formattedTimeAndDate;
}






// Function to check internet connectivity
function checkConnectivity() {
    const online = navigator.onLine;
    const internetOn = document.getElementById('internet-on');
    const internetOff = document.getElementById('internet-off');

    // Display the appropriate internet connectivity indicator
    if (online) {
        internetOn.style.display = 'block'; // Show 'Internet On' indicator
        internetOff.style.display = 'none'; // Hide 'Internet Off' indicator
    } else {
        internetOn.style.display = 'none'; // Hide 'Internet On' indicator
        internetOff.style.display = 'block'; // Show 'Internet Off' indicator
    }
}

// Initial display of time, date, and internet connectivity
updateTimeAndDate();
checkConnectivity();

// Update time and date, and check connectivity status every 5 seconds
setInterval(updateTimeAndDate, 5000);
setInterval(checkConnectivity, 5000);






// Function to update battery status
function updateBatteryInfo(battery) {
    const statusElement = document.getElementById('battery-status');
    const charging = battery.charging;
    const percentage = Math.round(battery.level * 100) + "%";

    // Define icons based on charging status
    const iconClass = charging ? "bolt" : "battery-empty";
    const iconHTML = `<i class="fas fa-${iconClass}"></i>`;

    // Display battery status with icons
    statusElement.innerHTML = `${iconHTML} Battery: ${percentage} ${charging ? 'Charging' : 'Not Charging'}`;
}





// Get battery information and update status
navigator.getBattery().then((battery) => {
    updateBatteryInfo(battery);

    // Update battery status every 5 seconds
    setInterval(() => {
        updateBatteryInfo(battery);
    }, 5000);

    // Event listeners for battery status changes
    battery.addEventListener('chargingchange', () => {
        updateBatteryInfo(battery);
    });

    battery.addEventListener('levelchange', () => {
        updateBatteryInfo(battery);
    });
});





// Function to speak given text
// function speak(text) {
//     const text_speak = new SpeechSynthesisUtterance(text);
//     jarvis_t.textContent = text; // Display the spoken text in the designated element

//     // Speech synthesis settings
//     text_speak.rate = 1;
//     text_speak.pitch = 1;

//     window.speechSynthesis.speak(text_speak); // Speak the provided text
// }





// // Function to greet based on time
// function wishMe() {
//     const hour = new Date().getHours();

//     // Greet based on the time of day
//     if (hour >= 0 && hour < 12) {
//         speak("Good Morning Boss...");
//     } else if (hour >= 12 && hour < 17) {
//         speak("Good Afternoon Boss...");
//     } else {
//         speak("Good Evening Sir...");
//     }
// }




// // Event listener when the window loads
// window.addEventListener('load', () => {
	
// 	var song = new Audio();// Initialize an audio element
// 	song.src = 'power up.mp3';
// 	song.play(); // Play the 'power up.mp3' audio file
	
//     speak("Initializing CAPTAIN..");
//     wishMe(); // Greet the user based on the time
// }
// ); 




// Create a SpeechRecognition object based on browser support
// const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
// const recognition = new SpeechRecognition();





// // Event handling when speech recognition detects a result
// recognition.onresult = async (event) => {
//     const current = event.resultIndex;
//     const transcript = event.results[current][0].transcript;
//     content.textContent = transcript; // Display the recognized speech content
//     await processCommand(transcript.toLowerCase()); // Process the recognized text as a command
// };





let musicPlayed = false;
let speechInitialized = false;
let recognitionStarted = false;

btn.addEventListener('click', () => {
    // if (!musicPlayed) {
    //     var song = new Audio(); // Initialize an audio element
    //     song.src = 'power up.mp3';
    //     song.play(); // Play the 'power up.mp3' audio file
    //     musicPlayed = true; // Update the flag to indicate music has been played
    // }

    {
        // fetch('http://127.0.0.1:8000/bot/')
        // //   .then(response => response.json())
        //   .then(data => console.log(data))
        //   .catch(error => console.error('Error:', error));
        var url = '/runbot/';

        // Navigate to the URL
        window.location.href = url;
    }

    // if (!speechInitialized) {
    //     speak("Initializing CAPTAIN..");
    //     wishMe(); // Greet the user based on the time
    //     speechInitialized = true; // Update the flag to indicate speech initialized
		
	// 	// Set recognitionStarted = true; after 5 seconds
    //     setTimeout(() => {
    //         recognitionStarted = true; // Update the flag to indicate recognition started
    //     }, 3000);
    // }
	
	setTimeout(() => {
		if (recognitionStarted) {
			content.textContent = "Listening...."; // Update content to "Listening...."
			recognition.start(); // Start speech recognition immediately
			recognitionStarted = true; // Update the flag to indicate recognition started
		}
	}, 5000);
});
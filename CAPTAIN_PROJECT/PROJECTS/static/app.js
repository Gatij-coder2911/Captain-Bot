const btn = document.querySelector('.talk'); // Select the button element for speech recognition

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


btn.addEventListener('click', () => {

    {
        var url = '/runbot/';

        // Navigate to the URL
        window.location.href = url;
    }
	
	// setTimeout(() => {
	// 	if (recognitionStarted) {
	// 		content.textContent = "Listening...."; // Update content to "Listening...."
	// 		recognition.start(); // Start speech recognition immediately
	// 		recognitionStarted = true; // Update the flag to indicate recognition started
	// 	}
	// }, 5000);
});
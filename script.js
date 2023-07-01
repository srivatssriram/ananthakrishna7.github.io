const date = new Date();
const dayNo = date.getDay()
let day = "Sunday"
switch (dayNo) {
    case 0:
        break;

    case 1:
        day = "Monday";
        break;
    
    case 2:
        day = "Tuesday";
        break;

    case 3:
        day = "Wednesday";
        break;

    case 4:
        day = "Thursday";
        break;

    case 5:
        day = "Friday";
        break;

    case 6:
        day = "Saturday";
        break;    

    default:
        break;
}

let month = "January";
let monthNo = date.getMonth();
switch (monthNo) {
    //0 is January
    case 1:
        month = "February";
        break;
    case 6:
        month = "July"
//Jaiaditya do this
    default:
        break;
}
console.log(date, day, dayNo);
document.getElementById("date").innerHTML = day+", "+date.getDate()+" "+month+" "+date.getFullYear();

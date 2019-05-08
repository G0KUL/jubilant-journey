function fetchCourseOfFaculty(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("View My courses successful");
            console.log(this.responseText);
            data = this.responseText.split(",");
            var course = document.getElementById('courseID');
            for(var i = 0; i < data.length - 1 ; i++) {
                var option = document.createElement('option');
                option.value = data[i].split(":")[0];
                option.text = data[i].split(":")[1];
                course.add(option, 0);
            }
        }
    };
    xhttp.open("POST", "/viewMyCourses", true);
    xhttp.send();
}

function onMyCourse(){
    $('#datapoint').load("static/html/facultyViewCourses.html");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("View My courses successful");
            console.log(this.responseText);
            data = this.responseText.split(",");
            var table = document.getElementById("tableContent");
            for(var i = 0; i < data.length - 1 ; i++) {
                var row = table.insertRow(1);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                cell1.innerHTML = data[i].split(":")[0];
                cell2.innerHTML = data[i].split(":")[1];
            }
        }
    };
    xhttp.open("POST", "/viewMyCourses", true);
    xhttp.send();
}

function assignCourseToStudent(){
    $('#datapoint').load("static/html/assignCourseToStudent.html");
    fetchCourseOfFaculty();
}



function onAssignStudent(){
    var success = "<p class='text-success'>";
    var error = "<p class='text-danger'>";

    var rollNo = document.getElementById('rollNo');
    var courseIDSelect = document.getElementById('courseID');
    var courseID = courseIDSelect.options[courseIDSelect.selectedIndex];            //

    var data = rollNo.value + "`" + courseID.value;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('msg').innerHTML = success + this.responseText + "</p>";
            console.log("OK OK successful");
            rollNo.value = '';
        }
    };
    xhttp.open("POST", "/assignCourseToStudent", true);
    xhttp.send(data);
}

function onAssignTA(){
    $('#datapoint').load("static/html/AddTA.html");
    fetchCourseOfFaculty();
}

function onAssignTASave(){
    var success = "<p class='text-success'>";
    var error = "<p class='text-danger'>";

    var rollNo = document.getElementById('rollNo');
    var courseIDSelect = document.getElementById('courseID');
    var courseID = courseIDSelect.options[courseIDSelect.selectedIndex];            //

    var data = rollNo.value + "`" + courseID.value;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('msg').innerHTML = success + this.responseText + "</p>";
            console.log("TA add successful");
            rollNo.value = '';
        }
    };
    xhttp.open("POST", "/assignTAToCourse", true);
    xhttp.send(data);
}
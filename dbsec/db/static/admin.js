function createCourse() {
    $('#datapoint').load("static/html/addCourse.html");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            //document.getElementById('msg').innerHTML = success + this.responseText + "</p>";
            console.log("Instructors loading successful");
            //console.log(this.responseText);
            data = this.responseText.split(",");

            var instructor = document.getElementById('courseInstructor');
            for(var i = 0; i < data.length - 1 ; i++) {
                var option = document.createElement('option');
                option.value = data[i].split(":")[0];
                option.text = data[i].split(":")[1];
                instructor.add(option, 0);
            }
        }
    };
    xhttp.open("POST", "/loadInstructor", true);
    xhttp.setRequestHeader('X-CSRFToken', getCookie("csrftoken"));
    xhttp.send();
}

function onCreateUser(){
    $('#datapoint').load("static/html/addUser.html");
}

function onViewStudents(){
     $('#datapoint').load("static/html/viewStudents.html");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("Students loading successful");
            data = this.responseText.split(",");
            console.log(data);
            console.log(data.length);

            var table = document.getElementById("tableContent");
            for(var i = 0; i < data.length - 1 ; i++) {
                console.log(data[i]);
                var row = table.insertRow(1);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                cell1.innerHTML = data[i].split(":")[0];
                cell2.innerHTML = data[i].split(":")[1];
                cell3.innerHTML = data[i].split(":")[2];
                cell4.innerHTML = data[i].split(":")[3];
            }
        }
    };
    xhttp.open("POST", "/viewStudents", true);
    xhttp.setRequestHeader('X-CSRFToken', getCookie("csrftoken"));
    xhttp.send();
}

function onViewFaculties() {
     $('#datapoint').load("static/html/viewFaculties.html");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("Students loading successful");
            data = this.responseText.split("~");
            console.log(data);
            console.log(data.length);

            var table = document.getElementById("tableContent");
            for(var i = 0; i < data.length - 1 ; i++) {
                console.log(data[i]);
                var row = table.insertRow(1);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                cell1.innerHTML = data[i].split("`")[0];
                cell2.innerHTML = data[i].split("`")[1];
                cell3.innerHTML = data[i].split("`")[2];
                cell4.innerHTML = data[i].split("`")[3];
            }
        }
    };
    xhttp.open("POST", "/viewFaculties", true);
    xhttp.setRequestHeader('X-CSRFToken', getCookie("csrftoken"));
    xhttp.send();
}

function onViewCourse(){
    $('#datapoint').load("static/html/viewCourses.html");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("Students loading successful");
            data = this.responseText.split("~");
            console.log(data);
            console.log(data.length);

            var table = document.getElementById("tableContent");
            for(var i = 0; i < data.length - 1 ; i++) {
                console.log(data[i]);
                var row = table.insertRow(1);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                cell1.innerHTML = data[i].split("`")[0];
                cell2.innerHTML = data[i].split("`")[1];
                cell3.innerHTML = data[i].split("`")[2];
                cell4.innerHTML = data[i].split("`")[3];
            }
        }
    };
    xhttp.open("POST", "/viewAllCourses", true);
    xhttp.setRequestHeader('X-CSRFToken', getCookie("csrftoken"));
    xhttp.send();
}

function onRoleChangeUser(){
    var role = document.getElementById('role');
    if (role.value == 'student')
        $('#rolecontent').load("static/html/studentDetails.html");
    else if (role.value == 'faculty')
        $('#rolecontent').load("static/html/facultyDetails.html");
}

function onCourseSave() {
    var success = "<p class='text-success'>";
    var error = "<p class='text-danger'>";
    var courseId = document.getElementById('courseId');
    var courseName = document.getElementById('courseName');
    var courseDesc = document.getElementById('courseDesc');
    var courseInstrSelect = document.getElementById('courseInstructor');
    var courseInstr = courseInstrSelect.options[courseInstrSelect.selectedIndex].value;
    //var strUser = e.options[e.selectedIndex].text;

    //var data = "CourseID=" + courseId.value + "&"
    //    + "courseName=" + courseName.value + "&"
    //    + "courseDesc=" + courseDesc.value + "&"
    //    + "courseInstr=" + courseInstr;
    var data = courseId.value + "&" + courseName.value + "&" + courseDesc.value + "&" + courseInstr;
    console.log(courseId.value);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('msg').innerHTML = success + this.responseText + "</p>";
            console.log("successful");
            onReset();
        }
    };
    xhttp.open("POST", "/createCourse", true);
    xhttp.setRequestHeader('X-CSRFToken', getCookie("csrftoken"));
    xhttp.send(data);
}

function onReset(){
    var courseId = document.getElementById('courseId');
    var courseName = document.getElementById('courseName');
    var courseDesc = document.getElementById('courseDesc');
    var courseInstr = document.getElementById('courseInstructor');
    courseId.value = '';
    courseName.value = '';
    courseDesc.value = '';
    courseInstr.selectedIndex = "1";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ')
            c = c.substring(1);
        if (c.indexOf(name) == 0)
            return c.substring(name.length, c.length);
    }
    return "";
}

function onSaveUser(){
    var success = "<p class='text-success'>";
    var error = "<p class='text-danger'>";
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    var roleSelect = document.getElementById('role');
    var role = roleSelect.options[roleSelect.selectedIndex];            //
    var data = username.value + "`" + password.value + "`" + role.value + "`";
    if (role.value == 'student'){
        var studId = document.getElementById('studId');
        var studentName = document.getElementById('studentName');
        var classSelect = document.getElementById('class');             //
        var class_ = classSelect.options[classSelect.selectedIndex];
        var yearSelect = document.getElementById('year');               //
        var year = yearSelect.options[yearSelect.selectedIndex];
        data += studId.value + "`" + studentName.value + "`" + class_.text + "`" + year.value;
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById('msg').innerHTML = success + this.responseText + "</p>";
                console.log("Student add successful");
                onUserReset();
            }
        };
        xhttp.open("POST", "/createStudent", true);
        xhttp.setRequestHeader('X-CSRFToken', getCookie("csrftoken"));
        xhttp.send(data);
    }
    else if(role.value == 'faculty'){
        var facultyId = document.getElementById('facultyId');
        var facultyName = document.getElementById('facultyName');
        var facultyDesigSelect = document.getElementById('facultyDesig'); //
        var facultyDesig = facultyDesigSelect.options[facultyDesigSelect.selectedIndex];
        var areaOfInterest = document.getElementById('facutlyAreaOfInterest');
        data += facultyId.value + "`" + facultyName.value + "`" + facultyDesig.value + "`" + areaOfInterest.value;
        //data += facultyName.value + "`" + facultyDesig.value + "`" + areaOfInterest.value;

        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById('msg').innerHTML = success + this.responseText + "</p>";
                console.log("Faculty adding successful");
                onUserReset();
            }
        };
        xhttp.open("POST", "/createFaculty", true);
        xhttp.setRequestHeader('X-CSRFToken', getCookie("csrftoken"));
        xhttp.send(data);
    }
}

function onUserReset(){
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    var roleSelect = document.getElementById('role');        //
    username.value = '';
    password.value = '';

    if (role.value == 'student'){
        var studId = document.getElementById('studId');
        var studentName = document.getElementById('studentName');
        var classSelect = document.getElementById('class');             //
        var yearSelect = document.getElementById('year');               //
        studId.value = '';
        studentName.value = '';
        classSelect.selectedIndex = 0;
        yearSelect.selectedIndex = 0;
    }
    else if(role.value == 'faculty'){
        var facultyId = document.getElementById('facultyId');
        var facultyName = document.getElementById('facultyName');
        var facultyDesigSelect = document.getElementById('facultyDesig');
        var areaOfInterest = document.getElementById('facutlyAreaOfInterest');
        facultyId.value = '';
        facultyName.value = '';
        facultyDesigSelect.selectedIndex = 0;
        areaOfInterest.value = '';
    }
    //roleSelect.selectedIndex = 0;
}
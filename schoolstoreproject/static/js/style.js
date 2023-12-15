
var departmentObject = {
  "Computer Science": {
    "Artificial Intelligence",
    "Data Science",
    "Machine Learning",
    "Software Development"
  },
  "Commerce": {
    "Bachelor of Commerce",
    "Chartered accountancy",
    "Bachelor of Economics",
    "Bachelor of Business Management"
  },
  "Bio Science": {
    "BSc Biotechnology",
    "Bachelor of Physiotherapy",
    "BSc Microbiology",
    "BTech Genetic Engineering"
  },
  "Humanities": {
    "Bachelor of Arts",
    "Economics",
    "Geography",
    "Law"
  },
  "Mathematics": {
    "Data Scientist",
    "Bsc Maths",
    "Msc Maths",
    "Statistics"
  },


}
window.onload = function() {
  var departmentSel = document.getElementById("department");
  var courseSel = document.getElementById("course");

  for (var x in departmentObject) {
    departmentSel.options[departmentSel.options.length] = new Option(x, x);
  }
  departmentSel.onchange = function() {


courseSel.length = 1;

    for (var y in departmentObject[this.value]) {
      courseSel.options[courseSel.options.length] = new Option(y, y);
    }
  }

}

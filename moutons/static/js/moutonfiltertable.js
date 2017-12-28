function filterTable(inputName, tableName,fieldNumber) {
  // Declare variables
  var input, filter, table, tr, td, i, f, showLine;
  input = document.getElementById(inputName);
  filter = input.value.toUpperCase();
  table = document.getElementById(tableName);
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    showLine = false;
    for (f = 0; f < fieldNumber.length; f++) {
      td = tr[i].getElementsByTagName("td")[fieldNumber[f]];
      if (td) {
        if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
          showLine = true;
        }
      }
    }
    if (showLine) {
      tr[i].style.display = "";
    } else {
        tr[i].style.display = "none";
    }
  }
}

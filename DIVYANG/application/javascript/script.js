var sidebarOpen = false;
var sidebar = document.querySelector("sidebar");


// Event listeners
document.addEventListener("DOMContentLoaded", function(event) {
  // Code to run when the page has finished loading
});

// Event listener for opening sidebar
var openBtn = document.querySelector("i.bx.bx-menu::before");
openBtn.addEventListener("click", openSidebar);

// Event listener for closing sidebar
var closeBtn = document.querySelector("close-sidebar-btn");
closeBtn.addEventListener("click", closeSidebar);


function openSidebar() {
  console.log("hellow world")
}

function closeSidebar() {
  if(sidebarOpen) {
    sidebar.classList.remove("sidebar-responsive");
    sidebarOpen = false;
  }
}
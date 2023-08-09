$(document).ready(function(){

    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;
    var current = 1;
    var steps = $("fieldset").length;
    
    setProgressBar(current);
    
    $(".next").click(function(){
    
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //Add Class Active
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;
    
    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    next_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(++current);
    });
    
    $(".previous").click(function(){
    
    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();
    
    //Remove class active
    $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
    
    //show the previous fieldset
    previous_fs.show();
    
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;
    
    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    previous_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(--current);
    });
    
    function setProgressBar(curStep){
    var percent = parseFloat(100 / steps) * curStep;
    percent = percent.toFixed();
    $(".progress-bar")
    .css("width",percent+"%")
    }
    
    $(".submit").click(function(){
    return false;
    })
     const textareas = document.querySelectorAll('.thesis-title');
    
        // Loop through each textarea and add the event listener
        textareas.forEach(textarea => {
          const charCountSpan = textarea.nextElementSibling.querySelector('.char-count');
    
          textarea.addEventListener('input', () => {
            const maxLength = parseInt(textarea.getAttribute('maxlength'));
            const remainingChars = maxLength - textarea.value.length;
            charCountSpan.textContent = remainingChars;
          });
        });
    
      function validateFile() {
          const fileInput = document.getElementById('pdfFile');
          const allowedTypes = ['application/pdf'];
          const maxFileSize = 10 * 1024 * 1024; // 10 MB
          const maxPages = 3;
    
          // Check if a file is selected
          if (fileInput.files.length === 0) {
            alert('Please choose a PDF file.');
            return false;
          }
    
          const file = fileInput.files[0];
    
          // Check file type
          if (!allowedTypes.includes(file.type)) {
            alert('Please choose a valid PDF file.');
            return false;
          }
       // Check file size
          if (file.size > maxFileSize) {
            alert('File size exceeds the maximum limit of 10 MB.');
            return false;
          }
    
          // Check number of pages
          // Add more checks here for the number of pages if needed
    
          return true;
        }
    
    
      
    
    });
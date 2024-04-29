$(document).ready(function() {
    let errorsVisible = false;
    let isLightMode = false;

    function sendTextToServer(text) {
        $.ajax({
            url: '/process',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({text: text}),
            success: function(data) {
                var formattedText = `\\( ${data.response} \\)`;
                $('#response').text(formattedText);
                $('#errorText').text("Errors: " + data.errors);
                if (errorsVisible && data.errors) {
                    $('#errorText').show();
                } else {
                    $('#errorText').hide();
                }
                MathJax.typesetPromise();
            }
        });
    }

    $('#uploadButton').click(function() {
        const file = $('#fileInput').prop('files')[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const fileContent = e.target.result;
                $('#inputText').val(fileContent);
                sendTextToServer(fileContent);
            };
            reader.readAsText(file);
        }
    });

    $('#inputText').keyup(function() {
        var text = $(this).val();
        $.ajax({
            url: '/process',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({text: text}),
            success: function(data) {
                var formattedText = `\\( \\large\\displaystyle {${data.response}} \\)`;
                $('#response').text(formattedText);
                $('#errorText').text("Errors: " + data.errors);
                if (data.errors) {
                    if (errorsVisible) {
                        $('#errorText').show();
                    }
                }
                if (MathJax && MathJax.typesetPromise) {
                    MathJax.typesetPromise();
                }
            }
        });
    });

    $('#showErrors').click(function() {
        errorsVisible = !errorsVisible;
        $(this).text(errorsVisible ? 'Hide Errors' : 'Show Errors');
        $('#errorText').toggle();
    });

    $('#toggleTheme').click(function() {
        isLightMode = !isLightMode;
        $('body').toggleClass('light-mode');
        
        // set body,html background color to white for light mode
        $('body, html').css('background-color', isLightMode ? '#FFF' : '#121212');
        
        // set body,html text color to black for light mode
        $('body, html').css('color', isLightMode ? '#333' : '#E0E0E0');

        $(this).text(isLightMode ? 'Dark Mode' : 'Light Mode');
    });
});

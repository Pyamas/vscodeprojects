document.addEventListener('DOMContentLoaded', function() {
    var descriptionText = document.getElementById('descriptionText');
    var backbutton = document.getElementById('backbutton');
    var sentences = [
        "Zdanie nr1.",
        "Zdanie nr2.",
        "Zdanie nqweqweqwwr3."
    ];

    var index = 0;

    function displayNextSentence() {
        if (index < sentences.length) {
            descriptionText .textContent = sentences[index];
            index++;
        } else {
            backbutton.textContent='koniec prezentacji';
        }
    }
    displayNextSentence();

    backbutton.addEventListener('click', function() {
        window.history.back();
    })

});

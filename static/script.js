function change() {
    fetch('/fetchtest').then(response => response.json()).then(function(data){
        document.getElementById('to_change').innerHTML = data['some text'];
    });
};

function ajaxRequest() {
    let select = document.getElementById('review_select')
    let value = select.value;

    document.getElementById('test-text').innerHTML = value;
    
};
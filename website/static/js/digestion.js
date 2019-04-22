

function validURL(str) {
  var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
    '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
  return !!pattern.test(str);
}

document.getElementById("urlDigestionSubmit").onclick = function(){
    var requestURL = document.getElementById('inputUrl').value
    if (requestURL){
        if (validURL(requestURL)){
            document.getElementById('outputUrl').value = "Processing ...";
            jQuery.ajax({
                type: 'PUT',
                url: '/api/v1.0/article',
                data: JSON.stringify({"url": requestURL}),
                headers: { "Content-Type": "application/json"},
                success: function (result) {
                    document.getElementById('outputUrl').value = result.title + "\n" + result.author +  ", " + result.publish_date + "\n" + result.digestion;
                },
                error: function (request, status, error) {
                    document.getElementById('outputUrl').value = "Unable to process article. ";
                }

            });
        } else {
            window.alert("Input is not a URL!");
        }
    } else {
        window.alert("URL is empty!");
    }
};
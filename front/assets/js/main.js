let numberConversion = () => {
    const api_url = 'http://localhost:1337/convert'

    const fromBase = document.getElementById('numberFromBase')
    const toBase = document.getElementById('numberToBase')
    const value = document.getElementById('numberToBeConverted')
    const responseModal = document.getElementById('response')

    let request = new XMLHttpRequest()
    let body = JSON.stringify({
        'fromBase': fromBase.value,
        'toBase': toBase.value,
        'value': value.value
    })

    console.log(body)

    request.open('POST', api_url)
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('Access-Control-Allow-Credentials', 'true');
    request.setRequestHeader('Access-Control-Max-Age', '1800');
    request.setRequestHeader('Access-Control-Allow-Origin', '*');
    request.setRequestHeader('Access-Control-Allow-Headers', '*');
    request.setRequestHeader('Access-Control-Request-Methods', 'GET,POST');

    request.send(body)
    request.onload = () => {
        if (request.status == 200) {
            responseModal.innerHTML = JSON.parse(request.response)["value"]
        } else {
            responseModal.innerHTML = JSON.parse(request.response)["msg"]
        }
    }
}

const convertButton = document.getElementById('convert')
convertButton.addEventListener('click', numberConversion)

const resultModal = document.getElementById("resultModal");
const convertButton = document.getElementById("convert");
const closeButton = document.getElementById("close");
const spinner = document.getElementById("spinner");

const numberConversion = () => {
  spinner.style.display = "inline-block";

  const fromBase = document.getElementById("numberFromBase").value;
  const toBase = document.getElementById("numberToBase").value;
  const value = document.getElementById("numberToBeConverted").value;
  const responseText = document.getElementById("response");

  const body = JSON.stringify({
    fromBase,
    toBase,
    value,
  });

  makeRequest(body)
    .then((response) => {
      if (response.status === 200) {
        responseText.innerText = JSON.parse(response.response)["value"];
      } else {
        responseText.innerText = JSON.parse(response.response)["msg"];
      }
    })
    .catch((error) => {
      console.error(error);
      responseText.innerText = "An error occurred while processing the request";
    });

  resultModal.style.display = "block";
};

const makeRequest = (body) => {
  const api_url = "http://localhost:1337/convert";
  const request = new XMLHttpRequest();

  request.open("POST", api_url);

  request.setRequestHeader("Content-Type", "application/json");
  request.setRequestHeader("Access-Control-Allow-Credentials", "true");
  request.setRequestHeader("Access-Control-Max-Age", "1800");
  request.setRequestHeader("Access-Control-Allow-Origin", "*");
  request.setRequestHeader("Access-Control-Allow-Headers", "*");
  request.setRequestHeader("Access-Control-Request-Methods", "GET,POST");

  return new Promise((resolve, reject) => {
    request.onload = () => {
      resolve(request);
    };
    request.onerror = () => {
      reject(Error("Network Error"));
    };
    request.onloadend = () => {
      spinner.style.display = "none";
    };
    request.send(body);
  });
};

const closeModal = () => {
  resultModal.style.display = "none";
};

convertButton.addEventListener("click", numberConversion);
closeButton.addEventListener("click", closeModal);

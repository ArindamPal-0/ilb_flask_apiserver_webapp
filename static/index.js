console.log("hello, world");
console.log(bulb_on_url);
console.log(bulb_off_url);

const url = '/api/led';

let ledOnButton, blinkingButton, img;
let blinking = false, ledOn = false;

function delay(delayInms) {
    return new Promise(resolve => {
        setInterval(() => {
            resolve();
        }, delayInms);
    });
}

window.addEventListener('load', (event) => {
    img = document.querySelector('#bulbImg');
    ledOnButton = document.querySelector('#ledOn');
    blinkingButton = document.querySelector('#blinking');

    console.log(img);
    console.log(ledOnButton);
    console.log(blinkingButton);

    fetch(url)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        ledOn = json.ledOn;
        blinking = json.blinking;
    });

    ledOnButton.addEventListener('click', (event) => {
        console.log('ledOn clicked');
        fetch(url, {
            method: 'POST',
            body: JSON.stringify({"ledOn": true}),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(json => {
            console.log(json);
            ledOn = json.ledOn;
            blinking = json.blinking;
        });
    });

    blinkingButton.addEventListener('click', event => {
        console.log('blinking clicked');
        fetch(url, {
            method: 'POST',
            body: JSON.stringify({"blinking": true}),
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(json => {
            console.log(json);
            ledOn = json.ledOn;
            blinking = json.blinking;
        });
    });

    setInterval(async () => {
        if(!ledOn) {
            img.src = bulb_off_url;
        }
        else {
            if(blinking) {
                img.src = bulb_on_url;
                await delay(500);
                img.src = bulb_off_url;
                await delay(500);
            } else {
                img.src = bulb_on_url;
            }
        }
    }, 1000);
});
document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#bttn').onclick = () => {

        console.log("clicked");

        const req = new XMLHttpRequest();
        req.open('GET', '/candy-data');
        req.onload = () => {

            const candies = JSON.parse(req.responseText);
            
            console.log(candies);

            if (candies != undefined){

                var candyList = '<ul class="candies">';
                
                for (var i=0; i<candies.length; i += 1) {
                    if (candies[i].quantity > 0) {
                        candyList += '<li class="item available">';
                    } else {
                        candyList += '<li class="item sold-out">';
                    }
                    candyList += candies[i].name + '<br>' + "Brand: " + candies[i].brand;
                    candyList += '<button id="bttn-"' + candies[i].name;
                    candyList += '>Buy</button>'
                    candyList += '</li>';
                }
                
                candyList += '</ul>';

                // console.log(candyList);
                
                document.getElementById('candyListing').innerHTML = candyList;

            }
        };
        req.send();

    };

});
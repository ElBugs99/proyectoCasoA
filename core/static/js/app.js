const perros = document.getElementById('perros');
const producto = document.querySelector('.producto');

const getData = () => {
    fetch('https://api.TheDogAPI.com/v1/breeds?limit=36')
    .then(response => response.json())
    .then(data => {

        const template = `
            <div class="container">
                ${data.map(data => (`
                    <div class="nombres">
                        <img class="imagenes" src=${data.image.url}></img>
                        <p class="dog-name">${data.name}</p>
                        <p class="dog-life-span">${data.life_span.replace('years', 'años')}</p>
                    </div>`
                )).join('')}
            </div>`;

            console.log(data);
        const element = document.querySelector('#perros');
        return element.innerHTML = template;
    });
}

perros.addEventListener('load', getData());
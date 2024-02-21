let pokemonTemplate = Handlebars.compile(document.getElementById("pokeCard").innerHTML);

let offset = 0;
const limit = 20;

async function fetchPokemon(){
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon?offset=${offset}&limit=${limit}`);
    const data = await response.json();
    offset += limit;
    pokemonsArr = [];
    data.results.forEach(element => {
        const url = element.url;
        const segments = url.split('/');
        const id = segments[segments.length - 2];
        pokemonsArr.push(
            {
                id : id,
                name : element.name,
                imageUrl : `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${id}.png`
            }
        )
    });
    return { pokemons : pokemonsArr };
}

function renderPokemon(pokemonList){
    const container = document.getElementById('list_pokemon_owned');
    const container2 = document.getElementById('content_unowned_pokemon');

    const html = pokemonTemplate(pokemonList);
    container.insertAdjacentHTML("beforeend", html);
    container2.insertAdjacentHTML("beforeend", html);
}

async function initialLoad(){
    const pokemonList = await fetchPokemon();
    renderPokemon(pokemonList);
}

window.addEventListener('scroll', async () => {
    if(window.innerHeight + window.scrollY >= document.body.offsetHeight){
        const pokemonList = await fetchPokemon();
        renderPokemon(pokemonList);
    } 
})

initialLoad();